""" Cisco_IOS_XR_ncs5500_qos_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5500\-qos package operational data.

This module contains definitions
for the following management objects\:
  platform\-qos\: DNX QoS EA operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class DnxQoseaShowActionEnum(Enum):
    """
    DnxQoseaShowActionEnum

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

    action_none = 0

    action_transmit = 1

    action_drop = 2

    action_mark = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowActionEnum']


class DnxQoseaShowHpLevelEnum(Enum):
    """
    DnxQoseaShowHpLevelEnum

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

    high_priority_level1 = 0

    high_priority_level2 = 1

    high_priority_level3 = 2

    high_priority_level4 = 3

    high_priority_level5 = 4

    high_priority_level6 = 5

    high_priority_level7 = 6

    unknown = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowHpLevelEnum']


class DnxQoseaShowIntfStatusEnum(Enum):
    """
    DnxQoseaShowIntfStatusEnum

    Intf Status

    .. data:: state_unknown = 0

    	State is unknown

    .. data:: state_down = 1

    	State is Down

    """

    state_unknown = 0

    state_down = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowIntfStatusEnum']


class DnxQoseaShowLevelEnum(Enum):
    """
    DnxQoseaShowLevelEnum

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

    level1 = 0

    level2 = 1

    level3 = 2

    level4 = 3

    level5 = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowLevelEnum']


class DnxQoseaShowMarkEnum(Enum):
    """
    DnxQoseaShowMarkEnum

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

    mark_none = 0

    dscp = 1

    precedence = 2

    mpls_topmost = 3

    mpls_imposition = 4

    qos_group = 5

    discard_class = 6

    cos = 7

    inner_cos = 8

    un_supported9 = 9

    un_supported10 = 10

    dscp_tunnel = 11

    precedence_tunnel = 12

    dei = 13

    dei_imposition = 14


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowMarkEnum']


class DnxQoseaShowPolicyStatusEnum(Enum):
    """
    DnxQoseaShowPolicyStatusEnum

    Status

    .. data:: no_error = 0

    	No errors

    .. data:: policy_in_reset = 1

    	QoS policy is reset

    """

    no_error = 0

    policy_in_reset = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowPolicyStatusEnum']


class DnxQoseaShowQueueEnum(Enum):
    """
    DnxQoseaShowQueueEnum

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

    low_priority_default_queue = 0

    low_priority_queue = 1

    high_priority_queue = 2

    unknown_queue_type = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowQueueEnum']


class DnxQoseaShowWredEnum(Enum):
    """
    DnxQoseaShowWredEnum

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

    wred_cos = 0

    wred_dscp = 1

    wred_precedence = 2

    wred_discard_class = 3

    wred_mpls_exp = 4

    red_with_user_min_max = 5

    red_with_default_min_max = 6

    wred_invalid = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowWredEnum']


class PolicyParamUnitEnum(Enum):
    """
    PolicyParamUnitEnum

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

    policy_param_unit_invalid = 0

    policy_param_unit_bytes = 1

    policy_param_unit_kbytes = 2

    policy_param_unit_mbytes = 3

    policy_param_unit_gbytes = 4

    policy_param_unit_bitsps = 5

    policy_param_unit_kbitsps = 6

    policy_param_unit_mbitsps = 7

    policy_param_unit_gbitsps = 8

    policy_param_unit_cells_ps = 9

    policy_param_unit_packets_ps = 10

    policy_param_unit_us = 11

    policy_param_unit_ms = 12

    policy_param_unit_seconds = 13

    policy_param_unit_packets = 14

    policy_param_unit_cells = 15

    policy_param_unit_percent = 16

    policy_param_unit_per_thousand = 17

    policy_param_unit_per_million = 18

    policy_param_unit_hz = 19

    policy_param_unit_khz = 20

    policy_param_unit_mhz = 21

    policy_param_unit_ratio = 22

    policy_param_unit_max = 23


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['PolicyParamUnitEnum']


class QosPolicyAccountEnumEnum(Enum):
    """
    QosPolicyAccountEnumEnum

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

    qos_serv_policy_no_ac_count_pref = 0

    qos_serv_policy_ac_count_l2 = 1

    qos_serv_policy_no_ac_count_l2 = 2

    qos_serv_policy_ac_count_user_def = 3

    qos_serv_policy_ac_count_l1 = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['QosPolicyAccountEnumEnum']



class PlatformQos(object):
    """
    DNX QoS EA operational data
    
    .. attribute:: nodes
    
    	List of nodes with platform specific QoS configuration
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes>`
    
    

    """

    _prefix = 'ncs5500-qos-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = PlatformQos.Nodes()
        self.nodes.parent = self


    class Nodes(object):
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
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
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
                self.parent = None
                self.node_name = None
                self.bundle_interfaces = PlatformQos.Nodes.Node.BundleInterfaces()
                self.bundle_interfaces.parent = self
                self.interfaces = PlatformQos.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self.remote_interfaces = PlatformQos.Nodes.Node.RemoteInterfaces()
                self.remote_interfaces.parent = self


            class BundleInterfaces(object):
                """
                QoS list of bundle interfaces
                
                .. attribute:: bundle_interface
                
                	QoS interface names
                	**type**\: list of    :py:class:`BundleInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface>`
                
                

                """

                _prefix = 'ncs5500-qos-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bundle_interface = YList()
                    self.bundle_interface.parent = self
                    self.bundle_interface.name = 'bundle_interface'


                class BundleInterface(object):
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
                        self.parent = None
                        self.interface_name = None
                        self.classes = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes()
                        self.classes.parent = self
                        self.member_interfaces = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces()
                        self.member_interfaces.parent = self
                        self.npu_id = None
                        self.policy_details = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails()
                        self.policy_details.parent = self
                        self.qos_direction = None


                    class MemberInterfaces(object):
                        """
                        QoS list of member interfaces
                        
                        .. attribute:: member_interface
                        
                        	QoS interface names
                        	**type**\: list of    :py:class:`MemberInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.member_interface = YList()
                            self.member_interface.parent = self
                            self.member_interface.name = 'member_interface'


                        class MemberInterface(object):
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
                                self.parent = None
                                self.interface_name = None
                                self.classes = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes()
                                self.classes.parent = self
                                self.policy_details = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails()
                                self.policy_details.parent = self


                            class PolicyDetails(object):
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
                                	**type**\:   :py:class:`DnxQoseaShowIntfStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowIntfStatusEnum>`
                                
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
                                	**type**\:   :py:class:`DnxQoseaShowPolicyStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyStatusEnum>`
                                
                                .. attribute:: stats_accounting_type
                                
                                	QoS Statistics Accounting Type
                                	**type**\:   :py:class:`QosPolicyAccountEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.QosPolicyAccountEnumEnum>`
                                
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
                                    self.parent = None
                                    self.interface_bandwidth_kbps = None
                                    self.interface_handle = None
                                    self.interface_status = None
                                    self.npu_id = None
                                    self.policy_name = None
                                    self.policy_status = None
                                    self.stats_accounting_type = None
                                    self.total_number_of_classes = None
                                    self.voq_base_address = None
                                    self.voq_stats_handle = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:policy-details'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.interface_bandwidth_kbps is not None:
                                        return True

                                    if self.interface_handle is not None:
                                        return True

                                    if self.interface_status is not None:
                                        return True

                                    if self.npu_id is not None:
                                        return True

                                    if self.policy_name is not None:
                                        return True

                                    if self.policy_status is not None:
                                        return True

                                    if self.stats_accounting_type is not None:
                                        return True

                                    if self.total_number_of_classes is not None:
                                        return True

                                    if self.voq_base_address is not None:
                                        return True

                                    if self.voq_stats_handle is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails']['meta_info']


                            class Classes(object):
                                """
                                QoS list of class names
                                
                                .. attribute:: class_
                                
                                	QoS policy class
                                	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.class_ = YList()
                                    self.class_.parent = self
                                    self.class_.name = 'class_'


                                class Class_(object):
                                    """
                                    QoS policy class
                                    
                                    .. attribute:: level_one_class_name  <key>
                                    
                                    	QoS policy class name at level 1
                                    	**type**\:  str
                                    
                                    .. attribute:: class_level
                                    
                                    	Class level
                                    	**type**\:   :py:class:`DnxQoseaShowLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevelEnum>`
                                    
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
                                    	**type**\:   :py:class:`DnxQoseaShowHpLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevelEnum>`
                                    
                                    .. attribute:: queue_type
                                    
                                    	Queue type
                                    	**type**\:   :py:class:`DnxQoseaShowQueueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueueEnum>`
                                    
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
                                        self.parent = None
                                        self.level_one_class_name = None
                                        self.class_level = None
                                        self.common_mark = YList()
                                        self.common_mark.parent = self
                                        self.common_mark.name = 'common_mark'
                                        self.config_excess_bandwidth_percent = None
                                        self.config_excess_bandwidth_unit = None
                                        self.config_max_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMaxRate()
                                        self.config_max_rate.parent = self
                                        self.config_min_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMinRate()
                                        self.config_min_rate.parent = self
                                        self.config_policer_average_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerAverageRate()
                                        self.config_policer_average_rate.parent = self
                                        self.config_policer_conform_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerConformBurst()
                                        self.config_policer_conform_burst.parent = self
                                        self.config_policer_excess_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerExcessBurst()
                                        self.config_policer_excess_burst.parent = self
                                        self.config_policer_peak_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerPeakRate()
                                        self.config_policer_peak_rate.parent = self
                                        self.config_queue_limit = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigQueueLimit()
                                        self.config_queue_limit.parent = self
                                        self.conform_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction()
                                        self.conform_action.parent = self
                                        self.egress_queue_id = None
                                        self.exceed_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction()
                                        self.exceed_action.parent = self
                                        self.hardware_excess_bandwidth_weight = None
                                        self.hardware_max_rate_kbps = None
                                        self.hardware_min_rate_kbps = None
                                        self.hardware_policer_average_rate_kbps = None
                                        self.hardware_policer_conform_burst_bytes = None
                                        self.hardware_policer_excess_burst_bytes = None
                                        self.hardware_policer_peak_rate_kbps = None
                                        self.hardware_queue_limit_bytes = None
                                        self.hardware_queue_limit_microseconds = None
                                        self.ip_mark = YList()
                                        self.ip_mark.parent = self
                                        self.ip_mark.name = 'ip_mark'
                                        self.level_two_class_name = None
                                        self.mpls_mark = YList()
                                        self.mpls_mark.parent = self
                                        self.mpls_mark.name = 'mpls_mark'
                                        self.network_min_bandwidth_kbps = None
                                        self.policer_bucket_id = None
                                        self.policer_stats_handle = None
                                        self.priority_level = None
                                        self.queue_type = None
                                        self.violate_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction()
                                        self.violate_action.parent = self
                                        self.wred = YList()
                                        self.wred.parent = self
                                        self.wred.name = 'wred'


                                    class ConfigMaxRate(object):
                                        """
                                        Configured maximum rate
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.policy_unit = None
                                            self.policy_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-max-rate'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.policy_unit is not None:
                                                return True

                                            if self.policy_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMaxRate']['meta_info']


                                    class ConfigMinRate(object):
                                        """
                                        Configured minimum rate
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.policy_unit = None
                                            self.policy_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-min-rate'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.policy_unit is not None:
                                                return True

                                            if self.policy_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMinRate']['meta_info']


                                    class ConfigQueueLimit(object):
                                        """
                                        Configured queue limit
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.policy_unit = None
                                            self.policy_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-queue-limit'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.policy_unit is not None:
                                                return True

                                            if self.policy_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigQueueLimit']['meta_info']


                                    class ConfigPolicerAverageRate(object):
                                        """
                                        Configured policer average rate
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.policy_unit = None
                                            self.policy_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-policer-average-rate'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.policy_unit is not None:
                                                return True

                                            if self.policy_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerAverageRate']['meta_info']


                                    class ConfigPolicerPeakRate(object):
                                        """
                                        Config policer peak rate
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.policy_unit = None
                                            self.policy_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-policer-peak-rate'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.policy_unit is not None:
                                                return True

                                            if self.policy_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerPeakRate']['meta_info']


                                    class ConfigPolicerConformBurst(object):
                                        """
                                        Configured policer conform burst
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.policy_unit = None
                                            self.policy_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-policer-conform-burst'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.policy_unit is not None:
                                                return True

                                            if self.policy_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerConformBurst']['meta_info']


                                    class ConfigPolicerExcessBurst(object):
                                        """
                                        Configured policer excess burst
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.policy_unit = None
                                            self.policy_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-policer-excess-burst'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.policy_unit is not None:
                                                return True

                                            if self.policy_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerExcessBurst']['meta_info']


                                    class ConformAction(object):
                                        """
                                        Conform action
                                        
                                        .. attribute:: action_type
                                        
                                        	Policer action type
                                        	**type**\:   :py:class:`DnxQoseaShowActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                        
                                        .. attribute:: mark
                                        
                                        	Action mark
                                        	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction.Mark>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.action_type = None
                                            self.mark = YList()
                                            self.mark.parent = self
                                            self.mark.name = 'mark'


                                        class Mark(object):
                                            """
                                            Action mark
                                            
                                            .. attribute:: mark_type
                                            
                                            	Mark type
                                            	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.mark_type = None
                                                self.mark_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:mark'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.mark_type is not None:
                                                    return True

                                                if self.mark_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction.Mark']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:conform-action'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.action_type is not None:
                                                return True

                                            if self.mark is not None:
                                                for child_ref in self.mark:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction']['meta_info']


                                    class ExceedAction(object):
                                        """
                                        Exceed action
                                        
                                        .. attribute:: action_type
                                        
                                        	Policer action type
                                        	**type**\:   :py:class:`DnxQoseaShowActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                        
                                        .. attribute:: mark
                                        
                                        	Action mark
                                        	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction.Mark>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.action_type = None
                                            self.mark = YList()
                                            self.mark.parent = self
                                            self.mark.name = 'mark'


                                        class Mark(object):
                                            """
                                            Action mark
                                            
                                            .. attribute:: mark_type
                                            
                                            	Mark type
                                            	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.mark_type = None
                                                self.mark_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:mark'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.mark_type is not None:
                                                    return True

                                                if self.mark_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction.Mark']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:exceed-action'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.action_type is not None:
                                                return True

                                            if self.mark is not None:
                                                for child_ref in self.mark:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction']['meta_info']


                                    class ViolateAction(object):
                                        """
                                        Violate action
                                        
                                        .. attribute:: action_type
                                        
                                        	Policer action type
                                        	**type**\:   :py:class:`DnxQoseaShowActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                        
                                        .. attribute:: mark
                                        
                                        	Action mark
                                        	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction.Mark>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.action_type = None
                                            self.mark = YList()
                                            self.mark.parent = self
                                            self.mark.name = 'mark'


                                        class Mark(object):
                                            """
                                            Action mark
                                            
                                            .. attribute:: mark_type
                                            
                                            	Mark type
                                            	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.mark_type = None
                                                self.mark_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:mark'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.mark_type is not None:
                                                    return True

                                                if self.mark_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction.Mark']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:violate-action'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.action_type is not None:
                                                return True

                                            if self.mark is not None:
                                                for child_ref in self.mark:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction']['meta_info']


                                    class IpMark(object):
                                        """
                                        IP mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.mark_type = None
                                            self.mark_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:ip-mark'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.mark_type is not None:
                                                return True

                                            if self.mark_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.IpMark']['meta_info']


                                    class CommonMark(object):
                                        """
                                        Common mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.mark_type = None
                                            self.mark_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:common-mark'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.mark_type is not None:
                                                return True

                                            if self.mark_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.CommonMark']['meta_info']


                                    class MplsMark(object):
                                        """
                                        MPLS mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.mark_type = None
                                            self.mark_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:mpls-mark'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.mark_type is not None:
                                                return True

                                            if self.mark_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.MplsMark']['meta_info']


                                    class Wred(object):
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
                                        	**type**\:   :py:class:`DnxQoseaShowWredEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWredEnum>`
                                        
                                        .. attribute:: wred_match_value
                                        
                                        	WRED match values
                                        	**type**\:   :py:class:`WredMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.config_max_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMaxThreshold()
                                            self.config_max_threshold.parent = self
                                            self.config_min_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMinThreshold()
                                            self.config_min_threshold.parent = self
                                            self.first_segment = None
                                            self.hardware_max_threshold_bytes = None
                                            self.hardware_min_threshold_bytes = None
                                            self.segment_size = None
                                            self.wred_match_type = None
                                            self.wred_match_value = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue()
                                            self.wred_match_value.parent = self


                                        class WredMatchValue(object):
                                            """
                                            WRED match values
                                            
                                            .. attribute:: dnx_qosea_show_red_match_value
                                            
                                            	dnx qosea show red match value
                                            	**type**\: list of    :py:class:`DnxQoseaShowRedMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.dnx_qosea_show_red_match_value = YList()
                                                self.dnx_qosea_show_red_match_value.parent = self
                                                self.dnx_qosea_show_red_match_value.name = 'dnx_qosea_show_red_match_value'


                                            class DnxQoseaShowRedMatchValue(object):
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
                                                    self.parent = None
                                                    self.range_end = None
                                                    self.range_start = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:dnx-qosea-show-red-match-value'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.range_end is not None:
                                                        return True

                                                    if self.range_start is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:wred-match-value'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.dnx_qosea_show_red_match_value is not None:
                                                    for child_ref in self.dnx_qosea_show_red_match_value:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue']['meta_info']


                                        class ConfigMinThreshold(object):
                                            """
                                            Configured minimum threshold
                                            
                                            .. attribute:: policy_unit
                                            
                                            	Policy unit
                                            	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                            
                                            .. attribute:: policy_value
                                            
                                            	Policy value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.policy_unit = None
                                                self.policy_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-min-threshold'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.policy_unit is not None:
                                                    return True

                                                if self.policy_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMinThreshold']['meta_info']


                                        class ConfigMaxThreshold(object):
                                            """
                                            Configured maximum threshold
                                            
                                            .. attribute:: policy_unit
                                            
                                            	Policy unit
                                            	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                            
                                            .. attribute:: policy_value
                                            
                                            	Policy value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.policy_unit = None
                                                self.policy_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-max-threshold'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.policy_unit is not None:
                                                    return True

                                                if self.policy_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMaxThreshold']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:wred'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.config_max_threshold is not None and self.config_max_threshold._has_data():
                                                return True

                                            if self.config_min_threshold is not None and self.config_min_threshold._has_data():
                                                return True

                                            if self.first_segment is not None:
                                                return True

                                            if self.hardware_max_threshold_bytes is not None:
                                                return True

                                            if self.hardware_min_threshold_bytes is not None:
                                                return True

                                            if self.segment_size is not None:
                                                return True

                                            if self.wred_match_type is not None:
                                                return True

                                            if self.wred_match_value is not None and self.wred_match_value._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.level_one_class_name is None:
                                            raise YPYModelError('Key property level_one_class_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:class[Cisco-IOS-XR-ncs5500-qos-oper:level-one-class-name = ' + str(self.level_one_class_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.level_one_class_name is not None:
                                            return True

                                        if self.class_level is not None:
                                            return True

                                        if self.common_mark is not None:
                                            for child_ref in self.common_mark:
                                                if child_ref._has_data():
                                                    return True

                                        if self.config_excess_bandwidth_percent is not None:
                                            return True

                                        if self.config_excess_bandwidth_unit is not None:
                                            return True

                                        if self.config_max_rate is not None and self.config_max_rate._has_data():
                                            return True

                                        if self.config_min_rate is not None and self.config_min_rate._has_data():
                                            return True

                                        if self.config_policer_average_rate is not None and self.config_policer_average_rate._has_data():
                                            return True

                                        if self.config_policer_conform_burst is not None and self.config_policer_conform_burst._has_data():
                                            return True

                                        if self.config_policer_excess_burst is not None and self.config_policer_excess_burst._has_data():
                                            return True

                                        if self.config_policer_peak_rate is not None and self.config_policer_peak_rate._has_data():
                                            return True

                                        if self.config_queue_limit is not None and self.config_queue_limit._has_data():
                                            return True

                                        if self.conform_action is not None and self.conform_action._has_data():
                                            return True

                                        if self.egress_queue_id is not None:
                                            return True

                                        if self.exceed_action is not None and self.exceed_action._has_data():
                                            return True

                                        if self.hardware_excess_bandwidth_weight is not None:
                                            return True

                                        if self.hardware_max_rate_kbps is not None:
                                            return True

                                        if self.hardware_min_rate_kbps is not None:
                                            return True

                                        if self.hardware_policer_average_rate_kbps is not None:
                                            return True

                                        if self.hardware_policer_conform_burst_bytes is not None:
                                            return True

                                        if self.hardware_policer_excess_burst_bytes is not None:
                                            return True

                                        if self.hardware_policer_peak_rate_kbps is not None:
                                            return True

                                        if self.hardware_queue_limit_bytes is not None:
                                            return True

                                        if self.hardware_queue_limit_microseconds is not None:
                                            return True

                                        if self.ip_mark is not None:
                                            for child_ref in self.ip_mark:
                                                if child_ref._has_data():
                                                    return True

                                        if self.level_two_class_name is not None:
                                            return True

                                        if self.mpls_mark is not None:
                                            for child_ref in self.mpls_mark:
                                                if child_ref._has_data():
                                                    return True

                                        if self.network_min_bandwidth_kbps is not None:
                                            return True

                                        if self.policer_bucket_id is not None:
                                            return True

                                        if self.policer_stats_handle is not None:
                                            return True

                                        if self.priority_level is not None:
                                            return True

                                        if self.queue_type is not None:
                                            return True

                                        if self.violate_action is not None and self.violate_action._has_data():
                                            return True

                                        if self.wred is not None:
                                            for child_ref in self.wred:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:classes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.class_ is not None:
                                        for child_ref in self.class_:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.interface_name is None:
                                    raise YPYModelError('Key property interface_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:member-interface[Cisco-IOS-XR-ncs5500-qos-oper:interface-name = ' + str(self.interface_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.interface_name is not None:
                                    return True

                                if self.classes is not None and self.classes._has_data():
                                    return True

                                if self.policy_details is not None and self.policy_details._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:member-interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.member_interface is not None:
                                for child_ref in self.member_interface:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces']['meta_info']


                    class PolicyDetails(object):
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
                        	**type**\:   :py:class:`DnxQoseaShowIntfStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowIntfStatusEnum>`
                        
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
                        	**type**\:   :py:class:`DnxQoseaShowPolicyStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyStatusEnum>`
                        
                        .. attribute:: stats_accounting_type
                        
                        	QoS Statistics Accounting Type
                        	**type**\:   :py:class:`QosPolicyAccountEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.QosPolicyAccountEnumEnum>`
                        
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
                            self.parent = None
                            self.interface_bandwidth_kbps = None
                            self.interface_handle = None
                            self.interface_status = None
                            self.npu_id = None
                            self.policy_name = None
                            self.policy_status = None
                            self.stats_accounting_type = None
                            self.total_number_of_classes = None
                            self.voq_base_address = None
                            self.voq_stats_handle = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:policy-details'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.interface_bandwidth_kbps is not None:
                                return True

                            if self.interface_handle is not None:
                                return True

                            if self.interface_status is not None:
                                return True

                            if self.npu_id is not None:
                                return True

                            if self.policy_name is not None:
                                return True

                            if self.policy_status is not None:
                                return True

                            if self.stats_accounting_type is not None:
                                return True

                            if self.total_number_of_classes is not None:
                                return True

                            if self.voq_base_address is not None:
                                return True

                            if self.voq_stats_handle is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails']['meta_info']


                    class Classes(object):
                        """
                        QoS list of class names
                        
                        .. attribute:: class_
                        
                        	QoS policy class
                        	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.class_ = YList()
                            self.class_.parent = self
                            self.class_.name = 'class_'


                        class Class_(object):
                            """
                            QoS policy class
                            
                            .. attribute:: level_one_class_name  <key>
                            
                            	QoS policy class name at level 1
                            	**type**\:  str
                            
                            .. attribute:: class_level
                            
                            	Class level
                            	**type**\:   :py:class:`DnxQoseaShowLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevelEnum>`
                            
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
                            	**type**\:   :py:class:`DnxQoseaShowHpLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevelEnum>`
                            
                            .. attribute:: queue_type
                            
                            	Queue type
                            	**type**\:   :py:class:`DnxQoseaShowQueueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueueEnum>`
                            
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
                                self.parent = None
                                self.level_one_class_name = None
                                self.class_level = None
                                self.common_mark = YList()
                                self.common_mark.parent = self
                                self.common_mark.name = 'common_mark'
                                self.config_excess_bandwidth_percent = None
                                self.config_excess_bandwidth_unit = None
                                self.config_max_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMaxRate()
                                self.config_max_rate.parent = self
                                self.config_min_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMinRate()
                                self.config_min_rate.parent = self
                                self.config_policer_average_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerAverageRate()
                                self.config_policer_average_rate.parent = self
                                self.config_policer_conform_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerConformBurst()
                                self.config_policer_conform_burst.parent = self
                                self.config_policer_excess_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerExcessBurst()
                                self.config_policer_excess_burst.parent = self
                                self.config_policer_peak_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerPeakRate()
                                self.config_policer_peak_rate.parent = self
                                self.config_queue_limit = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigQueueLimit()
                                self.config_queue_limit.parent = self
                                self.conform_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction()
                                self.conform_action.parent = self
                                self.egress_queue_id = None
                                self.exceed_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction()
                                self.exceed_action.parent = self
                                self.hardware_excess_bandwidth_weight = None
                                self.hardware_max_rate_kbps = None
                                self.hardware_min_rate_kbps = None
                                self.hardware_policer_average_rate_kbps = None
                                self.hardware_policer_conform_burst_bytes = None
                                self.hardware_policer_excess_burst_bytes = None
                                self.hardware_policer_peak_rate_kbps = None
                                self.hardware_queue_limit_bytes = None
                                self.hardware_queue_limit_microseconds = None
                                self.ip_mark = YList()
                                self.ip_mark.parent = self
                                self.ip_mark.name = 'ip_mark'
                                self.level_two_class_name = None
                                self.mpls_mark = YList()
                                self.mpls_mark.parent = self
                                self.mpls_mark.name = 'mpls_mark'
                                self.network_min_bandwidth_kbps = None
                                self.policer_bucket_id = None
                                self.policer_stats_handle = None
                                self.priority_level = None
                                self.queue_type = None
                                self.violate_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction()
                                self.violate_action.parent = self
                                self.wred = YList()
                                self.wred.parent = self
                                self.wred.name = 'wred'


                            class ConfigMaxRate(object):
                                """
                                Configured maximum rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.policy_unit = None
                                    self.policy_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-max-rate'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.policy_unit is not None:
                                        return True

                                    if self.policy_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMaxRate']['meta_info']


                            class ConfigMinRate(object):
                                """
                                Configured minimum rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.policy_unit = None
                                    self.policy_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-min-rate'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.policy_unit is not None:
                                        return True

                                    if self.policy_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMinRate']['meta_info']


                            class ConfigQueueLimit(object):
                                """
                                Configured queue limit
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.policy_unit = None
                                    self.policy_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-queue-limit'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.policy_unit is not None:
                                        return True

                                    if self.policy_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigQueueLimit']['meta_info']


                            class ConfigPolicerAverageRate(object):
                                """
                                Configured policer average rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.policy_unit = None
                                    self.policy_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-policer-average-rate'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.policy_unit is not None:
                                        return True

                                    if self.policy_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerAverageRate']['meta_info']


                            class ConfigPolicerPeakRate(object):
                                """
                                Config policer peak rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.policy_unit = None
                                    self.policy_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-policer-peak-rate'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.policy_unit is not None:
                                        return True

                                    if self.policy_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerPeakRate']['meta_info']


                            class ConfigPolicerConformBurst(object):
                                """
                                Configured policer conform burst
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.policy_unit = None
                                    self.policy_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-policer-conform-burst'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.policy_unit is not None:
                                        return True

                                    if self.policy_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerConformBurst']['meta_info']


                            class ConfigPolicerExcessBurst(object):
                                """
                                Configured policer excess burst
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.policy_unit = None
                                    self.policy_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-policer-excess-burst'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.policy_unit is not None:
                                        return True

                                    if self.policy_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerExcessBurst']['meta_info']


                            class ConformAction(object):
                                """
                                Conform action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:   :py:class:`DnxQoseaShowActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.action_type = None
                                    self.mark = YList()
                                    self.mark.parent = self
                                    self.mark.name = 'mark'


                                class Mark(object):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.mark_type = None
                                        self.mark_value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:mark'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.mark_type is not None:
                                            return True

                                        if self.mark_value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction.Mark']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:conform-action'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.action_type is not None:
                                        return True

                                    if self.mark is not None:
                                        for child_ref in self.mark:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction']['meta_info']


                            class ExceedAction(object):
                                """
                                Exceed action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:   :py:class:`DnxQoseaShowActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.action_type = None
                                    self.mark = YList()
                                    self.mark.parent = self
                                    self.mark.name = 'mark'


                                class Mark(object):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.mark_type = None
                                        self.mark_value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:mark'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.mark_type is not None:
                                            return True

                                        if self.mark_value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction.Mark']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:exceed-action'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.action_type is not None:
                                        return True

                                    if self.mark is not None:
                                        for child_ref in self.mark:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction']['meta_info']


                            class ViolateAction(object):
                                """
                                Violate action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:   :py:class:`DnxQoseaShowActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.action_type = None
                                    self.mark = YList()
                                    self.mark.parent = self
                                    self.mark.name = 'mark'


                                class Mark(object):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.mark_type = None
                                        self.mark_value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:mark'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.mark_type is not None:
                                            return True

                                        if self.mark_value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction.Mark']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:violate-action'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.action_type is not None:
                                        return True

                                    if self.mark is not None:
                                        for child_ref in self.mark:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction']['meta_info']


                            class IpMark(object):
                                """
                                IP mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.mark_type = None
                                    self.mark_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:ip-mark'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.mark_type is not None:
                                        return True

                                    if self.mark_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.IpMark']['meta_info']


                            class CommonMark(object):
                                """
                                Common mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.mark_type = None
                                    self.mark_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:common-mark'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.mark_type is not None:
                                        return True

                                    if self.mark_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.CommonMark']['meta_info']


                            class MplsMark(object):
                                """
                                MPLS mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.mark_type = None
                                    self.mark_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:mpls-mark'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.mark_type is not None:
                                        return True

                                    if self.mark_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.MplsMark']['meta_info']


                            class Wred(object):
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
                                	**type**\:   :py:class:`DnxQoseaShowWredEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWredEnum>`
                                
                                .. attribute:: wred_match_value
                                
                                	WRED match values
                                	**type**\:   :py:class:`WredMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.config_max_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMaxThreshold()
                                    self.config_max_threshold.parent = self
                                    self.config_min_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMinThreshold()
                                    self.config_min_threshold.parent = self
                                    self.first_segment = None
                                    self.hardware_max_threshold_bytes = None
                                    self.hardware_min_threshold_bytes = None
                                    self.segment_size = None
                                    self.wred_match_type = None
                                    self.wred_match_value = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue()
                                    self.wred_match_value.parent = self


                                class WredMatchValue(object):
                                    """
                                    WRED match values
                                    
                                    .. attribute:: dnx_qosea_show_red_match_value
                                    
                                    	dnx qosea show red match value
                                    	**type**\: list of    :py:class:`DnxQoseaShowRedMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.dnx_qosea_show_red_match_value = YList()
                                        self.dnx_qosea_show_red_match_value.parent = self
                                        self.dnx_qosea_show_red_match_value.name = 'dnx_qosea_show_red_match_value'


                                    class DnxQoseaShowRedMatchValue(object):
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
                                            self.parent = None
                                            self.range_end = None
                                            self.range_start = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:dnx-qosea-show-red-match-value'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.range_end is not None:
                                                return True

                                            if self.range_start is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:wred-match-value'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.dnx_qosea_show_red_match_value is not None:
                                            for child_ref in self.dnx_qosea_show_red_match_value:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue']['meta_info']


                                class ConfigMinThreshold(object):
                                    """
                                    Configured minimum threshold
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.policy_unit = None
                                        self.policy_value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-min-threshold'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.policy_unit is not None:
                                            return True

                                        if self.policy_value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMinThreshold']['meta_info']


                                class ConfigMaxThreshold(object):
                                    """
                                    Configured maximum threshold
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.policy_unit = None
                                        self.policy_value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-max-threshold'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.policy_unit is not None:
                                            return True

                                        if self.policy_value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMaxThreshold']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:wred'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.config_max_threshold is not None and self.config_max_threshold._has_data():
                                        return True

                                    if self.config_min_threshold is not None and self.config_min_threshold._has_data():
                                        return True

                                    if self.first_segment is not None:
                                        return True

                                    if self.hardware_max_threshold_bytes is not None:
                                        return True

                                    if self.hardware_min_threshold_bytes is not None:
                                        return True

                                    if self.segment_size is not None:
                                        return True

                                    if self.wred_match_type is not None:
                                        return True

                                    if self.wred_match_value is not None and self.wred_match_value._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.level_one_class_name is None:
                                    raise YPYModelError('Key property level_one_class_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:class[Cisco-IOS-XR-ncs5500-qos-oper:level-one-class-name = ' + str(self.level_one_class_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.level_one_class_name is not None:
                                    return True

                                if self.class_level is not None:
                                    return True

                                if self.common_mark is not None:
                                    for child_ref in self.common_mark:
                                        if child_ref._has_data():
                                            return True

                                if self.config_excess_bandwidth_percent is not None:
                                    return True

                                if self.config_excess_bandwidth_unit is not None:
                                    return True

                                if self.config_max_rate is not None and self.config_max_rate._has_data():
                                    return True

                                if self.config_min_rate is not None and self.config_min_rate._has_data():
                                    return True

                                if self.config_policer_average_rate is not None and self.config_policer_average_rate._has_data():
                                    return True

                                if self.config_policer_conform_burst is not None and self.config_policer_conform_burst._has_data():
                                    return True

                                if self.config_policer_excess_burst is not None and self.config_policer_excess_burst._has_data():
                                    return True

                                if self.config_policer_peak_rate is not None and self.config_policer_peak_rate._has_data():
                                    return True

                                if self.config_queue_limit is not None and self.config_queue_limit._has_data():
                                    return True

                                if self.conform_action is not None and self.conform_action._has_data():
                                    return True

                                if self.egress_queue_id is not None:
                                    return True

                                if self.exceed_action is not None and self.exceed_action._has_data():
                                    return True

                                if self.hardware_excess_bandwidth_weight is not None:
                                    return True

                                if self.hardware_max_rate_kbps is not None:
                                    return True

                                if self.hardware_min_rate_kbps is not None:
                                    return True

                                if self.hardware_policer_average_rate_kbps is not None:
                                    return True

                                if self.hardware_policer_conform_burst_bytes is not None:
                                    return True

                                if self.hardware_policer_excess_burst_bytes is not None:
                                    return True

                                if self.hardware_policer_peak_rate_kbps is not None:
                                    return True

                                if self.hardware_queue_limit_bytes is not None:
                                    return True

                                if self.hardware_queue_limit_microseconds is not None:
                                    return True

                                if self.ip_mark is not None:
                                    for child_ref in self.ip_mark:
                                        if child_ref._has_data():
                                            return True

                                if self.level_two_class_name is not None:
                                    return True

                                if self.mpls_mark is not None:
                                    for child_ref in self.mpls_mark:
                                        if child_ref._has_data():
                                            return True

                                if self.network_min_bandwidth_kbps is not None:
                                    return True

                                if self.policer_bucket_id is not None:
                                    return True

                                if self.policer_stats_handle is not None:
                                    return True

                                if self.priority_level is not None:
                                    return True

                                if self.queue_type is not None:
                                    return True

                                if self.violate_action is not None and self.violate_action._has_data():
                                    return True

                                if self.wred is not None:
                                    for child_ref in self.wred:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:classes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.class_ is not None:
                                for child_ref in self.class_:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:bundle-interface[Cisco-IOS-XR-ncs5500-qos-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.interface_name is not None:
                            return True

                        if self.classes is not None and self.classes._has_data():
                            return True

                        if self.member_interfaces is not None and self.member_interfaces._has_data():
                            return True

                        if self.npu_id is not None:
                            return True

                        if self.policy_details is not None and self.policy_details._has_data():
                            return True

                        if self.qos_direction is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:bundle-interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.bundle_interface is not None:
                        for child_ref in self.bundle_interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces']['meta_info']


            class Interfaces(object):
                """
                QoS list of interfaces
                
                .. attribute:: interface
                
                	QoS interface names
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'ncs5500-qos-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
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
                        self.parent = None
                        self.interface_name = None
                        self.classes = PlatformQos.Nodes.Node.Interfaces.Interface.Classes()
                        self.classes.parent = self
                        self.policy_details = PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails()
                        self.policy_details.parent = self
                        self.qos_direction = None


                    class PolicyDetails(object):
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
                        	**type**\:   :py:class:`DnxQoseaShowIntfStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowIntfStatusEnum>`
                        
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
                        	**type**\:   :py:class:`DnxQoseaShowPolicyStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyStatusEnum>`
                        
                        .. attribute:: stats_accounting_type
                        
                        	QoS Statistics Accounting Type
                        	**type**\:   :py:class:`QosPolicyAccountEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.QosPolicyAccountEnumEnum>`
                        
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
                            self.parent = None
                            self.interface_bandwidth_kbps = None
                            self.interface_handle = None
                            self.interface_status = None
                            self.npu_id = None
                            self.policy_name = None
                            self.policy_status = None
                            self.stats_accounting_type = None
                            self.total_number_of_classes = None
                            self.voq_base_address = None
                            self.voq_stats_handle = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:policy-details'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.interface_bandwidth_kbps is not None:
                                return True

                            if self.interface_handle is not None:
                                return True

                            if self.interface_status is not None:
                                return True

                            if self.npu_id is not None:
                                return True

                            if self.policy_name is not None:
                                return True

                            if self.policy_status is not None:
                                return True

                            if self.stats_accounting_type is not None:
                                return True

                            if self.total_number_of_classes is not None:
                                return True

                            if self.voq_base_address is not None:
                                return True

                            if self.voq_stats_handle is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails']['meta_info']


                    class Classes(object):
                        """
                        QoS list of class names
                        
                        .. attribute:: class_
                        
                        	QoS policy class
                        	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.class_ = YList()
                            self.class_.parent = self
                            self.class_.name = 'class_'


                        class Class_(object):
                            """
                            QoS policy class
                            
                            .. attribute:: level_one_class_name  <key>
                            
                            	QoS policy class name at level 1
                            	**type**\:  str
                            
                            .. attribute:: class_level
                            
                            	Class level
                            	**type**\:   :py:class:`DnxQoseaShowLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevelEnum>`
                            
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
                            	**type**\:   :py:class:`DnxQoseaShowHpLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevelEnum>`
                            
                            .. attribute:: queue_type
                            
                            	Queue type
                            	**type**\:   :py:class:`DnxQoseaShowQueueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueueEnum>`
                            
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
                                self.parent = None
                                self.level_one_class_name = None
                                self.class_level = None
                                self.common_mark = YList()
                                self.common_mark.parent = self
                                self.common_mark.name = 'common_mark'
                                self.config_excess_bandwidth_percent = None
                                self.config_excess_bandwidth_unit = None
                                self.config_max_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMaxRate()
                                self.config_max_rate.parent = self
                                self.config_min_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMinRate()
                                self.config_min_rate.parent = self
                                self.config_policer_average_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerAverageRate()
                                self.config_policer_average_rate.parent = self
                                self.config_policer_conform_burst = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerConformBurst()
                                self.config_policer_conform_burst.parent = self
                                self.config_policer_excess_burst = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerExcessBurst()
                                self.config_policer_excess_burst.parent = self
                                self.config_policer_peak_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerPeakRate()
                                self.config_policer_peak_rate.parent = self
                                self.config_queue_limit = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigQueueLimit()
                                self.config_queue_limit.parent = self
                                self.conform_action = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction()
                                self.conform_action.parent = self
                                self.egress_queue_id = None
                                self.exceed_action = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction()
                                self.exceed_action.parent = self
                                self.hardware_excess_bandwidth_weight = None
                                self.hardware_max_rate_kbps = None
                                self.hardware_min_rate_kbps = None
                                self.hardware_policer_average_rate_kbps = None
                                self.hardware_policer_conform_burst_bytes = None
                                self.hardware_policer_excess_burst_bytes = None
                                self.hardware_policer_peak_rate_kbps = None
                                self.hardware_queue_limit_bytes = None
                                self.hardware_queue_limit_microseconds = None
                                self.ip_mark = YList()
                                self.ip_mark.parent = self
                                self.ip_mark.name = 'ip_mark'
                                self.level_two_class_name = None
                                self.mpls_mark = YList()
                                self.mpls_mark.parent = self
                                self.mpls_mark.name = 'mpls_mark'
                                self.network_min_bandwidth_kbps = None
                                self.policer_bucket_id = None
                                self.policer_stats_handle = None
                                self.priority_level = None
                                self.queue_type = None
                                self.violate_action = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction()
                                self.violate_action.parent = self
                                self.wred = YList()
                                self.wred.parent = self
                                self.wred.name = 'wred'


                            class ConfigMaxRate(object):
                                """
                                Configured maximum rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.policy_unit = None
                                    self.policy_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-max-rate'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.policy_unit is not None:
                                        return True

                                    if self.policy_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMaxRate']['meta_info']


                            class ConfigMinRate(object):
                                """
                                Configured minimum rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.policy_unit = None
                                    self.policy_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-min-rate'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.policy_unit is not None:
                                        return True

                                    if self.policy_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMinRate']['meta_info']


                            class ConfigQueueLimit(object):
                                """
                                Configured queue limit
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.policy_unit = None
                                    self.policy_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-queue-limit'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.policy_unit is not None:
                                        return True

                                    if self.policy_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigQueueLimit']['meta_info']


                            class ConfigPolicerAverageRate(object):
                                """
                                Configured policer average rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.policy_unit = None
                                    self.policy_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-policer-average-rate'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.policy_unit is not None:
                                        return True

                                    if self.policy_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerAverageRate']['meta_info']


                            class ConfigPolicerPeakRate(object):
                                """
                                Config policer peak rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.policy_unit = None
                                    self.policy_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-policer-peak-rate'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.policy_unit is not None:
                                        return True

                                    if self.policy_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerPeakRate']['meta_info']


                            class ConfigPolicerConformBurst(object):
                                """
                                Configured policer conform burst
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.policy_unit = None
                                    self.policy_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-policer-conform-burst'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.policy_unit is not None:
                                        return True

                                    if self.policy_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerConformBurst']['meta_info']


                            class ConfigPolicerExcessBurst(object):
                                """
                                Configured policer excess burst
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.policy_unit = None
                                    self.policy_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-policer-excess-burst'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.policy_unit is not None:
                                        return True

                                    if self.policy_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerExcessBurst']['meta_info']


                            class ConformAction(object):
                                """
                                Conform action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:   :py:class:`DnxQoseaShowActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.action_type = None
                                    self.mark = YList()
                                    self.mark.parent = self
                                    self.mark.name = 'mark'


                                class Mark(object):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.mark_type = None
                                        self.mark_value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:mark'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.mark_type is not None:
                                            return True

                                        if self.mark_value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction.Mark']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:conform-action'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.action_type is not None:
                                        return True

                                    if self.mark is not None:
                                        for child_ref in self.mark:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction']['meta_info']


                            class ExceedAction(object):
                                """
                                Exceed action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:   :py:class:`DnxQoseaShowActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.action_type = None
                                    self.mark = YList()
                                    self.mark.parent = self
                                    self.mark.name = 'mark'


                                class Mark(object):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.mark_type = None
                                        self.mark_value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:mark'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.mark_type is not None:
                                            return True

                                        if self.mark_value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction.Mark']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:exceed-action'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.action_type is not None:
                                        return True

                                    if self.mark is not None:
                                        for child_ref in self.mark:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction']['meta_info']


                            class ViolateAction(object):
                                """
                                Violate action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:   :py:class:`DnxQoseaShowActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.action_type = None
                                    self.mark = YList()
                                    self.mark.parent = self
                                    self.mark.name = 'mark'


                                class Mark(object):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.mark_type = None
                                        self.mark_value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:mark'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.mark_type is not None:
                                            return True

                                        if self.mark_value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction.Mark']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:violate-action'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.action_type is not None:
                                        return True

                                    if self.mark is not None:
                                        for child_ref in self.mark:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction']['meta_info']


                            class IpMark(object):
                                """
                                IP mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.mark_type = None
                                    self.mark_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:ip-mark'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.mark_type is not None:
                                        return True

                                    if self.mark_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.IpMark']['meta_info']


                            class CommonMark(object):
                                """
                                Common mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.mark_type = None
                                    self.mark_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:common-mark'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.mark_type is not None:
                                        return True

                                    if self.mark_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.CommonMark']['meta_info']


                            class MplsMark(object):
                                """
                                MPLS mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:   :py:class:`DnxQoseaShowMarkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.mark_type = None
                                    self.mark_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:mpls-mark'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.mark_type is not None:
                                        return True

                                    if self.mark_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.MplsMark']['meta_info']


                            class Wred(object):
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
                                	**type**\:   :py:class:`DnxQoseaShowWredEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWredEnum>`
                                
                                .. attribute:: wred_match_value
                                
                                	WRED match values
                                	**type**\:   :py:class:`WredMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.config_max_threshold = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMaxThreshold()
                                    self.config_max_threshold.parent = self
                                    self.config_min_threshold = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMinThreshold()
                                    self.config_min_threshold.parent = self
                                    self.first_segment = None
                                    self.hardware_max_threshold_bytes = None
                                    self.hardware_min_threshold_bytes = None
                                    self.segment_size = None
                                    self.wred_match_type = None
                                    self.wred_match_value = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue()
                                    self.wred_match_value.parent = self


                                class WredMatchValue(object):
                                    """
                                    WRED match values
                                    
                                    .. attribute:: dnx_qosea_show_red_match_value
                                    
                                    	dnx qosea show red match value
                                    	**type**\: list of    :py:class:`DnxQoseaShowRedMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.dnx_qosea_show_red_match_value = YList()
                                        self.dnx_qosea_show_red_match_value.parent = self
                                        self.dnx_qosea_show_red_match_value.name = 'dnx_qosea_show_red_match_value'


                                    class DnxQoseaShowRedMatchValue(object):
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
                                            self.parent = None
                                            self.range_end = None
                                            self.range_start = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:dnx-qosea-show-red-match-value'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.range_end is not None:
                                                return True

                                            if self.range_start is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:wred-match-value'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.dnx_qosea_show_red_match_value is not None:
                                            for child_ref in self.dnx_qosea_show_red_match_value:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue']['meta_info']


                                class ConfigMinThreshold(object):
                                    """
                                    Configured minimum threshold
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.policy_unit = None
                                        self.policy_value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-min-threshold'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.policy_unit is not None:
                                            return True

                                        if self.policy_value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMinThreshold']['meta_info']


                                class ConfigMaxThreshold(object):
                                    """
                                    Configured maximum threshold
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:   :py:class:`PolicyParamUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnitEnum>`
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.policy_unit = None
                                        self.policy_value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:config-max-threshold'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.policy_unit is not None:
                                            return True

                                        if self.policy_value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMaxThreshold']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:wred'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.config_max_threshold is not None and self.config_max_threshold._has_data():
                                        return True

                                    if self.config_min_threshold is not None and self.config_min_threshold._has_data():
                                        return True

                                    if self.first_segment is not None:
                                        return True

                                    if self.hardware_max_threshold_bytes is not None:
                                        return True

                                    if self.hardware_min_threshold_bytes is not None:
                                        return True

                                    if self.segment_size is not None:
                                        return True

                                    if self.wred_match_type is not None:
                                        return True

                                    if self.wred_match_value is not None and self.wred_match_value._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.level_one_class_name is None:
                                    raise YPYModelError('Key property level_one_class_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:class[Cisco-IOS-XR-ncs5500-qos-oper:level-one-class-name = ' + str(self.level_one_class_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.level_one_class_name is not None:
                                    return True

                                if self.class_level is not None:
                                    return True

                                if self.common_mark is not None:
                                    for child_ref in self.common_mark:
                                        if child_ref._has_data():
                                            return True

                                if self.config_excess_bandwidth_percent is not None:
                                    return True

                                if self.config_excess_bandwidth_unit is not None:
                                    return True

                                if self.config_max_rate is not None and self.config_max_rate._has_data():
                                    return True

                                if self.config_min_rate is not None and self.config_min_rate._has_data():
                                    return True

                                if self.config_policer_average_rate is not None and self.config_policer_average_rate._has_data():
                                    return True

                                if self.config_policer_conform_burst is not None and self.config_policer_conform_burst._has_data():
                                    return True

                                if self.config_policer_excess_burst is not None and self.config_policer_excess_burst._has_data():
                                    return True

                                if self.config_policer_peak_rate is not None and self.config_policer_peak_rate._has_data():
                                    return True

                                if self.config_queue_limit is not None and self.config_queue_limit._has_data():
                                    return True

                                if self.conform_action is not None and self.conform_action._has_data():
                                    return True

                                if self.egress_queue_id is not None:
                                    return True

                                if self.exceed_action is not None and self.exceed_action._has_data():
                                    return True

                                if self.hardware_excess_bandwidth_weight is not None:
                                    return True

                                if self.hardware_max_rate_kbps is not None:
                                    return True

                                if self.hardware_min_rate_kbps is not None:
                                    return True

                                if self.hardware_policer_average_rate_kbps is not None:
                                    return True

                                if self.hardware_policer_conform_burst_bytes is not None:
                                    return True

                                if self.hardware_policer_excess_burst_bytes is not None:
                                    return True

                                if self.hardware_policer_peak_rate_kbps is not None:
                                    return True

                                if self.hardware_queue_limit_bytes is not None:
                                    return True

                                if self.hardware_queue_limit_microseconds is not None:
                                    return True

                                if self.ip_mark is not None:
                                    for child_ref in self.ip_mark:
                                        if child_ref._has_data():
                                            return True

                                if self.level_two_class_name is not None:
                                    return True

                                if self.mpls_mark is not None:
                                    for child_ref in self.mpls_mark:
                                        if child_ref._has_data():
                                            return True

                                if self.network_min_bandwidth_kbps is not None:
                                    return True

                                if self.policer_bucket_id is not None:
                                    return True

                                if self.policer_stats_handle is not None:
                                    return True

                                if self.priority_level is not None:
                                    return True

                                if self.queue_type is not None:
                                    return True

                                if self.violate_action is not None and self.violate_action._has_data():
                                    return True

                                if self.wred is not None:
                                    for child_ref in self.wred:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:classes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.class_ is not None:
                                for child_ref in self.class_:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:interface[Cisco-IOS-XR-ncs5500-qos-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.interface_name is not None:
                            return True

                        if self.classes is not None and self.classes._has_data():
                            return True

                        if self.policy_details is not None and self.policy_details._has_data():
                            return True

                        if self.qos_direction is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces']['meta_info']


            class RemoteInterfaces(object):
                """
                QoS list of remote interfaces
                
                .. attribute:: remote_interface
                
                	QoS remote interface names
                	**type**\: list of    :py:class:`RemoteInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface>`
                
                

                """

                _prefix = 'ncs5500-qos-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.remote_interface = YList()
                    self.remote_interface.parent = self
                    self.remote_interface.name = 'remote_interface'


                class RemoteInterface(object):
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
                        self.parent = None
                        self.interface_name = None
                        self.interface_handle = None
                        self.number_of_classes = None
                        self.number_of_virtual_output_queues = None
                        self.policy_name = None
                        self.remote_class = YList()
                        self.remote_class.parent = self
                        self.remote_class.name = 'remote_class'
                        self.virtual_output_queue_statistics_handle = None


                    class RemoteClass(object):
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
                            self.parent = None
                            self.class_id = None
                            self.class_name = None
                            self.cos_q = None
                            self.hardware_queue_limit = None
                            self.hw_wred = YList()
                            self.hw_wred.parent = self
                            self.hw_wred.name = 'hw_wred'
                            self.queue_limit = None
                            self.wred = YList()
                            self.wred.parent = self
                            self.wred.name = 'wred'


                        class Wred(object):
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
                                self.parent = None
                                self.drop_probability = None
                                self.max_threshold = None
                                self.min_threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:wred'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.drop_probability is not None:
                                    return True

                                if self.max_threshold is not None:
                                    return True

                                if self.min_threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred']['meta_info']


                        class HwWred(object):
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
                                self.parent = None
                                self.drop_probability = None
                                self.max_threshold = None
                                self.min_threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:hw-wred'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.drop_probability is not None:
                                    return True

                                if self.max_threshold is not None:
                                    return True

                                if self.min_threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:remote-class'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.class_id is not None:
                                return True

                            if self.class_name is not None:
                                return True

                            if self.cos_q is not None:
                                return True

                            if self.hardware_queue_limit is not None:
                                return True

                            if self.hw_wred is not None:
                                for child_ref in self.hw_wred:
                                    if child_ref._has_data():
                                        return True

                            if self.queue_limit is not None:
                                return True

                            if self.wred is not None:
                                for child_ref in self.wred:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                            return meta._meta_table['PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:remote-interface[Cisco-IOS-XR-ncs5500-qos-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.interface_name is not None:
                            return True

                        if self.interface_handle is not None:
                            return True

                        if self.number_of_classes is not None:
                            return True

                        if self.number_of_virtual_output_queues is not None:
                            return True

                        if self.policy_name is not None:
                            return True

                        if self.remote_class is not None:
                            for child_ref in self.remote_class:
                                if child_ref._has_data():
                                    return True

                        if self.virtual_output_queue_statistics_handle is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                        return meta._meta_table['PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-qos-oper:remote-interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.remote_interface is not None:
                        for child_ref in self.remote_interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                    return meta._meta_table['PlatformQos.Nodes.Node.RemoteInterfaces']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ncs5500-qos-oper:platform-qos/Cisco-IOS-XR-ncs5500-qos-oper:nodes/Cisco-IOS-XR-ncs5500-qos-oper:node[Cisco-IOS-XR-ncs5500-qos-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.node_name is not None:
                    return True

                if self.bundle_interfaces is not None and self.bundle_interfaces._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.remote_interfaces is not None and self.remote_interfaces._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                return meta._meta_table['PlatformQos.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ncs5500-qos-oper:platform-qos/Cisco-IOS-XR-ncs5500-qos-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
            return meta._meta_table['PlatformQos.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ncs5500-qos-oper:platform-qos'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['PlatformQos']['meta_info']



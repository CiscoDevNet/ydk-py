""" Cisco_IOS_XR_ncs5500_qos_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5500\-qos package operational data.

This module contains definitions
for the following management objects\:
  platform\-qos\: DNX QoS EA operational data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
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

    .. data:: ACTION_NONE = 0

    	None

    .. data:: ACTION_TRANSMIT = 1

    	Transmit

    .. data:: ACTION_DROP = 2

    	Drop

    .. data:: ACTION_MARK = 3

    	Mark

    """

    ACTION_NONE = 0

    ACTION_TRANSMIT = 1

    ACTION_DROP = 2

    ACTION_MARK = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowActionEnum']


class DnxQoseaShowHpLevelEnum(Enum):
    """
    DnxQoseaShowHpLevelEnum

    Priority level

    .. data:: HIGH_PRIORITY_LEVEL1 = 0

    	High priority queue level 1

    .. data:: HIGH_PRIORITY_LEVEL2 = 1

    	High priority queue level 2

    .. data:: HIGH_PRIORITY_LEVEL3 = 2

    	High priority queue level 3

    .. data:: HIGH_PRIORITY_LEVEL4 = 3

    	High priority queue level 4

    .. data:: HIGH_PRIORITY_LEVEL5 = 4

    	High priority queue level 5

    .. data:: HIGH_PRIORITY_LEVEL6 = 5

    	High priority queue level 6

    .. data:: HIGH_PRIORITY_LEVEL7 = 6

    	High priority queue level 7

    .. data:: UNKNOWN = 7

    	Unknown

    """

    HIGH_PRIORITY_LEVEL1 = 0

    HIGH_PRIORITY_LEVEL2 = 1

    HIGH_PRIORITY_LEVEL3 = 2

    HIGH_PRIORITY_LEVEL4 = 3

    HIGH_PRIORITY_LEVEL5 = 4

    HIGH_PRIORITY_LEVEL6 = 5

    HIGH_PRIORITY_LEVEL7 = 6

    UNKNOWN = 7


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowHpLevelEnum']


class DnxQoseaShowIntfStatusEnum(Enum):
    """
    DnxQoseaShowIntfStatusEnum

    Intf Status

    .. data:: STATE_UNKNOWN = 0

    	State is unknown

    .. data:: STATE_DOWN = 1

    	State is Down

    """

    STATE_UNKNOWN = 0

    STATE_DOWN = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowIntfStatusEnum']


class DnxQoseaShowLevelEnum(Enum):
    """
    DnxQoseaShowLevelEnum

    Level type

    .. data:: LEVEL1 = 0

    	QoS level1 class

    .. data:: LEVEL2 = 1

    	QoS level2 class

    .. data:: LEVEL3 = 2

    	QoS level3 class

    .. data:: LEVEL4 = 3

    	QoS level4 class

    .. data:: LEVEL5 = 4

    	QoS level5 class

    """

    LEVEL1 = 0

    LEVEL2 = 1

    LEVEL3 = 2

    LEVEL4 = 3

    LEVEL5 = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowLevelEnum']


class DnxQoseaShowMarkEnum(Enum):
    """
    DnxQoseaShowMarkEnum

    Mark type

    .. data:: MARK_NONE = 0

    	None

    .. data:: DSCP = 1

    	DSCP

    .. data:: PRECEDENCE = 2

    	Precedence

    .. data:: MPLS_TOPMOST = 3

    	MPLS topmost

    .. data:: MPLS_IMPOSITION = 4

    	MPLS imposition

    .. data:: QOS_GROUP = 5

    	Qos group

    .. data:: DISCARD_CLASS = 6

    	Discard class

    .. data:: COS = 7

    	COS

    .. data:: INNER_COS = 8

    	Inner COS

    .. data:: DSCP_TUNNEL = 9

    	DSCP tunnel

    .. data:: PRECEDENCE_TUNNEL = 10

    	Precedence tunnel

    """

    MARK_NONE = 0

    DSCP = 1

    PRECEDENCE = 2

    MPLS_TOPMOST = 3

    MPLS_IMPOSITION = 4

    QOS_GROUP = 5

    DISCARD_CLASS = 6

    COS = 7

    INNER_COS = 8

    DSCP_TUNNEL = 9

    PRECEDENCE_TUNNEL = 10


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowMarkEnum']


class DnxQoseaShowPolicyStatusEnum(Enum):
    """
    DnxQoseaShowPolicyStatusEnum

    Status

    .. data:: NO_ERROR = 0

    	No errors

    .. data:: POLICY_IN_RESET = 1

    	QoS policy is reset

    """

    NO_ERROR = 0

    POLICY_IN_RESET = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowPolicyStatusEnum']


class DnxQoseaShowPolicyUnitEnum(Enum):
    """
    DnxQoseaShowPolicyUnitEnum

    Policy parameter unit type

    .. data:: INVALID = 0

    	Invalid uint type

    .. data:: BYTES = 1

    	Units in bytes

    .. data:: KILO_BYTES = 2

    	Units in kilobytes

    .. data:: MEGA_BYTES = 3

    	Units in megabytes

    .. data:: GIGA_BYTES = 4

    	Units in gigabytes

    .. data:: BITS_PER_SECOND = 5

    	Units in bits per second

    .. data:: KILO_BITS_PER_SECOND = 6

    	Units in kilo bits per second

    .. data:: MEGA_BITS_PER_SECOND = 7

    	Units in mega bits per second

    .. data:: GIGA_BITS_PER_SECOND = 8

    	Units in giga bits per second

    .. data:: CELLS_PER_SECOND = 9

    	Units in cells per second

    .. data:: PACKETS_PER_SECOND = 10

    	Units in Packets Per Second

    .. data:: MICROSECONDS = 11

    	Units in microseconds

    .. data:: MILLISECONDS = 12

    	Units in milliseconds

    .. data:: PACKETS = 13

    	Units in packets

    .. data:: CELLS = 14

    	Units in cells

    .. data:: PERCENT = 15

    	Units in percentage

    .. data:: RATIO = 16

    	Units in ratio

    """

    INVALID = 0

    BYTES = 1

    KILO_BYTES = 2

    MEGA_BYTES = 3

    GIGA_BYTES = 4

    BITS_PER_SECOND = 5

    KILO_BITS_PER_SECOND = 6

    MEGA_BITS_PER_SECOND = 7

    GIGA_BITS_PER_SECOND = 8

    CELLS_PER_SECOND = 9

    PACKETS_PER_SECOND = 10

    MICROSECONDS = 11

    MILLISECONDS = 12

    PACKETS = 13

    CELLS = 14

    PERCENT = 15

    RATIO = 16


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowPolicyUnitEnum']


class DnxQoseaShowQueueEnum(Enum):
    """
    DnxQoseaShowQueueEnum

    Priority Queue Type

    .. data:: LOW_PRIORITY_DEFAULT_QUEUE = 0

    	Low priority default queue

    .. data:: LOW_PRIORITY_QUEUE = 1

    	Low priority queue

    .. data:: HIGH_PRIORITY_QUEUE = 2

    	High priority queue

    .. data:: UNKNOWN_QUEUE_TYPE = 3

    	Queue priority unknown

    """

    LOW_PRIORITY_DEFAULT_QUEUE = 0

    LOW_PRIORITY_QUEUE = 1

    HIGH_PRIORITY_QUEUE = 2

    UNKNOWN_QUEUE_TYPE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowQueueEnum']


class DnxQoseaShowWredEnum(Enum):
    """
    DnxQoseaShowWredEnum

    WRED type

    .. data:: WRED_COS = 0

    	WRED based on COS

    .. data:: WRED_DSCP = 1

    	WRED based on DSCP

    .. data:: WRED_PRECEDENCE = 2

    	WRED based on Precedence

    .. data:: WRED_DISCARD_CLASS = 3

    	WRED based on discard class

    .. data:: WRED_MPLS_EXP = 4

    	WRED based on MPLS EXP

    .. data:: RED_WITH_USER_MIN_MAX = 5

    	RED with user defined min and max

    .. data:: RED_WITH_DEFAULT_MIN_MAX = 6

    	RED with default min and max

    .. data:: WRED_INVALID = 7

    	Invalid

    """

    WRED_COS = 0

    WRED_DSCP = 1

    WRED_PRECEDENCE = 2

    WRED_DISCARD_CLASS = 3

    WRED_MPLS_EXP = 4

    RED_WITH_USER_MIN_MAX = 5

    RED_WITH_DEFAULT_MIN_MAX = 6

    WRED_INVALID = 7


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['DnxQoseaShowWredEnum']


class QosPolicyAccountEnumEnum(Enum):
    """
    QosPolicyAccountEnumEnum

    Qos policy account enum

    .. data:: QOS_SERV_POLICY_NO_AC_COUNT_PREF = 0

    	qos serv policy no ac count pref

    .. data:: QOS_SERV_POLICY_AC_COUNT_L2 = 1

    	qos serv policy ac count l2

    .. data:: QOS_SERV_POLICY_NO_AC_COUNT_L2 = 2

    	qos serv policy no ac count l2

    .. data:: QOS_SERV_POLICY_AC_COUNT_USER_DEF = 3

    	qos serv policy ac count user def

    .. data:: QOS_SERV_POLICY_AC_COUNT_L1 = 4

    	qos serv policy ac count l1

    """

    QOS_SERV_POLICY_NO_AC_COUNT_PREF = 0

    QOS_SERV_POLICY_AC_COUNT_L2 = 1

    QOS_SERV_POLICY_NO_AC_COUNT_L2 = 2

    QOS_SERV_POLICY_AC_COUNT_USER_DEF = 3

    QOS_SERV_POLICY_AC_COUNT_L1 = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['QosPolicyAccountEnumEnum']



class PlatformQos(object):
    """
    DNX QoS EA operational data
    
    .. attribute:: nodes
    
    	List of nodes with platform specific QoS configuration
    	**type**\: :py:class:`Nodes <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes>`
    
    

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
        	**type**\: list of :py:class:`Node <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node>`
        
        

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
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: bundle_interfaces
            
            	QoS list of bundle interfaces
            	**type**\: :py:class:`BundleInterfaces <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces>`
            
            .. attribute:: interfaces
            
            	QoS list of interfaces
            	**type**\: :py:class:`Interfaces <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces>`
            
            .. attribute:: remote_interfaces
            
            	QoS list of remote interfaces
            	**type**\: :py:class:`RemoteInterfaces <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces>`
            
            

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
                	**type**\: list of :py:class:`BundleInterface <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface>`
                
                

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
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: classes
                    
                    	QoS list of class names
                    	**type**\: :py:class:`Classes <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes>`
                    
                    .. attribute:: member_interfaces
                    
                    	QoS list of member interfaces
                    	**type**\: :py:class:`MemberInterfaces <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces>`
                    
                    .. attribute:: npu_id
                    
                    	NPU ID
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: policy_details
                    
                    	Policy Details
                    	**type**\: :py:class:`PolicyDetails <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails>`
                    
                    .. attribute:: qos_direction
                    
                    	The interface direction on which QoS is applied to
                    	**type**\: str
                    
                    

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
                        	**type**\: list of :py:class:`MemberInterface <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface>`
                        
                        

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
                            	**type**\: str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: classes
                            
                            	QoS list of class names
                            	**type**\: :py:class:`Classes <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes>`
                            
                            .. attribute:: policy_details
                            
                            	Policy Details
                            	**type**\: :py:class:`PolicyDetails <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails>`
                            
                            

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
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_handle
                                
                                	InterfaceHandle
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_status
                                
                                	Interface Status
                                	**type**\: :py:class:`DnxQoseaShowIntfStatusEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowIntfStatusEnum>`
                                
                                .. attribute:: npu_id
                                
                                	NPU ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                	**range:** 0..64
                                
                                .. attribute:: policy_status
                                
                                	Policy Status
                                	**type**\: :py:class:`DnxQoseaShowPolicyStatusEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyStatusEnum>`
                                
                                .. attribute:: stats_accounting_type
                                
                                	QoS Statistics Accounting Type
                                	**type**\: :py:class:`QosPolicyAccountEnumEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.QosPolicyAccountEnumEnum>`
                                
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
                                	**type**\: long
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails']['meta_info']


                            class Classes(object):
                                """
                                QoS list of class names
                                
                                .. attribute:: class_
                                
                                	QoS policy class
                                	**type**\: list of :py:class:`Class <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.class_ = YList()
                                    self.class_.parent = self
                                    self.class_.name = 'class_'


                                class Class(object):
                                    """
                                    QoS policy class
                                    
                                    .. attribute:: level_one_class_name  <key>
                                    
                                    	QoS policy class name at level 1
                                    	**type**\: str
                                    
                                    .. attribute:: class_level
                                    
                                    	Class level
                                    	**type**\: :py:class:`DnxQoseaShowLevelEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevelEnum>`
                                    
                                    .. attribute:: common_mark
                                    
                                    	Common mark
                                    	**type**\: list of :py:class:`CommonMark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.CommonMark>`
                                    
                                    .. attribute:: config_excess_bandwidth_percent
                                    
                                    	Configured excess bandwidth percentage
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: config_excess_bandwidth_unit
                                    
                                    	Configured excess bandwidth unit
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: config_max_rate
                                    
                                    	Configured maximum rate
                                    	**type**\: :py:class:`ConfigMaxRate <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigMaxRate>`
                                    
                                    .. attribute:: config_min_rate
                                    
                                    	Configured minimum rate
                                    	**type**\: :py:class:`ConfigMinRate <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigMinRate>`
                                    
                                    .. attribute:: config_policer_average_rate
                                    
                                    	Configured policer average rate
                                    	**type**\: :py:class:`ConfigPolicerAverageRate <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerAverageRate>`
                                    
                                    .. attribute:: config_policer_conform_burst
                                    
                                    	Configured policer conform burst
                                    	**type**\: :py:class:`ConfigPolicerConformBurst <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerConformBurst>`
                                    
                                    .. attribute:: config_policer_excess_burst
                                    
                                    	Configured policer excess burst
                                    	**type**\: :py:class:`ConfigPolicerExcessBurst <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerExcessBurst>`
                                    
                                    .. attribute:: config_policer_peak_rate
                                    
                                    	Config policer peak rate
                                    	**type**\: :py:class:`ConfigPolicerPeakRate <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerPeakRate>`
                                    
                                    .. attribute:: config_queue_limit
                                    
                                    	Configured queue limit
                                    	**type**\: :py:class:`ConfigQueueLimit <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigQueueLimit>`
                                    
                                    .. attribute:: conform_action
                                    
                                    	Conform action
                                    	**type**\: :py:class:`ConformAction <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConformAction>`
                                    
                                    .. attribute:: egress_queue_id
                                    
                                    	Egress Queue ID
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: exceed_action
                                    
                                    	Exceed action
                                    	**type**\: :py:class:`ExceedAction <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ExceedAction>`
                                    
                                    .. attribute:: hardware_excess_bandwidth_weight
                                    
                                    	Hardware excess bandwidth weight
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_max_rate_kbps
                                    
                                    	Hardware maximum rate in kbps
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_min_rate_kbps
                                    
                                    	Hardware minimum rate in kbps
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_policer_average_rate_kbps
                                    
                                    	Hardware policer average in kbps
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
                                    
                                    .. attribute:: hardware_policer_peak_rate_kbps
                                    
                                    	Hardware policer peak rate
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_queue_limit_bytes
                                    
                                    	Hardware queue limit in bytes
                                    	**type**\: long
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: hardware_queue_limit_microseconds
                                    
                                    	Hardware queue limit in microseconds
                                    	**type**\: long
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: ip_mark
                                    
                                    	IP mark
                                    	**type**\: list of :py:class:`IpMark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.IpMark>`
                                    
                                    .. attribute:: level_two_class_name
                                    
                                    	QoS policy child class name at level 2
                                    	**type**\: str
                                    
                                    .. attribute:: mpls_mark
                                    
                                    	MPLS mark
                                    	**type**\: list of :py:class:`MplsMark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.MplsMark>`
                                    
                                    .. attribute:: network_min_bandwidth_kbps
                                    
                                    	Network minimum Bandwith
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policer_bucket_id
                                    
                                    	PolicerBucketID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policer_stats_handle
                                    
                                    	PolicerStatsHandle
                                    	**type**\: long
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: priority_level
                                    
                                    	Priority level
                                    	**type**\: :py:class:`DnxQoseaShowHpLevelEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevelEnum>`
                                    
                                    .. attribute:: queue_type
                                    
                                    	Queue type
                                    	**type**\: :py:class:`DnxQoseaShowQueueEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueueEnum>`
                                    
                                    .. attribute:: violate_action
                                    
                                    	Violate action
                                    	**type**\: :py:class:`ViolateAction <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ViolateAction>`
                                    
                                    .. attribute:: wred
                                    
                                    	WRED parameters
                                    	**type**\: list of :py:class:`Wred <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred>`
                                    
                                    

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
                                        self.config_max_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigMaxRate()
                                        self.config_max_rate.parent = self
                                        self.config_min_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigMinRate()
                                        self.config_min_rate.parent = self
                                        self.config_policer_average_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerAverageRate()
                                        self.config_policer_average_rate.parent = self
                                        self.config_policer_conform_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerConformBurst()
                                        self.config_policer_conform_burst.parent = self
                                        self.config_policer_excess_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerExcessBurst()
                                        self.config_policer_excess_burst.parent = self
                                        self.config_policer_peak_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerPeakRate()
                                        self.config_policer_peak_rate.parent = self
                                        self.config_queue_limit = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigQueueLimit()
                                        self.config_queue_limit.parent = self
                                        self.conform_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConformAction()
                                        self.conform_action.parent = self
                                        self.egress_queue_id = None
                                        self.exceed_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ExceedAction()
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
                                        self.violate_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ViolateAction()
                                        self.violate_action.parent = self
                                        self.wred = YList()
                                        self.wred.parent = self
                                        self.wred.name = 'wred'


                                    class ConfigMaxRate(object):
                                        """
                                        Configured maximum rate
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigMaxRate']['meta_info']


                                    class ConfigMinRate(object):
                                        """
                                        Configured minimum rate
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigMinRate']['meta_info']


                                    class ConfigQueueLimit(object):
                                        """
                                        Configured queue limit
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigQueueLimit']['meta_info']


                                    class ConfigPolicerAverageRate(object):
                                        """
                                        Configured policer average rate
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerAverageRate']['meta_info']


                                    class ConfigPolicerPeakRate(object):
                                        """
                                        Config policer peak rate
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerPeakRate']['meta_info']


                                    class ConfigPolicerConformBurst(object):
                                        """
                                        Configured policer conform burst
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerConformBurst']['meta_info']


                                    class ConfigPolicerExcessBurst(object):
                                        """
                                        Configured policer excess burst
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerExcessBurst']['meta_info']


                                    class ConformAction(object):
                                        """
                                        Conform action
                                        
                                        .. attribute:: action_type
                                        
                                        	Policer action type
                                        	**type**\: :py:class:`DnxQoseaShowActionEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                        
                                        .. attribute:: mark
                                        
                                        	Action mark
                                        	**type**\: list of :py:class:`Mark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConformAction.Mark>`
                                        
                                        

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
                                            	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\: int
                                            
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
                                                from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConformAction.Mark']['meta_info']

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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConformAction']['meta_info']


                                    class ExceedAction(object):
                                        """
                                        Exceed action
                                        
                                        .. attribute:: action_type
                                        
                                        	Policer action type
                                        	**type**\: :py:class:`DnxQoseaShowActionEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                        
                                        .. attribute:: mark
                                        
                                        	Action mark
                                        	**type**\: list of :py:class:`Mark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ExceedAction.Mark>`
                                        
                                        

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
                                            	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\: int
                                            
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
                                                from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ExceedAction.Mark']['meta_info']

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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ExceedAction']['meta_info']


                                    class ViolateAction(object):
                                        """
                                        Violate action
                                        
                                        .. attribute:: action_type
                                        
                                        	Policer action type
                                        	**type**\: :py:class:`DnxQoseaShowActionEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                        
                                        .. attribute:: mark
                                        
                                        	Action mark
                                        	**type**\: list of :py:class:`Mark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ViolateAction.Mark>`
                                        
                                        

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
                                            	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\: int
                                            
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
                                                from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ViolateAction.Mark']['meta_info']

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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ViolateAction']['meta_info']


                                    class IpMark(object):
                                        """
                                        IP mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.IpMark']['meta_info']


                                    class CommonMark(object):
                                        """
                                        Common mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.CommonMark']['meta_info']


                                    class MplsMark(object):
                                        """
                                        MPLS mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.MplsMark']['meta_info']


                                    class Wred(object):
                                        """
                                        WRED parameters
                                        
                                        .. attribute:: config_max_threshold
                                        
                                        	Configured maximum threshold
                                        	**type**\: :py:class:`ConfigMaxThreshold <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.ConfigMaxThreshold>`
                                        
                                        .. attribute:: config_min_threshold
                                        
                                        	Configured minimum threshold
                                        	**type**\: :py:class:`ConfigMinThreshold <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.ConfigMinThreshold>`
                                        
                                        .. attribute:: first_segment
                                        
                                        	First segment
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: hardware_max_threshold_bytes
                                        
                                        	Hardware maximum threshold
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: hardware_min_threshold_bytes
                                        
                                        	Hardware minimum threshold
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: segment_size
                                        
                                        	Segment size
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: wred_match_type
                                        
                                        	WREDMatchType
                                        	**type**\: :py:class:`DnxQoseaShowWredEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWredEnum>`
                                        
                                        .. attribute:: wred_match_value
                                        
                                        	WRED match values
                                        	**type**\: :py:class:`WredMatchValue <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.WredMatchValue>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.config_max_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.ConfigMaxThreshold()
                                            self.config_max_threshold.parent = self
                                            self.config_min_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.ConfigMinThreshold()
                                            self.config_min_threshold.parent = self
                                            self.first_segment = None
                                            self.hardware_max_threshold_bytes = None
                                            self.hardware_min_threshold_bytes = None
                                            self.segment_size = None
                                            self.wred_match_type = None
                                            self.wred_match_value = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.WredMatchValue()
                                            self.wred_match_value.parent = self


                                        class WredMatchValue(object):
                                            """
                                            WRED match values
                                            
                                            .. attribute:: dnx_qosea_show_red_match_value
                                            
                                            	dnx qosea show red match value
                                            	**type**\: list of :py:class:`DnxQoseaShowRedMatchValue <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                            
                                            

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
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: range_start
                                                
                                                	Start value of a range
                                                	**type**\: int
                                                
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
                                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue']['meta_info']

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
                                                from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.WredMatchValue']['meta_info']


                                        class ConfigMinThreshold(object):
                                            """
                                            Configured minimum threshold
                                            
                                            .. attribute:: policy_unit
                                            
                                            	Policy unit
                                            	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                            
                                            .. attribute:: policy_value
                                            
                                            	Policy value
                                            	**type**\: int
                                            
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
                                                from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.ConfigMinThreshold']['meta_info']


                                        class ConfigMaxThreshold(object):
                                            """
                                            Configured maximum threshold
                                            
                                            .. attribute:: policy_unit
                                            
                                            	Policy unit
                                            	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                            
                                            .. attribute:: policy_value
                                            
                                            	Policy value
                                            	**type**\: int
                                            
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
                                                from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.ConfigMaxThreshold']['meta_info']

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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred']['meta_info']

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
                                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info']

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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
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
                                from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
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
                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces']['meta_info']


                    class PolicyDetails(object):
                        """
                        Policy Details
                        
                        .. attribute:: interface_bandwidth_kbps
                        
                        	Interface Bandwidth (in kbps)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_handle
                        
                        	InterfaceHandle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_status
                        
                        	Interface Status
                        	**type**\: :py:class:`DnxQoseaShowIntfStatusEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowIntfStatusEnum>`
                        
                        .. attribute:: npu_id
                        
                        	NPU ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: policy_name
                        
                        	Policy name
                        	**type**\: str
                        
                        	**range:** 0..64
                        
                        .. attribute:: policy_status
                        
                        	Policy Status
                        	**type**\: :py:class:`DnxQoseaShowPolicyStatusEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyStatusEnum>`
                        
                        .. attribute:: stats_accounting_type
                        
                        	QoS Statistics Accounting Type
                        	**type**\: :py:class:`QosPolicyAccountEnumEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.QosPolicyAccountEnumEnum>`
                        
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
                        	**type**\: long
                        
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
                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails']['meta_info']


                    class Classes(object):
                        """
                        QoS list of class names
                        
                        .. attribute:: class_
                        
                        	QoS policy class
                        	**type**\: list of :py:class:`Class <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.class_ = YList()
                            self.class_.parent = self
                            self.class_.name = 'class_'


                        class Class(object):
                            """
                            QoS policy class
                            
                            .. attribute:: level_one_class_name  <key>
                            
                            	QoS policy class name at level 1
                            	**type**\: str
                            
                            .. attribute:: class_level
                            
                            	Class level
                            	**type**\: :py:class:`DnxQoseaShowLevelEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevelEnum>`
                            
                            .. attribute:: common_mark
                            
                            	Common mark
                            	**type**\: list of :py:class:`CommonMark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.CommonMark>`
                            
                            .. attribute:: config_excess_bandwidth_percent
                            
                            	Configured excess bandwidth percentage
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: config_excess_bandwidth_unit
                            
                            	Configured excess bandwidth unit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: config_max_rate
                            
                            	Configured maximum rate
                            	**type**\: :py:class:`ConfigMaxRate <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigMaxRate>`
                            
                            .. attribute:: config_min_rate
                            
                            	Configured minimum rate
                            	**type**\: :py:class:`ConfigMinRate <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigMinRate>`
                            
                            .. attribute:: config_policer_average_rate
                            
                            	Configured policer average rate
                            	**type**\: :py:class:`ConfigPolicerAverageRate <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerAverageRate>`
                            
                            .. attribute:: config_policer_conform_burst
                            
                            	Configured policer conform burst
                            	**type**\: :py:class:`ConfigPolicerConformBurst <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerConformBurst>`
                            
                            .. attribute:: config_policer_excess_burst
                            
                            	Configured policer excess burst
                            	**type**\: :py:class:`ConfigPolicerExcessBurst <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerExcessBurst>`
                            
                            .. attribute:: config_policer_peak_rate
                            
                            	Config policer peak rate
                            	**type**\: :py:class:`ConfigPolicerPeakRate <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerPeakRate>`
                            
                            .. attribute:: config_queue_limit
                            
                            	Configured queue limit
                            	**type**\: :py:class:`ConfigQueueLimit <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigQueueLimit>`
                            
                            .. attribute:: conform_action
                            
                            	Conform action
                            	**type**\: :py:class:`ConformAction <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConformAction>`
                            
                            .. attribute:: egress_queue_id
                            
                            	Egress Queue ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: exceed_action
                            
                            	Exceed action
                            	**type**\: :py:class:`ExceedAction <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ExceedAction>`
                            
                            .. attribute:: hardware_excess_bandwidth_weight
                            
                            	Hardware excess bandwidth weight
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_max_rate_kbps
                            
                            	Hardware maximum rate in kbps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_min_rate_kbps
                            
                            	Hardware minimum rate in kbps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_policer_average_rate_kbps
                            
                            	Hardware policer average in kbps
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
                            
                            .. attribute:: hardware_policer_peak_rate_kbps
                            
                            	Hardware policer peak rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_queue_limit_bytes
                            
                            	Hardware queue limit in bytes
                            	**type**\: long
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: hardware_queue_limit_microseconds
                            
                            	Hardware queue limit in microseconds
                            	**type**\: long
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ip_mark
                            
                            	IP mark
                            	**type**\: list of :py:class:`IpMark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.IpMark>`
                            
                            .. attribute:: level_two_class_name
                            
                            	QoS policy child class name at level 2
                            	**type**\: str
                            
                            .. attribute:: mpls_mark
                            
                            	MPLS mark
                            	**type**\: list of :py:class:`MplsMark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.MplsMark>`
                            
                            .. attribute:: network_min_bandwidth_kbps
                            
                            	Network minimum Bandwith
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: policer_bucket_id
                            
                            	PolicerBucketID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: policer_stats_handle
                            
                            	PolicerStatsHandle
                            	**type**\: long
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: priority_level
                            
                            	Priority level
                            	**type**\: :py:class:`DnxQoseaShowHpLevelEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevelEnum>`
                            
                            .. attribute:: queue_type
                            
                            	Queue type
                            	**type**\: :py:class:`DnxQoseaShowQueueEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueueEnum>`
                            
                            .. attribute:: violate_action
                            
                            	Violate action
                            	**type**\: :py:class:`ViolateAction <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ViolateAction>`
                            
                            .. attribute:: wred
                            
                            	WRED parameters
                            	**type**\: list of :py:class:`Wred <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred>`
                            
                            

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
                                self.config_max_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigMaxRate()
                                self.config_max_rate.parent = self
                                self.config_min_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigMinRate()
                                self.config_min_rate.parent = self
                                self.config_policer_average_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerAverageRate()
                                self.config_policer_average_rate.parent = self
                                self.config_policer_conform_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerConformBurst()
                                self.config_policer_conform_burst.parent = self
                                self.config_policer_excess_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerExcessBurst()
                                self.config_policer_excess_burst.parent = self
                                self.config_policer_peak_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerPeakRate()
                                self.config_policer_peak_rate.parent = self
                                self.config_queue_limit = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigQueueLimit()
                                self.config_queue_limit.parent = self
                                self.conform_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConformAction()
                                self.conform_action.parent = self
                                self.egress_queue_id = None
                                self.exceed_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ExceedAction()
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
                                self.violate_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ViolateAction()
                                self.violate_action.parent = self
                                self.wred = YList()
                                self.wred.parent = self
                                self.wred.name = 'wred'


                            class ConfigMaxRate(object):
                                """
                                Configured maximum rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigMaxRate']['meta_info']


                            class ConfigMinRate(object):
                                """
                                Configured minimum rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigMinRate']['meta_info']


                            class ConfigQueueLimit(object):
                                """
                                Configured queue limit
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigQueueLimit']['meta_info']


                            class ConfigPolicerAverageRate(object):
                                """
                                Configured policer average rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerAverageRate']['meta_info']


                            class ConfigPolicerPeakRate(object):
                                """
                                Config policer peak rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerPeakRate']['meta_info']


                            class ConfigPolicerConformBurst(object):
                                """
                                Configured policer conform burst
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerConformBurst']['meta_info']


                            class ConfigPolicerExcessBurst(object):
                                """
                                Configured policer excess burst
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerExcessBurst']['meta_info']


                            class ConformAction(object):
                                """
                                Conform action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\: :py:class:`DnxQoseaShowActionEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of :py:class:`Mark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConformAction.Mark>`
                                
                                

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
                                    	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
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
                                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConformAction.Mark']['meta_info']

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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConformAction']['meta_info']


                            class ExceedAction(object):
                                """
                                Exceed action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\: :py:class:`DnxQoseaShowActionEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of :py:class:`Mark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ExceedAction.Mark>`
                                
                                

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
                                    	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
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
                                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ExceedAction.Mark']['meta_info']

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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ExceedAction']['meta_info']


                            class ViolateAction(object):
                                """
                                Violate action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\: :py:class:`DnxQoseaShowActionEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of :py:class:`Mark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ViolateAction.Mark>`
                                
                                

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
                                    	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
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
                                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ViolateAction.Mark']['meta_info']

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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ViolateAction']['meta_info']


                            class IpMark(object):
                                """
                                IP mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.IpMark']['meta_info']


                            class CommonMark(object):
                                """
                                Common mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.CommonMark']['meta_info']


                            class MplsMark(object):
                                """
                                MPLS mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.MplsMark']['meta_info']


                            class Wred(object):
                                """
                                WRED parameters
                                
                                .. attribute:: config_max_threshold
                                
                                	Configured maximum threshold
                                	**type**\: :py:class:`ConfigMaxThreshold <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.ConfigMaxThreshold>`
                                
                                .. attribute:: config_min_threshold
                                
                                	Configured minimum threshold
                                	**type**\: :py:class:`ConfigMinThreshold <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.ConfigMinThreshold>`
                                
                                .. attribute:: first_segment
                                
                                	First segment
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: hardware_max_threshold_bytes
                                
                                	Hardware maximum threshold
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_min_threshold_bytes
                                
                                	Hardware minimum threshold
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: segment_size
                                
                                	Segment size
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: wred_match_type
                                
                                	WREDMatchType
                                	**type**\: :py:class:`DnxQoseaShowWredEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWredEnum>`
                                
                                .. attribute:: wred_match_value
                                
                                	WRED match values
                                	**type**\: :py:class:`WredMatchValue <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.WredMatchValue>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.config_max_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.ConfigMaxThreshold()
                                    self.config_max_threshold.parent = self
                                    self.config_min_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.ConfigMinThreshold()
                                    self.config_min_threshold.parent = self
                                    self.first_segment = None
                                    self.hardware_max_threshold_bytes = None
                                    self.hardware_min_threshold_bytes = None
                                    self.segment_size = None
                                    self.wred_match_type = None
                                    self.wred_match_value = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.WredMatchValue()
                                    self.wred_match_value.parent = self


                                class WredMatchValue(object):
                                    """
                                    WRED match values
                                    
                                    .. attribute:: dnx_qosea_show_red_match_value
                                    
                                    	dnx qosea show red match value
                                    	**type**\: list of :py:class:`DnxQoseaShowRedMatchValue <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                    
                                    

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
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: range_start
                                        
                                        	Start value of a range
                                        	**type**\: int
                                        
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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue']['meta_info']

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
                                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.WredMatchValue']['meta_info']


                                class ConfigMinThreshold(object):
                                    """
                                    Configured minimum threshold
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
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
                                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.ConfigMinThreshold']['meta_info']


                                class ConfigMaxThreshold(object):
                                    """
                                    Configured maximum threshold
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
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
                                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.ConfigMaxThreshold']['meta_info']

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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred']['meta_info']

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
                                from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info']

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
                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
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
                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
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
                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces']['meta_info']


            class Interfaces(object):
                """
                QoS list of interfaces
                
                .. attribute:: interface
                
                	QoS interface names
                	**type**\: list of :py:class:`Interface <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface>`
                
                

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
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: classes
                    
                    	QoS list of class names
                    	**type**\: :py:class:`Classes <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes>`
                    
                    .. attribute:: policy_details
                    
                    	Policy Details
                    	**type**\: :py:class:`PolicyDetails <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails>`
                    
                    .. attribute:: qos_direction
                    
                    	The interface direction on which QoS is applied to
                    	**type**\: str
                    
                    

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
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_handle
                        
                        	InterfaceHandle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_status
                        
                        	Interface Status
                        	**type**\: :py:class:`DnxQoseaShowIntfStatusEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowIntfStatusEnum>`
                        
                        .. attribute:: npu_id
                        
                        	NPU ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: policy_name
                        
                        	Policy name
                        	**type**\: str
                        
                        	**range:** 0..64
                        
                        .. attribute:: policy_status
                        
                        	Policy Status
                        	**type**\: :py:class:`DnxQoseaShowPolicyStatusEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyStatusEnum>`
                        
                        .. attribute:: stats_accounting_type
                        
                        	QoS Statistics Accounting Type
                        	**type**\: :py:class:`QosPolicyAccountEnumEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.QosPolicyAccountEnumEnum>`
                        
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
                        	**type**\: long
                        
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
                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails']['meta_info']


                    class Classes(object):
                        """
                        QoS list of class names
                        
                        .. attribute:: class_
                        
                        	QoS policy class
                        	**type**\: list of :py:class:`Class <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.class_ = YList()
                            self.class_.parent = self
                            self.class_.name = 'class_'


                        class Class(object):
                            """
                            QoS policy class
                            
                            .. attribute:: level_one_class_name  <key>
                            
                            	QoS policy class name at level 1
                            	**type**\: str
                            
                            .. attribute:: class_level
                            
                            	Class level
                            	**type**\: :py:class:`DnxQoseaShowLevelEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevelEnum>`
                            
                            .. attribute:: common_mark
                            
                            	Common mark
                            	**type**\: list of :py:class:`CommonMark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.CommonMark>`
                            
                            .. attribute:: config_excess_bandwidth_percent
                            
                            	Configured excess bandwidth percentage
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: config_excess_bandwidth_unit
                            
                            	Configured excess bandwidth unit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: config_max_rate
                            
                            	Configured maximum rate
                            	**type**\: :py:class:`ConfigMaxRate <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigMaxRate>`
                            
                            .. attribute:: config_min_rate
                            
                            	Configured minimum rate
                            	**type**\: :py:class:`ConfigMinRate <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigMinRate>`
                            
                            .. attribute:: config_policer_average_rate
                            
                            	Configured policer average rate
                            	**type**\: :py:class:`ConfigPolicerAverageRate <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerAverageRate>`
                            
                            .. attribute:: config_policer_conform_burst
                            
                            	Configured policer conform burst
                            	**type**\: :py:class:`ConfigPolicerConformBurst <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerConformBurst>`
                            
                            .. attribute:: config_policer_excess_burst
                            
                            	Configured policer excess burst
                            	**type**\: :py:class:`ConfigPolicerExcessBurst <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerExcessBurst>`
                            
                            .. attribute:: config_policer_peak_rate
                            
                            	Config policer peak rate
                            	**type**\: :py:class:`ConfigPolicerPeakRate <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerPeakRate>`
                            
                            .. attribute:: config_queue_limit
                            
                            	Configured queue limit
                            	**type**\: :py:class:`ConfigQueueLimit <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigQueueLimit>`
                            
                            .. attribute:: conform_action
                            
                            	Conform action
                            	**type**\: :py:class:`ConformAction <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConformAction>`
                            
                            .. attribute:: egress_queue_id
                            
                            	Egress Queue ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: exceed_action
                            
                            	Exceed action
                            	**type**\: :py:class:`ExceedAction <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ExceedAction>`
                            
                            .. attribute:: hardware_excess_bandwidth_weight
                            
                            	Hardware excess bandwidth weight
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_max_rate_kbps
                            
                            	Hardware maximum rate in kbps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_min_rate_kbps
                            
                            	Hardware minimum rate in kbps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_policer_average_rate_kbps
                            
                            	Hardware policer average in kbps
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
                            
                            .. attribute:: hardware_policer_peak_rate_kbps
                            
                            	Hardware policer peak rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_queue_limit_bytes
                            
                            	Hardware queue limit in bytes
                            	**type**\: long
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: hardware_queue_limit_microseconds
                            
                            	Hardware queue limit in microseconds
                            	**type**\: long
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ip_mark
                            
                            	IP mark
                            	**type**\: list of :py:class:`IpMark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.IpMark>`
                            
                            .. attribute:: level_two_class_name
                            
                            	QoS policy child class name at level 2
                            	**type**\: str
                            
                            .. attribute:: mpls_mark
                            
                            	MPLS mark
                            	**type**\: list of :py:class:`MplsMark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.MplsMark>`
                            
                            .. attribute:: network_min_bandwidth_kbps
                            
                            	Network minimum Bandwith
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: policer_bucket_id
                            
                            	PolicerBucketID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: policer_stats_handle
                            
                            	PolicerStatsHandle
                            	**type**\: long
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: priority_level
                            
                            	Priority level
                            	**type**\: :py:class:`DnxQoseaShowHpLevelEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevelEnum>`
                            
                            .. attribute:: queue_type
                            
                            	Queue type
                            	**type**\: :py:class:`DnxQoseaShowQueueEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueueEnum>`
                            
                            .. attribute:: violate_action
                            
                            	Violate action
                            	**type**\: :py:class:`ViolateAction <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ViolateAction>`
                            
                            .. attribute:: wred
                            
                            	WRED parameters
                            	**type**\: list of :py:class:`Wred <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred>`
                            
                            

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
                                self.config_max_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigMaxRate()
                                self.config_max_rate.parent = self
                                self.config_min_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigMinRate()
                                self.config_min_rate.parent = self
                                self.config_policer_average_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerAverageRate()
                                self.config_policer_average_rate.parent = self
                                self.config_policer_conform_burst = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerConformBurst()
                                self.config_policer_conform_burst.parent = self
                                self.config_policer_excess_burst = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerExcessBurst()
                                self.config_policer_excess_burst.parent = self
                                self.config_policer_peak_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerPeakRate()
                                self.config_policer_peak_rate.parent = self
                                self.config_queue_limit = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigQueueLimit()
                                self.config_queue_limit.parent = self
                                self.conform_action = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConformAction()
                                self.conform_action.parent = self
                                self.egress_queue_id = None
                                self.exceed_action = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ExceedAction()
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
                                self.violate_action = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ViolateAction()
                                self.violate_action.parent = self
                                self.wred = YList()
                                self.wred.parent = self
                                self.wred.name = 'wred'


                            class ConfigMaxRate(object):
                                """
                                Configured maximum rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigMaxRate']['meta_info']


                            class ConfigMinRate(object):
                                """
                                Configured minimum rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigMinRate']['meta_info']


                            class ConfigQueueLimit(object):
                                """
                                Configured queue limit
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigQueueLimit']['meta_info']


                            class ConfigPolicerAverageRate(object):
                                """
                                Configured policer average rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerAverageRate']['meta_info']


                            class ConfigPolicerPeakRate(object):
                                """
                                Config policer peak rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerPeakRate']['meta_info']


                            class ConfigPolicerConformBurst(object):
                                """
                                Configured policer conform burst
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerConformBurst']['meta_info']


                            class ConfigPolicerExcessBurst(object):
                                """
                                Configured policer excess burst
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerExcessBurst']['meta_info']


                            class ConformAction(object):
                                """
                                Conform action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\: :py:class:`DnxQoseaShowActionEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of :py:class:`Mark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConformAction.Mark>`
                                
                                

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
                                    	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
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
                                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConformAction.Mark']['meta_info']

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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConformAction']['meta_info']


                            class ExceedAction(object):
                                """
                                Exceed action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\: :py:class:`DnxQoseaShowActionEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of :py:class:`Mark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ExceedAction.Mark>`
                                
                                

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
                                    	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
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
                                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ExceedAction.Mark']['meta_info']

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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ExceedAction']['meta_info']


                            class ViolateAction(object):
                                """
                                Violate action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\: :py:class:`DnxQoseaShowActionEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowActionEnum>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of :py:class:`Mark <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ViolateAction.Mark>`
                                
                                

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
                                    	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
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
                                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ViolateAction.Mark']['meta_info']

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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ViolateAction']['meta_info']


                            class IpMark(object):
                                """
                                IP mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.IpMark']['meta_info']


                            class CommonMark(object):
                                """
                                Common mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.CommonMark']['meta_info']


                            class MplsMark(object):
                                """
                                MPLS mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\: :py:class:`DnxQoseaShowMarkEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMarkEnum>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\: int
                                
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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.MplsMark']['meta_info']


                            class Wred(object):
                                """
                                WRED parameters
                                
                                .. attribute:: config_max_threshold
                                
                                	Configured maximum threshold
                                	**type**\: :py:class:`ConfigMaxThreshold <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.ConfigMaxThreshold>`
                                
                                .. attribute:: config_min_threshold
                                
                                	Configured minimum threshold
                                	**type**\: :py:class:`ConfigMinThreshold <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.ConfigMinThreshold>`
                                
                                .. attribute:: first_segment
                                
                                	First segment
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: hardware_max_threshold_bytes
                                
                                	Hardware maximum threshold
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_min_threshold_bytes
                                
                                	Hardware minimum threshold
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: segment_size
                                
                                	Segment size
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: wred_match_type
                                
                                	WREDMatchType
                                	**type**\: :py:class:`DnxQoseaShowWredEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWredEnum>`
                                
                                .. attribute:: wred_match_value
                                
                                	WRED match values
                                	**type**\: :py:class:`WredMatchValue <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.WredMatchValue>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.config_max_threshold = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.ConfigMaxThreshold()
                                    self.config_max_threshold.parent = self
                                    self.config_min_threshold = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.ConfigMinThreshold()
                                    self.config_min_threshold.parent = self
                                    self.first_segment = None
                                    self.hardware_max_threshold_bytes = None
                                    self.hardware_min_threshold_bytes = None
                                    self.segment_size = None
                                    self.wred_match_type = None
                                    self.wred_match_value = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.WredMatchValue()
                                    self.wred_match_value.parent = self


                                class WredMatchValue(object):
                                    """
                                    WRED match values
                                    
                                    .. attribute:: dnx_qosea_show_red_match_value
                                    
                                    	dnx qosea show red match value
                                    	**type**\: list of :py:class:`DnxQoseaShowRedMatchValue <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                    
                                    

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
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: range_start
                                        
                                        	Start value of a range
                                        	**type**\: int
                                        
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
                                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue']['meta_info']

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
                                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.WredMatchValue']['meta_info']


                                class ConfigMinThreshold(object):
                                    """
                                    Configured minimum threshold
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
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
                                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.ConfigMinThreshold']['meta_info']


                                class ConfigMaxThreshold(object):
                                    """
                                    Configured maximum threshold
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\: :py:class:`DnxQoseaShowPolicyUnitEnum <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyUnitEnum>`
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
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
                                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.ConfigMaxThreshold']['meta_info']

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
                                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred']['meta_info']

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
                                from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info']

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
                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
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
                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
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
                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces']['meta_info']


            class RemoteInterfaces(object):
                """
                QoS list of remote interfaces
                
                .. attribute:: remote_interface
                
                	QoS remote interface names
                	**type**\: list of :py:class:`RemoteInterface <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface>`
                
                

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
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface_handle
                    
                    	Interface Handle
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_classes
                    
                    	Number of Classes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_virtual_output_queues
                    
                    	Number of Virtual Output Queues
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: policy_name
                    
                    	Policy Name
                    	**type**\: str
                    
                    	**range:** 0..64
                    
                    .. attribute:: remote_class
                    
                    	Remote Class array
                    	**type**\: list of :py:class:`RemoteClass <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass>`
                    
                    .. attribute:: virtual_output_queue_statistics_handle
                    
                    	Virtual output queue statistics handle
                    	**type**\: long
                    
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
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cos_q
                        
                        	Class of Service Queue
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hardware_queue_limit
                        
                        	Hardware queue limit in bytes
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hw_wred
                        
                        	Hardware WRED profiles
                        	**type**\: list of :py:class:`HwWred <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred>`
                        
                        .. attribute:: queue_limit
                        
                        	Default/Configured queue limit in bytes
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wred
                        
                        	Default/Configured WRED profiles
                        	**type**\: list of :py:class:`Wred <ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.class_id = None
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
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: max_threshold
                            
                            	Maximum Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: min_threshold
                            
                            	Minimum Threshold
                            	**type**\: int
                            
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
                                from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred']['meta_info']


                        class HwWred(object):
                            """
                            Hardware WRED profiles
                            
                            .. attribute:: drop_probability
                            
                            	Drop Probability
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: max_threshold
                            
                            	Maximum Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: min_threshold
                            
                            	Minimum Threshold
                            	**type**\: int
                            
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
                                from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
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
                            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
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
                        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
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
                    from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
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
                from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
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
            from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
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
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_oper as meta
        return meta._meta_table['PlatformQos']['meta_info']



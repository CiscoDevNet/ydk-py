""" Cisco_IOS_XR_skp_qos_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR skp\-qos package operational data.

This module contains definitions
for the following management objects\:
  platform\-qos\: QoS Skywarp platform operational data 
  platform\-qos\-ea\: platform qos ea

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class ActionEnum(Enum):
    """
    ActionEnum

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

    police_transmit = 0

    police_set_transmit = 1

    police_drop = 2

    police_unknown = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['ActionEnum']


class ActionOpcodeEnum(Enum):
    """
    ActionOpcodeEnum

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

    precedence = 0

    dscp = 1

    discard_class = 2

    qos_group = 3

    cos_inner = 4

    cos = 5

    exp_top = 6

    exp_imp = 7

    tunnel_precedence = 8

    tunnel_dscp = 9

    itag_dei = 10

    itag_cos = 11

    cos_imposition = 12

    dei_imposition = 13

    dei = 14

    no_marking = 15


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['ActionOpcodeEnum']


class CacStateEnum(Enum):
    """
    CacStateEnum

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

    unknown = 0

    admit = 1

    redirect = 2

    ubrl = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['CacStateEnum']


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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['PolicyParamUnitEnum']


class PolicyStateEnum(Enum):
    """
    PolicyStateEnum

    Different Interface states

    .. data:: active = 0

    	active

    .. data:: suspended = 1

    	suspended

    """

    active = 0

    suspended = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['PolicyStateEnum']


class QosUnitEnum(Enum):
    """
    QosUnitEnum

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

    invalid = 0

    bytes = 1

    kilobytes = 2

    megabytes = 3

    gigabytes = 4

    bps = 5

    kbps = 6

    mbps = 7

    gbps = 8

    cells_per_second = 9

    packets_per_second = 10

    microsecond = 11

    millisecond = 12

    packets = 13

    cells = 14

    percentage = 15

    ratio = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['QosUnitEnum']


class TbAlgorithmEnum(Enum):
    """
    TbAlgorithmEnum

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

    inactive = 0

    single = 1

    single_rate_tcm = 2

    two_rate_tcm = 3

    mef_tcm = 4

    dummy = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['TbAlgorithmEnum']


class WredEnum(Enum):
    """
    WredEnum

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

    wred_cos_cmd = 0

    wred_dscp_cmd = 1

    wred_precedence_cmd = 2

    wred_discard_class_cmd = 3

    wred_mpls_exp_cmd = 4

    red_with_user_min_max = 5

    red_with_default_min_max = 6

    wred_dei_cmd = 7

    wred_ecn_cmd = 8

    wred_invalid_cmd = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['WredEnum']



class PlatformQos(object):
    """
    QoS Skywarp platform operational data 
    
    .. attribute:: nodes
    
    	List of nodes with platform specific QoS configuration
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes>`
    
    

    """

    _prefix = 'skp-qos-oper'
    _revision = '2016-02-18'

    def __init__(self):
        self.nodes = PlatformQos.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        List of nodes with platform specific QoS
        configuration
        
        .. attribute:: node
        
        	Node with platform specific QoS configuration
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node>`
        
        

        """

        _prefix = 'skp-qos-oper'
        _revision = '2016-02-18'

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
            	**type**\:   :py:class:`BundleInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces>`
            
            .. attribute:: capability
            
            	QoS system capability
            	**type**\:   :py:class:`Capability <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Capability>`
            
            .. attribute:: interfaces
            
            	QoS list of interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'skp-qos-oper'
            _revision = '2016-02-18'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.bundle_interfaces = PlatformQos.Nodes.Node.BundleInterfaces()
                self.bundle_interfaces.parent = self
                self.capability = PlatformQos.Nodes.Node.Capability()
                self.capability.parent = self
                self.interfaces = PlatformQos.Nodes.Node.Interfaces()
                self.interfaces.parent = self


            class BundleInterfaces(object):
                """
                QoS list of bundle interfaces
                
                .. attribute:: bundle_interface
                
                	QoS interface name
                	**type**\: list of    :py:class:`BundleInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface>`
                
                

                """

                _prefix = 'skp-qos-oper'
                _revision = '2016-02-18'

                def __init__(self):
                    self.parent = None
                    self.bundle_interface = YList()
                    self.bundle_interface.parent = self
                    self.bundle_interface.name = 'bundle_interface'


                class BundleInterface(object):
                    """
                    QoS interface name
                    
                    .. attribute:: interface_name  <key>
                    
                    	Bundle interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: member_interfaces
                    
                    	QoS list of member interfaces
                    	**type**\:   :py:class:`MemberInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces>`
                    
                    

                    """

                    _prefix = 'skp-qos-oper'
                    _revision = '2016-02-18'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.member_interfaces = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces()
                        self.member_interfaces.parent = self


                    class MemberInterfaces(object):
                        """
                        QoS list of member interfaces
                        
                        .. attribute:: member_interface
                        
                        	QoS interface name
                        	**type**\: list of    :py:class:`MemberInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface>`
                        
                        

                        """

                        _prefix = 'skp-qos-oper'
                        _revision = '2016-02-18'

                        def __init__(self):
                            self.parent = None
                            self.member_interface = YList()
                            self.member_interface.parent = self
                            self.member_interface.name = 'member_interface'


                        class MemberInterface(object):
                            """
                            QoS interface name
                            
                            .. attribute:: interface_name  <key>
                            
                            	Memeber interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: bundle_input
                            
                            	QoS policy direction input
                            	**type**\:   :py:class:`BundleInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput>`
                            
                            .. attribute:: bundle_output
                            
                            	QoS policy direction output
                            	**type**\:   :py:class:`BundleOutput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput>`
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None
                                self.bundle_input = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput()
                                self.bundle_input.parent = self
                                self.bundle_output = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput()
                                self.bundle_output.parent = self


                            class BundleInput(object):
                                """
                                QoS policy direction input
                                
                                .. attribute:: header
                                
                                	QoS EA policy header
                                	**type**\:   :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Header>`
                                
                                .. attribute:: interface_parameters
                                
                                	QoS Interface Parameters
                                	**type**\:   :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters>`
                                
                                .. attribute:: skywarp_qos_policy_class
                                
                                	Skywarp QoS policy class details
                                	**type**\:   :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass>`
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.header = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Header()
                                    self.header.parent = self
                                    self.interface_parameters = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters()
                                    self.interface_parameters.parent = self
                                    self.skywarp_qos_policy_class = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass()
                                    self.skywarp_qos_policy_class.parent = self


                                class Header(object):
                                    """
                                    QoS EA policy header
                                    
                                    .. attribute:: classes
                                    
                                    	Number of classes
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: direction
                                    
                                    	Direction
                                    	**type**\:  str
                                    
                                    	**length:** 0..11
                                    
                                    .. attribute:: interface_name
                                    
                                    	Interface Name
                                    	**type**\:  str
                                    
                                    	**length:** 0..101
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\:  str
                                    
                                    	**length:** 0..65
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.classes = None
                                        self.direction = None
                                        self.interface_name = None
                                        self.policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:header'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.classes is not None:
                                            return True

                                        if self.direction is not None:
                                            return True

                                        if self.interface_name is not None:
                                            return True

                                        if self.policy_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Header']['meta_info']


                                class InterfaceParameters(object):
                                    """
                                    QoS Interface Parameters
                                    
                                    .. attribute:: interface_config_rate
                                    
                                    	Interface Configured Rate
                                    	**type**\:   :py:class:`InterfaceConfigRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceConfigRate>`
                                    
                                    .. attribute:: interface_program_rate
                                    
                                    	Interface Programmed Rate
                                    	**type**\:   :py:class:`InterfaceProgramRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceProgramRate>`
                                    
                                    .. attribute:: port_shaper_rate
                                    
                                    	Port Shaper Rate
                                    	**type**\:   :py:class:`PortShaperRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.PortShaperRate>`
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.interface_config_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceConfigRate()
                                        self.interface_config_rate.parent = self
                                        self.interface_program_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceProgramRate()
                                        self.interface_program_rate.parent = self
                                        self.port_shaper_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.PortShaperRate()
                                        self.port_shaper_rate.parent = self


                                    class InterfaceConfigRate(object):
                                        """
                                        Interface Configured Rate
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-config-rate'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceConfigRate']['meta_info']


                                    class InterfaceProgramRate(object):
                                        """
                                        Interface Programmed Rate
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-program-rate'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceProgramRate']['meta_info']


                                    class PortShaperRate(object):
                                        """
                                        Port Shaper Rate
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:port-shaper-rate'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.PortShaperRate']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-parameters'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.interface_config_rate is not None and self.interface_config_rate._has_data():
                                            return True

                                        if self.interface_program_rate is not None and self.interface_program_rate._has_data():
                                            return True

                                        if self.port_shaper_rate is not None and self.port_shaper_rate._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters']['meta_info']


                                class SkywarpQosPolicyClass(object):
                                    """
                                    Skywarp QoS policy class details
                                    
                                    .. attribute:: qos_show_pclass_st
                                    
                                    	qos show pclass st
                                    	**type**\: list of    :py:class:`QosShowPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt>`
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.qos_show_pclass_st = YList()
                                        self.qos_show_pclass_st.parent = self
                                        self.qos_show_pclass_st.name = 'qos_show_pclass_st'


                                    class QosShowPclassSt(object):
                                        """
                                        qos show pclass st
                                        
                                        .. attribute:: class_level
                                        
                                        	Class level
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: class_name
                                        
                                        	Class name
                                        	**type**\:  str
                                        
                                        	**length:** 0..65
                                        
                                        .. attribute:: marking
                                        
                                        	QoS Mark parameters
                                        	**type**\:   :py:class:`Marking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking>`
                                        
                                        .. attribute:: police
                                        
                                        	QoS Policer parameters
                                        	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police>`
                                        
                                        .. attribute:: queue
                                        
                                        	QoS Queue parameters
                                        	**type**\:   :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Queue>`
                                        
                                        .. attribute:: shape
                                        
                                        	QoS EA Shaper parameters
                                        	**type**\:   :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape>`
                                        
                                        .. attribute:: wfq
                                        
                                        	QoS WFQ parameters
                                        	**type**\:   :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq>`
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.class_level = None
                                            self.class_name = None
                                            self.marking = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking()
                                            self.marking.parent = self
                                            self.police = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police()
                                            self.police.parent = self
                                            self.queue = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Queue()
                                            self.queue.parent = self
                                            self.shape = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape()
                                            self.shape.parent = self
                                            self.wfq = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq()
                                            self.wfq.parent = self


                                        class Queue(object):
                                            """
                                            QoS Queue parameters
                                            
                                            .. attribute:: queue_id
                                            
                                            	Queue ID
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: queue_type
                                            
                                            	Queue Type
                                            	**type**\:  str
                                            
                                            	**length:** 0..101
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.queue_id = None
                                                self.queue_type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:queue'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.queue_id is not None:
                                                    return True

                                                if self.queue_type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Queue']['meta_info']


                                        class Shape(object):
                                            """
                                            QoS EA Shaper parameters
                                            
                                            .. attribute:: pbs
                                            
                                            	PBS in bytes
                                            	**type**\:   :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs>`
                                            
                                            .. attribute:: pir
                                            
                                            	PIR in kbps
                                            	**type**\:   :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir>`
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.pbs = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs()
                                                self.pbs.parent = self
                                                self.pir = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir()
                                                self.pir.parent = self


                                            class Pir(object):
                                                """
                                                PIR in kbps
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pir'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir']['meta_info']


                                            class Pbs(object):
                                                """
                                                PBS in bytes
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pbs'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:shape'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.pbs is not None and self.pbs._has_data():
                                                    return True

                                                if self.pir is not None and self.pir._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']


                                        class Wfq(object):
                                            """
                                            QoS WFQ parameters
                                            
                                            .. attribute:: committed_weight
                                            
                                            	Committed Weight
                                            	**type**\:   :py:class:`CommittedWeight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight>`
                                            
                                            .. attribute:: excess_weight
                                            
                                            	Excess Weight
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: programmed_wfq
                                            
                                            	QoS Programmed WFQ parameters
                                            	**type**\:   :py:class:`ProgrammedWfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq>`
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.committed_weight = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight()
                                                self.committed_weight.parent = self
                                                self.excess_weight = None
                                                self.programmed_wfq = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq()
                                                self.programmed_wfq.parent = self


                                            class CommittedWeight(object):
                                                """
                                                Committed Weight
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:committed-weight'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight']['meta_info']


                                            class ProgrammedWfq(object):
                                                """
                                                QoS Programmed WFQ parameters
                                                
                                                .. attribute:: bandwidth
                                                
                                                	Bandwidth
                                                	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth>`
                                                
                                                .. attribute:: excess_ratio
                                                
                                                	Excess Ratio
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                .. attribute:: sum_of_bandwidth
                                                
                                                	Sum of Bandwidth
                                                	**type**\:   :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth>`
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.bandwidth = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth()
                                                    self.bandwidth.parent = self
                                                    self.excess_ratio = None
                                                    self.sum_of_bandwidth = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth()
                                                    self.sum_of_bandwidth.parent = self


                                                class Bandwidth(object):
                                                    """
                                                    Bandwidth
                                                    
                                                    .. attribute:: unit
                                                    
                                                    	Config unit
                                                    	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                    
                                                    .. attribute:: value
                                                    
                                                    	Config value
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.unit = None
                                                        self.value = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bandwidth'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.unit is not None:
                                                            return True

                                                        if self.value is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth']['meta_info']


                                                class SumOfBandwidth(object):
                                                    """
                                                    Sum of Bandwidth
                                                    
                                                    .. attribute:: unit
                                                    
                                                    	Config unit
                                                    	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                    
                                                    .. attribute:: value
                                                    
                                                    	Config value
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.unit = None
                                                        self.value = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:sum-of-bandwidth'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.unit is not None:
                                                            return True

                                                        if self.value is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:programmed-wfq'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.bandwidth is not None and self.bandwidth._has_data():
                                                        return True

                                                    if self.excess_ratio is not None:
                                                        return True

                                                    if self.sum_of_bandwidth is not None and self.sum_of_bandwidth._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:wfq'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.committed_weight is not None and self.committed_weight._has_data():
                                                    return True

                                                if self.excess_weight is not None:
                                                    return True

                                                if self.programmed_wfq is not None and self.programmed_wfq._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']


                                        class Police(object):
                                            """
                                            QoS Policer parameters
                                            
                                            .. attribute:: cbs
                                            
                                            	CBS
                                            	**type**\:   :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs>`
                                            
                                            .. attribute:: cir
                                            
                                            	CIR
                                            	**type**\:   :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir>`
                                            
                                            .. attribute:: policer_id
                                            
                                            	policer ID
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: policer_type
                                            
                                            	Policer type
                                            	**type**\:   :py:class:`TbAlgorithmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithmEnum>`
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.cbs = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs()
                                                self.cbs.parent = self
                                                self.cir = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir()
                                                self.cir.parent = self
                                                self.policer_id = None
                                                self.policer_type = None


                                            class Cir(object):
                                                """
                                                CIR
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cir'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir']['meta_info']


                                            class Cbs(object):
                                                """
                                                CBS
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cbs'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.cbs is not None and self.cbs._has_data():
                                                    return True

                                                if self.cir is not None and self.cir._has_data():
                                                    return True

                                                if self.policer_id is not None:
                                                    return True

                                                if self.policer_type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']


                                        class Marking(object):
                                            """
                                            QoS Mark parameters
                                            
                                            .. attribute:: mark_only
                                            
                                            	Mark Only
                                            	**type**\:   :py:class:`MarkOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly>`
                                            
                                            .. attribute:: police_conform
                                            
                                            	Police conform mark
                                            	**type**\:   :py:class:`PoliceConform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform>`
                                            
                                            .. attribute:: police_exceed
                                            
                                            	Police exceed mark
                                            	**type**\:   :py:class:`PoliceExceed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed>`
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.mark_only = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly()
                                                self.mark_only.parent = self
                                                self.police_conform = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform()
                                                self.police_conform.parent = self
                                                self.police_exceed = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed()
                                                self.police_exceed.parent = self


                                            class MarkOnly(object):
                                                """
                                                Mark Only
                                                
                                                .. attribute:: action_type
                                                
                                                	Action type
                                                	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionEnum>`
                                                
                                                .. attribute:: mark_detail
                                                
                                                	Mark value
                                                	**type**\: list of    :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail>`
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.action_type = None
                                                    self.mark_detail = YList()
                                                    self.mark_detail.parent = self
                                                    self.mark_detail.name = 'mark_detail'


                                                class MarkDetail(object):
                                                    """
                                                    Mark value
                                                    
                                                    .. attribute:: action_opcode
                                                    
                                                    	Action opcode
                                                    	**type**\:   :py:class:`ActionOpcodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcodeEnum>`
                                                    
                                                    .. attribute:: mark_value
                                                    
                                                    	Mark value
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.action_opcode = None
                                                        self.mark_value = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-detail'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.action_opcode is not None:
                                                            return True

                                                        if self.mark_value is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-only'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.action_type is not None:
                                                        return True

                                                    if self.mark_detail is not None:
                                                        for child_ref in self.mark_detail:
                                                            if child_ref._has_data():
                                                                return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info']


                                            class PoliceConform(object):
                                                """
                                                Police conform mark
                                                
                                                .. attribute:: action_type
                                                
                                                	Action type
                                                	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionEnum>`
                                                
                                                .. attribute:: mark_detail
                                                
                                                	Mark value
                                                	**type**\: list of    :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail>`
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.action_type = None
                                                    self.mark_detail = YList()
                                                    self.mark_detail.parent = self
                                                    self.mark_detail.name = 'mark_detail'


                                                class MarkDetail(object):
                                                    """
                                                    Mark value
                                                    
                                                    .. attribute:: action_opcode
                                                    
                                                    	Action opcode
                                                    	**type**\:   :py:class:`ActionOpcodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcodeEnum>`
                                                    
                                                    .. attribute:: mark_value
                                                    
                                                    	Mark value
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.action_opcode = None
                                                        self.mark_value = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-detail'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.action_opcode is not None:
                                                            return True

                                                        if self.mark_value is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police-conform'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.action_type is not None:
                                                        return True

                                                    if self.mark_detail is not None:
                                                        for child_ref in self.mark_detail:
                                                            if child_ref._has_data():
                                                                return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info']


                                            class PoliceExceed(object):
                                                """
                                                Police exceed mark
                                                
                                                .. attribute:: action_type
                                                
                                                	Action type
                                                	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionEnum>`
                                                
                                                .. attribute:: mark_detail
                                                
                                                	Mark value
                                                	**type**\: list of    :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail>`
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.action_type = None
                                                    self.mark_detail = YList()
                                                    self.mark_detail.parent = self
                                                    self.mark_detail.name = 'mark_detail'


                                                class MarkDetail(object):
                                                    """
                                                    Mark value
                                                    
                                                    .. attribute:: action_opcode
                                                    
                                                    	Action opcode
                                                    	**type**\:   :py:class:`ActionOpcodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcodeEnum>`
                                                    
                                                    .. attribute:: mark_value
                                                    
                                                    	Mark value
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.action_opcode = None
                                                        self.mark_value = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-detail'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.action_opcode is not None:
                                                            return True

                                                        if self.mark_value is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police-exceed'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.action_type is not None:
                                                        return True

                                                    if self.mark_detail is not None:
                                                        for child_ref in self.mark_detail:
                                                            if child_ref._has_data():
                                                                return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:marking'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.mark_only is not None and self.mark_only._has_data():
                                                    return True

                                                if self.police_conform is not None and self.police_conform._has_data():
                                                    return True

                                                if self.police_exceed is not None and self.police_exceed._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:qos-show-pclass-st'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.class_level is not None:
                                                return True

                                            if self.class_name is not None:
                                                return True

                                            if self.marking is not None and self.marking._has_data():
                                                return True

                                            if self.police is not None and self.police._has_data():
                                                return True

                                            if self.queue is not None and self.queue._has_data():
                                                return True

                                            if self.shape is not None and self.shape._has_data():
                                                return True

                                            if self.wfq is not None and self.wfq._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:skywarp-qos-policy-class'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.qos_show_pclass_st is not None:
                                            for child_ref in self.qos_show_pclass_st:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bundle-input'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.header is not None and self.header._has_data():
                                        return True

                                    if self.interface_parameters is not None and self.interface_parameters._has_data():
                                        return True

                                    if self.skywarp_qos_policy_class is not None and self.skywarp_qos_policy_class._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput']['meta_info']


                            class BundleOutput(object):
                                """
                                QoS policy direction output
                                
                                .. attribute:: header
                                
                                	QoS EA policy header
                                	**type**\:   :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Header>`
                                
                                .. attribute:: interface_parameters
                                
                                	QoS Interface Parameters
                                	**type**\:   :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters>`
                                
                                .. attribute:: skywarp_qos_policy_class
                                
                                	Skywarp QoS policy class details
                                	**type**\:   :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass>`
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.header = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Header()
                                    self.header.parent = self
                                    self.interface_parameters = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters()
                                    self.interface_parameters.parent = self
                                    self.skywarp_qos_policy_class = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass()
                                    self.skywarp_qos_policy_class.parent = self


                                class Header(object):
                                    """
                                    QoS EA policy header
                                    
                                    .. attribute:: classes
                                    
                                    	Number of classes
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: direction
                                    
                                    	Direction
                                    	**type**\:  str
                                    
                                    	**length:** 0..11
                                    
                                    .. attribute:: interface_name
                                    
                                    	Interface Name
                                    	**type**\:  str
                                    
                                    	**length:** 0..101
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\:  str
                                    
                                    	**length:** 0..65
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.classes = None
                                        self.direction = None
                                        self.interface_name = None
                                        self.policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:header'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.classes is not None:
                                            return True

                                        if self.direction is not None:
                                            return True

                                        if self.interface_name is not None:
                                            return True

                                        if self.policy_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Header']['meta_info']


                                class InterfaceParameters(object):
                                    """
                                    QoS Interface Parameters
                                    
                                    .. attribute:: interface_config_rate
                                    
                                    	Interface Configured Rate
                                    	**type**\:   :py:class:`InterfaceConfigRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceConfigRate>`
                                    
                                    .. attribute:: interface_program_rate
                                    
                                    	Interface Programmed Rate
                                    	**type**\:   :py:class:`InterfaceProgramRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceProgramRate>`
                                    
                                    .. attribute:: port_shaper_rate
                                    
                                    	Port Shaper Rate
                                    	**type**\:   :py:class:`PortShaperRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.PortShaperRate>`
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.interface_config_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceConfigRate()
                                        self.interface_config_rate.parent = self
                                        self.interface_program_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceProgramRate()
                                        self.interface_program_rate.parent = self
                                        self.port_shaper_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.PortShaperRate()
                                        self.port_shaper_rate.parent = self


                                    class InterfaceConfigRate(object):
                                        """
                                        Interface Configured Rate
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-config-rate'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceConfigRate']['meta_info']


                                    class InterfaceProgramRate(object):
                                        """
                                        Interface Programmed Rate
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-program-rate'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceProgramRate']['meta_info']


                                    class PortShaperRate(object):
                                        """
                                        Port Shaper Rate
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:port-shaper-rate'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.PortShaperRate']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-parameters'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.interface_config_rate is not None and self.interface_config_rate._has_data():
                                            return True

                                        if self.interface_program_rate is not None and self.interface_program_rate._has_data():
                                            return True

                                        if self.port_shaper_rate is not None and self.port_shaper_rate._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters']['meta_info']


                                class SkywarpQosPolicyClass(object):
                                    """
                                    Skywarp QoS policy class details
                                    
                                    .. attribute:: qos_show_pclass_st
                                    
                                    	qos show pclass st
                                    	**type**\: list of    :py:class:`QosShowPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt>`
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.qos_show_pclass_st = YList()
                                        self.qos_show_pclass_st.parent = self
                                        self.qos_show_pclass_st.name = 'qos_show_pclass_st'


                                    class QosShowPclassSt(object):
                                        """
                                        qos show pclass st
                                        
                                        .. attribute:: class_level
                                        
                                        	Class level
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: class_name
                                        
                                        	Class name
                                        	**type**\:  str
                                        
                                        	**length:** 0..65
                                        
                                        .. attribute:: marking
                                        
                                        	QoS Mark parameters
                                        	**type**\:   :py:class:`Marking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking>`
                                        
                                        .. attribute:: police
                                        
                                        	QoS Policer parameters
                                        	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police>`
                                        
                                        .. attribute:: queue
                                        
                                        	QoS Queue parameters
                                        	**type**\:   :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Queue>`
                                        
                                        .. attribute:: shape
                                        
                                        	QoS EA Shaper parameters
                                        	**type**\:   :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape>`
                                        
                                        .. attribute:: wfq
                                        
                                        	QoS WFQ parameters
                                        	**type**\:   :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq>`
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.class_level = None
                                            self.class_name = None
                                            self.marking = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking()
                                            self.marking.parent = self
                                            self.police = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police()
                                            self.police.parent = self
                                            self.queue = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Queue()
                                            self.queue.parent = self
                                            self.shape = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape()
                                            self.shape.parent = self
                                            self.wfq = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq()
                                            self.wfq.parent = self


                                        class Queue(object):
                                            """
                                            QoS Queue parameters
                                            
                                            .. attribute:: queue_id
                                            
                                            	Queue ID
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: queue_type
                                            
                                            	Queue Type
                                            	**type**\:  str
                                            
                                            	**length:** 0..101
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.queue_id = None
                                                self.queue_type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:queue'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.queue_id is not None:
                                                    return True

                                                if self.queue_type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Queue']['meta_info']


                                        class Shape(object):
                                            """
                                            QoS EA Shaper parameters
                                            
                                            .. attribute:: pbs
                                            
                                            	PBS in bytes
                                            	**type**\:   :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs>`
                                            
                                            .. attribute:: pir
                                            
                                            	PIR in kbps
                                            	**type**\:   :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir>`
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.pbs = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs()
                                                self.pbs.parent = self
                                                self.pir = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir()
                                                self.pir.parent = self


                                            class Pir(object):
                                                """
                                                PIR in kbps
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pir'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir']['meta_info']


                                            class Pbs(object):
                                                """
                                                PBS in bytes
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pbs'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:shape'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.pbs is not None and self.pbs._has_data():
                                                    return True

                                                if self.pir is not None and self.pir._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']


                                        class Wfq(object):
                                            """
                                            QoS WFQ parameters
                                            
                                            .. attribute:: committed_weight
                                            
                                            	Committed Weight
                                            	**type**\:   :py:class:`CommittedWeight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight>`
                                            
                                            .. attribute:: excess_weight
                                            
                                            	Excess Weight
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: programmed_wfq
                                            
                                            	QoS Programmed WFQ parameters
                                            	**type**\:   :py:class:`ProgrammedWfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq>`
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.committed_weight = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight()
                                                self.committed_weight.parent = self
                                                self.excess_weight = None
                                                self.programmed_wfq = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq()
                                                self.programmed_wfq.parent = self


                                            class CommittedWeight(object):
                                                """
                                                Committed Weight
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:committed-weight'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight']['meta_info']


                                            class ProgrammedWfq(object):
                                                """
                                                QoS Programmed WFQ parameters
                                                
                                                .. attribute:: bandwidth
                                                
                                                	Bandwidth
                                                	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth>`
                                                
                                                .. attribute:: excess_ratio
                                                
                                                	Excess Ratio
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                .. attribute:: sum_of_bandwidth
                                                
                                                	Sum of Bandwidth
                                                	**type**\:   :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth>`
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.bandwidth = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth()
                                                    self.bandwidth.parent = self
                                                    self.excess_ratio = None
                                                    self.sum_of_bandwidth = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth()
                                                    self.sum_of_bandwidth.parent = self


                                                class Bandwidth(object):
                                                    """
                                                    Bandwidth
                                                    
                                                    .. attribute:: unit
                                                    
                                                    	Config unit
                                                    	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                    
                                                    .. attribute:: value
                                                    
                                                    	Config value
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.unit = None
                                                        self.value = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bandwidth'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.unit is not None:
                                                            return True

                                                        if self.value is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth']['meta_info']


                                                class SumOfBandwidth(object):
                                                    """
                                                    Sum of Bandwidth
                                                    
                                                    .. attribute:: unit
                                                    
                                                    	Config unit
                                                    	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                    
                                                    .. attribute:: value
                                                    
                                                    	Config value
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.unit = None
                                                        self.value = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:sum-of-bandwidth'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.unit is not None:
                                                            return True

                                                        if self.value is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:programmed-wfq'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.bandwidth is not None and self.bandwidth._has_data():
                                                        return True

                                                    if self.excess_ratio is not None:
                                                        return True

                                                    if self.sum_of_bandwidth is not None and self.sum_of_bandwidth._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:wfq'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.committed_weight is not None and self.committed_weight._has_data():
                                                    return True

                                                if self.excess_weight is not None:
                                                    return True

                                                if self.programmed_wfq is not None and self.programmed_wfq._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']


                                        class Police(object):
                                            """
                                            QoS Policer parameters
                                            
                                            .. attribute:: cbs
                                            
                                            	CBS
                                            	**type**\:   :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs>`
                                            
                                            .. attribute:: cir
                                            
                                            	CIR
                                            	**type**\:   :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir>`
                                            
                                            .. attribute:: policer_id
                                            
                                            	policer ID
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: policer_type
                                            
                                            	Policer type
                                            	**type**\:   :py:class:`TbAlgorithmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithmEnum>`
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.cbs = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs()
                                                self.cbs.parent = self
                                                self.cir = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir()
                                                self.cir.parent = self
                                                self.policer_id = None
                                                self.policer_type = None


                                            class Cir(object):
                                                """
                                                CIR
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cir'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir']['meta_info']


                                            class Cbs(object):
                                                """
                                                CBS
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cbs'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.cbs is not None and self.cbs._has_data():
                                                    return True

                                                if self.cir is not None and self.cir._has_data():
                                                    return True

                                                if self.policer_id is not None:
                                                    return True

                                                if self.policer_type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']


                                        class Marking(object):
                                            """
                                            QoS Mark parameters
                                            
                                            .. attribute:: mark_only
                                            
                                            	Mark Only
                                            	**type**\:   :py:class:`MarkOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly>`
                                            
                                            .. attribute:: police_conform
                                            
                                            	Police conform mark
                                            	**type**\:   :py:class:`PoliceConform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform>`
                                            
                                            .. attribute:: police_exceed
                                            
                                            	Police exceed mark
                                            	**type**\:   :py:class:`PoliceExceed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed>`
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.mark_only = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly()
                                                self.mark_only.parent = self
                                                self.police_conform = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform()
                                                self.police_conform.parent = self
                                                self.police_exceed = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed()
                                                self.police_exceed.parent = self


                                            class MarkOnly(object):
                                                """
                                                Mark Only
                                                
                                                .. attribute:: action_type
                                                
                                                	Action type
                                                	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionEnum>`
                                                
                                                .. attribute:: mark_detail
                                                
                                                	Mark value
                                                	**type**\: list of    :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail>`
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.action_type = None
                                                    self.mark_detail = YList()
                                                    self.mark_detail.parent = self
                                                    self.mark_detail.name = 'mark_detail'


                                                class MarkDetail(object):
                                                    """
                                                    Mark value
                                                    
                                                    .. attribute:: action_opcode
                                                    
                                                    	Action opcode
                                                    	**type**\:   :py:class:`ActionOpcodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcodeEnum>`
                                                    
                                                    .. attribute:: mark_value
                                                    
                                                    	Mark value
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.action_opcode = None
                                                        self.mark_value = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-detail'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.action_opcode is not None:
                                                            return True

                                                        if self.mark_value is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-only'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.action_type is not None:
                                                        return True

                                                    if self.mark_detail is not None:
                                                        for child_ref in self.mark_detail:
                                                            if child_ref._has_data():
                                                                return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info']


                                            class PoliceConform(object):
                                                """
                                                Police conform mark
                                                
                                                .. attribute:: action_type
                                                
                                                	Action type
                                                	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionEnum>`
                                                
                                                .. attribute:: mark_detail
                                                
                                                	Mark value
                                                	**type**\: list of    :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail>`
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.action_type = None
                                                    self.mark_detail = YList()
                                                    self.mark_detail.parent = self
                                                    self.mark_detail.name = 'mark_detail'


                                                class MarkDetail(object):
                                                    """
                                                    Mark value
                                                    
                                                    .. attribute:: action_opcode
                                                    
                                                    	Action opcode
                                                    	**type**\:   :py:class:`ActionOpcodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcodeEnum>`
                                                    
                                                    .. attribute:: mark_value
                                                    
                                                    	Mark value
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.action_opcode = None
                                                        self.mark_value = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-detail'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.action_opcode is not None:
                                                            return True

                                                        if self.mark_value is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police-conform'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.action_type is not None:
                                                        return True

                                                    if self.mark_detail is not None:
                                                        for child_ref in self.mark_detail:
                                                            if child_ref._has_data():
                                                                return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info']


                                            class PoliceExceed(object):
                                                """
                                                Police exceed mark
                                                
                                                .. attribute:: action_type
                                                
                                                	Action type
                                                	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionEnum>`
                                                
                                                .. attribute:: mark_detail
                                                
                                                	Mark value
                                                	**type**\: list of    :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail>`
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.action_type = None
                                                    self.mark_detail = YList()
                                                    self.mark_detail.parent = self
                                                    self.mark_detail.name = 'mark_detail'


                                                class MarkDetail(object):
                                                    """
                                                    Mark value
                                                    
                                                    .. attribute:: action_opcode
                                                    
                                                    	Action opcode
                                                    	**type**\:   :py:class:`ActionOpcodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcodeEnum>`
                                                    
                                                    .. attribute:: mark_value
                                                    
                                                    	Mark value
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.action_opcode = None
                                                        self.mark_value = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-detail'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.action_opcode is not None:
                                                            return True

                                                        if self.mark_value is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police-exceed'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.action_type is not None:
                                                        return True

                                                    if self.mark_detail is not None:
                                                        for child_ref in self.mark_detail:
                                                            if child_ref._has_data():
                                                                return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:marking'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.mark_only is not None and self.mark_only._has_data():
                                                    return True

                                                if self.police_conform is not None and self.police_conform._has_data():
                                                    return True

                                                if self.police_exceed is not None and self.police_exceed._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:qos-show-pclass-st'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.class_level is not None:
                                                return True

                                            if self.class_name is not None:
                                                return True

                                            if self.marking is not None and self.marking._has_data():
                                                return True

                                            if self.police is not None and self.police._has_data():
                                                return True

                                            if self.queue is not None and self.queue._has_data():
                                                return True

                                            if self.shape is not None and self.shape._has_data():
                                                return True

                                            if self.wfq is not None and self.wfq._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:skywarp-qos-policy-class'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.qos_show_pclass_st is not None:
                                            for child_ref in self.qos_show_pclass_st:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bundle-output'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.header is not None and self.header._has_data():
                                        return True

                                    if self.interface_parameters is not None and self.interface_parameters._has_data():
                                        return True

                                    if self.skywarp_qos_policy_class is not None and self.skywarp_qos_policy_class._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.interface_name is None:
                                    raise YPYModelError('Key property interface_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:member-interface[Cisco-IOS-XR-skp-qos-oper:interface-name = ' + str(self.interface_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.interface_name is not None:
                                    return True

                                if self.bundle_input is not None and self.bundle_input._has_data():
                                    return True

                                if self.bundle_output is not None and self.bundle_output._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:member-interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.member_interface is not None:
                                for child_ref in self.member_interface:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bundle-interface[Cisco-IOS-XR-skp-qos-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.member_interfaces is not None and self.member_interfaces._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bundle-interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bundle_interface is not None:
                        for child_ref in self.bundle_interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces']['meta_info']


            class Capability(object):
                """
                QoS system capability
                
                .. attribute:: max_bundle_members
                
                	Maximum bundle members
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_classes_per_policy
                
                	Maximum classes per policy
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_classmap_name_length
                
                	Maximum classmap name length
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_marking_actions_per_class
                
                	Maximum marking action  per class
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_matches_per_class
                
                	Maximum matches per class
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_police_actions_per_class
                
                	Maximum police actions per class
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_policy_hierarchy
                
                	Maximum policy hierarchy
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_policy_maps
                
                	Maximum policy maps per system
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_policy_name_length
                
                	Maximum policy name length
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'skp-qos-oper'
                _revision = '2016-02-18'

                def __init__(self):
                    self.parent = None
                    self.max_bundle_members = None
                    self.max_classes_per_policy = None
                    self.max_classmap_name_length = None
                    self.max_marking_actions_per_class = None
                    self.max_matches_per_class = None
                    self.max_police_actions_per_class = None
                    self.max_policy_hierarchy = None
                    self.max_policy_maps = None
                    self.max_policy_name_length = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:capability'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.max_bundle_members is not None:
                        return True

                    if self.max_classes_per_policy is not None:
                        return True

                    if self.max_classmap_name_length is not None:
                        return True

                    if self.max_marking_actions_per_class is not None:
                        return True

                    if self.max_matches_per_class is not None:
                        return True

                    if self.max_police_actions_per_class is not None:
                        return True

                    if self.max_policy_hierarchy is not None:
                        return True

                    if self.max_policy_maps is not None:
                        return True

                    if self.max_policy_name_length is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                    return meta._meta_table['PlatformQos.Nodes.Node.Capability']['meta_info']


            class Interfaces(object):
                """
                QoS list of interfaces
                
                .. attribute:: interface
                
                	QoS interface name
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'skp-qos-oper'
                _revision = '2016-02-18'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    QoS interface name
                    
                    .. attribute:: interface_name  <key>
                    
                    	The name of the interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: input
                    
                    	QoS policy direction ingress
                    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input>`
                    
                    .. attribute:: output
                    
                    	QoS policy direction egress
                    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output>`
                    
                    

                    """

                    _prefix = 'skp-qos-oper'
                    _revision = '2016-02-18'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.input = PlatformQos.Nodes.Node.Interfaces.Interface.Input()
                        self.input.parent = self
                        self.output = PlatformQos.Nodes.Node.Interfaces.Interface.Output()
                        self.output.parent = self


                    class Output(object):
                        """
                        QoS policy direction egress
                        
                        .. attribute:: header
                        
                        	QoS EA policy header
                        	**type**\:   :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.Header>`
                        
                        .. attribute:: interface_parameters
                        
                        	QoS Interface Parameters
                        	**type**\:   :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters>`
                        
                        .. attribute:: skywarp_qos_policy_class
                        
                        	Skywarp QoS policy class details
                        	**type**\:   :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass>`
                        
                        

                        """

                        _prefix = 'skp-qos-oper'
                        _revision = '2016-02-18'

                        def __init__(self):
                            self.parent = None
                            self.header = PlatformQos.Nodes.Node.Interfaces.Interface.Output.Header()
                            self.header.parent = self
                            self.interface_parameters = PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters()
                            self.interface_parameters.parent = self
                            self.skywarp_qos_policy_class = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass()
                            self.skywarp_qos_policy_class.parent = self


                        class Header(object):
                            """
                            QoS EA policy header
                            
                            .. attribute:: classes
                            
                            	Number of classes
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: direction
                            
                            	Direction
                            	**type**\:  str
                            
                            	**length:** 0..11
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            	**length:** 0..101
                            
                            .. attribute:: policy_name
                            
                            	Policy name
                            	**type**\:  str
                            
                            	**length:** 0..65
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                self.parent = None
                                self.classes = None
                                self.direction = None
                                self.interface_name = None
                                self.policy_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:header'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.classes is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.policy_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Header']['meta_info']


                        class InterfaceParameters(object):
                            """
                            QoS Interface Parameters
                            
                            .. attribute:: interface_config_rate
                            
                            	Interface Configured Rate
                            	**type**\:   :py:class:`InterfaceConfigRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceConfigRate>`
                            
                            .. attribute:: interface_program_rate
                            
                            	Interface Programmed Rate
                            	**type**\:   :py:class:`InterfaceProgramRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceProgramRate>`
                            
                            .. attribute:: port_shaper_rate
                            
                            	Port Shaper Rate
                            	**type**\:   :py:class:`PortShaperRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.PortShaperRate>`
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                self.parent = None
                                self.interface_config_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceConfigRate()
                                self.interface_config_rate.parent = self
                                self.interface_program_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceProgramRate()
                                self.interface_program_rate.parent = self
                                self.port_shaper_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.PortShaperRate()
                                self.port_shaper_rate.parent = self


                            class InterfaceConfigRate(object):
                                """
                                Interface Configured Rate
                                
                                .. attribute:: unit
                                
                                	Config unit
                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                
                                .. attribute:: value
                                
                                	Config value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.unit = None
                                    self.value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-config-rate'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.unit is not None:
                                        return True

                                    if self.value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceConfigRate']['meta_info']


                            class InterfaceProgramRate(object):
                                """
                                Interface Programmed Rate
                                
                                .. attribute:: unit
                                
                                	Config unit
                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                
                                .. attribute:: value
                                
                                	Config value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.unit = None
                                    self.value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-program-rate'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.unit is not None:
                                        return True

                                    if self.value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceProgramRate']['meta_info']


                            class PortShaperRate(object):
                                """
                                Port Shaper Rate
                                
                                .. attribute:: unit
                                
                                	Config unit
                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                
                                .. attribute:: value
                                
                                	Config value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.unit = None
                                    self.value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:port-shaper-rate'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.unit is not None:
                                        return True

                                    if self.value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.PortShaperRate']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-parameters'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.interface_config_rate is not None and self.interface_config_rate._has_data():
                                    return True

                                if self.interface_program_rate is not None and self.interface_program_rate._has_data():
                                    return True

                                if self.port_shaper_rate is not None and self.port_shaper_rate._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters']['meta_info']


                        class SkywarpQosPolicyClass(object):
                            """
                            Skywarp QoS policy class details
                            
                            .. attribute:: qos_show_pclass_st
                            
                            	qos show pclass st
                            	**type**\: list of    :py:class:`QosShowPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt>`
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                self.parent = None
                                self.qos_show_pclass_st = YList()
                                self.qos_show_pclass_st.parent = self
                                self.qos_show_pclass_st.name = 'qos_show_pclass_st'


                            class QosShowPclassSt(object):
                                """
                                qos show pclass st
                                
                                .. attribute:: class_level
                                
                                	Class level
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: class_name
                                
                                	Class name
                                	**type**\:  str
                                
                                	**length:** 0..65
                                
                                .. attribute:: marking
                                
                                	QoS Mark parameters
                                	**type**\:   :py:class:`Marking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking>`
                                
                                .. attribute:: police
                                
                                	QoS Policer parameters
                                	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police>`
                                
                                .. attribute:: queue
                                
                                	QoS Queue parameters
                                	**type**\:   :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Queue>`
                                
                                .. attribute:: shape
                                
                                	QoS EA Shaper parameters
                                	**type**\:   :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape>`
                                
                                .. attribute:: wfq
                                
                                	QoS WFQ parameters
                                	**type**\:   :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq>`
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.class_level = None
                                    self.class_name = None
                                    self.marking = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking()
                                    self.marking.parent = self
                                    self.police = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police()
                                    self.police.parent = self
                                    self.queue = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Queue()
                                    self.queue.parent = self
                                    self.shape = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape()
                                    self.shape.parent = self
                                    self.wfq = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq()
                                    self.wfq.parent = self


                                class Queue(object):
                                    """
                                    QoS Queue parameters
                                    
                                    .. attribute:: queue_id
                                    
                                    	Queue ID
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: queue_type
                                    
                                    	Queue Type
                                    	**type**\:  str
                                    
                                    	**length:** 0..101
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.queue_id = None
                                        self.queue_type = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:queue'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.queue_id is not None:
                                            return True

                                        if self.queue_type is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Queue']['meta_info']


                                class Shape(object):
                                    """
                                    QoS EA Shaper parameters
                                    
                                    .. attribute:: pbs
                                    
                                    	PBS in bytes
                                    	**type**\:   :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs>`
                                    
                                    .. attribute:: pir
                                    
                                    	PIR in kbps
                                    	**type**\:   :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir>`
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.pbs = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs()
                                        self.pbs.parent = self
                                        self.pir = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir()
                                        self.pir.parent = self


                                    class Pir(object):
                                        """
                                        PIR in kbps
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pir'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir']['meta_info']


                                    class Pbs(object):
                                        """
                                        PBS in bytes
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pbs'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:shape'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.pbs is not None and self.pbs._has_data():
                                            return True

                                        if self.pir is not None and self.pir._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']


                                class Wfq(object):
                                    """
                                    QoS WFQ parameters
                                    
                                    .. attribute:: committed_weight
                                    
                                    	Committed Weight
                                    	**type**\:   :py:class:`CommittedWeight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight>`
                                    
                                    .. attribute:: excess_weight
                                    
                                    	Excess Weight
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: programmed_wfq
                                    
                                    	QoS Programmed WFQ parameters
                                    	**type**\:   :py:class:`ProgrammedWfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq>`
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.committed_weight = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight()
                                        self.committed_weight.parent = self
                                        self.excess_weight = None
                                        self.programmed_wfq = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq()
                                        self.programmed_wfq.parent = self


                                    class CommittedWeight(object):
                                        """
                                        Committed Weight
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:committed-weight'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight']['meta_info']


                                    class ProgrammedWfq(object):
                                        """
                                        QoS Programmed WFQ parameters
                                        
                                        .. attribute:: bandwidth
                                        
                                        	Bandwidth
                                        	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth>`
                                        
                                        .. attribute:: excess_ratio
                                        
                                        	Excess Ratio
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: sum_of_bandwidth
                                        
                                        	Sum of Bandwidth
                                        	**type**\:   :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth>`
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.bandwidth = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth()
                                            self.bandwidth.parent = self
                                            self.excess_ratio = None
                                            self.sum_of_bandwidth = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth()
                                            self.sum_of_bandwidth.parent = self


                                        class Bandwidth(object):
                                            """
                                            Bandwidth
                                            
                                            .. attribute:: unit
                                            
                                            	Config unit
                                            	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                            
                                            .. attribute:: value
                                            
                                            	Config value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.unit = None
                                                self.value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bandwidth'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.unit is not None:
                                                    return True

                                                if self.value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth']['meta_info']


                                        class SumOfBandwidth(object):
                                            """
                                            Sum of Bandwidth
                                            
                                            .. attribute:: unit
                                            
                                            	Config unit
                                            	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                            
                                            .. attribute:: value
                                            
                                            	Config value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.unit = None
                                                self.value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:sum-of-bandwidth'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.unit is not None:
                                                    return True

                                                if self.value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:programmed-wfq'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.bandwidth is not None and self.bandwidth._has_data():
                                                return True

                                            if self.excess_ratio is not None:
                                                return True

                                            if self.sum_of_bandwidth is not None and self.sum_of_bandwidth._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:wfq'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.committed_weight is not None and self.committed_weight._has_data():
                                            return True

                                        if self.excess_weight is not None:
                                            return True

                                        if self.programmed_wfq is not None and self.programmed_wfq._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']


                                class Police(object):
                                    """
                                    QoS Policer parameters
                                    
                                    .. attribute:: cbs
                                    
                                    	CBS
                                    	**type**\:   :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs>`
                                    
                                    .. attribute:: cir
                                    
                                    	CIR
                                    	**type**\:   :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir>`
                                    
                                    .. attribute:: policer_id
                                    
                                    	policer ID
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policer_type
                                    
                                    	Policer type
                                    	**type**\:   :py:class:`TbAlgorithmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithmEnum>`
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.cbs = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs()
                                        self.cbs.parent = self
                                        self.cir = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir()
                                        self.cir.parent = self
                                        self.policer_id = None
                                        self.policer_type = None


                                    class Cir(object):
                                        """
                                        CIR
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cir'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir']['meta_info']


                                    class Cbs(object):
                                        """
                                        CBS
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cbs'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.cbs is not None and self.cbs._has_data():
                                            return True

                                        if self.cir is not None and self.cir._has_data():
                                            return True

                                        if self.policer_id is not None:
                                            return True

                                        if self.policer_type is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']


                                class Marking(object):
                                    """
                                    QoS Mark parameters
                                    
                                    .. attribute:: mark_only
                                    
                                    	Mark Only
                                    	**type**\:   :py:class:`MarkOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly>`
                                    
                                    .. attribute:: police_conform
                                    
                                    	Police conform mark
                                    	**type**\:   :py:class:`PoliceConform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform>`
                                    
                                    .. attribute:: police_exceed
                                    
                                    	Police exceed mark
                                    	**type**\:   :py:class:`PoliceExceed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed>`
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.mark_only = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly()
                                        self.mark_only.parent = self
                                        self.police_conform = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform()
                                        self.police_conform.parent = self
                                        self.police_exceed = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed()
                                        self.police_exceed.parent = self


                                    class MarkOnly(object):
                                        """
                                        Mark Only
                                        
                                        .. attribute:: action_type
                                        
                                        	Action type
                                        	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionEnum>`
                                        
                                        .. attribute:: mark_detail
                                        
                                        	Mark value
                                        	**type**\: list of    :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail>`
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.action_type = None
                                            self.mark_detail = YList()
                                            self.mark_detail.parent = self
                                            self.mark_detail.name = 'mark_detail'


                                        class MarkDetail(object):
                                            """
                                            Mark value
                                            
                                            .. attribute:: action_opcode
                                            
                                            	Action opcode
                                            	**type**\:   :py:class:`ActionOpcodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcodeEnum>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.action_opcode = None
                                                self.mark_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-detail'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.action_opcode is not None:
                                                    return True

                                                if self.mark_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-only'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.action_type is not None:
                                                return True

                                            if self.mark_detail is not None:
                                                for child_ref in self.mark_detail:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info']


                                    class PoliceConform(object):
                                        """
                                        Police conform mark
                                        
                                        .. attribute:: action_type
                                        
                                        	Action type
                                        	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionEnum>`
                                        
                                        .. attribute:: mark_detail
                                        
                                        	Mark value
                                        	**type**\: list of    :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail>`
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.action_type = None
                                            self.mark_detail = YList()
                                            self.mark_detail.parent = self
                                            self.mark_detail.name = 'mark_detail'


                                        class MarkDetail(object):
                                            """
                                            Mark value
                                            
                                            .. attribute:: action_opcode
                                            
                                            	Action opcode
                                            	**type**\:   :py:class:`ActionOpcodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcodeEnum>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.action_opcode = None
                                                self.mark_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-detail'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.action_opcode is not None:
                                                    return True

                                                if self.mark_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police-conform'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.action_type is not None:
                                                return True

                                            if self.mark_detail is not None:
                                                for child_ref in self.mark_detail:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info']


                                    class PoliceExceed(object):
                                        """
                                        Police exceed mark
                                        
                                        .. attribute:: action_type
                                        
                                        	Action type
                                        	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionEnum>`
                                        
                                        .. attribute:: mark_detail
                                        
                                        	Mark value
                                        	**type**\: list of    :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail>`
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.action_type = None
                                            self.mark_detail = YList()
                                            self.mark_detail.parent = self
                                            self.mark_detail.name = 'mark_detail'


                                        class MarkDetail(object):
                                            """
                                            Mark value
                                            
                                            .. attribute:: action_opcode
                                            
                                            	Action opcode
                                            	**type**\:   :py:class:`ActionOpcodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcodeEnum>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.action_opcode = None
                                                self.mark_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-detail'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.action_opcode is not None:
                                                    return True

                                                if self.mark_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police-exceed'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.action_type is not None:
                                                return True

                                            if self.mark_detail is not None:
                                                for child_ref in self.mark_detail:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:marking'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.mark_only is not None and self.mark_only._has_data():
                                            return True

                                        if self.police_conform is not None and self.police_conform._has_data():
                                            return True

                                        if self.police_exceed is not None and self.police_exceed._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:qos-show-pclass-st'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.class_level is not None:
                                        return True

                                    if self.class_name is not None:
                                        return True

                                    if self.marking is not None and self.marking._has_data():
                                        return True

                                    if self.police is not None and self.police._has_data():
                                        return True

                                    if self.queue is not None and self.queue._has_data():
                                        return True

                                    if self.shape is not None and self.shape._has_data():
                                        return True

                                    if self.wfq is not None and self.wfq._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:skywarp-qos-policy-class'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.qos_show_pclass_st is not None:
                                    for child_ref in self.qos_show_pclass_st:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:output'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.header is not None and self.header._has_data():
                                return True

                            if self.interface_parameters is not None and self.interface_parameters._has_data():
                                return True

                            if self.skywarp_qos_policy_class is not None and self.skywarp_qos_policy_class._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output']['meta_info']


                    class Input(object):
                        """
                        QoS policy direction ingress
                        
                        .. attribute:: header
                        
                        	QoS EA policy header
                        	**type**\:   :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.Header>`
                        
                        .. attribute:: interface_parameters
                        
                        	QoS Interface Parameters
                        	**type**\:   :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters>`
                        
                        .. attribute:: skywarp_qos_policy_class
                        
                        	Skywarp QoS policy class details
                        	**type**\:   :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass>`
                        
                        

                        """

                        _prefix = 'skp-qos-oper'
                        _revision = '2016-02-18'

                        def __init__(self):
                            self.parent = None
                            self.header = PlatformQos.Nodes.Node.Interfaces.Interface.Input.Header()
                            self.header.parent = self
                            self.interface_parameters = PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters()
                            self.interface_parameters.parent = self
                            self.skywarp_qos_policy_class = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass()
                            self.skywarp_qos_policy_class.parent = self


                        class Header(object):
                            """
                            QoS EA policy header
                            
                            .. attribute:: classes
                            
                            	Number of classes
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: direction
                            
                            	Direction
                            	**type**\:  str
                            
                            	**length:** 0..11
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            	**length:** 0..101
                            
                            .. attribute:: policy_name
                            
                            	Policy name
                            	**type**\:  str
                            
                            	**length:** 0..65
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                self.parent = None
                                self.classes = None
                                self.direction = None
                                self.interface_name = None
                                self.policy_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:header'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.classes is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.policy_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Header']['meta_info']


                        class InterfaceParameters(object):
                            """
                            QoS Interface Parameters
                            
                            .. attribute:: interface_config_rate
                            
                            	Interface Configured Rate
                            	**type**\:   :py:class:`InterfaceConfigRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceConfigRate>`
                            
                            .. attribute:: interface_program_rate
                            
                            	Interface Programmed Rate
                            	**type**\:   :py:class:`InterfaceProgramRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceProgramRate>`
                            
                            .. attribute:: port_shaper_rate
                            
                            	Port Shaper Rate
                            	**type**\:   :py:class:`PortShaperRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.PortShaperRate>`
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                self.parent = None
                                self.interface_config_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceConfigRate()
                                self.interface_config_rate.parent = self
                                self.interface_program_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceProgramRate()
                                self.interface_program_rate.parent = self
                                self.port_shaper_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.PortShaperRate()
                                self.port_shaper_rate.parent = self


                            class InterfaceConfigRate(object):
                                """
                                Interface Configured Rate
                                
                                .. attribute:: unit
                                
                                	Config unit
                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                
                                .. attribute:: value
                                
                                	Config value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.unit = None
                                    self.value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-config-rate'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.unit is not None:
                                        return True

                                    if self.value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceConfigRate']['meta_info']


                            class InterfaceProgramRate(object):
                                """
                                Interface Programmed Rate
                                
                                .. attribute:: unit
                                
                                	Config unit
                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                
                                .. attribute:: value
                                
                                	Config value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.unit = None
                                    self.value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-program-rate'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.unit is not None:
                                        return True

                                    if self.value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceProgramRate']['meta_info']


                            class PortShaperRate(object):
                                """
                                Port Shaper Rate
                                
                                .. attribute:: unit
                                
                                	Config unit
                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                
                                .. attribute:: value
                                
                                	Config value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.unit = None
                                    self.value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:port-shaper-rate'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.unit is not None:
                                        return True

                                    if self.value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.PortShaperRate']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-parameters'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.interface_config_rate is not None and self.interface_config_rate._has_data():
                                    return True

                                if self.interface_program_rate is not None and self.interface_program_rate._has_data():
                                    return True

                                if self.port_shaper_rate is not None and self.port_shaper_rate._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters']['meta_info']


                        class SkywarpQosPolicyClass(object):
                            """
                            Skywarp QoS policy class details
                            
                            .. attribute:: qos_show_pclass_st
                            
                            	qos show pclass st
                            	**type**\: list of    :py:class:`QosShowPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt>`
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                self.parent = None
                                self.qos_show_pclass_st = YList()
                                self.qos_show_pclass_st.parent = self
                                self.qos_show_pclass_st.name = 'qos_show_pclass_st'


                            class QosShowPclassSt(object):
                                """
                                qos show pclass st
                                
                                .. attribute:: class_level
                                
                                	Class level
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: class_name
                                
                                	Class name
                                	**type**\:  str
                                
                                	**length:** 0..65
                                
                                .. attribute:: marking
                                
                                	QoS Mark parameters
                                	**type**\:   :py:class:`Marking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking>`
                                
                                .. attribute:: police
                                
                                	QoS Policer parameters
                                	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police>`
                                
                                .. attribute:: queue
                                
                                	QoS Queue parameters
                                	**type**\:   :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Queue>`
                                
                                .. attribute:: shape
                                
                                	QoS EA Shaper parameters
                                	**type**\:   :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape>`
                                
                                .. attribute:: wfq
                                
                                	QoS WFQ parameters
                                	**type**\:   :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq>`
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.class_level = None
                                    self.class_name = None
                                    self.marking = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking()
                                    self.marking.parent = self
                                    self.police = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police()
                                    self.police.parent = self
                                    self.queue = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Queue()
                                    self.queue.parent = self
                                    self.shape = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape()
                                    self.shape.parent = self
                                    self.wfq = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq()
                                    self.wfq.parent = self


                                class Queue(object):
                                    """
                                    QoS Queue parameters
                                    
                                    .. attribute:: queue_id
                                    
                                    	Queue ID
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: queue_type
                                    
                                    	Queue Type
                                    	**type**\:  str
                                    
                                    	**length:** 0..101
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.queue_id = None
                                        self.queue_type = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:queue'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.queue_id is not None:
                                            return True

                                        if self.queue_type is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Queue']['meta_info']


                                class Shape(object):
                                    """
                                    QoS EA Shaper parameters
                                    
                                    .. attribute:: pbs
                                    
                                    	PBS in bytes
                                    	**type**\:   :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs>`
                                    
                                    .. attribute:: pir
                                    
                                    	PIR in kbps
                                    	**type**\:   :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir>`
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.pbs = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs()
                                        self.pbs.parent = self
                                        self.pir = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir()
                                        self.pir.parent = self


                                    class Pir(object):
                                        """
                                        PIR in kbps
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pir'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir']['meta_info']


                                    class Pbs(object):
                                        """
                                        PBS in bytes
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pbs'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:shape'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.pbs is not None and self.pbs._has_data():
                                            return True

                                        if self.pir is not None and self.pir._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']


                                class Wfq(object):
                                    """
                                    QoS WFQ parameters
                                    
                                    .. attribute:: committed_weight
                                    
                                    	Committed Weight
                                    	**type**\:   :py:class:`CommittedWeight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight>`
                                    
                                    .. attribute:: excess_weight
                                    
                                    	Excess Weight
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: programmed_wfq
                                    
                                    	QoS Programmed WFQ parameters
                                    	**type**\:   :py:class:`ProgrammedWfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq>`
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.committed_weight = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight()
                                        self.committed_weight.parent = self
                                        self.excess_weight = None
                                        self.programmed_wfq = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq()
                                        self.programmed_wfq.parent = self


                                    class CommittedWeight(object):
                                        """
                                        Committed Weight
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:committed-weight'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight']['meta_info']


                                    class ProgrammedWfq(object):
                                        """
                                        QoS Programmed WFQ parameters
                                        
                                        .. attribute:: bandwidth
                                        
                                        	Bandwidth
                                        	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth>`
                                        
                                        .. attribute:: excess_ratio
                                        
                                        	Excess Ratio
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: sum_of_bandwidth
                                        
                                        	Sum of Bandwidth
                                        	**type**\:   :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth>`
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.bandwidth = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth()
                                            self.bandwidth.parent = self
                                            self.excess_ratio = None
                                            self.sum_of_bandwidth = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth()
                                            self.sum_of_bandwidth.parent = self


                                        class Bandwidth(object):
                                            """
                                            Bandwidth
                                            
                                            .. attribute:: unit
                                            
                                            	Config unit
                                            	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                            
                                            .. attribute:: value
                                            
                                            	Config value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.unit = None
                                                self.value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bandwidth'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.unit is not None:
                                                    return True

                                                if self.value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth']['meta_info']


                                        class SumOfBandwidth(object):
                                            """
                                            Sum of Bandwidth
                                            
                                            .. attribute:: unit
                                            
                                            	Config unit
                                            	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                            
                                            .. attribute:: value
                                            
                                            	Config value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.unit = None
                                                self.value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:sum-of-bandwidth'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.unit is not None:
                                                    return True

                                                if self.value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:programmed-wfq'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.bandwidth is not None and self.bandwidth._has_data():
                                                return True

                                            if self.excess_ratio is not None:
                                                return True

                                            if self.sum_of_bandwidth is not None and self.sum_of_bandwidth._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:wfq'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.committed_weight is not None and self.committed_weight._has_data():
                                            return True

                                        if self.excess_weight is not None:
                                            return True

                                        if self.programmed_wfq is not None and self.programmed_wfq._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']


                                class Police(object):
                                    """
                                    QoS Policer parameters
                                    
                                    .. attribute:: cbs
                                    
                                    	CBS
                                    	**type**\:   :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs>`
                                    
                                    .. attribute:: cir
                                    
                                    	CIR
                                    	**type**\:   :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir>`
                                    
                                    .. attribute:: policer_id
                                    
                                    	policer ID
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policer_type
                                    
                                    	Policer type
                                    	**type**\:   :py:class:`TbAlgorithmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithmEnum>`
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.cbs = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs()
                                        self.cbs.parent = self
                                        self.cir = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir()
                                        self.cir.parent = self
                                        self.policer_id = None
                                        self.policer_type = None


                                    class Cir(object):
                                        """
                                        CIR
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cir'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir']['meta_info']


                                    class Cbs(object):
                                        """
                                        CBS
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.unit = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cbs'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.unit is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.cbs is not None and self.cbs._has_data():
                                            return True

                                        if self.cir is not None and self.cir._has_data():
                                            return True

                                        if self.policer_id is not None:
                                            return True

                                        if self.policer_type is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']


                                class Marking(object):
                                    """
                                    QoS Mark parameters
                                    
                                    .. attribute:: mark_only
                                    
                                    	Mark Only
                                    	**type**\:   :py:class:`MarkOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly>`
                                    
                                    .. attribute:: police_conform
                                    
                                    	Police conform mark
                                    	**type**\:   :py:class:`PoliceConform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform>`
                                    
                                    .. attribute:: police_exceed
                                    
                                    	Police exceed mark
                                    	**type**\:   :py:class:`PoliceExceed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed>`
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.mark_only = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly()
                                        self.mark_only.parent = self
                                        self.police_conform = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform()
                                        self.police_conform.parent = self
                                        self.police_exceed = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed()
                                        self.police_exceed.parent = self


                                    class MarkOnly(object):
                                        """
                                        Mark Only
                                        
                                        .. attribute:: action_type
                                        
                                        	Action type
                                        	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionEnum>`
                                        
                                        .. attribute:: mark_detail
                                        
                                        	Mark value
                                        	**type**\: list of    :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail>`
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.action_type = None
                                            self.mark_detail = YList()
                                            self.mark_detail.parent = self
                                            self.mark_detail.name = 'mark_detail'


                                        class MarkDetail(object):
                                            """
                                            Mark value
                                            
                                            .. attribute:: action_opcode
                                            
                                            	Action opcode
                                            	**type**\:   :py:class:`ActionOpcodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcodeEnum>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.action_opcode = None
                                                self.mark_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-detail'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.action_opcode is not None:
                                                    return True

                                                if self.mark_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-only'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.action_type is not None:
                                                return True

                                            if self.mark_detail is not None:
                                                for child_ref in self.mark_detail:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info']


                                    class PoliceConform(object):
                                        """
                                        Police conform mark
                                        
                                        .. attribute:: action_type
                                        
                                        	Action type
                                        	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionEnum>`
                                        
                                        .. attribute:: mark_detail
                                        
                                        	Mark value
                                        	**type**\: list of    :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail>`
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.action_type = None
                                            self.mark_detail = YList()
                                            self.mark_detail.parent = self
                                            self.mark_detail.name = 'mark_detail'


                                        class MarkDetail(object):
                                            """
                                            Mark value
                                            
                                            .. attribute:: action_opcode
                                            
                                            	Action opcode
                                            	**type**\:   :py:class:`ActionOpcodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcodeEnum>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.action_opcode = None
                                                self.mark_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-detail'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.action_opcode is not None:
                                                    return True

                                                if self.mark_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police-conform'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.action_type is not None:
                                                return True

                                            if self.mark_detail is not None:
                                                for child_ref in self.mark_detail:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info']


                                    class PoliceExceed(object):
                                        """
                                        Police exceed mark
                                        
                                        .. attribute:: action_type
                                        
                                        	Action type
                                        	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionEnum>`
                                        
                                        .. attribute:: mark_detail
                                        
                                        	Mark value
                                        	**type**\: list of    :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail>`
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.action_type = None
                                            self.mark_detail = YList()
                                            self.mark_detail.parent = self
                                            self.mark_detail.name = 'mark_detail'


                                        class MarkDetail(object):
                                            """
                                            Mark value
                                            
                                            .. attribute:: action_opcode
                                            
                                            	Action opcode
                                            	**type**\:   :py:class:`ActionOpcodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcodeEnum>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.action_opcode = None
                                                self.mark_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:mark-detail'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.action_opcode is not None:
                                                    return True

                                                if self.mark_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police-exceed'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.action_type is not None:
                                                return True

                                            if self.mark_detail is not None:
                                                for child_ref in self.mark_detail:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:marking'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.mark_only is not None and self.mark_only._has_data():
                                            return True

                                        if self.police_conform is not None and self.police_conform._has_data():
                                            return True

                                        if self.police_exceed is not None and self.police_exceed._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:qos-show-pclass-st'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.class_level is not None:
                                        return True

                                    if self.class_name is not None:
                                        return True

                                    if self.marking is not None and self.marking._has_data():
                                        return True

                                    if self.police is not None and self.police._has_data():
                                        return True

                                    if self.queue is not None and self.queue._has_data():
                                        return True

                                    if self.shape is not None and self.shape._has_data():
                                        return True

                                    if self.wfq is not None and self.wfq._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:skywarp-qos-policy-class'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.qos_show_pclass_st is not None:
                                    for child_ref in self.qos_show_pclass_st:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:input'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.header is not None and self.header._has_data():
                                return True

                            if self.interface_parameters is not None and self.interface_parameters._has_data():
                                return True

                            if self.skywarp_qos_policy_class is not None and self.skywarp_qos_policy_class._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface[Cisco-IOS-XR-skp-qos-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.input is not None and self.input._has_data():
                            return True

                        if self.output is not None and self.output._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-skp-qos-oper:platform-qos/Cisco-IOS-XR-skp-qos-oper:nodes/Cisco-IOS-XR-skp-qos-oper:node[Cisco-IOS-XR-skp-qos-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.bundle_interfaces is not None and self.bundle_interfaces._has_data():
                    return True

                if self.capability is not None and self.capability._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                return meta._meta_table['PlatformQos.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-skp-qos-oper:platform-qos/Cisco-IOS-XR-skp-qos-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
            return meta._meta_table['PlatformQos.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-skp-qos-oper:platform-qos'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['PlatformQos']['meta_info']


class PlatformQosEa(object):
    """
    platform qos ea
    
    .. attribute:: nodes
    
    	List of nodes with platform specific QoS\-EA configuration
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes>`
    
    

    """

    _prefix = 'skp-qos-oper'
    _revision = '2016-02-18'

    def __init__(self):
        self.nodes = PlatformQosEa.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        List of nodes with platform specific QoS\-EA
        configuration
        
        .. attribute:: node
        
        	Node with platform specific QoS\-EA configuration
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node>`
        
        

        """

        _prefix = 'skp-qos-oper'
        _revision = '2016-02-18'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Node with platform specific QoS\-EA
            configuration
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: bundle_interfaces
            
            	QoS\-EA list of bundle interfaces
            	**type**\:   :py:class:`BundleInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces>`
            
            .. attribute:: interfaces
            
            	QoS\-EA list of interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'skp-qos-oper'
            _revision = '2016-02-18'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.bundle_interfaces = PlatformQosEa.Nodes.Node.BundleInterfaces()
                self.bundle_interfaces.parent = self
                self.interfaces = PlatformQosEa.Nodes.Node.Interfaces()
                self.interfaces.parent = self


            class BundleInterfaces(object):
                """
                QoS\-EA list of bundle interfaces
                
                .. attribute:: bundle_interface
                
                	QoS\-EA interface name
                	**type**\: list of    :py:class:`BundleInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface>`
                
                

                """

                _prefix = 'skp-qos-oper'
                _revision = '2016-02-18'

                def __init__(self):
                    self.parent = None
                    self.bundle_interface = YList()
                    self.bundle_interface.parent = self
                    self.bundle_interface.name = 'bundle_interface'


                class BundleInterface(object):
                    """
                    QoS\-EA interface name
                    
                    .. attribute:: interface_name  <key>
                    
                    	Bundle interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: member_interfaces
                    
                    	QoS\-EA list of member interfaces
                    	**type**\:   :py:class:`MemberInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces>`
                    
                    

                    """

                    _prefix = 'skp-qos-oper'
                    _revision = '2016-02-18'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.member_interfaces = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces()
                        self.member_interfaces.parent = self


                    class MemberInterfaces(object):
                        """
                        QoS\-EA list of member interfaces
                        
                        .. attribute:: member_interface
                        
                        	QoS\-EA interface name
                        	**type**\: list of    :py:class:`MemberInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface>`
                        
                        

                        """

                        _prefix = 'skp-qos-oper'
                        _revision = '2016-02-18'

                        def __init__(self):
                            self.parent = None
                            self.member_interface = YList()
                            self.member_interface.parent = self
                            self.member_interface.name = 'member_interface'


                        class MemberInterface(object):
                            """
                            QoS\-EA interface name
                            
                            .. attribute:: interface_name  <key>
                            
                            	Memeber interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: bundle_input
                            
                            	QoS\-EA policy direction input
                            	**type**\:   :py:class:`BundleInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput>`
                            
                            .. attribute:: bundle_output
                            
                            	QoS\-EA policy direction output
                            	**type**\:   :py:class:`BundleOutput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput>`
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None
                                self.bundle_input = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput()
                                self.bundle_input.parent = self
                                self.bundle_output = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput()
                                self.bundle_output.parent = self


                            class BundleOutput(object):
                                """
                                QoS\-EA policy direction output
                                
                                .. attribute:: details
                                
                                	QoS\-EA policy details
                                	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details>`
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.details = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details()
                                    self.details.parent = self


                                class Details(object):
                                    """
                                    QoS\-EA policy details
                                    
                                    .. attribute:: header
                                    
                                    	QoS EA policy header
                                    	**type**\:   :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.Header>`
                                    
                                    .. attribute:: interface_parameters
                                    
                                    	QoS EA Interface Parameters
                                    	**type**\:   :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.InterfaceParameters>`
                                    
                                    .. attribute:: skywarp_qos_policy_class
                                    
                                    	Skywarp QoS EA policy class details
                                    	**type**\:   :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass>`
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.header = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.Header()
                                        self.header.parent = self
                                        self.interface_parameters = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.InterfaceParameters()
                                        self.interface_parameters.parent = self
                                        self.skywarp_qos_policy_class = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass()
                                        self.skywarp_qos_policy_class.parent = self


                                    class Header(object):
                                        """
                                        QoS EA policy header
                                        
                                        .. attribute:: classes
                                        
                                        	Number of classes
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: direction
                                        
                                        	Direction
                                        	**type**\:  str
                                        
                                        	**length:** 0..11
                                        
                                        .. attribute:: interface_name
                                        
                                        	Interface Name
                                        	**type**\:  str
                                        
                                        	**length:** 0..101
                                        
                                        .. attribute:: policy_name
                                        
                                        	Policy name
                                        	**type**\:  str
                                        
                                        	**length:** 0..65
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.classes = None
                                            self.direction = None
                                            self.interface_name = None
                                            self.policy_name = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:header'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.classes is not None:
                                                return True

                                            if self.direction is not None:
                                                return True

                                            if self.interface_name is not None:
                                                return True

                                            if self.policy_name is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.Header']['meta_info']


                                    class InterfaceParameters(object):
                                        """
                                        QoS EA Interface Parameters
                                        
                                        .. attribute:: bundle_id
                                        
                                        	Bundle Interface ID
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: hierarchical_depth
                                        
                                        	Max Hierarchial Depth
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: interface_handle
                                        
                                        	Interface Handle
                                        	**type**\:  str
                                        
                                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                        
                                        .. attribute:: interface_rate
                                        
                                        	Interface Programmed Rate
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: interface_type
                                        
                                        	Interface Type
                                        	**type**\:  str
                                        
                                        	**length:** 0..101
                                        
                                        .. attribute:: policy_map_id
                                        
                                        	Policy Map ID
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: policy_name
                                        
                                        	Policy name
                                        	**type**\:  str
                                        
                                        	**length:** 0..65
                                        
                                        .. attribute:: port
                                        
                                        	Local Port
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: port_shaper_rate
                                        
                                        	Port Shaper Rate
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: qos_interface_handle
                                        
                                        	QoS Interface handle
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: uidb_index
                                        
                                        	UIDB Index
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: under_line_interface_handle
                                        
                                        	UnderLineInterface Handle
                                        	**type**\:  str
                                        
                                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.bundle_id = None
                                            self.hierarchical_depth = None
                                            self.interface_handle = None
                                            self.interface_rate = None
                                            self.interface_type = None
                                            self.policy_map_id = None
                                            self.policy_name = None
                                            self.port = None
                                            self.port_shaper_rate = None
                                            self.qos_interface_handle = None
                                            self.uidb_index = None
                                            self.under_line_interface_handle = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-parameters'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.bundle_id is not None:
                                                return True

                                            if self.hierarchical_depth is not None:
                                                return True

                                            if self.interface_handle is not None:
                                                return True

                                            if self.interface_rate is not None:
                                                return True

                                            if self.interface_type is not None:
                                                return True

                                            if self.policy_map_id is not None:
                                                return True

                                            if self.policy_name is not None:
                                                return True

                                            if self.port is not None:
                                                return True

                                            if self.port_shaper_rate is not None:
                                                return True

                                            if self.qos_interface_handle is not None:
                                                return True

                                            if self.uidb_index is not None:
                                                return True

                                            if self.under_line_interface_handle is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.InterfaceParameters']['meta_info']


                                    class SkywarpQosPolicyClass(object):
                                        """
                                        Skywarp QoS EA policy class details
                                        
                                        .. attribute:: qos_show_ea_pclass_st
                                        
                                        	qos show ea pclass st
                                        	**type**\: list of    :py:class:`QosShowEaPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt>`
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.qos_show_ea_pclass_st = YList()
                                            self.qos_show_ea_pclass_st.parent = self
                                            self.qos_show_ea_pclass_st.name = 'qos_show_ea_pclass_st'


                                        class QosShowEaPclassSt(object):
                                            """
                                            qos show ea pclass st
                                            
                                            .. attribute:: class_level
                                            
                                            	Class level
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: class_name
                                            
                                            	Class name
                                            	**type**\:  str
                                            
                                            	**length:** 0..65
                                            
                                            .. attribute:: config
                                            
                                            	QoS EA Class Configuration
                                            	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config>`
                                            
                                            .. attribute:: index
                                            
                                            	Class Index
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: node_flags
                                            
                                            	Node Flags
                                            	**type**\:  str
                                            
                                            	**length:** 0..101
                                            
                                            .. attribute:: policy_name
                                            
                                            	Policy name
                                            	**type**\:  str
                                            
                                            	**length:** 0..65
                                            
                                            .. attribute:: result
                                            
                                            	QoS EA Class Result
                                            	**type**\:   :py:class:`Result <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result>`
                                            
                                            .. attribute:: stats_flags
                                            
                                            	Statistical Flags
                                            	**type**\:  str
                                            
                                            	**length:** 0..101
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.class_level = None
                                                self.class_name = None
                                                self.config = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config()
                                                self.config.parent = self
                                                self.index = None
                                                self.node_flags = None
                                                self.policy_name = None
                                                self.result = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result()
                                                self.result.parent = self
                                                self.stats_flags = None


                                            class Config(object):
                                                """
                                                QoS EA Class Configuration
                                                
                                                .. attribute:: node_config
                                                
                                                	Node Config
                                                	**type**\:  str
                                                
                                                	**length:** 0..101
                                                
                                                .. attribute:: police
                                                
                                                	QoS EA Policer parameters
                                                	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police>`
                                                
                                                .. attribute:: shape
                                                
                                                	QoS EA Shaper parameters
                                                	**type**\:   :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape>`
                                                
                                                .. attribute:: wfq
                                                
                                                	QoS EA WFQ parameters
                                                	**type**\:   :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq>`
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.node_config = None
                                                    self.police = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police()
                                                    self.police.parent = self
                                                    self.shape = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape()
                                                    self.shape.parent = self
                                                    self.wfq = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq()
                                                    self.wfq.parent = self


                                                class Police(object):
                                                    """
                                                    QoS EA Policer parameters
                                                    
                                                    .. attribute:: cbs
                                                    
                                                    	CBS
                                                    	**type**\:   :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs>`
                                                    
                                                    .. attribute:: cir
                                                    
                                                    	CIR
                                                    	**type**\:   :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir>`
                                                    
                                                    .. attribute:: color_aware
                                                    
                                                    	Color Aware
                                                    	**type**\:  bool
                                                    
                                                    .. attribute:: policer_type
                                                    
                                                    	Policer type
                                                    	**type**\:   :py:class:`TbAlgorithmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithmEnum>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.cbs = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs()
                                                        self.cbs.parent = self
                                                        self.cir = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir()
                                                        self.cir.parent = self
                                                        self.color_aware = None
                                                        self.policer_type = None


                                                    class Cir(object):
                                                        """
                                                        CIR
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.unit = None
                                                            self.value = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cir'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.unit is not None:
                                                                return True

                                                            if self.value is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir']['meta_info']


                                                    class Cbs(object):
                                                        """
                                                        CBS
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.unit = None
                                                            self.value = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cbs'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.unit is not None:
                                                                return True

                                                            if self.value is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.cbs is not None and self.cbs._has_data():
                                                            return True

                                                        if self.cir is not None and self.cir._has_data():
                                                            return True

                                                        if self.color_aware is not None:
                                                            return True

                                                        if self.policer_type is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']


                                                class Shape(object):
                                                    """
                                                    QoS EA Shaper parameters
                                                    
                                                    .. attribute:: pbs
                                                    
                                                    	PBS in bytes
                                                    	**type**\:   :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs>`
                                                    
                                                    .. attribute:: pir
                                                    
                                                    	PIR in kbps
                                                    	**type**\:   :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.pbs = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs()
                                                        self.pbs.parent = self
                                                        self.pir = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir()
                                                        self.pir.parent = self


                                                    class Pir(object):
                                                        """
                                                        PIR in kbps
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.unit = None
                                                            self.value = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pir'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.unit is not None:
                                                                return True

                                                            if self.value is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir']['meta_info']


                                                    class Pbs(object):
                                                        """
                                                        PBS in bytes
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.unit = None
                                                            self.value = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pbs'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.unit is not None:
                                                                return True

                                                            if self.value is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:shape'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.pbs is not None and self.pbs._has_data():
                                                            return True

                                                        if self.pir is not None and self.pir._has_data():
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']


                                                class Wfq(object):
                                                    """
                                                    QoS EA WFQ parameters
                                                    
                                                    .. attribute:: bandwidth
                                                    
                                                    	Bandwidth
                                                    	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth>`
                                                    
                                                    .. attribute:: excess_ratio
                                                    
                                                    	Excess Ratio
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: sum_of_bandwidth
                                                    
                                                    	Sum of Bandwidth
                                                    	**type**\:   :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.bandwidth = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth()
                                                        self.bandwidth.parent = self
                                                        self.excess_ratio = None
                                                        self.sum_of_bandwidth = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth()
                                                        self.sum_of_bandwidth.parent = self


                                                    class Bandwidth(object):
                                                        """
                                                        Bandwidth
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.unit = None
                                                            self.value = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bandwidth'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.unit is not None:
                                                                return True

                                                            if self.value is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth']['meta_info']


                                                    class SumOfBandwidth(object):
                                                        """
                                                        Sum of Bandwidth
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.unit = None
                                                            self.value = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:sum-of-bandwidth'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.unit is not None:
                                                                return True

                                                            if self.value is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:wfq'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.bandwidth is not None and self.bandwidth._has_data():
                                                            return True

                                                        if self.excess_ratio is not None:
                                                            return True

                                                        if self.sum_of_bandwidth is not None and self.sum_of_bandwidth._has_data():
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:config'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.node_config is not None:
                                                        return True

                                                    if self.police is not None and self.police._has_data():
                                                        return True

                                                    if self.shape is not None and self.shape._has_data():
                                                        return True

                                                    if self.wfq is not None and self.wfq._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']


                                            class Result(object):
                                                """
                                                QoS EA Class Result
                                                
                                                .. attribute:: police
                                                
                                                	QoS EA Policer Result
                                                	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police>`
                                                
                                                .. attribute:: queue
                                                
                                                	QoS EA Queue Result
                                                	**type**\:   :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue>`
                                                
                                                .. attribute:: stats_id
                                                
                                                	Stats ID
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.police = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police()
                                                    self.police.parent = self
                                                    self.queue = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue()
                                                    self.queue.parent = self
                                                    self.stats_id = None


                                                class Queue(object):
                                                    """
                                                    QoS EA Queue Result
                                                    
                                                    .. attribute:: commit_tx
                                                    
                                                    	Commit Tx
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: drop
                                                    
                                                    	Drop
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: excess_tx
                                                    
                                                    	Excess Tx
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: queue_id
                                                    
                                                    	Queue ID
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.commit_tx = None
                                                        self.drop = None
                                                        self.excess_tx = None
                                                        self.queue_id = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:queue'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.commit_tx is not None:
                                                            return True

                                                        if self.drop is not None:
                                                            return True

                                                        if self.excess_tx is not None:
                                                            return True

                                                        if self.queue_id is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue']['meta_info']


                                                class Police(object):
                                                    """
                                                    QoS EA Policer Result
                                                    
                                                    .. attribute:: conform
                                                    
                                                    	Conform Rate
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: exceed
                                                    
                                                    	Exceed Rate
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: token_bucket_id
                                                    
                                                    	Token Bucket ID
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: violate
                                                    
                                                    	Violate Rate
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.conform = None
                                                        self.exceed = None
                                                        self.token_bucket_id = None
                                                        self.violate = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.conform is not None:
                                                            return True

                                                        if self.exceed is not None:
                                                            return True

                                                        if self.token_bucket_id is not None:
                                                            return True

                                                        if self.violate is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:result'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.police is not None and self.police._has_data():
                                                        return True

                                                    if self.queue is not None and self.queue._has_data():
                                                        return True

                                                    if self.stats_id is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:qos-show-ea-pclass-st'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.class_level is not None:
                                                    return True

                                                if self.class_name is not None:
                                                    return True

                                                if self.config is not None and self.config._has_data():
                                                    return True

                                                if self.index is not None:
                                                    return True

                                                if self.node_flags is not None:
                                                    return True

                                                if self.policy_name is not None:
                                                    return True

                                                if self.result is not None and self.result._has_data():
                                                    return True

                                                if self.stats_flags is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:skywarp-qos-policy-class'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.qos_show_ea_pclass_st is not None:
                                                for child_ref in self.qos_show_ea_pclass_st:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:details'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.header is not None and self.header._has_data():
                                            return True

                                        if self.interface_parameters is not None and self.interface_parameters._has_data():
                                            return True

                                        if self.skywarp_qos_policy_class is not None and self.skywarp_qos_policy_class._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bundle-output'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.details is not None and self.details._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput']['meta_info']


                            class BundleInput(object):
                                """
                                QoS\-EA policy direction input
                                
                                .. attribute:: details
                                
                                	QoS\-EA policy details
                                	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details>`
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.details = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details()
                                    self.details.parent = self


                                class Details(object):
                                    """
                                    QoS\-EA policy details
                                    
                                    .. attribute:: header
                                    
                                    	QoS EA policy header
                                    	**type**\:   :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.Header>`
                                    
                                    .. attribute:: interface_parameters
                                    
                                    	QoS EA Interface Parameters
                                    	**type**\:   :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.InterfaceParameters>`
                                    
                                    .. attribute:: skywarp_qos_policy_class
                                    
                                    	Skywarp QoS EA policy class details
                                    	**type**\:   :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass>`
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.header = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.Header()
                                        self.header.parent = self
                                        self.interface_parameters = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.InterfaceParameters()
                                        self.interface_parameters.parent = self
                                        self.skywarp_qos_policy_class = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass()
                                        self.skywarp_qos_policy_class.parent = self


                                    class Header(object):
                                        """
                                        QoS EA policy header
                                        
                                        .. attribute:: classes
                                        
                                        	Number of classes
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: direction
                                        
                                        	Direction
                                        	**type**\:  str
                                        
                                        	**length:** 0..11
                                        
                                        .. attribute:: interface_name
                                        
                                        	Interface Name
                                        	**type**\:  str
                                        
                                        	**length:** 0..101
                                        
                                        .. attribute:: policy_name
                                        
                                        	Policy name
                                        	**type**\:  str
                                        
                                        	**length:** 0..65
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.classes = None
                                            self.direction = None
                                            self.interface_name = None
                                            self.policy_name = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:header'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.classes is not None:
                                                return True

                                            if self.direction is not None:
                                                return True

                                            if self.interface_name is not None:
                                                return True

                                            if self.policy_name is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.Header']['meta_info']


                                    class InterfaceParameters(object):
                                        """
                                        QoS EA Interface Parameters
                                        
                                        .. attribute:: bundle_id
                                        
                                        	Bundle Interface ID
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: hierarchical_depth
                                        
                                        	Max Hierarchial Depth
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: interface_handle
                                        
                                        	Interface Handle
                                        	**type**\:  str
                                        
                                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                        
                                        .. attribute:: interface_rate
                                        
                                        	Interface Programmed Rate
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: interface_type
                                        
                                        	Interface Type
                                        	**type**\:  str
                                        
                                        	**length:** 0..101
                                        
                                        .. attribute:: policy_map_id
                                        
                                        	Policy Map ID
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: policy_name
                                        
                                        	Policy name
                                        	**type**\:  str
                                        
                                        	**length:** 0..65
                                        
                                        .. attribute:: port
                                        
                                        	Local Port
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: port_shaper_rate
                                        
                                        	Port Shaper Rate
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: qos_interface_handle
                                        
                                        	QoS Interface handle
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: uidb_index
                                        
                                        	UIDB Index
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: under_line_interface_handle
                                        
                                        	UnderLineInterface Handle
                                        	**type**\:  str
                                        
                                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.bundle_id = None
                                            self.hierarchical_depth = None
                                            self.interface_handle = None
                                            self.interface_rate = None
                                            self.interface_type = None
                                            self.policy_map_id = None
                                            self.policy_name = None
                                            self.port = None
                                            self.port_shaper_rate = None
                                            self.qos_interface_handle = None
                                            self.uidb_index = None
                                            self.under_line_interface_handle = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-parameters'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.bundle_id is not None:
                                                return True

                                            if self.hierarchical_depth is not None:
                                                return True

                                            if self.interface_handle is not None:
                                                return True

                                            if self.interface_rate is not None:
                                                return True

                                            if self.interface_type is not None:
                                                return True

                                            if self.policy_map_id is not None:
                                                return True

                                            if self.policy_name is not None:
                                                return True

                                            if self.port is not None:
                                                return True

                                            if self.port_shaper_rate is not None:
                                                return True

                                            if self.qos_interface_handle is not None:
                                                return True

                                            if self.uidb_index is not None:
                                                return True

                                            if self.under_line_interface_handle is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.InterfaceParameters']['meta_info']


                                    class SkywarpQosPolicyClass(object):
                                        """
                                        Skywarp QoS EA policy class details
                                        
                                        .. attribute:: qos_show_ea_pclass_st
                                        
                                        	qos show ea pclass st
                                        	**type**\: list of    :py:class:`QosShowEaPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt>`
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.qos_show_ea_pclass_st = YList()
                                            self.qos_show_ea_pclass_st.parent = self
                                            self.qos_show_ea_pclass_st.name = 'qos_show_ea_pclass_st'


                                        class QosShowEaPclassSt(object):
                                            """
                                            qos show ea pclass st
                                            
                                            .. attribute:: class_level
                                            
                                            	Class level
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: class_name
                                            
                                            	Class name
                                            	**type**\:  str
                                            
                                            	**length:** 0..65
                                            
                                            .. attribute:: config
                                            
                                            	QoS EA Class Configuration
                                            	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config>`
                                            
                                            .. attribute:: index
                                            
                                            	Class Index
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: node_flags
                                            
                                            	Node Flags
                                            	**type**\:  str
                                            
                                            	**length:** 0..101
                                            
                                            .. attribute:: policy_name
                                            
                                            	Policy name
                                            	**type**\:  str
                                            
                                            	**length:** 0..65
                                            
                                            .. attribute:: result
                                            
                                            	QoS EA Class Result
                                            	**type**\:   :py:class:`Result <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result>`
                                            
                                            .. attribute:: stats_flags
                                            
                                            	Statistical Flags
                                            	**type**\:  str
                                            
                                            	**length:** 0..101
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.class_level = None
                                                self.class_name = None
                                                self.config = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config()
                                                self.config.parent = self
                                                self.index = None
                                                self.node_flags = None
                                                self.policy_name = None
                                                self.result = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result()
                                                self.result.parent = self
                                                self.stats_flags = None


                                            class Config(object):
                                                """
                                                QoS EA Class Configuration
                                                
                                                .. attribute:: node_config
                                                
                                                	Node Config
                                                	**type**\:  str
                                                
                                                	**length:** 0..101
                                                
                                                .. attribute:: police
                                                
                                                	QoS EA Policer parameters
                                                	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police>`
                                                
                                                .. attribute:: shape
                                                
                                                	QoS EA Shaper parameters
                                                	**type**\:   :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape>`
                                                
                                                .. attribute:: wfq
                                                
                                                	QoS EA WFQ parameters
                                                	**type**\:   :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq>`
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.node_config = None
                                                    self.police = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police()
                                                    self.police.parent = self
                                                    self.shape = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape()
                                                    self.shape.parent = self
                                                    self.wfq = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq()
                                                    self.wfq.parent = self


                                                class Police(object):
                                                    """
                                                    QoS EA Policer parameters
                                                    
                                                    .. attribute:: cbs
                                                    
                                                    	CBS
                                                    	**type**\:   :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs>`
                                                    
                                                    .. attribute:: cir
                                                    
                                                    	CIR
                                                    	**type**\:   :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir>`
                                                    
                                                    .. attribute:: color_aware
                                                    
                                                    	Color Aware
                                                    	**type**\:  bool
                                                    
                                                    .. attribute:: policer_type
                                                    
                                                    	Policer type
                                                    	**type**\:   :py:class:`TbAlgorithmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithmEnum>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.cbs = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs()
                                                        self.cbs.parent = self
                                                        self.cir = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir()
                                                        self.cir.parent = self
                                                        self.color_aware = None
                                                        self.policer_type = None


                                                    class Cir(object):
                                                        """
                                                        CIR
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.unit = None
                                                            self.value = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cir'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.unit is not None:
                                                                return True

                                                            if self.value is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir']['meta_info']


                                                    class Cbs(object):
                                                        """
                                                        CBS
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.unit = None
                                                            self.value = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cbs'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.unit is not None:
                                                                return True

                                                            if self.value is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.cbs is not None and self.cbs._has_data():
                                                            return True

                                                        if self.cir is not None and self.cir._has_data():
                                                            return True

                                                        if self.color_aware is not None:
                                                            return True

                                                        if self.policer_type is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']


                                                class Shape(object):
                                                    """
                                                    QoS EA Shaper parameters
                                                    
                                                    .. attribute:: pbs
                                                    
                                                    	PBS in bytes
                                                    	**type**\:   :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs>`
                                                    
                                                    .. attribute:: pir
                                                    
                                                    	PIR in kbps
                                                    	**type**\:   :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.pbs = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs()
                                                        self.pbs.parent = self
                                                        self.pir = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir()
                                                        self.pir.parent = self


                                                    class Pir(object):
                                                        """
                                                        PIR in kbps
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.unit = None
                                                            self.value = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pir'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.unit is not None:
                                                                return True

                                                            if self.value is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir']['meta_info']


                                                    class Pbs(object):
                                                        """
                                                        PBS in bytes
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.unit = None
                                                            self.value = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pbs'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.unit is not None:
                                                                return True

                                                            if self.value is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:shape'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.pbs is not None and self.pbs._has_data():
                                                            return True

                                                        if self.pir is not None and self.pir._has_data():
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']


                                                class Wfq(object):
                                                    """
                                                    QoS EA WFQ parameters
                                                    
                                                    .. attribute:: bandwidth
                                                    
                                                    	Bandwidth
                                                    	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth>`
                                                    
                                                    .. attribute:: excess_ratio
                                                    
                                                    	Excess Ratio
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: sum_of_bandwidth
                                                    
                                                    	Sum of Bandwidth
                                                    	**type**\:   :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.bandwidth = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth()
                                                        self.bandwidth.parent = self
                                                        self.excess_ratio = None
                                                        self.sum_of_bandwidth = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth()
                                                        self.sum_of_bandwidth.parent = self


                                                    class Bandwidth(object):
                                                        """
                                                        Bandwidth
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.unit = None
                                                            self.value = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bandwidth'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.unit is not None:
                                                                return True

                                                            if self.value is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth']['meta_info']


                                                    class SumOfBandwidth(object):
                                                        """
                                                        Sum of Bandwidth
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.unit = None
                                                            self.value = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:sum-of-bandwidth'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.unit is not None:
                                                                return True

                                                            if self.value is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:wfq'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.bandwidth is not None and self.bandwidth._has_data():
                                                            return True

                                                        if self.excess_ratio is not None:
                                                            return True

                                                        if self.sum_of_bandwidth is not None and self.sum_of_bandwidth._has_data():
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:config'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.node_config is not None:
                                                        return True

                                                    if self.police is not None and self.police._has_data():
                                                        return True

                                                    if self.shape is not None and self.shape._has_data():
                                                        return True

                                                    if self.wfq is not None and self.wfq._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']


                                            class Result(object):
                                                """
                                                QoS EA Class Result
                                                
                                                .. attribute:: police
                                                
                                                	QoS EA Policer Result
                                                	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police>`
                                                
                                                .. attribute:: queue
                                                
                                                	QoS EA Queue Result
                                                	**type**\:   :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue>`
                                                
                                                .. attribute:: stats_id
                                                
                                                	Stats ID
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.police = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police()
                                                    self.police.parent = self
                                                    self.queue = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue()
                                                    self.queue.parent = self
                                                    self.stats_id = None


                                                class Queue(object):
                                                    """
                                                    QoS EA Queue Result
                                                    
                                                    .. attribute:: commit_tx
                                                    
                                                    	Commit Tx
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: drop
                                                    
                                                    	Drop
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: excess_tx
                                                    
                                                    	Excess Tx
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: queue_id
                                                    
                                                    	Queue ID
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.commit_tx = None
                                                        self.drop = None
                                                        self.excess_tx = None
                                                        self.queue_id = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:queue'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.commit_tx is not None:
                                                            return True

                                                        if self.drop is not None:
                                                            return True

                                                        if self.excess_tx is not None:
                                                            return True

                                                        if self.queue_id is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue']['meta_info']


                                                class Police(object):
                                                    """
                                                    QoS EA Policer Result
                                                    
                                                    .. attribute:: conform
                                                    
                                                    	Conform Rate
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: exceed
                                                    
                                                    	Exceed Rate
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: token_bucket_id
                                                    
                                                    	Token Bucket ID
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: violate
                                                    
                                                    	Violate Rate
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.conform = None
                                                        self.exceed = None
                                                        self.token_bucket_id = None
                                                        self.violate = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.conform is not None:
                                                            return True

                                                        if self.exceed is not None:
                                                            return True

                                                        if self.token_bucket_id is not None:
                                                            return True

                                                        if self.violate is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:result'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.police is not None and self.police._has_data():
                                                        return True

                                                    if self.queue is not None and self.queue._has_data():
                                                        return True

                                                    if self.stats_id is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:qos-show-ea-pclass-st'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.class_level is not None:
                                                    return True

                                                if self.class_name is not None:
                                                    return True

                                                if self.config is not None and self.config._has_data():
                                                    return True

                                                if self.index is not None:
                                                    return True

                                                if self.node_flags is not None:
                                                    return True

                                                if self.policy_name is not None:
                                                    return True

                                                if self.result is not None and self.result._has_data():
                                                    return True

                                                if self.stats_flags is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:skywarp-qos-policy-class'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.qos_show_ea_pclass_st is not None:
                                                for child_ref in self.qos_show_ea_pclass_st:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:details'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.header is not None and self.header._has_data():
                                            return True

                                        if self.interface_parameters is not None and self.interface_parameters._has_data():
                                            return True

                                        if self.skywarp_qos_policy_class is not None and self.skywarp_qos_policy_class._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bundle-input'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.details is not None and self.details._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.interface_name is None:
                                    raise YPYModelError('Key property interface_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:member-interface[Cisco-IOS-XR-skp-qos-oper:interface-name = ' + str(self.interface_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.interface_name is not None:
                                    return True

                                if self.bundle_input is not None and self.bundle_input._has_data():
                                    return True

                                if self.bundle_output is not None and self.bundle_output._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:member-interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.member_interface is not None:
                                for child_ref in self.member_interface:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bundle-interface[Cisco-IOS-XR-skp-qos-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.member_interfaces is not None and self.member_interfaces._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bundle-interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bundle_interface is not None:
                        for child_ref in self.bundle_interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                    return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces']['meta_info']


            class Interfaces(object):
                """
                QoS\-EA list of interfaces
                
                .. attribute:: interface
                
                	QoS\-EA interface name
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'skp-qos-oper'
                _revision = '2016-02-18'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    QoS\-EA interface name
                    
                    .. attribute:: interface_name  <key>
                    
                    	The name of the interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: input
                    
                    	QoS\-EA policy direction ingress
                    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input>`
                    
                    .. attribute:: output
                    
                    	QoS\-EA policy direction egress
                    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output>`
                    
                    

                    """

                    _prefix = 'skp-qos-oper'
                    _revision = '2016-02-18'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.input = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input()
                        self.input.parent = self
                        self.output = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output()
                        self.output.parent = self


                    class Output(object):
                        """
                        QoS\-EA policy direction egress
                        
                        .. attribute:: details
                        
                        	QoS\-EA policy details
                        	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details>`
                        
                        

                        """

                        _prefix = 'skp-qos-oper'
                        _revision = '2016-02-18'

                        def __init__(self):
                            self.parent = None
                            self.details = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details()
                            self.details.parent = self


                        class Details(object):
                            """
                            QoS\-EA policy details
                            
                            .. attribute:: header
                            
                            	QoS EA policy header
                            	**type**\:   :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.Header>`
                            
                            .. attribute:: interface_parameters
                            
                            	QoS EA Interface Parameters
                            	**type**\:   :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.InterfaceParameters>`
                            
                            .. attribute:: skywarp_qos_policy_class
                            
                            	Skywarp QoS EA policy class details
                            	**type**\:   :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass>`
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                self.parent = None
                                self.header = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.Header()
                                self.header.parent = self
                                self.interface_parameters = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.InterfaceParameters()
                                self.interface_parameters.parent = self
                                self.skywarp_qos_policy_class = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass()
                                self.skywarp_qos_policy_class.parent = self


                            class Header(object):
                                """
                                QoS EA policy header
                                
                                .. attribute:: classes
                                
                                	Number of classes
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: direction
                                
                                	Direction
                                	**type**\:  str
                                
                                	**length:** 0..11
                                
                                .. attribute:: interface_name
                                
                                	Interface Name
                                	**type**\:  str
                                
                                	**length:** 0..101
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\:  str
                                
                                	**length:** 0..65
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.classes = None
                                    self.direction = None
                                    self.interface_name = None
                                    self.policy_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:header'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.classes is not None:
                                        return True

                                    if self.direction is not None:
                                        return True

                                    if self.interface_name is not None:
                                        return True

                                    if self.policy_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.Header']['meta_info']


                            class InterfaceParameters(object):
                                """
                                QoS EA Interface Parameters
                                
                                .. attribute:: bundle_id
                                
                                	Bundle Interface ID
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: hierarchical_depth
                                
                                	Max Hierarchial Depth
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: interface_handle
                                
                                	Interface Handle
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: interface_rate
                                
                                	Interface Programmed Rate
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_type
                                
                                	Interface Type
                                	**type**\:  str
                                
                                	**length:** 0..101
                                
                                .. attribute:: policy_map_id
                                
                                	Policy Map ID
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\:  str
                                
                                	**length:** 0..65
                                
                                .. attribute:: port
                                
                                	Local Port
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: port_shaper_rate
                                
                                	Port Shaper Rate
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: qos_interface_handle
                                
                                	QoS Interface handle
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: uidb_index
                                
                                	UIDB Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: under_line_interface_handle
                                
                                	UnderLineInterface Handle
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.bundle_id = None
                                    self.hierarchical_depth = None
                                    self.interface_handle = None
                                    self.interface_rate = None
                                    self.interface_type = None
                                    self.policy_map_id = None
                                    self.policy_name = None
                                    self.port = None
                                    self.port_shaper_rate = None
                                    self.qos_interface_handle = None
                                    self.uidb_index = None
                                    self.under_line_interface_handle = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-parameters'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.bundle_id is not None:
                                        return True

                                    if self.hierarchical_depth is not None:
                                        return True

                                    if self.interface_handle is not None:
                                        return True

                                    if self.interface_rate is not None:
                                        return True

                                    if self.interface_type is not None:
                                        return True

                                    if self.policy_map_id is not None:
                                        return True

                                    if self.policy_name is not None:
                                        return True

                                    if self.port is not None:
                                        return True

                                    if self.port_shaper_rate is not None:
                                        return True

                                    if self.qos_interface_handle is not None:
                                        return True

                                    if self.uidb_index is not None:
                                        return True

                                    if self.under_line_interface_handle is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.InterfaceParameters']['meta_info']


                            class SkywarpQosPolicyClass(object):
                                """
                                Skywarp QoS EA policy class details
                                
                                .. attribute:: qos_show_ea_pclass_st
                                
                                	qos show ea pclass st
                                	**type**\: list of    :py:class:`QosShowEaPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt>`
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.qos_show_ea_pclass_st = YList()
                                    self.qos_show_ea_pclass_st.parent = self
                                    self.qos_show_ea_pclass_st.name = 'qos_show_ea_pclass_st'


                                class QosShowEaPclassSt(object):
                                    """
                                    qos show ea pclass st
                                    
                                    .. attribute:: class_level
                                    
                                    	Class level
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: class_name
                                    
                                    	Class name
                                    	**type**\:  str
                                    
                                    	**length:** 0..65
                                    
                                    .. attribute:: config
                                    
                                    	QoS EA Class Configuration
                                    	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config>`
                                    
                                    .. attribute:: index
                                    
                                    	Class Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: node_flags
                                    
                                    	Node Flags
                                    	**type**\:  str
                                    
                                    	**length:** 0..101
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\:  str
                                    
                                    	**length:** 0..65
                                    
                                    .. attribute:: result
                                    
                                    	QoS EA Class Result
                                    	**type**\:   :py:class:`Result <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result>`
                                    
                                    .. attribute:: stats_flags
                                    
                                    	Statistical Flags
                                    	**type**\:  str
                                    
                                    	**length:** 0..101
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.class_level = None
                                        self.class_name = None
                                        self.config = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config()
                                        self.config.parent = self
                                        self.index = None
                                        self.node_flags = None
                                        self.policy_name = None
                                        self.result = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result()
                                        self.result.parent = self
                                        self.stats_flags = None


                                    class Config(object):
                                        """
                                        QoS EA Class Configuration
                                        
                                        .. attribute:: node_config
                                        
                                        	Node Config
                                        	**type**\:  str
                                        
                                        	**length:** 0..101
                                        
                                        .. attribute:: police
                                        
                                        	QoS EA Policer parameters
                                        	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police>`
                                        
                                        .. attribute:: shape
                                        
                                        	QoS EA Shaper parameters
                                        	**type**\:   :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape>`
                                        
                                        .. attribute:: wfq
                                        
                                        	QoS EA WFQ parameters
                                        	**type**\:   :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq>`
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.node_config = None
                                            self.police = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police()
                                            self.police.parent = self
                                            self.shape = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape()
                                            self.shape.parent = self
                                            self.wfq = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq()
                                            self.wfq.parent = self


                                        class Police(object):
                                            """
                                            QoS EA Policer parameters
                                            
                                            .. attribute:: cbs
                                            
                                            	CBS
                                            	**type**\:   :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs>`
                                            
                                            .. attribute:: cir
                                            
                                            	CIR
                                            	**type**\:   :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir>`
                                            
                                            .. attribute:: color_aware
                                            
                                            	Color Aware
                                            	**type**\:  bool
                                            
                                            .. attribute:: policer_type
                                            
                                            	Policer type
                                            	**type**\:   :py:class:`TbAlgorithmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithmEnum>`
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.cbs = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs()
                                                self.cbs.parent = self
                                                self.cir = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir()
                                                self.cir.parent = self
                                                self.color_aware = None
                                                self.policer_type = None


                                            class Cir(object):
                                                """
                                                CIR
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cir'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir']['meta_info']


                                            class Cbs(object):
                                                """
                                                CBS
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cbs'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.cbs is not None and self.cbs._has_data():
                                                    return True

                                                if self.cir is not None and self.cir._has_data():
                                                    return True

                                                if self.color_aware is not None:
                                                    return True

                                                if self.policer_type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']


                                        class Shape(object):
                                            """
                                            QoS EA Shaper parameters
                                            
                                            .. attribute:: pbs
                                            
                                            	PBS in bytes
                                            	**type**\:   :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs>`
                                            
                                            .. attribute:: pir
                                            
                                            	PIR in kbps
                                            	**type**\:   :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir>`
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.pbs = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs()
                                                self.pbs.parent = self
                                                self.pir = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir()
                                                self.pir.parent = self


                                            class Pir(object):
                                                """
                                                PIR in kbps
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pir'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir']['meta_info']


                                            class Pbs(object):
                                                """
                                                PBS in bytes
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pbs'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:shape'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.pbs is not None and self.pbs._has_data():
                                                    return True

                                                if self.pir is not None and self.pir._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']


                                        class Wfq(object):
                                            """
                                            QoS EA WFQ parameters
                                            
                                            .. attribute:: bandwidth
                                            
                                            	Bandwidth
                                            	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth>`
                                            
                                            .. attribute:: excess_ratio
                                            
                                            	Excess Ratio
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: sum_of_bandwidth
                                            
                                            	Sum of Bandwidth
                                            	**type**\:   :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth>`
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.bandwidth = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth()
                                                self.bandwidth.parent = self
                                                self.excess_ratio = None
                                                self.sum_of_bandwidth = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth()
                                                self.sum_of_bandwidth.parent = self


                                            class Bandwidth(object):
                                                """
                                                Bandwidth
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bandwidth'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth']['meta_info']


                                            class SumOfBandwidth(object):
                                                """
                                                Sum of Bandwidth
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:sum-of-bandwidth'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:wfq'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.bandwidth is not None and self.bandwidth._has_data():
                                                    return True

                                                if self.excess_ratio is not None:
                                                    return True

                                                if self.sum_of_bandwidth is not None and self.sum_of_bandwidth._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:config'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.node_config is not None:
                                                return True

                                            if self.police is not None and self.police._has_data():
                                                return True

                                            if self.shape is not None and self.shape._has_data():
                                                return True

                                            if self.wfq is not None and self.wfq._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']


                                    class Result(object):
                                        """
                                        QoS EA Class Result
                                        
                                        .. attribute:: police
                                        
                                        	QoS EA Policer Result
                                        	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police>`
                                        
                                        .. attribute:: queue
                                        
                                        	QoS EA Queue Result
                                        	**type**\:   :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue>`
                                        
                                        .. attribute:: stats_id
                                        
                                        	Stats ID
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.police = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police()
                                            self.police.parent = self
                                            self.queue = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue()
                                            self.queue.parent = self
                                            self.stats_id = None


                                        class Queue(object):
                                            """
                                            QoS EA Queue Result
                                            
                                            .. attribute:: commit_tx
                                            
                                            	Commit Tx
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: drop
                                            
                                            	Drop
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: excess_tx
                                            
                                            	Excess Tx
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: queue_id
                                            
                                            	Queue ID
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.commit_tx = None
                                                self.drop = None
                                                self.excess_tx = None
                                                self.queue_id = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:queue'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.commit_tx is not None:
                                                    return True

                                                if self.drop is not None:
                                                    return True

                                                if self.excess_tx is not None:
                                                    return True

                                                if self.queue_id is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue']['meta_info']


                                        class Police(object):
                                            """
                                            QoS EA Policer Result
                                            
                                            .. attribute:: conform
                                            
                                            	Conform Rate
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: exceed
                                            
                                            	Exceed Rate
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: token_bucket_id
                                            
                                            	Token Bucket ID
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: violate
                                            
                                            	Violate Rate
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.conform = None
                                                self.exceed = None
                                                self.token_bucket_id = None
                                                self.violate = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.conform is not None:
                                                    return True

                                                if self.exceed is not None:
                                                    return True

                                                if self.token_bucket_id is not None:
                                                    return True

                                                if self.violate is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:result'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.police is not None and self.police._has_data():
                                                return True

                                            if self.queue is not None and self.queue._has_data():
                                                return True

                                            if self.stats_id is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:qos-show-ea-pclass-st'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.class_level is not None:
                                            return True

                                        if self.class_name is not None:
                                            return True

                                        if self.config is not None and self.config._has_data():
                                            return True

                                        if self.index is not None:
                                            return True

                                        if self.node_flags is not None:
                                            return True

                                        if self.policy_name is not None:
                                            return True

                                        if self.result is not None and self.result._has_data():
                                            return True

                                        if self.stats_flags is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:skywarp-qos-policy-class'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.qos_show_ea_pclass_st is not None:
                                        for child_ref in self.qos_show_ea_pclass_st:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:details'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.header is not None and self.header._has_data():
                                    return True

                                if self.interface_parameters is not None and self.interface_parameters._has_data():
                                    return True

                                if self.skywarp_qos_policy_class is not None and self.skywarp_qos_policy_class._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:output'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.details is not None and self.details._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                            return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output']['meta_info']


                    class Input(object):
                        """
                        QoS\-EA policy direction ingress
                        
                        .. attribute:: details
                        
                        	QoS\-EA policy details
                        	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details>`
                        
                        

                        """

                        _prefix = 'skp-qos-oper'
                        _revision = '2016-02-18'

                        def __init__(self):
                            self.parent = None
                            self.details = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details()
                            self.details.parent = self


                        class Details(object):
                            """
                            QoS\-EA policy details
                            
                            .. attribute:: header
                            
                            	QoS EA policy header
                            	**type**\:   :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.Header>`
                            
                            .. attribute:: interface_parameters
                            
                            	QoS EA Interface Parameters
                            	**type**\:   :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.InterfaceParameters>`
                            
                            .. attribute:: skywarp_qos_policy_class
                            
                            	Skywarp QoS EA policy class details
                            	**type**\:   :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass>`
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                self.parent = None
                                self.header = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.Header()
                                self.header.parent = self
                                self.interface_parameters = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.InterfaceParameters()
                                self.interface_parameters.parent = self
                                self.skywarp_qos_policy_class = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass()
                                self.skywarp_qos_policy_class.parent = self


                            class Header(object):
                                """
                                QoS EA policy header
                                
                                .. attribute:: classes
                                
                                	Number of classes
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: direction
                                
                                	Direction
                                	**type**\:  str
                                
                                	**length:** 0..11
                                
                                .. attribute:: interface_name
                                
                                	Interface Name
                                	**type**\:  str
                                
                                	**length:** 0..101
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\:  str
                                
                                	**length:** 0..65
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.classes = None
                                    self.direction = None
                                    self.interface_name = None
                                    self.policy_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:header'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.classes is not None:
                                        return True

                                    if self.direction is not None:
                                        return True

                                    if self.interface_name is not None:
                                        return True

                                    if self.policy_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.Header']['meta_info']


                            class InterfaceParameters(object):
                                """
                                QoS EA Interface Parameters
                                
                                .. attribute:: bundle_id
                                
                                	Bundle Interface ID
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: hierarchical_depth
                                
                                	Max Hierarchial Depth
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: interface_handle
                                
                                	Interface Handle
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: interface_rate
                                
                                	Interface Programmed Rate
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_type
                                
                                	Interface Type
                                	**type**\:  str
                                
                                	**length:** 0..101
                                
                                .. attribute:: policy_map_id
                                
                                	Policy Map ID
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\:  str
                                
                                	**length:** 0..65
                                
                                .. attribute:: port
                                
                                	Local Port
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: port_shaper_rate
                                
                                	Port Shaper Rate
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: qos_interface_handle
                                
                                	QoS Interface handle
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: uidb_index
                                
                                	UIDB Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: under_line_interface_handle
                                
                                	UnderLineInterface Handle
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.bundle_id = None
                                    self.hierarchical_depth = None
                                    self.interface_handle = None
                                    self.interface_rate = None
                                    self.interface_type = None
                                    self.policy_map_id = None
                                    self.policy_name = None
                                    self.port = None
                                    self.port_shaper_rate = None
                                    self.qos_interface_handle = None
                                    self.uidb_index = None
                                    self.under_line_interface_handle = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface-parameters'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.bundle_id is not None:
                                        return True

                                    if self.hierarchical_depth is not None:
                                        return True

                                    if self.interface_handle is not None:
                                        return True

                                    if self.interface_rate is not None:
                                        return True

                                    if self.interface_type is not None:
                                        return True

                                    if self.policy_map_id is not None:
                                        return True

                                    if self.policy_name is not None:
                                        return True

                                    if self.port is not None:
                                        return True

                                    if self.port_shaper_rate is not None:
                                        return True

                                    if self.qos_interface_handle is not None:
                                        return True

                                    if self.uidb_index is not None:
                                        return True

                                    if self.under_line_interface_handle is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.InterfaceParameters']['meta_info']


                            class SkywarpQosPolicyClass(object):
                                """
                                Skywarp QoS EA policy class details
                                
                                .. attribute:: qos_show_ea_pclass_st
                                
                                	qos show ea pclass st
                                	**type**\: list of    :py:class:`QosShowEaPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt>`
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    self.parent = None
                                    self.qos_show_ea_pclass_st = YList()
                                    self.qos_show_ea_pclass_st.parent = self
                                    self.qos_show_ea_pclass_st.name = 'qos_show_ea_pclass_st'


                                class QosShowEaPclassSt(object):
                                    """
                                    qos show ea pclass st
                                    
                                    .. attribute:: class_level
                                    
                                    	Class level
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: class_name
                                    
                                    	Class name
                                    	**type**\:  str
                                    
                                    	**length:** 0..65
                                    
                                    .. attribute:: config
                                    
                                    	QoS EA Class Configuration
                                    	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config>`
                                    
                                    .. attribute:: index
                                    
                                    	Class Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: node_flags
                                    
                                    	Node Flags
                                    	**type**\:  str
                                    
                                    	**length:** 0..101
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\:  str
                                    
                                    	**length:** 0..65
                                    
                                    .. attribute:: result
                                    
                                    	QoS EA Class Result
                                    	**type**\:   :py:class:`Result <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result>`
                                    
                                    .. attribute:: stats_flags
                                    
                                    	Statistical Flags
                                    	**type**\:  str
                                    
                                    	**length:** 0..101
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.class_level = None
                                        self.class_name = None
                                        self.config = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config()
                                        self.config.parent = self
                                        self.index = None
                                        self.node_flags = None
                                        self.policy_name = None
                                        self.result = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result()
                                        self.result.parent = self
                                        self.stats_flags = None


                                    class Config(object):
                                        """
                                        QoS EA Class Configuration
                                        
                                        .. attribute:: node_config
                                        
                                        	Node Config
                                        	**type**\:  str
                                        
                                        	**length:** 0..101
                                        
                                        .. attribute:: police
                                        
                                        	QoS EA Policer parameters
                                        	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police>`
                                        
                                        .. attribute:: shape
                                        
                                        	QoS EA Shaper parameters
                                        	**type**\:   :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape>`
                                        
                                        .. attribute:: wfq
                                        
                                        	QoS EA WFQ parameters
                                        	**type**\:   :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq>`
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.node_config = None
                                            self.police = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police()
                                            self.police.parent = self
                                            self.shape = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape()
                                            self.shape.parent = self
                                            self.wfq = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq()
                                            self.wfq.parent = self


                                        class Police(object):
                                            """
                                            QoS EA Policer parameters
                                            
                                            .. attribute:: cbs
                                            
                                            	CBS
                                            	**type**\:   :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs>`
                                            
                                            .. attribute:: cir
                                            
                                            	CIR
                                            	**type**\:   :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir>`
                                            
                                            .. attribute:: color_aware
                                            
                                            	Color Aware
                                            	**type**\:  bool
                                            
                                            .. attribute:: policer_type
                                            
                                            	Policer type
                                            	**type**\:   :py:class:`TbAlgorithmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithmEnum>`
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.cbs = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs()
                                                self.cbs.parent = self
                                                self.cir = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir()
                                                self.cir.parent = self
                                                self.color_aware = None
                                                self.policer_type = None


                                            class Cir(object):
                                                """
                                                CIR
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cir'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir']['meta_info']


                                            class Cbs(object):
                                                """
                                                CBS
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:cbs'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.cbs is not None and self.cbs._has_data():
                                                    return True

                                                if self.cir is not None and self.cir._has_data():
                                                    return True

                                                if self.color_aware is not None:
                                                    return True

                                                if self.policer_type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']


                                        class Shape(object):
                                            """
                                            QoS EA Shaper parameters
                                            
                                            .. attribute:: pbs
                                            
                                            	PBS in bytes
                                            	**type**\:   :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs>`
                                            
                                            .. attribute:: pir
                                            
                                            	PIR in kbps
                                            	**type**\:   :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir>`
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.pbs = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs()
                                                self.pbs.parent = self
                                                self.pir = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir()
                                                self.pir.parent = self


                                            class Pir(object):
                                                """
                                                PIR in kbps
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pir'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir']['meta_info']


                                            class Pbs(object):
                                                """
                                                PBS in bytes
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:pbs'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:shape'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.pbs is not None and self.pbs._has_data():
                                                    return True

                                                if self.pir is not None and self.pir._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']


                                        class Wfq(object):
                                            """
                                            QoS EA WFQ parameters
                                            
                                            .. attribute:: bandwidth
                                            
                                            	Bandwidth
                                            	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth>`
                                            
                                            .. attribute:: excess_ratio
                                            
                                            	Excess Ratio
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: sum_of_bandwidth
                                            
                                            	Sum of Bandwidth
                                            	**type**\:   :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth>`
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.bandwidth = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth()
                                                self.bandwidth.parent = self
                                                self.excess_ratio = None
                                                self.sum_of_bandwidth = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth()
                                                self.sum_of_bandwidth.parent = self


                                            class Bandwidth(object):
                                                """
                                                Bandwidth
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:bandwidth'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth']['meta_info']


                                            class SumOfBandwidth(object):
                                                """
                                                Sum of Bandwidth
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:   :py:class:`QosUnitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnitEnum>`
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.unit = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:sum-of-bandwidth'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.unit is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:wfq'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.bandwidth is not None and self.bandwidth._has_data():
                                                    return True

                                                if self.excess_ratio is not None:
                                                    return True

                                                if self.sum_of_bandwidth is not None and self.sum_of_bandwidth._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:config'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.node_config is not None:
                                                return True

                                            if self.police is not None and self.police._has_data():
                                                return True

                                            if self.shape is not None and self.shape._has_data():
                                                return True

                                            if self.wfq is not None and self.wfq._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']


                                    class Result(object):
                                        """
                                        QoS EA Class Result
                                        
                                        .. attribute:: police
                                        
                                        	QoS EA Policer Result
                                        	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police>`
                                        
                                        .. attribute:: queue
                                        
                                        	QoS EA Queue Result
                                        	**type**\:   :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue>`
                                        
                                        .. attribute:: stats_id
                                        
                                        	Stats ID
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.police = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police()
                                            self.police.parent = self
                                            self.queue = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue()
                                            self.queue.parent = self
                                            self.stats_id = None


                                        class Queue(object):
                                            """
                                            QoS EA Queue Result
                                            
                                            .. attribute:: commit_tx
                                            
                                            	Commit Tx
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: drop
                                            
                                            	Drop
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: excess_tx
                                            
                                            	Excess Tx
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: queue_id
                                            
                                            	Queue ID
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.commit_tx = None
                                                self.drop = None
                                                self.excess_tx = None
                                                self.queue_id = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:queue'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.commit_tx is not None:
                                                    return True

                                                if self.drop is not None:
                                                    return True

                                                if self.excess_tx is not None:
                                                    return True

                                                if self.queue_id is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue']['meta_info']


                                        class Police(object):
                                            """
                                            QoS EA Policer Result
                                            
                                            .. attribute:: conform
                                            
                                            	Conform Rate
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: exceed
                                            
                                            	Exceed Rate
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: token_bucket_id
                                            
                                            	Token Bucket ID
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: violate
                                            
                                            	Violate Rate
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                self.parent = None
                                                self.conform = None
                                                self.exceed = None
                                                self.token_bucket_id = None
                                                self.violate = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:police'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.conform is not None:
                                                    return True

                                                if self.exceed is not None:
                                                    return True

                                                if self.token_bucket_id is not None:
                                                    return True

                                                if self.violate is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:result'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.police is not None and self.police._has_data():
                                                return True

                                            if self.queue is not None and self.queue._has_data():
                                                return True

                                            if self.stats_id is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:qos-show-ea-pclass-st'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.class_level is not None:
                                            return True

                                        if self.class_name is not None:
                                            return True

                                        if self.config is not None and self.config._has_data():
                                            return True

                                        if self.index is not None:
                                            return True

                                        if self.node_flags is not None:
                                            return True

                                        if self.policy_name is not None:
                                            return True

                                        if self.result is not None and self.result._has_data():
                                            return True

                                        if self.stats_flags is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:skywarp-qos-policy-class'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.qos_show_ea_pclass_st is not None:
                                        for child_ref in self.qos_show_ea_pclass_st:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:details'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.header is not None and self.header._has_data():
                                    return True

                                if self.interface_parameters is not None and self.interface_parameters._has_data():
                                    return True

                                if self.skywarp_qos_policy_class is not None and self.skywarp_qos_policy_class._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:input'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.details is not None and self.details._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                            return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interface[Cisco-IOS-XR-skp-qos-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.input is not None and self.input._has_data():
                            return True

                        if self.output is not None and self.output._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                        return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-skp-qos-oper:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-skp-qos-oper:platform-qos-ea/Cisco-IOS-XR-skp-qos-oper:nodes/Cisco-IOS-XR-skp-qos-oper:node[Cisco-IOS-XR-skp-qos-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.bundle_interfaces is not None and self.bundle_interfaces._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                return meta._meta_table['PlatformQosEa.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-skp-qos-oper:platform-qos-ea/Cisco-IOS-XR-skp-qos-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
            return meta._meta_table['PlatformQosEa.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-skp-qos-oper:platform-qos-ea'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['PlatformQosEa']['meta_info']



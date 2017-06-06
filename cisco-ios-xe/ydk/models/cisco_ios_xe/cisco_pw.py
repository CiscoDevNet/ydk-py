""" cisco_pw 

This YANG module describes the configuration and operational
model of Psuedowire on PE router

Terms and Acronyms
   AC    \: Attachment Circuit
   BD    \: Bridge Domain
   L2VPN \: Layer 2 Virtual Private Network
   PE    \: Provider Edge
   PW    \: Pseudowire
   VFI   \: Virtual Forwarding Instance
   VPLS  \: Virtual Private LAN Service
   VLAN  \: Virtual Local Area Network


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class PwOperStateTypeEnum(Enum):
    """
    PwOperStateTypeEnum

    Indicates the operational status of the PW VC

    .. data:: up = 1

    	Pseudowire is established, i.e., it is operational

    	and available to carry packets

    .. data:: down = 2

    	Pseudowire is idle, i.e., it is administratively up

    	but network connectivity with the neighbor is not

    	established

    .. data:: cold_standby = 3

    	Pseudowire can take over traffic for another

    	pseudowire

    .. data:: hot_standby = 4

    	Pseudowire is available to immediately take over

    	traffic from another pseudowire

    .. data:: recovering = 5

    	Pseudowire was previously in active state and is

    	in the process of being restored to active state

    .. data:: no_hardware = 6

    	Pseudowire no longer has the required hardware

    	resources to be able to offer packet service to

    	the system

    .. data:: unresolved = 7

    	Pseudowire is not completely provisioned

    .. data:: provisioned = 8

    	Pseudowire has received local configuration

    .. data:: remote_standby = 9

    	Pseudowire neighbor has sent its pseudowire

    	binding information

    .. data:: local_ready = 10

    	Pseudowire is provisioned, got a local label, and

    	its local binding has been sent to the neighbor

    .. data:: all_ready = 11

    	Pseudowire is locally provisioned, local binding

    	has been sent, and remote binding was received

    	from the neighbor

    """

    up = 1

    down = 2

    cold_standby = 3

    hot_standby = 4

    recovering = 5

    no_hardware = 6

    unresolved = 7

    provisioned = 8

    remote_standby = 9

    local_ready = 10

    all_ready = 11


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwOperStateTypeEnum']



class PwLoadBalanceTypeIdentity(object):
    """
    Base type for load\-balancing type
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwLoadBalanceTypeIdentity']['meta_info']


class PwSignalingProtocolTypeIdentity(object):
    """
    Base identity for PW signaling protocol
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwSignalingProtocolTypeIdentity']['meta_info']


class PwSequencingTypeIdentity(object):
    """
    Sequencing options for PW
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwSequencingTypeIdentity']['meta_info']


class PwVcTypeIdentity(object):
    """
    Base identity for VC type in PW
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwVcTypeIdentity']['meta_info']


class PwEncapsulationTypeIdentity(object):
    """
    Base identity for PW encapsulations.
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwEncapsulationTypeIdentity']['meta_info']


class PseudowireConfig(object):
    """
    Pseudowire configuration data.
    
    .. attribute:: global_
    
    	Global configurations related to pseudowires
    	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.Global_>`
    
    .. attribute:: pw_static_oam_classes
    
    	List of pseudowire static oam classes
    	**type**\:   :py:class:`PwStaticOamClasses <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwStaticOamClasses>`
    
    .. attribute:: pw_templates
    
    	Contains list of all pw\-template definitions. Also called PW Class (XR) and Port Profile (NX\-OS)
    	**type**\:   :py:class:`PwTemplates <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates>`
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        self.global_ = PseudowireConfig.Global_()
        self.global_.parent = self
        self.pw_static_oam_classes = PseudowireConfig.PwStaticOamClasses()
        self.pw_static_oam_classes.parent = self
        self.pw_templates = PseudowireConfig.PwTemplates()
        self.pw_templates.parent = self


    class Global_(object):
        """
        Global configurations related to pseudowires.
        
        .. attribute:: predictive_redundancy
        
        	Enable predictive redundancy
        	**type**\:  bool
        
        .. attribute:: pw_grouping
        
        	Enable pw\-grouping.  When pseudowires (PW) are established, each PW is assigned a group ID that is common for all PWs created from the same physical port. Hence, when the physical port becomes non\-functional or is deleted, L2VPN sends a single message to advertise the status change of all PWs belonging to the group. A single L2VPN signal thus avoids a lot of processing and loss in reactivity
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: pw_oam_refresh_transmit
        
        	Set pseudowire oam transmit refresh time (in seconds)
        	**type**\:  int
        
        	**range:** 1..4095
        
        .. attribute:: pw_status
        
        	Enable pw\-status
        	**type**\:  bool
        
        .. attribute:: vc_state_notification_batch_size
        
        	'vc\-state\-notification' allows batching of pseudowires in order to reduce number of notifications generated from the device. All pseudowires in a batched notification MUST share same state at the same time.  This leaf defines the maximum number of VCs that can be batched in vc\-state\-notification
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_state_notification_enabled
        
        	If this leaf is set to true, then it enables the emission of 'vc\-state\-notification'; otherwise these notifications are not emitted
        	**type**\:  bool
        
        .. attribute:: vc_state_notification_rate
        
        	This leaf defines the maximum number of VC state change notifications that can be emitted from the device per second
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'l2vpn-pw'
        _revision = '2016-12-07'

        def __init__(self):
            self.parent = None
            self.predictive_redundancy = None
            self.pw_grouping = None
            self.pw_oam_refresh_transmit = None
            self.pw_status = None
            self.vc_state_notification_batch_size = None
            self.vc_state_notification_enabled = None
            self.vc_state_notification_rate = None

        @property
        def _common_path(self):

            return '/cisco-pw:pseudowire-config/cisco-pw:global'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.predictive_redundancy is not None:
                return True

            if self.pw_grouping is not None:
                return True

            if self.pw_oam_refresh_transmit is not None:
                return True

            if self.pw_status is not None:
                return True

            if self.vc_state_notification_batch_size is not None:
                return True

            if self.vc_state_notification_enabled is not None:
                return True

            if self.vc_state_notification_rate is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
            return meta._meta_table['PseudowireConfig.Global_']['meta_info']


    class PwTemplates(object):
        """
        Contains list of all pw\-template definitions.
        Also called PW Class (XR) and Port Profile (NX\-OS)
        
        .. attribute:: pw_template
        
        	Pseudowire template list
        	**type**\: list of    :py:class:`PwTemplate <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate>`
        
        

        """

        _prefix = 'l2vpn-pw'
        _revision = '2016-12-07'

        def __init__(self):
            self.parent = None
            self.pw_template = YList()
            self.pw_template.parent = self
            self.pw_template.name = 'pw_template'


        class PwTemplate(object):
            """
            Pseudowire template list.
            
            .. attribute:: name  <key>
            
            	PW Template name
            	**type**\:  str
            
            .. attribute:: control_word
            
            	Use control word in the MPLS PW header
            	**type**\:  bool
            
            .. attribute:: encapsulation
            
            	Encapsulation used for PW
            	**type**\:   :py:class:`PwEncapsulationTypeIdentity <ydk.models.cisco_ios_xe.cisco_pw.PwEncapsulationTypeIdentity>`
            
            .. attribute:: load_balance
            
            	Load balancing mechanism
            	**type**\:   :py:class:`LoadBalance <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.LoadBalance>`
            
            .. attribute:: mac_withdraw
            
            	Send Mac\-withdraw message when PW becomes active
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: port_profile_spec
            
            	Pseudowire port profile configurations
            	**type**\:   :py:class:`PortProfileSpec <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec>`
            
            .. attribute:: preferred_path
            
            	Preferred path for the PW
            	**type**\:   :py:class:`PreferredPath <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.PreferredPath>`
            
            .. attribute:: sequencing
            
            	Sequencing options
            	**type**\:   :py:class:`Sequencing <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.Sequencing>`
            
            .. attribute:: signaling_protocol
            
            	Signaling protocol to use
            	**type**\:   :py:class:`PwSignalingProtocolTypeIdentity <ydk.models.cisco_ios_xe.cisco_pw.PwSignalingProtocolTypeIdentity>`
            
            .. attribute:: source_ip
            
            	The local source IPv4 address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: status
            
            	TODO
            	**type**\:   :py:class:`Status <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.Status>`
            
            .. attribute:: switching_tlv
            
            	Send switching TLV
            	**type**\:  bool
            
            .. attribute:: switchover_delay
            
            	Timer configuration related to pseudowire redundancy switchover and restoring to primary
            	**type**\:   :py:class:`SwitchoverDelay <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay>`
            
            .. attribute:: tag_rewrite_ingress_vlan
            
            	Configure ingress tag rewrite vlan
            	**type**\:  int
            
            	**range:** 1..4094
            
            .. attribute:: vc_type
            
            	Type of VC in the PW
            	**type**\:   :py:class:`PwVcTypeIdentity <ydk.models.cisco_ios_xe.cisco_pw.PwVcTypeIdentity>`
            
            .. attribute:: vccv
            
            	VCCV configuration
            	**type**\:   :py:class:`Vccv <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.Vccv>`
            
            

            """

            _prefix = 'l2vpn-pw'
            _revision = '2016-12-07'

            def __init__(self):
                self.parent = None
                self.name = None
                self.control_word = None
                self.encapsulation = None
                self.load_balance = PseudowireConfig.PwTemplates.PwTemplate.LoadBalance()
                self.load_balance.parent = self
                self.mac_withdraw = None
                self.port_profile_spec = PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec()
                self.port_profile_spec.parent = self
                self.preferred_path = PseudowireConfig.PwTemplates.PwTemplate.PreferredPath()
                self.preferred_path.parent = self
                self.sequencing = PseudowireConfig.PwTemplates.PwTemplate.Sequencing()
                self.sequencing.parent = self
                self.signaling_protocol = None
                self.source_ip = None
                self.status = PseudowireConfig.PwTemplates.PwTemplate.Status()
                self.status.parent = self
                self.switching_tlv = None
                self.switchover_delay = PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay()
                self.switchover_delay.parent = self
                self.tag_rewrite_ingress_vlan = None
                self.vc_type = None
                self.vccv = PseudowireConfig.PwTemplates.PwTemplate.Vccv()
                self.vccv.parent = self


            class LoadBalance(object):
                """
                Load balancing mechanism.
                
                .. attribute:: ethernet
                
                	Ethernet mac address based load balancing
                	**type**\:   :py:class:`PwLbEthernetTypeIdentity <ydk.models.cisco_ios_xe.cisco_pw.PwLbEthernetTypeIdentity>`
                
                	**default value**\: pw-lb-eth-src-dst-mac
                
                .. attribute:: flow_label
                
                	Enable Flow Aware Label (FAT) PW \- the capability to carry flow label on PW
                	**type**\:   :py:class:`FlowLabel <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel>`
                
                .. attribute:: ip
                
                	IP address based load balancing
                	**type**\:   :py:class:`PwLbIpTypeIdentity <ydk.models.cisco_ios_xe.cisco_pw.PwLbIpTypeIdentity>`
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    self.parent = None
                    self.ethernet = None
                    self.flow_label = PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel()
                    self.flow_label.parent = self
                    self.ip = None


                class FlowLabel(object):
                    """
                    Enable Flow Aware Label (FAT) PW \- the capability to
                    carry flow label on PW
                    
                    .. attribute:: direction
                    
                    	Directions to enable Flow Aware Label PW
                    	**type**\:   :py:class:`DirectionEnum <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel.DirectionEnum>`
                    
                    .. attribute:: static
                    
                    	Use statically configured flow label on traffic flowing on the PW
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: tlv_code_17
                    
                    	Carry code 0x17 as Flow Aware Label (FAT) PW signalled sub\-tlv id
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'l2vpn-pw'
                    _revision = '2016-12-07'

                    def __init__(self):
                        self.parent = None
                        self.direction = None
                        self.static = None
                        self.tlv_code_17 = None

                    class DirectionEnum(Enum):
                        """
                        DirectionEnum

                        Directions to enable Flow Aware Label PW

                        .. data:: transmit = 1

                        	TODO

                        .. data:: receive = 2

                        	TODO

                        .. data:: both = 3

                        	TODO

                        """

                        transmit = 1

                        receive = 2

                        both = 3


                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
                            return meta._meta_table['PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel.DirectionEnum']


                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/cisco-pw:flow-label'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.direction is not None:
                            return True

                        if self.static is not None:
                            return True

                        if self.tlv_code_17 is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
                        return meta._meta_table['PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-pw:load-balance'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ethernet is not None:
                        return True

                    if self.flow_label is not None and self.flow_label._has_data():
                        return True

                    if self.ip is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
                    return meta._meta_table['PseudowireConfig.PwTemplates.PwTemplate.LoadBalance']['meta_info']


            class PreferredPath(object):
                """
                Preferred path for the PW
                
                .. attribute:: address
                
                	TODO
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: disable_fallback
                
                	Disable fall back to alternative route
                	**type**\:  bool
                
                .. attribute:: hostname
                
                	TODO
                	**type**\:  str
                
                .. attribute:: interface
                
                	Reference to a tunnel interface
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.disable_fallback = None
                    self.hostname = None
                    self.interface = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-pw:preferred-path'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.address is not None:
                        return True

                    if self.disable_fallback is not None:
                        return True

                    if self.hostname is not None:
                        return True

                    if self.interface is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
                    return meta._meta_table['PseudowireConfig.PwTemplates.PwTemplate.PreferredPath']['meta_info']


            class Sequencing(object):
                """
                Sequencing options
                
                .. attribute:: direction
                
                	TODO
                	**type**\:   :py:class:`PwSequencingTypeIdentity <ydk.models.cisco_ios_xe.cisco_pw.PwSequencingTypeIdentity>`
                
                .. attribute:: resync
                
                	TODO
                	**type**\:  int
                
                	**range:** 5..65535
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    self.parent = None
                    self.direction = None
                    self.resync = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-pw:sequencing'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.direction is not None:
                        return True

                    if self.resync is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
                    return meta._meta_table['PseudowireConfig.PwTemplates.PwTemplate.Sequencing']['meta_info']


            class Vccv(object):
                """
                VCCV configuration
                
                .. attribute:: control_word
                
                	Enable VCCV verification type
                	**type**\:  bool
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    self.parent = None
                    self.control_word = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-pw:vccv'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.control_word is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
                    return meta._meta_table['PseudowireConfig.PwTemplates.PwTemplate.Vccv']['meta_info']


            class SwitchoverDelay(object):
                """
                Timer configuration related to pseudowire redundancy
                switchover and restoring to primary
                
                .. attribute:: never
                
                	The primary pseudowire never takes over for the backup
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: switchover_timer
                
                	Specifies how long the backup pseudowire should wait before taking over
                	**type**\:  int
                
                	**range:** 0..120
                
                .. attribute:: timer
                
                	Specifies how long the primary pseudowire should wait after it becomes active to take over for the backup pseudowire
                	**type**\:  int
                
                	**range:** 0..180
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    self.parent = None
                    self.never = None
                    self.switchover_timer = None
                    self.timer = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-pw:switchover-delay'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.never is not None:
                        return True

                    if self.switchover_timer is not None:
                        return True

                    if self.timer is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
                    return meta._meta_table['PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay']['meta_info']


            class Status(object):
                """
                TODO
                
                .. attribute:: decoupled
                
                	Reflect standby status of the attachment circuit as up on the pseudowire
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: disable
                
                	Do not send pseudowire status to peer
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: peer_topo_dual_homed
                
                	Our peer(s) are participating in a redundant solution with some form of redundancy protocol running between the peer routers. Only one of the remote peers will advertise a status of UP at a time. The other will advertise standby. Change our configuration so we can send a status of UP on both active and redundant pseudowires
                	**type**\:  bool
                
                .. attribute:: redundancy_master
                
                	Make the PE as master to enables Pseudowire Preferential Forwarding feature to display the status of  the active and backup pseudowires
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: route_watch_disable
                
                	Disable listening for routing events to trigger redundancy status changes
                	**type**\:  bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    self.parent = None
                    self.decoupled = None
                    self.disable = None
                    self.peer_topo_dual_homed = None
                    self.redundancy_master = None
                    self.route_watch_disable = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-pw:status'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.decoupled is not None:
                        return True

                    if self.disable is not None:
                        return True

                    if self.peer_topo_dual_homed is not None:
                        return True

                    if self.redundancy_master is not None:
                        return True

                    if self.route_watch_disable is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
                    return meta._meta_table['PseudowireConfig.PwTemplates.PwTemplate.Status']['meta_info']


            class PortProfileSpec(object):
                """
                Pseudowire port profile configurations.
                
                .. attribute:: description
                
                	Description string for the port profile
                	**type**\:  str
                
                .. attribute:: enabled
                
                	Enable this port profile
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: max_ports
                
                	Maximum number of ports
                	**type**\:  int
                
                	**range:** 1..16384
                
                .. attribute:: mtu
                
                	MTU of the port
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: shut_force
                
                	Force shut down this port profile
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: shutdown
                
                	Shut down this template
                	**type**\:  bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    self.parent = None
                    self.description = None
                    self.enabled = None
                    self.max_ports = None
                    self.mtu = None
                    self.shut_force = None
                    self.shutdown = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-pw:port-profile-spec'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.description is not None:
                        return True

                    if self.enabled is not None:
                        return True

                    if self.max_ports is not None:
                        return True

                    if self.mtu is not None:
                        return True

                    if self.shut_force is not None:
                        return True

                    if self.shutdown is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
                    return meta._meta_table['PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/cisco-pw:pseudowire-config/cisco-pw:pw-templates/cisco-pw:pw-template[cisco-pw:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.control_word is not None:
                    return True

                if self.encapsulation is not None:
                    return True

                if self.load_balance is not None and self.load_balance._has_data():
                    return True

                if self.mac_withdraw is not None:
                    return True

                if self.port_profile_spec is not None and self.port_profile_spec._has_data():
                    return True

                if self.preferred_path is not None and self.preferred_path._has_data():
                    return True

                if self.sequencing is not None and self.sequencing._has_data():
                    return True

                if self.signaling_protocol is not None:
                    return True

                if self.source_ip is not None:
                    return True

                if self.status is not None and self.status._has_data():
                    return True

                if self.switching_tlv is not None:
                    return True

                if self.switchover_delay is not None and self.switchover_delay._has_data():
                    return True

                if self.tag_rewrite_ingress_vlan is not None:
                    return True

                if self.vc_type is not None:
                    return True

                if self.vccv is not None and self.vccv._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
                return meta._meta_table['PseudowireConfig.PwTemplates.PwTemplate']['meta_info']

        @property
        def _common_path(self):

            return '/cisco-pw:pseudowire-config/cisco-pw:pw-templates'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.pw_template is not None:
                for child_ref in self.pw_template:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
            return meta._meta_table['PseudowireConfig.PwTemplates']['meta_info']


    class PwStaticOamClasses(object):
        """
        List of pseudowire static oam classes.
        
        .. attribute:: pw_static_oam_class
        
        	Pseudowire static oam class configuration
        	**type**\: list of    :py:class:`PwStaticOamClass <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwStaticOamClasses.PwStaticOamClass>`
        
        

        """

        _prefix = 'l2vpn-pw'
        _revision = '2016-12-07'

        def __init__(self):
            self.parent = None
            self.pw_static_oam_class = YList()
            self.pw_static_oam_class.parent = self
            self.pw_static_oam_class.name = 'pw_static_oam_class'


        class PwStaticOamClass(object):
            """
            Pseudowire static oam class configuration
            
            .. attribute:: name  <key>
            
            	OAM class name
            	**type**\:  str
            
            .. attribute:: ack
            
            	Enable ack
            	**type**\:  bool
            
            .. attribute:: keepalive
            
            	Keepalive in seconds
            	**type**\:  int
            
            	**range:** 1..4095
            
            	**default value**\: 600
            
            .. attribute:: timeout_refresh_ack
            
            	Ack timeout in seconds
            	**type**\:  int
            
            	**range:** 1..4095
            
            	**default value**\: 600
            
            .. attribute:: timeout_refresh_send
            
            	Refresh timeout in seconds
            	**type**\:  int
            
            	**range:** 1..4095
            
            	**default value**\: 30
            
            

            """

            _prefix = 'l2vpn-pw'
            _revision = '2016-12-07'

            def __init__(self):
                self.parent = None
                self.name = None
                self.ack = None
                self.keepalive = None
                self.timeout_refresh_ack = None
                self.timeout_refresh_send = None

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/cisco-pw:pseudowire-config/cisco-pw:pw-static-oam-classes/cisco-pw:pw-static-oam-class[cisco-pw:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.ack is not None:
                    return True

                if self.keepalive is not None:
                    return True

                if self.timeout_refresh_ack is not None:
                    return True

                if self.timeout_refresh_send is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
                return meta._meta_table['PseudowireConfig.PwStaticOamClasses.PwStaticOamClass']['meta_info']

        @property
        def _common_path(self):

            return '/cisco-pw:pseudowire-config/cisco-pw:pw-static-oam-classes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.pw_static_oam_class is not None:
                for child_ref in self.pw_static_oam_class:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
            return meta._meta_table['PseudowireConfig.PwStaticOamClasses']['meta_info']

    @property
    def _common_path(self):

        return '/cisco-pw:pseudowire-config'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.global_ is not None and self.global_._has_data():
            return True

        if self.pw_static_oam_classes is not None and self.pw_static_oam_classes._has_data():
            return True

        if self.pw_templates is not None and self.pw_templates._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PseudowireConfig']['meta_info']


class PseudowireState(object):
    """
    Contains the operational state for all the pseudowire
    instances in the switch, no matter what L2VPN service
    created them.
    
    .. attribute:: pseudowires
    
    	Each list element contains the state for a pseudowire instance. The list can be optionally keyed by any combination of vc\-id, peer\-address, etc. Additional filtering of the list by the agent may be performed upon request by the client using subtree filtering as described in RFC 6020 Section 6
    	**type**\: list of    :py:class:`Pseudowires <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires>`
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        self.pseudowires = YList()
        self.pseudowires.parent = self
        self.pseudowires.name = 'pseudowires'


    class Pseudowires(object):
        """
        Each list element contains the state for a pseudowire
        instance. The list can be optionally keyed by any
        combination of vc\-id, peer\-address, etc.
        Additional filtering of the list by the agent may be
        performed upon request by the client using subtree
        filtering as described in RFC 6020 Section 6.
        
        .. attribute:: vc_peer_address  <key>
        
        	This object contains the value of the peer node address of the PW/PE protocol entity
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: vc_id  <key>
        
        	Used to distinguish between pseudowires going to the same peer node
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_owner_type  <key>
        
        	Indicates the service responsible for establishing this VC
        	**type**\:   :py:class:`VcOwnerTypeEnum <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires.VcOwnerTypeEnum>`
        
        .. attribute:: vc_name  <key>
        
        	The canonical name assigned to the VC. The name may be autogenerated by the device; this Yang model does not currently support direct configuration of this name
        	**type**\:  str
        
        .. attribute:: vc_index  <key>
        
        	Locally\-unique ID within the device for this pseudowire
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: statistics
        
        	A collection of pseudowire\-related statistics objects
        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires.Statistics>`
        
        .. attribute:: vc_control_word
        
        	Indicates if the control word is sent with each packet by the local node
        	**type**\:  bool
        
        .. attribute:: vc_inbound_label
        
        	The VC label used in the inbound direction (i.e. packets received from the PSN). Example\: for MPLS PSN, it represents the 20 bits of VC tag, for L2TP it represents the 32 bits Session ID. If the label is not yet known (signaling in process), the object should return a value of 0xFFFFFFFF
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_inbound_oper_status
        
        	Indicates the actual operational status of this VC in the  inbound direction
        	**type**\:   :py:class:`PwOperStateTypeEnum <ydk.models.cisco_ios_xe.cisco_pw.PwOperStateTypeEnum>`
        
        .. attribute:: vc_local_group_id
        
        	Used to identify which local pseudowire group this pseudowire belongs to
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_local_if_mtu
        
        	If not zero, this represents the locally supported MTU size over the interface (or the virtual interface) associated with the VC
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_oper_status
        
        	Indicates the actual combined operational status of this VC. It is 'up' if both vc\-inbound\-oper\-status and vc\-outbound\-oper\-status are in 'up' state. For all other values, if the VCs in both directions are of the same value it reflects that value, otherwise it is set to the most severe status out of the two statuses. The order of severance from most severe to less severe is\: unknown, notPresent, down, lowerLayerDown, dormant, testing, up. The operator may consult the per direction oper\-status for fault isolation per direction
        	**type**\:   :py:class:`PwOperStateTypeEnum <ydk.models.cisco_ios_xe.cisco_pw.PwOperStateTypeEnum>`
        
        .. attribute:: vc_outbound_label
        
        	The VC label used in the outbound direction (i.e. toward the PSN). Example\: for MPLS PSN, it represents the 20 bits of VC tag, for L2TP it represent the 32 bits Session ID. If the label is not yet known (signaling in procesS), the object should return a value of 0xFFFFFFFF
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_outbound_oper_status
        
        	Indicates the actual operational status of this VC in the outbound direction
        	**type**\:   :py:class:`PwOperStateTypeEnum <ydk.models.cisco_ios_xe.cisco_pw.PwOperStateTypeEnum>`
        
        .. attribute:: vc_owner_name
        
        	Name of the L2VPN service instance that created the pseudowire VC
        	**type**\:  str
        
        .. attribute:: vc_psn_type
        
        	Indicates the type of packet\-switched network that carries this VC
        	**type**\:   :py:class:`VcPsnTypeEnum <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires.VcPsnTypeEnum>`
        
        .. attribute:: vc_remote_control_word
        
        	Indicates whether MPLS control words are used by the pseudowire PSN service
        	**type**\:   :py:class:`VcRemoteControlWordEnum <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires.VcRemoteControlWordEnum>`
        
        .. attribute:: vc_remote_group_id
        
        	If not zero, indicates the pseudowire group to which this pseudowire belongs on the peer node
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_remote_if_mtu
        
        	The remote interface MTU as (optionally) received from the remote node via the signaling protocol. Should be zero if this parameter is not available or not used
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_type
        
        	Indicates the service to be carried over this VC
        	**type**\:   :py:class:`PwVcTypeIdentity <ydk.models.cisco_ios_xe.cisco_pw.PwVcTypeIdentity>`
        
        

        """

        _prefix = 'l2vpn-pw'
        _revision = '2016-12-07'

        def __init__(self):
            self.parent = None
            self.vc_peer_address = None
            self.vc_id = None
            self.vc_owner_type = None
            self.vc_name = None
            self.vc_index = None
            self.statistics = PseudowireState.Pseudowires.Statistics()
            self.statistics.parent = self
            self.vc_control_word = None
            self.vc_inbound_label = None
            self.vc_inbound_oper_status = None
            self.vc_local_group_id = None
            self.vc_local_if_mtu = None
            self.vc_oper_status = None
            self.vc_outbound_label = None
            self.vc_outbound_oper_status = None
            self.vc_owner_name = None
            self.vc_psn_type = None
            self.vc_remote_control_word = None
            self.vc_remote_group_id = None
            self.vc_remote_if_mtu = None
            self.vc_type = None

        class VcOwnerTypeEnum(Enum):
            """
            VcOwnerTypeEnum

            Indicates the service responsible for establishing

            this VC

            .. data:: vpws = 1

            	Created under VPWS context

            .. data:: vpls_vfi = 2

            	Created under VFI context

            .. data:: vpls_bridge_domain = 3

            	Created under bridge domain context

            .. data:: interface = 4

            	Created by manual pseudowire interface

            	configuration

            """

            vpws = 1

            vpls_vfi = 2

            vpls_bridge_domain = 3

            interface = 4


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
                return meta._meta_table['PseudowireState.Pseudowires.VcOwnerTypeEnum']


        class VcPsnTypeEnum(Enum):
            """
            VcPsnTypeEnum

            Indicates the type of packet\-switched network

            that carries this VC

            .. data:: mpls = 1

            	MPLS encapsulation

            .. data:: l2tp = 2

            	L2TP encapsulation

            .. data:: ip = 3

            	IP core

            .. data:: mpls_over_ip = 4

            	MPLS encapsulation over IP core

            .. data:: gre = 5

            	GRE encapsulation

            .. data:: other = 6

            	Some other encapsulation

            """

            mpls = 1

            l2tp = 2

            ip = 3

            mpls_over_ip = 4

            gre = 5

            other = 6


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
                return meta._meta_table['PseudowireState.Pseudowires.VcPsnTypeEnum']


        class VcRemoteControlWordEnum(Enum):
            """
            VcRemoteControlWordEnum

            Indicates whether MPLS control words are used by the

            pseudowire PSN service

            .. data:: noControlWord = 1

            	Peer sends control word

            .. data:: withControlWord = 2

            	Peer does not send control word

            .. data:: notYetKnown = 3

            	Have not received indication yet if peer sends

            	control word

            """

            noControlWord = 1

            withControlWord = 2

            notYetKnown = 3


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
                return meta._meta_table['PseudowireState.Pseudowires.VcRemoteControlWordEnum']



        class Statistics(object):
            """
            A collection of pseudowire\-related statistics objects
            
            .. attribute:: discontinuity_time
            
            	The time on the most recent occasion at which any of this pseudowire's counters sufferred discontinuity. If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this node contains the time the local management subsystem re\-initialized itself
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            	**mandatory**\: True
            
            .. attribute:: in_errors
            
            	The total number of inbound packets that contained errors.  Discontinuities in the value of this counter can occur at re\-initialization of the management system and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_octets
            
            	The total number of octets received on this pseudowire.  Discontinuities in the value of this counter can occur at re\-initialization of the management system and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_pkts
            
            	The total number of packets received on this pseudowire.  Discontinuities in the value of this counter can occur at re\-initialization of the management system and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_errors
            
            	The total number of outbound packets that could not be sent on this pseudowire.  Discontinuities in the value of this counter can occur at re\-initialization of the management system and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_octets
            
            	The total number of octets sent on this pseudowire.  Discontinuities in the value of this counter can occur at re\-initialization of the management system and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_pkts
            
            	The total number of packets sent on this pseudowire.  Discontinuities in the value of this counter can occur at re\-initialization of the management system and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: vc_create_time
            
            	System time when this VC was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vc_up_time
            
            	Number of consecutive ticks this VC has been 'up' in both directions together
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'l2vpn-pw'
            _revision = '2016-12-07'

            def __init__(self):
                self.parent = None
                self.discontinuity_time = None
                self.in_errors = None
                self.in_octets = None
                self.in_pkts = None
                self.out_errors = None
                self.out_octets = None
                self.out_pkts = None
                self.vc_create_time = None
                self.vc_up_time = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/cisco-pw:statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.discontinuity_time is not None:
                    return True

                if self.in_errors is not None:
                    return True

                if self.in_octets is not None:
                    return True

                if self.in_pkts is not None:
                    return True

                if self.out_errors is not None:
                    return True

                if self.out_octets is not None:
                    return True

                if self.out_pkts is not None:
                    return True

                if self.vc_create_time is not None:
                    return True

                if self.vc_up_time is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
                return meta._meta_table['PseudowireState.Pseudowires.Statistics']['meta_info']

        @property
        def _common_path(self):
            if self.vc_peer_address is None:
                raise YPYModelError('Key property vc_peer_address is None')
            if self.vc_id is None:
                raise YPYModelError('Key property vc_id is None')
            if self.vc_owner_type is None:
                raise YPYModelError('Key property vc_owner_type is None')
            if self.vc_name is None:
                raise YPYModelError('Key property vc_name is None')
            if self.vc_index is None:
                raise YPYModelError('Key property vc_index is None')

            return '/cisco-pw:pseudowire-state/cisco-pw:pseudowires[cisco-pw:vc-peer-address = ' + str(self.vc_peer_address) + '][cisco-pw:vc-id = ' + str(self.vc_id) + '][cisco-pw:vc-owner-type = ' + str(self.vc_owner_type) + '][cisco-pw:vc-name = ' + str(self.vc_name) + '][cisco-pw:vc-index = ' + str(self.vc_index) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vc_peer_address is not None:
                return True

            if self.vc_id is not None:
                return True

            if self.vc_owner_type is not None:
                return True

            if self.vc_name is not None:
                return True

            if self.vc_index is not None:
                return True

            if self.statistics is not None and self.statistics._has_data():
                return True

            if self.vc_control_word is not None:
                return True

            if self.vc_inbound_label is not None:
                return True

            if self.vc_inbound_oper_status is not None:
                return True

            if self.vc_local_group_id is not None:
                return True

            if self.vc_local_if_mtu is not None:
                return True

            if self.vc_oper_status is not None:
                return True

            if self.vc_outbound_label is not None:
                return True

            if self.vc_outbound_oper_status is not None:
                return True

            if self.vc_owner_name is not None:
                return True

            if self.vc_psn_type is not None:
                return True

            if self.vc_remote_control_word is not None:
                return True

            if self.vc_remote_group_id is not None:
                return True

            if self.vc_remote_if_mtu is not None:
                return True

            if self.vc_type is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
            return meta._meta_table['PseudowireState.Pseudowires']['meta_info']

    @property
    def _common_path(self):

        return '/cisco-pw:pseudowire-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.pseudowires is not None:
            for child_ref in self.pseudowires:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PseudowireState']['meta_info']


class PwSequencingTransmitIdentity(PwSequencingTypeIdentity):
    """
    Transmit sequencing option for PW
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwSequencingTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwSequencingTransmitIdentity']['meta_info']


class PwSignalingProtocolNoneIdentity(PwSignalingProtocolTypeIdentity):
    """
    No PW signaling protocol
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwSignalingProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwSignalingProtocolNoneIdentity']['meta_info']


class PwVcTypeVlanPassthroughIdentity(PwVcTypeIdentity):
    """
    Identity for VLAN passthrough VC type (XR)
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwVcTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwVcTypeVlanPassthroughIdentity']['meta_info']


class PwVcTypeVlanIdentity(PwVcTypeIdentity):
    """
    Identity for VLAN VC type
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwVcTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwVcTypeVlanIdentity']['meta_info']


class PwSequencingReceiveIdentity(PwSequencingTypeIdentity):
    """
    Receive sequencing option for PW
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwSequencingTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwSequencingReceiveIdentity']['meta_info']


class PwSignalingProtocolLdpIdentity(PwSignalingProtocolTypeIdentity):
    """
    Use MPLS LDP for PW signaling protocol
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwSignalingProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwSignalingProtocolLdpIdentity']['meta_info']


class PwLbEthernetTypeIdentity(PwLoadBalanceTypeIdentity):
    """
    Base type for load\-balancing with ethernet fields
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwLoadBalanceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwLbEthernetTypeIdentity']['meta_info']


class PwSequencingBothIdentity(PwSequencingTypeIdentity):
    """
    Receive and Transmit sequencing option for PW
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwSequencingTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwSequencingBothIdentity']['meta_info']


class PwVcTypeEtherIdentity(PwVcTypeIdentity):
    """
    Identity for Ethernet VC type
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwVcTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwVcTypeEtherIdentity']['meta_info']


class PwLbIpTypeIdentity(PwLoadBalanceTypeIdentity):
    """
    Base type for load\-balancing with IP
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwLoadBalanceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwLbIpTypeIdentity']['meta_info']


class PwLbIpDstIpIdentity(PwLoadBalanceTypeIdentity):
    """
    Load\-balancing with IP destination IP field
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwLoadBalanceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwLbIpDstIpIdentity']['meta_info']


class PwEncapMplsIdentity(PwEncapsulationTypeIdentity):
    """
    Use MPLS for PW encapsulation
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwEncapsulationTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwEncapMplsIdentity']['meta_info']


class PwSignalingProtocolBgpIdentity(PwSignalingProtocolTypeIdentity):
    """
    Use BGP for PW signaling protocol
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwSignalingProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwSignalingProtocolBgpIdentity']['meta_info']


class PwLbIpSrcDstIpIdentity(PwLbIpTypeIdentity):
    """
    Load\-balancing with IP source and destination IP fields
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwLbIpTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwLbIpSrcDstIpIdentity']['meta_info']


class PwLbEthSrcDstMacIdentity(PwLbEthernetTypeIdentity):
    """
    Load\-balancing with ethernet source and destination MAC
    fields
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwLbEthernetTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwLbEthSrcDstMacIdentity']['meta_info']


class PwLbEthSrcMacIdentity(PwLbEthernetTypeIdentity):
    """
    Load\-balancing with ethernet source MAC field
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwLbEthernetTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwLbEthSrcMacIdentity']['meta_info']


class PwLbEthDstMacIdentity(PwLbEthernetTypeIdentity):
    """
    Load\-balancing with ethernet destination MAC field
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwLbEthernetTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwLbEthDstMacIdentity']['meta_info']


class PwLbIpSrcIpIdentity(PwLbIpTypeIdentity):
    """
    Load\-balancing with IP source IP field
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        PwLbIpTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_pw as meta
        return meta._meta_table['PwLbIpSrcIpIdentity']['meta_info']



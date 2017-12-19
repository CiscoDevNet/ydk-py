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
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class PwOperStateType(Enum):
    """
    PwOperStateType

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

    up = Enum.YLeaf(1, "up")

    down = Enum.YLeaf(2, "down")

    cold_standby = Enum.YLeaf(3, "cold-standby")

    hot_standby = Enum.YLeaf(4, "hot-standby")

    recovering = Enum.YLeaf(5, "recovering")

    no_hardware = Enum.YLeaf(6, "no-hardware")

    unresolved = Enum.YLeaf(7, "unresolved")

    provisioned = Enum.YLeaf(8, "provisioned")

    remote_standby = Enum.YLeaf(9, "remote-standby")

    local_ready = Enum.YLeaf(10, "local-ready")

    all_ready = Enum.YLeaf(11, "all-ready")



class PwEncapsulationType(Identity):
    """
    Base identity for PW encapsulations.
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwEncapsulationType, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-encapsulation-type")


class PwVcType(Identity):
    """
    Base identity for VC type in PW
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwVcType, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-vc-type")


class PwLoadBalanceType(Identity):
    """
    Base type for load\-balancing type
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLoadBalanceType, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-load-balance-type")


class PwSignalingProtocolType(Identity):
    """
    Base identity for PW signaling protocol
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwSignalingProtocolType, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-signaling-protocol-type")


class PwSequencingType(Identity):
    """
    Sequencing options for PW
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwSequencingType, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-sequencing-type")


class PseudowireConfig(Entity):
    """
    Pseudowire configuration data.
    
    .. attribute:: global_
    
    	Global configurations related to pseudowires
    	**type**\:  :py:class:`Global_ <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.Global_>`
    
    .. attribute:: pw_templates
    
    	Contains list of all pw\-template definitions. Also called PW Class (XR) and Port Profile (NX\-OS)
    	**type**\:  :py:class:`PwTemplates <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates>`
    
    .. attribute:: pw_static_oam_classes
    
    	List of pseudowire static oam classes
    	**type**\:  :py:class:`PwStaticOamClasses <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwStaticOamClasses>`
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PseudowireConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "pseudowire-config"
        self.yang_parent_name = "cisco-pw"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"global" : ("global_", PseudowireConfig.Global_), "pw-templates" : ("pw_templates", PseudowireConfig.PwTemplates), "pw-static-oam-classes" : ("pw_static_oam_classes", PseudowireConfig.PwStaticOamClasses)}
        self._child_list_classes = {}

        self.global_ = PseudowireConfig.Global_()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._children_yang_names.add("global")

        self.pw_templates = PseudowireConfig.PwTemplates()
        self.pw_templates.parent = self
        self._children_name_map["pw_templates"] = "pw-templates"
        self._children_yang_names.add("pw-templates")

        self.pw_static_oam_classes = PseudowireConfig.PwStaticOamClasses()
        self.pw_static_oam_classes.parent = self
        self._children_name_map["pw_static_oam_classes"] = "pw-static-oam-classes"
        self._children_yang_names.add("pw-static-oam-classes")
        self._segment_path = lambda: "cisco-pw:pseudowire-config"


    class Global_(Entity):
        """
        Global configurations related to pseudowires.
        
        .. attribute:: pw_grouping
        
        	Enable pw\-grouping.  When pseudowires (PW) are established, each PW is assigned a group ID that is common for all PWs created from the same physical port. Hence, when the physical port becomes non\-functional or is deleted, L2VPN sends a single message to advertise the status change of all PWs belonging to the group. A single L2VPN signal thus avoids a lot of processing and loss in reactivity
        	**type**\: bool
        
        	**default value**\: false
        
        .. attribute:: pw_oam_refresh_transmit
        
        	Set pseudowire oam transmit refresh time (in seconds)
        	**type**\: int
        
        	**range:** 1..4095
        
        .. attribute:: pw_status
        
        	Enable pw\-status
        	**type**\: bool
        
        .. attribute:: predictive_redundancy
        
        	Enable predictive redundancy
        	**type**\: bool
        
        .. attribute:: vc_state_notification_enabled
        
        	If this leaf is set to true, then it enables the emission of 'vc\-state\-notification'; otherwise these notifications are not emitted
        	**type**\: bool
        
        .. attribute:: vc_state_notification_batch_size
        
        	'vc\-state\-notification' allows batching of pseudowires in order to reduce number of notifications generated from the device. All pseudowires in a batched notification MUST share same state at the same time.  This leaf defines the maximum number of VCs that can be batched in vc\-state\-notification
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_state_notification_rate
        
        	This leaf defines the maximum number of VC state change notifications that can be emitted from the device per second
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'l2vpn-pw'
        _revision = '2016-12-07'

        def __init__(self):
            super(PseudowireConfig.Global_, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "pseudowire-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.pw_grouping = YLeaf(YType.boolean, "pw-grouping")

            self.pw_oam_refresh_transmit = YLeaf(YType.uint32, "pw-oam-refresh-transmit")

            self.pw_status = YLeaf(YType.boolean, "pw-status")

            self.predictive_redundancy = YLeaf(YType.boolean, "predictive-redundancy")

            self.vc_state_notification_enabled = YLeaf(YType.boolean, "vc-state-notification-enabled")

            self.vc_state_notification_batch_size = YLeaf(YType.uint32, "vc-state-notification-batch-size")

            self.vc_state_notification_rate = YLeaf(YType.uint32, "vc-state-notification-rate")
            self._segment_path = lambda: "global"
            self._absolute_path = lambda: "cisco-pw:pseudowire-config/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PseudowireConfig.Global_, ['pw_grouping', 'pw_oam_refresh_transmit', 'pw_status', 'predictive_redundancy', 'vc_state_notification_enabled', 'vc_state_notification_batch_size', 'vc_state_notification_rate'], name, value)


    class PwTemplates(Entity):
        """
        Contains list of all pw\-template definitions.
        Also called PW Class (XR) and Port Profile (NX\-OS)
        
        .. attribute:: pw_template
        
        	Pseudowire template list
        	**type**\: list of  		 :py:class:`PwTemplate <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate>`
        
        

        """

        _prefix = 'l2vpn-pw'
        _revision = '2016-12-07'

        def __init__(self):
            super(PseudowireConfig.PwTemplates, self).__init__()

            self.yang_name = "pw-templates"
            self.yang_parent_name = "pseudowire-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"pw-template" : ("pw_template", PseudowireConfig.PwTemplates.PwTemplate)}

            self.pw_template = YList(self)
            self._segment_path = lambda: "pw-templates"
            self._absolute_path = lambda: "cisco-pw:pseudowire-config/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PseudowireConfig.PwTemplates, [], name, value)


        class PwTemplate(Entity):
            """
            Pseudowire template list.
            
            .. attribute:: name  <key>
            
            	PW Template name
            	**type**\: str
            
            .. attribute:: encapsulation
            
            	Encapsulation used for PW
            	**type**\:  :py:class:`PwEncapsulationType <ydk.models.cisco_ios_xe.cisco_pw.PwEncapsulationType>`
            
            .. attribute:: control_word
            
            	Use control word in the MPLS PW header
            	**type**\: bool
            
            .. attribute:: signaling_protocol
            
            	Signaling protocol to use
            	**type**\:  :py:class:`PwSignalingProtocolType <ydk.models.cisco_ios_xe.cisco_pw.PwSignalingProtocolType>`
            
            .. attribute:: load_balance
            
            	Load balancing mechanism
            	**type**\:  :py:class:`LoadBalance <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.LoadBalance>`
            
            .. attribute:: preferred_path
            
            	Preferred path for the PW
            	**type**\:  :py:class:`PreferredPath <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.PreferredPath>`
            
            .. attribute:: sequencing
            
            	Sequencing options
            	**type**\:  :py:class:`Sequencing <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.Sequencing>`
            
            .. attribute:: vc_type
            
            	Type of VC in the PW
            	**type**\:  :py:class:`PwVcType <ydk.models.cisco_ios_xe.cisco_pw.PwVcType>`
            
            .. attribute:: switching_tlv
            
            	Send switching TLV
            	**type**\: bool
            
            .. attribute:: vccv
            
            	VCCV configuration
            	**type**\:  :py:class:`Vccv <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.Vccv>`
            
            .. attribute:: switchover_delay
            
            	Timer configuration related to pseudowire redundancy switchover and restoring to primary
            	**type**\:  :py:class:`SwitchoverDelay <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay>`
            
            .. attribute:: source_ip
            
            	The local source IPv4 address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tag_rewrite_ingress_vlan
            
            	Configure ingress tag rewrite vlan
            	**type**\: int
            
            	**range:** 1..4094
            
            .. attribute:: mac_withdraw
            
            	Send Mac\-withdraw message when PW becomes active
            	**type**\: bool
            
            	**default value**\: false
            
            .. attribute:: status
            
            	TODO
            	**type**\:  :py:class:`Status <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.Status>`
            
            .. attribute:: port_profile_spec
            
            	Pseudowire port profile configurations
            	**type**\:  :py:class:`PortProfileSpec <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec>`
            
            

            """

            _prefix = 'l2vpn-pw'
            _revision = '2016-12-07'

            def __init__(self):
                super(PseudowireConfig.PwTemplates.PwTemplate, self).__init__()

                self.yang_name = "pw-template"
                self.yang_parent_name = "pw-templates"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"load-balance" : ("load_balance", PseudowireConfig.PwTemplates.PwTemplate.LoadBalance), "preferred-path" : ("preferred_path", PseudowireConfig.PwTemplates.PwTemplate.PreferredPath), "sequencing" : ("sequencing", PseudowireConfig.PwTemplates.PwTemplate.Sequencing), "vccv" : ("vccv", PseudowireConfig.PwTemplates.PwTemplate.Vccv), "switchover-delay" : ("switchover_delay", PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay), "status" : ("status", PseudowireConfig.PwTemplates.PwTemplate.Status), "port-profile-spec" : ("port_profile_spec", PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec)}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.encapsulation = YLeaf(YType.identityref, "encapsulation")

                self.control_word = YLeaf(YType.boolean, "control-word")

                self.signaling_protocol = YLeaf(YType.identityref, "signaling-protocol")

                self.vc_type = YLeaf(YType.identityref, "vc-type")

                self.switching_tlv = YLeaf(YType.boolean, "switching-tlv")

                self.source_ip = YLeaf(YType.str, "source-ip")

                self.tag_rewrite_ingress_vlan = YLeaf(YType.uint16, "tag-rewrite-ingress-vlan")

                self.mac_withdraw = YLeaf(YType.boolean, "mac-withdraw")

                self.load_balance = PseudowireConfig.PwTemplates.PwTemplate.LoadBalance()
                self.load_balance.parent = self
                self._children_name_map["load_balance"] = "load-balance"
                self._children_yang_names.add("load-balance")

                self.preferred_path = PseudowireConfig.PwTemplates.PwTemplate.PreferredPath()
                self.preferred_path.parent = self
                self._children_name_map["preferred_path"] = "preferred-path"
                self._children_yang_names.add("preferred-path")

                self.sequencing = PseudowireConfig.PwTemplates.PwTemplate.Sequencing()
                self.sequencing.parent = self
                self._children_name_map["sequencing"] = "sequencing"
                self._children_yang_names.add("sequencing")

                self.vccv = PseudowireConfig.PwTemplates.PwTemplate.Vccv()
                self.vccv.parent = self
                self._children_name_map["vccv"] = "vccv"
                self._children_yang_names.add("vccv")

                self.switchover_delay = PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay()
                self.switchover_delay.parent = self
                self._children_name_map["switchover_delay"] = "switchover-delay"
                self._children_yang_names.add("switchover-delay")

                self.status = PseudowireConfig.PwTemplates.PwTemplate.Status()
                self.status.parent = self
                self._children_name_map["status"] = "status"
                self._children_yang_names.add("status")

                self.port_profile_spec = PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec()
                self.port_profile_spec.parent = self
                self._children_name_map["port_profile_spec"] = "port-profile-spec"
                self._children_yang_names.add("port-profile-spec")
                self._segment_path = lambda: "pw-template" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "cisco-pw:pseudowire-config/pw-templates/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PseudowireConfig.PwTemplates.PwTemplate, ['name', 'encapsulation', 'control_word', 'signaling_protocol', 'vc_type', 'switching_tlv', 'source_ip', 'tag_rewrite_ingress_vlan', 'mac_withdraw'], name, value)


            class LoadBalance(Entity):
                """
                Load balancing mechanism.
                
                .. attribute:: ethernet
                
                	Ethernet mac address based load balancing
                	**type**\:  :py:class:`PwLbEthernetType <ydk.models.cisco_ios_xe.cisco_pw.PwLbEthernetType>`
                
                	**default value**\: pw-lb-eth-src-dst-mac
                
                .. attribute:: ip
                
                	IP address based load balancing
                	**type**\:  :py:class:`PwLbIpType <ydk.models.cisco_ios_xe.cisco_pw.PwLbIpType>`
                
                .. attribute:: flow_label
                
                	Enable Flow Aware Label (FAT) PW \- the capability to carry flow label on PW
                	**type**\:  :py:class:`FlowLabel <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel>`
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    super(PseudowireConfig.PwTemplates.PwTemplate.LoadBalance, self).__init__()

                    self.yang_name = "load-balance"
                    self.yang_parent_name = "pw-template"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"flow-label" : ("flow_label", PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel)}
                    self._child_list_classes = {}

                    self.ethernet = YLeaf(YType.identityref, "ethernet")

                    self.ip = YLeaf(YType.identityref, "ip")

                    self.flow_label = PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel()
                    self.flow_label.parent = self
                    self._children_name_map["flow_label"] = "flow-label"
                    self._children_yang_names.add("flow-label")
                    self._segment_path = lambda: "load-balance"

                def __setattr__(self, name, value):
                    self._perform_setattr(PseudowireConfig.PwTemplates.PwTemplate.LoadBalance, ['ethernet', 'ip'], name, value)


                class FlowLabel(Entity):
                    """
                    Enable Flow Aware Label (FAT) PW \- the capability to
                    carry flow label on PW
                    
                    .. attribute:: direction
                    
                    	Directions to enable Flow Aware Label PW
                    	**type**\:  :py:class:`Direction <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel.Direction>`
                    
                    .. attribute:: tlv_code_17
                    
                    	Carry code 0x17 as Flow Aware Label (FAT) PW signalled sub\-tlv id
                    	**type**\: bool
                    
                    .. attribute:: static
                    
                    	Use statically configured flow label on traffic flowing on the PW
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'l2vpn-pw'
                    _revision = '2016-12-07'

                    def __init__(self):
                        super(PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel, self).__init__()

                        self.yang_name = "flow-label"
                        self.yang_parent_name = "load-balance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.direction = YLeaf(YType.enumeration, "direction")

                        self.tlv_code_17 = YLeaf(YType.boolean, "tlv-code-17")

                        self.static = YLeaf(YType.boolean, "static")
                        self._segment_path = lambda: "flow-label"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel, ['direction', 'tlv_code_17', 'static'], name, value)

                    class Direction(Enum):
                        """
                        Direction

                        Directions to enable Flow Aware Label PW

                        .. data:: transmit = 1

                        	TODO

                        .. data:: receive = 2

                        	TODO

                        .. data:: both = 3

                        	TODO

                        """

                        transmit = Enum.YLeaf(1, "transmit")

                        receive = Enum.YLeaf(2, "receive")

                        both = Enum.YLeaf(3, "both")



            class PreferredPath(Entity):
                """
                Preferred path for the PW
                
                .. attribute:: interface
                
                	Reference to a tunnel interface
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                .. attribute:: address
                
                	TODO
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: hostname
                
                	TODO
                	**type**\: str
                
                .. attribute:: disable_fallback
                
                	Disable fall back to alternative route
                	**type**\: bool
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    super(PseudowireConfig.PwTemplates.PwTemplate.PreferredPath, self).__init__()

                    self.yang_name = "preferred-path"
                    self.yang_parent_name = "pw-template"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface = YLeaf(YType.str, "interface")

                    self.address = YLeaf(YType.str, "address")

                    self.hostname = YLeaf(YType.str, "hostname")

                    self.disable_fallback = YLeaf(YType.boolean, "disable-fallback")
                    self._segment_path = lambda: "preferred-path"

                def __setattr__(self, name, value):
                    self._perform_setattr(PseudowireConfig.PwTemplates.PwTemplate.PreferredPath, ['interface', 'address', 'hostname', 'disable_fallback'], name, value)


            class Sequencing(Entity):
                """
                Sequencing options
                
                .. attribute:: direction
                
                	TODO
                	**type**\:  :py:class:`PwSequencingType <ydk.models.cisco_ios_xe.cisco_pw.PwSequencingType>`
                
                .. attribute:: resync
                
                	TODO
                	**type**\: int
                
                	**range:** 5..65535
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    super(PseudowireConfig.PwTemplates.PwTemplate.Sequencing, self).__init__()

                    self.yang_name = "sequencing"
                    self.yang_parent_name = "pw-template"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.direction = YLeaf(YType.identityref, "direction")

                    self.resync = YLeaf(YType.int32, "resync")
                    self._segment_path = lambda: "sequencing"

                def __setattr__(self, name, value):
                    self._perform_setattr(PseudowireConfig.PwTemplates.PwTemplate.Sequencing, ['direction', 'resync'], name, value)


            class Vccv(Entity):
                """
                VCCV configuration
                
                .. attribute:: control_word
                
                	Enable VCCV verification type
                	**type**\: bool
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    super(PseudowireConfig.PwTemplates.PwTemplate.Vccv, self).__init__()

                    self.yang_name = "vccv"
                    self.yang_parent_name = "pw-template"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.control_word = YLeaf(YType.boolean, "control-word")
                    self._segment_path = lambda: "vccv"

                def __setattr__(self, name, value):
                    self._perform_setattr(PseudowireConfig.PwTemplates.PwTemplate.Vccv, ['control_word'], name, value)


            class SwitchoverDelay(Entity):
                """
                Timer configuration related to pseudowire redundancy
                switchover and restoring to primary
                
                .. attribute:: switchover_timer
                
                	Specifies how long the backup pseudowire should wait before taking over
                	**type**\: int
                
                	**range:** 0..120
                
                .. attribute:: timer
                
                	Specifies how long the primary pseudowire should wait after it becomes active to take over for the backup pseudowire
                	**type**\: int
                
                	**range:** 0..180
                
                .. attribute:: never
                
                	The primary pseudowire never takes over for the backup
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    super(PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay, self).__init__()

                    self.yang_name = "switchover-delay"
                    self.yang_parent_name = "pw-template"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.switchover_timer = YLeaf(YType.uint8, "switchover-timer")

                    self.timer = YLeaf(YType.uint8, "timer")

                    self.never = YLeaf(YType.boolean, "never")
                    self._segment_path = lambda: "switchover-delay"

                def __setattr__(self, name, value):
                    self._perform_setattr(PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay, ['switchover_timer', 'timer', 'never'], name, value)


            class Status(Entity):
                """
                TODO
                
                .. attribute:: decoupled
                
                	Reflect standby status of the attachment circuit as up on the pseudowire
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: disable
                
                	Do not send pseudowire status to peer
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: peer_topo_dual_homed
                
                	Our peer(s) are participating in a redundant solution with some form of redundancy protocol running between the peer routers. Only one of the remote peers will advertise a status of UP at a time. The other will advertise standby. Change our configuration so we can send a status of UP on both active and redundant pseudowires
                	**type**\: bool
                
                .. attribute:: route_watch_disable
                
                	Disable listening for routing events to trigger redundancy status changes
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: redundancy_master
                
                	Make the PE as master to enables Pseudowire Preferential Forwarding feature to display the status of  the active and backup pseudowires
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    super(PseudowireConfig.PwTemplates.PwTemplate.Status, self).__init__()

                    self.yang_name = "status"
                    self.yang_parent_name = "pw-template"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.decoupled = YLeaf(YType.boolean, "decoupled")

                    self.disable = YLeaf(YType.boolean, "disable")

                    self.peer_topo_dual_homed = YLeaf(YType.boolean, "peer-topo-dual-homed")

                    self.route_watch_disable = YLeaf(YType.boolean, "route-watch-disable")

                    self.redundancy_master = YLeaf(YType.boolean, "redundancy-master")
                    self._segment_path = lambda: "status"

                def __setattr__(self, name, value):
                    self._perform_setattr(PseudowireConfig.PwTemplates.PwTemplate.Status, ['decoupled', 'disable', 'peer_topo_dual_homed', 'route_watch_disable', 'redundancy_master'], name, value)


            class PortProfileSpec(Entity):
                """
                Pseudowire port profile configurations.
                
                .. attribute:: description
                
                	Description string for the port profile
                	**type**\: str
                
                .. attribute:: shutdown
                
                	Shut down this template
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: shut_force
                
                	Force shut down this port profile
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: mtu
                
                	MTU of the port
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_ports
                
                	Maximum number of ports
                	**type**\: int
                
                	**range:** 1..16384
                
                .. attribute:: enabled
                
                	Enable this port profile
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    super(PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec, self).__init__()

                    self.yang_name = "port-profile-spec"
                    self.yang_parent_name = "pw-template"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.description = YLeaf(YType.str, "description")

                    self.shutdown = YLeaf(YType.boolean, "shutdown")

                    self.shut_force = YLeaf(YType.boolean, "shut-force")

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.max_ports = YLeaf(YType.uint16, "max-ports")

                    self.enabled = YLeaf(YType.boolean, "enabled")
                    self._segment_path = lambda: "port-profile-spec"

                def __setattr__(self, name, value):
                    self._perform_setattr(PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec, ['description', 'shutdown', 'shut_force', 'mtu', 'max_ports', 'enabled'], name, value)


    class PwStaticOamClasses(Entity):
        """
        List of pseudowire static oam classes.
        
        .. attribute:: pw_static_oam_class
        
        	Pseudowire static oam class configuration
        	**type**\: list of  		 :py:class:`PwStaticOamClass <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwStaticOamClasses.PwStaticOamClass>`
        
        

        """

        _prefix = 'l2vpn-pw'
        _revision = '2016-12-07'

        def __init__(self):
            super(PseudowireConfig.PwStaticOamClasses, self).__init__()

            self.yang_name = "pw-static-oam-classes"
            self.yang_parent_name = "pseudowire-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"pw-static-oam-class" : ("pw_static_oam_class", PseudowireConfig.PwStaticOamClasses.PwStaticOamClass)}

            self.pw_static_oam_class = YList(self)
            self._segment_path = lambda: "pw-static-oam-classes"
            self._absolute_path = lambda: "cisco-pw:pseudowire-config/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PseudowireConfig.PwStaticOamClasses, [], name, value)


        class PwStaticOamClass(Entity):
            """
            Pseudowire static oam class configuration
            
            .. attribute:: name  <key>
            
            	OAM class name
            	**type**\: str
            
            .. attribute:: ack
            
            	Enable ack
            	**type**\: bool
            
            .. attribute:: keepalive
            
            	Keepalive in seconds
            	**type**\: int
            
            	**range:** 1..4095
            
            	**default value**\: 600
            
            .. attribute:: timeout_refresh_send
            
            	Refresh timeout in seconds
            	**type**\: int
            
            	**range:** 1..4095
            
            	**default value**\: 30
            
            .. attribute:: timeout_refresh_ack
            
            	Ack timeout in seconds
            	**type**\: int
            
            	**range:** 1..4095
            
            	**default value**\: 600
            
            

            """

            _prefix = 'l2vpn-pw'
            _revision = '2016-12-07'

            def __init__(self):
                super(PseudowireConfig.PwStaticOamClasses.PwStaticOamClass, self).__init__()

                self.yang_name = "pw-static-oam-class"
                self.yang_parent_name = "pw-static-oam-classes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.ack = YLeaf(YType.boolean, "ack")

                self.keepalive = YLeaf(YType.uint32, "keepalive")

                self.timeout_refresh_send = YLeaf(YType.uint32, "timeout-refresh-send")

                self.timeout_refresh_ack = YLeaf(YType.uint32, "timeout-refresh-ack")
                self._segment_path = lambda: "pw-static-oam-class" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "cisco-pw:pseudowire-config/pw-static-oam-classes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PseudowireConfig.PwStaticOamClasses.PwStaticOamClass, ['name', 'ack', 'keepalive', 'timeout_refresh_send', 'timeout_refresh_ack'], name, value)

    def clone_ptr(self):
        self._top_entity = PseudowireConfig()
        return self._top_entity

class PseudowireState(Entity):
    """
    Contains the operational state for all the pseudowire
    instances in the switch, no matter what L2VPN service
    created them.
    
    .. attribute:: pseudowires
    
    	Each list element contains the state for a pseudowire instance. The list can be optionally keyed by any combination of vc\-id, peer\-address, etc. Additional filtering of the list by the agent may be performed upon request by the client using subtree filtering as described in RFC 6020 Section 6
    	**type**\: list of  		 :py:class:`Pseudowires <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires>`
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PseudowireState, self).__init__()
        self._top_entity = None

        self.yang_name = "pseudowire-state"
        self.yang_parent_name = "cisco-pw"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"pseudowires" : ("pseudowires", PseudowireState.Pseudowires)}

        self.pseudowires = YList(self)
        self._segment_path = lambda: "cisco-pw:pseudowire-state"

    def __setattr__(self, name, value):
        self._perform_setattr(PseudowireState, [], name, value)


    class Pseudowires(Entity):
        """
        Each list element contains the state for a pseudowire
        instance. The list can be optionally keyed by any
        combination of vc\-id, peer\-address, etc.
        Additional filtering of the list by the agent may be
        performed upon request by the client using subtree
        filtering as described in RFC 6020 Section 6.
        
        .. attribute:: vc_peer_address  <key>
        
        	This object contains the value of the peer node address of the PW/PE protocol entity
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: vc_id  <key>
        
        	Used to distinguish between pseudowires going to the same peer node
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_owner_type  <key>
        
        	Indicates the service responsible for establishing this VC
        	**type**\:  :py:class:`VcOwnerType <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires.VcOwnerType>`
        
        .. attribute:: vc_name  <key>
        
        	The canonical name assigned to the VC. The name may be autogenerated by the device; this Yang model does not currently support direct configuration of this name
        	**type**\: str
        
        .. attribute:: vc_index  <key>
        
        	Locally\-unique ID within the device for this pseudowire
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_type
        
        	Indicates the service to be carried over this VC
        	**type**\:  :py:class:`PwVcType <ydk.models.cisco_ios_xe.cisco_pw.PwVcType>`
        
        .. attribute:: vc_owner_name
        
        	Name of the L2VPN service instance that created the pseudowire VC
        	**type**\: str
        
        .. attribute:: vc_psn_type
        
        	Indicates the type of packet\-switched network that carries this VC
        	**type**\:  :py:class:`VcPsnType <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires.VcPsnType>`
        
        .. attribute:: vc_local_group_id
        
        	Used to identify which local pseudowire group this pseudowire belongs to
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_control_word
        
        	Indicates if the control word is sent with each packet by the local node
        	**type**\: bool
        
        .. attribute:: vc_local_if_mtu
        
        	If not zero, this represents the locally supported MTU size over the interface (or the virtual interface) associated with the VC
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_remote_group_id
        
        	If not zero, indicates the pseudowire group to which this pseudowire belongs on the peer node
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_remote_control_word
        
        	Indicates whether MPLS control words are used by the pseudowire PSN service
        	**type**\:  :py:class:`VcRemoteControlWord <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires.VcRemoteControlWord>`
        
        .. attribute:: vc_remote_if_mtu
        
        	The remote interface MTU as (optionally) received from the remote node via the signaling protocol. Should be zero if this parameter is not available or not used
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_outbound_label
        
        	The VC label used in the outbound direction (i.e. toward the PSN). Example\: for MPLS PSN, it represents the 20 bits of VC tag, for L2TP it represent the 32 bits Session ID. If the label is not yet known (signaling in procesS), the object should return a value of 0xFFFFFFFF
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_inbound_label
        
        	The VC label used in the inbound direction (i.e. packets received from the PSN). Example\: for MPLS PSN, it represents the 20 bits of VC tag, for L2TP it represents the 32 bits Session ID. If the label is not yet known (signaling in process), the object should return a value of 0xFFFFFFFF
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_oper_status
        
        	Indicates the actual combined operational status of this VC. It is 'up' if both vc\-inbound\-oper\-status and vc\-outbound\-oper\-status are in 'up' state. For all other values, if the VCs in both directions are of the same value it reflects that value, otherwise it is set to the most severe status out of the two statuses. The order of severance from most severe to less severe is\: unknown, notPresent, down, lowerLayerDown, dormant, testing, up. The operator may consult the per direction oper\-status for fault isolation per direction
        	**type**\:  :py:class:`PwOperStateType <ydk.models.cisco_ios_xe.cisco_pw.PwOperStateType>`
        
        .. attribute:: vc_inbound_oper_status
        
        	Indicates the actual operational status of this VC in the  inbound direction
        	**type**\:  :py:class:`PwOperStateType <ydk.models.cisco_ios_xe.cisco_pw.PwOperStateType>`
        
        .. attribute:: vc_outbound_oper_status
        
        	Indicates the actual operational status of this VC in the outbound direction
        	**type**\:  :py:class:`PwOperStateType <ydk.models.cisco_ios_xe.cisco_pw.PwOperStateType>`
        
        .. attribute:: statistics
        
        	A collection of pseudowire\-related statistics objects
        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires.Statistics>`
        
        

        """

        _prefix = 'l2vpn-pw'
        _revision = '2016-12-07'

        def __init__(self):
            super(PseudowireState.Pseudowires, self).__init__()

            self.yang_name = "pseudowires"
            self.yang_parent_name = "pseudowire-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"statistics" : ("statistics", PseudowireState.Pseudowires.Statistics)}
            self._child_list_classes = {}

            self.vc_peer_address = YLeaf(YType.str, "vc-peer-address")

            self.vc_id = YLeaf(YType.uint32, "vc-id")

            self.vc_owner_type = YLeaf(YType.enumeration, "vc-owner-type")

            self.vc_name = YLeaf(YType.str, "vc-name")

            self.vc_index = YLeaf(YType.uint32, "vc-index")

            self.vc_type = YLeaf(YType.identityref, "vc-type")

            self.vc_owner_name = YLeaf(YType.str, "vc-owner-name")

            self.vc_psn_type = YLeaf(YType.enumeration, "vc-psn-type")

            self.vc_local_group_id = YLeaf(YType.uint32, "vc-local-group-id")

            self.vc_control_word = YLeaf(YType.boolean, "vc-control-word")

            self.vc_local_if_mtu = YLeaf(YType.uint32, "vc-local-if-mtu")

            self.vc_remote_group_id = YLeaf(YType.uint32, "vc-remote-group-id")

            self.vc_remote_control_word = YLeaf(YType.enumeration, "vc-remote-control-word")

            self.vc_remote_if_mtu = YLeaf(YType.uint32, "vc-remote-if-mtu")

            self.vc_outbound_label = YLeaf(YType.uint32, "vc-outbound-label")

            self.vc_inbound_label = YLeaf(YType.uint32, "vc-inbound-label")

            self.vc_oper_status = YLeaf(YType.enumeration, "vc-oper-status")

            self.vc_inbound_oper_status = YLeaf(YType.enumeration, "vc-inbound-oper-status")

            self.vc_outbound_oper_status = YLeaf(YType.enumeration, "vc-outbound-oper-status")

            self.statistics = PseudowireState.Pseudowires.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"
            self._children_yang_names.add("statistics")
            self._segment_path = lambda: "pseudowires" + "[vc-peer-address='" + self.vc_peer_address.get() + "']" + "[vc-id='" + self.vc_id.get() + "']" + "[vc-owner-type='" + self.vc_owner_type.get() + "']" + "[vc-name='" + self.vc_name.get() + "']" + "[vc-index='" + self.vc_index.get() + "']"
            self._absolute_path = lambda: "cisco-pw:pseudowire-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PseudowireState.Pseudowires, ['vc_peer_address', 'vc_id', 'vc_owner_type', 'vc_name', 'vc_index', 'vc_type', 'vc_owner_name', 'vc_psn_type', 'vc_local_group_id', 'vc_control_word', 'vc_local_if_mtu', 'vc_remote_group_id', 'vc_remote_control_word', 'vc_remote_if_mtu', 'vc_outbound_label', 'vc_inbound_label', 'vc_oper_status', 'vc_inbound_oper_status', 'vc_outbound_oper_status'], name, value)

        class VcOwnerType(Enum):
            """
            VcOwnerType

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

            vpws = Enum.YLeaf(1, "vpws")

            vpls_vfi = Enum.YLeaf(2, "vpls-vfi")

            vpls_bridge_domain = Enum.YLeaf(3, "vpls-bridge-domain")

            interface = Enum.YLeaf(4, "interface")


        class VcPsnType(Enum):
            """
            VcPsnType

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

            mpls = Enum.YLeaf(1, "mpls")

            l2tp = Enum.YLeaf(2, "l2tp")

            ip = Enum.YLeaf(3, "ip")

            mpls_over_ip = Enum.YLeaf(4, "mpls-over-ip")

            gre = Enum.YLeaf(5, "gre")

            other = Enum.YLeaf(6, "other")


        class VcRemoteControlWord(Enum):
            """
            VcRemoteControlWord

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

            noControlWord = Enum.YLeaf(1, "noControlWord")

            withControlWord = Enum.YLeaf(2, "withControlWord")

            notYetKnown = Enum.YLeaf(3, "notYetKnown")



        class Statistics(Entity):
            """
            A collection of pseudowire\-related statistics objects
            
            .. attribute:: vc_create_time
            
            	System time when this VC was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vc_up_time
            
            	Number of consecutive ticks this VC has been 'up' in both directions together
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: discontinuity_time
            
            	The time on the most recent occasion at which any of this pseudowire's counters sufferred discontinuity. If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this node contains the time the local management subsystem re\-initialized itself
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            	**mandatory**\: True
            
            .. attribute:: in_octets
            
            	The total number of octets received on this pseudowire.  Discontinuities in the value of this counter can occur at re\-initialization of the management system and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_pkts
            
            	The total number of packets received on this pseudowire.  Discontinuities in the value of this counter can occur at re\-initialization of the management system and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_errors
            
            	The total number of inbound packets that contained errors.  Discontinuities in the value of this counter can occur at re\-initialization of the management system and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_octets
            
            	The total number of octets sent on this pseudowire.  Discontinuities in the value of this counter can occur at re\-initialization of the management system and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_pkts
            
            	The total number of packets sent on this pseudowire.  Discontinuities in the value of this counter can occur at re\-initialization of the management system and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_errors
            
            	The total number of outbound packets that could not be sent on this pseudowire.  Discontinuities in the value of this counter can occur at re\-initialization of the management system and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'l2vpn-pw'
            _revision = '2016-12-07'

            def __init__(self):
                super(PseudowireState.Pseudowires.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "pseudowires"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.vc_create_time = YLeaf(YType.uint32, "vc-create-time")

                self.vc_up_time = YLeaf(YType.uint32, "vc-up-time")

                self.discontinuity_time = YLeaf(YType.str, "discontinuity-time")

                self.in_octets = YLeaf(YType.uint64, "in-octets")

                self.in_pkts = YLeaf(YType.uint64, "in-pkts")

                self.in_errors = YLeaf(YType.uint64, "in-errors")

                self.out_octets = YLeaf(YType.uint64, "out-octets")

                self.out_pkts = YLeaf(YType.uint64, "out-pkts")

                self.out_errors = YLeaf(YType.uint64, "out-errors")
                self._segment_path = lambda: "statistics"

            def __setattr__(self, name, value):
                self._perform_setattr(PseudowireState.Pseudowires.Statistics, ['vc_create_time', 'vc_up_time', 'discontinuity_time', 'in_octets', 'in_pkts', 'in_errors', 'out_octets', 'out_pkts', 'out_errors'], name, value)

    def clone_ptr(self):
        self._top_entity = PseudowireState()
        return self._top_entity

class PwEncapMpls(Identity):
    """
    Use MPLS for PW encapsulation
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwEncapMpls, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-encap-mpls")


class PwVcTypeEther(Identity):
    """
    Identity for Ethernet VC type
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwVcTypeEther, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-vc-type-ether")


class PwVcTypeVlan(Identity):
    """
    Identity for VLAN VC type
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwVcTypeVlan, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-vc-type-vlan")


class PwVcTypeVlanPassthrough(Identity):
    """
    Identity for VLAN passthrough VC type (XR)
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwVcTypeVlanPassthrough, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-vc-type-vlan-passthrough")


class PwLbEthernetType(Identity):
    """
    Base type for load\-balancing with ethernet fields
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLbEthernetType, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-lb-ethernet-type")


class PwLbEthSrcMac(Identity):
    """
    Load\-balancing with ethernet source MAC field
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLbEthSrcMac, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-lb-eth-src-mac")


class PwLbEthDstMac(Identity):
    """
    Load\-balancing with ethernet destination MAC field
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLbEthDstMac, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-lb-eth-dst-mac")


class PwLbEthSrcDstMac(Identity):
    """
    Load\-balancing with ethernet source and destination MAC
    fields
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLbEthSrcDstMac, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-lb-eth-src-dst-mac")


class PwLbIpType(Identity):
    """
    Base type for load\-balancing with IP
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLbIpType, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-lb-ip-type")


class PwLbIpSrcIp(Identity):
    """
    Load\-balancing with IP source IP field
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLbIpSrcIp, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-lb-ip-src-ip")


class PwLbIpDstIp(Identity):
    """
    Load\-balancing with IP destination IP field
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLbIpDstIp, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-lb-ip-dst-ip")


class PwLbIpSrcDstIp(Identity):
    """
    Load\-balancing with IP source and destination IP fields
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLbIpSrcDstIp, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-lb-ip-src-dst-ip")


class PwSignalingProtocolNone(Identity):
    """
    No PW signaling protocol
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwSignalingProtocolNone, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-signaling-protocol-none")


class PwSignalingProtocolLdp(Identity):
    """
    Use MPLS LDP for PW signaling protocol
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwSignalingProtocolLdp, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-signaling-protocol-ldp")


class PwSignalingProtocolBgp(Identity):
    """
    Use BGP for PW signaling protocol
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwSignalingProtocolBgp, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-signaling-protocol-bgp")


class PwSequencingReceive(Identity):
    """
    Receive sequencing option for PW
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwSequencingReceive, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-sequencing-receive")


class PwSequencingTransmit(Identity):
    """
    Transmit sequencing option for PW
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwSequencingTransmit, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-sequencing-transmit")


class PwSequencingBoth(Identity):
    """
    Receive and Transmit sequencing option for PW
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwSequencingBoth, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-sequencing-both")



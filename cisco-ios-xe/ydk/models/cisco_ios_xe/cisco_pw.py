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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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



class PwLoadBalanceType(Identity):
    """
    Base type for load\-balancing type
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLoadBalanceType, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-load-balance-type")


class PwVcType(Identity):
    """
    Base identity for VC type in PW
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwVcType, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-vc-type")


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


class PwEncapsulationType(Identity):
    """
    Base identity for PW encapsulations.
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwEncapsulationType, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-encapsulation-type")


class PseudowireConfig(Entity):
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
        super(PseudowireConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "pseudowire-config"
        self.yang_parent_name = "cisco-pw"

        self.global_ = PseudowireConfig.Global_()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._children_yang_names.add("global")

        self.pw_static_oam_classes = PseudowireConfig.PwStaticOamClasses()
        self.pw_static_oam_classes.parent = self
        self._children_name_map["pw_static_oam_classes"] = "pw-static-oam-classes"
        self._children_yang_names.add("pw-static-oam-classes")

        self.pw_templates = PseudowireConfig.PwTemplates()
        self.pw_templates.parent = self
        self._children_name_map["pw_templates"] = "pw-templates"
        self._children_yang_names.add("pw-templates")


    class Global_(Entity):
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
            super(PseudowireConfig.Global_, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "pseudowire-config"

            self.predictive_redundancy = YLeaf(YType.boolean, "predictive-redundancy")

            self.pw_grouping = YLeaf(YType.boolean, "pw-grouping")

            self.pw_oam_refresh_transmit = YLeaf(YType.uint32, "pw-oam-refresh-transmit")

            self.pw_status = YLeaf(YType.boolean, "pw-status")

            self.vc_state_notification_batch_size = YLeaf(YType.uint32, "vc-state-notification-batch-size")

            self.vc_state_notification_enabled = YLeaf(YType.boolean, "vc-state-notification-enabled")

            self.vc_state_notification_rate = YLeaf(YType.uint32, "vc-state-notification-rate")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("predictive_redundancy",
                            "pw_grouping",
                            "pw_oam_refresh_transmit",
                            "pw_status",
                            "vc_state_notification_batch_size",
                            "vc_state_notification_enabled",
                            "vc_state_notification_rate") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(PseudowireConfig.Global_, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PseudowireConfig.Global_, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.predictive_redundancy.is_set or
                self.pw_grouping.is_set or
                self.pw_oam_refresh_transmit.is_set or
                self.pw_status.is_set or
                self.vc_state_notification_batch_size.is_set or
                self.vc_state_notification_enabled.is_set or
                self.vc_state_notification_rate.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.predictive_redundancy.yfilter != YFilter.not_set or
                self.pw_grouping.yfilter != YFilter.not_set or
                self.pw_oam_refresh_transmit.yfilter != YFilter.not_set or
                self.pw_status.yfilter != YFilter.not_set or
                self.vc_state_notification_batch_size.yfilter != YFilter.not_set or
                self.vc_state_notification_enabled.yfilter != YFilter.not_set or
                self.vc_state_notification_rate.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "global" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-pw:pseudowire-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.predictive_redundancy.is_set or self.predictive_redundancy.yfilter != YFilter.not_set):
                leaf_name_data.append(self.predictive_redundancy.get_name_leafdata())
            if (self.pw_grouping.is_set or self.pw_grouping.yfilter != YFilter.not_set):
                leaf_name_data.append(self.pw_grouping.get_name_leafdata())
            if (self.pw_oam_refresh_transmit.is_set or self.pw_oam_refresh_transmit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.pw_oam_refresh_transmit.get_name_leafdata())
            if (self.pw_status.is_set or self.pw_status.yfilter != YFilter.not_set):
                leaf_name_data.append(self.pw_status.get_name_leafdata())
            if (self.vc_state_notification_batch_size.is_set or self.vc_state_notification_batch_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_state_notification_batch_size.get_name_leafdata())
            if (self.vc_state_notification_enabled.is_set or self.vc_state_notification_enabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_state_notification_enabled.get_name_leafdata())
            if (self.vc_state_notification_rate.is_set or self.vc_state_notification_rate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_state_notification_rate.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "predictive-redundancy" or name == "pw-grouping" or name == "pw-oam-refresh-transmit" or name == "pw-status" or name == "vc-state-notification-batch-size" or name == "vc-state-notification-enabled" or name == "vc-state-notification-rate"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "predictive-redundancy"):
                self.predictive_redundancy = value
                self.predictive_redundancy.value_namespace = name_space
                self.predictive_redundancy.value_namespace_prefix = name_space_prefix
            if(value_path == "pw-grouping"):
                self.pw_grouping = value
                self.pw_grouping.value_namespace = name_space
                self.pw_grouping.value_namespace_prefix = name_space_prefix
            if(value_path == "pw-oam-refresh-transmit"):
                self.pw_oam_refresh_transmit = value
                self.pw_oam_refresh_transmit.value_namespace = name_space
                self.pw_oam_refresh_transmit.value_namespace_prefix = name_space_prefix
            if(value_path == "pw-status"):
                self.pw_status = value
                self.pw_status.value_namespace = name_space
                self.pw_status.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-state-notification-batch-size"):
                self.vc_state_notification_batch_size = value
                self.vc_state_notification_batch_size.value_namespace = name_space
                self.vc_state_notification_batch_size.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-state-notification-enabled"):
                self.vc_state_notification_enabled = value
                self.vc_state_notification_enabled.value_namespace = name_space
                self.vc_state_notification_enabled.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-state-notification-rate"):
                self.vc_state_notification_rate = value
                self.vc_state_notification_rate.value_namespace = name_space
                self.vc_state_notification_rate.value_namespace_prefix = name_space_prefix


    class PwTemplates(Entity):
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
            super(PseudowireConfig.PwTemplates, self).__init__()

            self.yang_name = "pw-templates"
            self.yang_parent_name = "pseudowire-config"

            self.pw_template = YList(self)

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
                        super(PseudowireConfig.PwTemplates, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PseudowireConfig.PwTemplates, self).__setattr__(name, value)


        class PwTemplate(Entity):
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
            	**type**\:   :py:class:`PwEncapsulationType <ydk.models.cisco_ios_xe.cisco_pw.PwEncapsulationType>`
            
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
            	**type**\:   :py:class:`PwSignalingProtocolType <ydk.models.cisco_ios_xe.cisco_pw.PwSignalingProtocolType>`
            
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
            	**type**\:   :py:class:`PwVcType <ydk.models.cisco_ios_xe.cisco_pw.PwVcType>`
            
            .. attribute:: vccv
            
            	VCCV configuration
            	**type**\:   :py:class:`Vccv <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.Vccv>`
            
            

            """

            _prefix = 'l2vpn-pw'
            _revision = '2016-12-07'

            def __init__(self):
                super(PseudowireConfig.PwTemplates.PwTemplate, self).__init__()

                self.yang_name = "pw-template"
                self.yang_parent_name = "pw-templates"

                self.name = YLeaf(YType.str, "name")

                self.control_word = YLeaf(YType.boolean, "control-word")

                self.encapsulation = YLeaf(YType.identityref, "encapsulation")

                self.mac_withdraw = YLeaf(YType.boolean, "mac-withdraw")

                self.signaling_protocol = YLeaf(YType.identityref, "signaling-protocol")

                self.source_ip = YLeaf(YType.str, "source-ip")

                self.switching_tlv = YLeaf(YType.boolean, "switching-tlv")

                self.tag_rewrite_ingress_vlan = YLeaf(YType.uint16, "tag-rewrite-ingress-vlan")

                self.vc_type = YLeaf(YType.identityref, "vc-type")

                self.load_balance = PseudowireConfig.PwTemplates.PwTemplate.LoadBalance()
                self.load_balance.parent = self
                self._children_name_map["load_balance"] = "load-balance"
                self._children_yang_names.add("load-balance")

                self.port_profile_spec = PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec()
                self.port_profile_spec.parent = self
                self._children_name_map["port_profile_spec"] = "port-profile-spec"
                self._children_yang_names.add("port-profile-spec")

                self.preferred_path = PseudowireConfig.PwTemplates.PwTemplate.PreferredPath()
                self.preferred_path.parent = self
                self._children_name_map["preferred_path"] = "preferred-path"
                self._children_yang_names.add("preferred-path")

                self.sequencing = PseudowireConfig.PwTemplates.PwTemplate.Sequencing()
                self.sequencing.parent = self
                self._children_name_map["sequencing"] = "sequencing"
                self._children_yang_names.add("sequencing")

                self.status = PseudowireConfig.PwTemplates.PwTemplate.Status()
                self.status.parent = self
                self._children_name_map["status"] = "status"
                self._children_yang_names.add("status")

                self.switchover_delay = PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay()
                self.switchover_delay.parent = self
                self._children_name_map["switchover_delay"] = "switchover-delay"
                self._children_yang_names.add("switchover-delay")

                self.vccv = PseudowireConfig.PwTemplates.PwTemplate.Vccv()
                self.vccv.parent = self
                self._children_name_map["vccv"] = "vccv"
                self._children_yang_names.add("vccv")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "control_word",
                                "encapsulation",
                                "mac_withdraw",
                                "signaling_protocol",
                                "source_ip",
                                "switching_tlv",
                                "tag_rewrite_ingress_vlan",
                                "vc_type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PseudowireConfig.PwTemplates.PwTemplate, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PseudowireConfig.PwTemplates.PwTemplate, self).__setattr__(name, value)


            class LoadBalance(Entity):
                """
                Load balancing mechanism.
                
                .. attribute:: ethernet
                
                	Ethernet mac address based load balancing
                	**type**\:   :py:class:`PwLbEthernetType <ydk.models.cisco_ios_xe.cisco_pw.PwLbEthernetType>`
                
                	**default value**\: pw-lb-eth-src-dst-mac
                
                .. attribute:: flow_label
                
                	Enable Flow Aware Label (FAT) PW \- the capability to carry flow label on PW
                	**type**\:   :py:class:`FlowLabel <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel>`
                
                .. attribute:: ip
                
                	IP address based load balancing
                	**type**\:   :py:class:`PwLbIpType <ydk.models.cisco_ios_xe.cisco_pw.PwLbIpType>`
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    super(PseudowireConfig.PwTemplates.PwTemplate.LoadBalance, self).__init__()

                    self.yang_name = "load-balance"
                    self.yang_parent_name = "pw-template"

                    self.ethernet = YLeaf(YType.identityref, "ethernet")

                    self.ip = YLeaf(YType.identityref, "ip")

                    self.flow_label = PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel()
                    self.flow_label.parent = self
                    self._children_name_map["flow_label"] = "flow-label"
                    self._children_yang_names.add("flow-label")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ethernet",
                                    "ip") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PseudowireConfig.PwTemplates.PwTemplate.LoadBalance, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PseudowireConfig.PwTemplates.PwTemplate.LoadBalance, self).__setattr__(name, value)


                class FlowLabel(Entity):
                    """
                    Enable Flow Aware Label (FAT) PW \- the capability to
                    carry flow label on PW
                    
                    .. attribute:: direction
                    
                    	Directions to enable Flow Aware Label PW
                    	**type**\:   :py:class:`Direction <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel.Direction>`
                    
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
                        super(PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel, self).__init__()

                        self.yang_name = "flow-label"
                        self.yang_parent_name = "load-balance"

                        self.direction = YLeaf(YType.enumeration, "direction")

                        self.static = YLeaf(YType.boolean, "static")

                        self.tlv_code_17 = YLeaf(YType.boolean, "tlv-code-17")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("direction",
                                        "static",
                                        "tlv_code_17") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel, self).__setattr__(name, value)

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


                    def has_data(self):
                        return (
                            self.direction.is_set or
                            self.static.is_set or
                            self.tlv_code_17.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.direction.yfilter != YFilter.not_set or
                            self.static.yfilter != YFilter.not_set or
                            self.tlv_code_17.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "flow-label" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.direction.get_name_leafdata())
                        if (self.static.is_set or self.static.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.static.get_name_leafdata())
                        if (self.tlv_code_17.is_set or self.tlv_code_17.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tlv_code_17.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "direction" or name == "static" or name == "tlv-code-17"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "direction"):
                            self.direction = value
                            self.direction.value_namespace = name_space
                            self.direction.value_namespace_prefix = name_space_prefix
                        if(value_path == "static"):
                            self.static = value
                            self.static.value_namespace = name_space
                            self.static.value_namespace_prefix = name_space_prefix
                        if(value_path == "tlv-code-17"):
                            self.tlv_code_17 = value
                            self.tlv_code_17.value_namespace = name_space
                            self.tlv_code_17.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.ethernet.is_set or
                        self.ip.is_set or
                        (self.flow_label is not None and self.flow_label.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ethernet.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        (self.flow_label is not None and self.flow_label.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "load-balance" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ethernet.is_set or self.ethernet.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ethernet.get_name_leafdata())
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "flow-label"):
                        if (self.flow_label is None):
                            self.flow_label = PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel()
                            self.flow_label.parent = self
                            self._children_name_map["flow_label"] = "flow-label"
                        return self.flow_label

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "flow-label" or name == "ethernet" or name == "ip"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ethernet"):
                        self.ethernet = value
                        self.ethernet.value_namespace = name_space
                        self.ethernet.value_namespace_prefix = name_space_prefix
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix


            class PreferredPath(Entity):
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
                    super(PseudowireConfig.PwTemplates.PwTemplate.PreferredPath, self).__init__()

                    self.yang_name = "preferred-path"
                    self.yang_parent_name = "pw-template"

                    self.address = YLeaf(YType.str, "address")

                    self.disable_fallback = YLeaf(YType.boolean, "disable-fallback")

                    self.hostname = YLeaf(YType.str, "hostname")

                    self.interface = YLeaf(YType.str, "interface")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("address",
                                    "disable_fallback",
                                    "hostname",
                                    "interface") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PseudowireConfig.PwTemplates.PwTemplate.PreferredPath, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PseudowireConfig.PwTemplates.PwTemplate.PreferredPath, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.address.is_set or
                        self.disable_fallback.is_set or
                        self.hostname.is_set or
                        self.interface.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address.yfilter != YFilter.not_set or
                        self.disable_fallback.yfilter != YFilter.not_set or
                        self.hostname.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "preferred-path" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address.get_name_leafdata())
                    if (self.disable_fallback.is_set or self.disable_fallback.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disable_fallback.get_name_leafdata())
                    if (self.hostname.is_set or self.hostname.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hostname.get_name_leafdata())
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "address" or name == "disable-fallback" or name == "hostname" or name == "interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address"):
                        self.address = value
                        self.address.value_namespace = name_space
                        self.address.value_namespace_prefix = name_space_prefix
                    if(value_path == "disable-fallback"):
                        self.disable_fallback = value
                        self.disable_fallback.value_namespace = name_space
                        self.disable_fallback.value_namespace_prefix = name_space_prefix
                    if(value_path == "hostname"):
                        self.hostname = value
                        self.hostname.value_namespace = name_space
                        self.hostname.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix


            class Sequencing(Entity):
                """
                Sequencing options
                
                .. attribute:: direction
                
                	TODO
                	**type**\:   :py:class:`PwSequencingType <ydk.models.cisco_ios_xe.cisco_pw.PwSequencingType>`
                
                .. attribute:: resync
                
                	TODO
                	**type**\:  int
                
                	**range:** 5..65535
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    super(PseudowireConfig.PwTemplates.PwTemplate.Sequencing, self).__init__()

                    self.yang_name = "sequencing"
                    self.yang_parent_name = "pw-template"

                    self.direction = YLeaf(YType.identityref, "direction")

                    self.resync = YLeaf(YType.int32, "resync")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("direction",
                                    "resync") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PseudowireConfig.PwTemplates.PwTemplate.Sequencing, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PseudowireConfig.PwTemplates.PwTemplate.Sequencing, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.direction.is_set or
                        self.resync.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.direction.yfilter != YFilter.not_set or
                        self.resync.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "sequencing" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.direction.get_name_leafdata())
                    if (self.resync.is_set or self.resync.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.resync.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "direction" or name == "resync"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "direction"):
                        self.direction = value
                        self.direction.value_namespace = name_space
                        self.direction.value_namespace_prefix = name_space_prefix
                    if(value_path == "resync"):
                        self.resync = value
                        self.resync.value_namespace = name_space
                        self.resync.value_namespace_prefix = name_space_prefix


            class Vccv(Entity):
                """
                VCCV configuration
                
                .. attribute:: control_word
                
                	Enable VCCV verification type
                	**type**\:  bool
                
                

                """

                _prefix = 'l2vpn-pw'
                _revision = '2016-12-07'

                def __init__(self):
                    super(PseudowireConfig.PwTemplates.PwTemplate.Vccv, self).__init__()

                    self.yang_name = "vccv"
                    self.yang_parent_name = "pw-template"

                    self.control_word = YLeaf(YType.boolean, "control-word")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("control_word") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PseudowireConfig.PwTemplates.PwTemplate.Vccv, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PseudowireConfig.PwTemplates.PwTemplate.Vccv, self).__setattr__(name, value)

                def has_data(self):
                    return self.control_word.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.control_word.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vccv" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.control_word.is_set or self.control_word.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.control_word.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "control-word"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "control-word"):
                        self.control_word = value
                        self.control_word.value_namespace = name_space
                        self.control_word.value_namespace_prefix = name_space_prefix


            class SwitchoverDelay(Entity):
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
                    super(PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay, self).__init__()

                    self.yang_name = "switchover-delay"
                    self.yang_parent_name = "pw-template"

                    self.never = YLeaf(YType.boolean, "never")

                    self.switchover_timer = YLeaf(YType.uint8, "switchover-timer")

                    self.timer = YLeaf(YType.uint8, "timer")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("never",
                                    "switchover_timer",
                                    "timer") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.never.is_set or
                        self.switchover_timer.is_set or
                        self.timer.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.never.yfilter != YFilter.not_set or
                        self.switchover_timer.yfilter != YFilter.not_set or
                        self.timer.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "switchover-delay" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.never.is_set or self.never.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.never.get_name_leafdata())
                    if (self.switchover_timer.is_set or self.switchover_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.switchover_timer.get_name_leafdata())
                    if (self.timer.is_set or self.timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.timer.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "never" or name == "switchover-timer" or name == "timer"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "never"):
                        self.never = value
                        self.never.value_namespace = name_space
                        self.never.value_namespace_prefix = name_space_prefix
                    if(value_path == "switchover-timer"):
                        self.switchover_timer = value
                        self.switchover_timer.value_namespace = name_space
                        self.switchover_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "timer"):
                        self.timer = value
                        self.timer.value_namespace = name_space
                        self.timer.value_namespace_prefix = name_space_prefix


            class Status(Entity):
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
                    super(PseudowireConfig.PwTemplates.PwTemplate.Status, self).__init__()

                    self.yang_name = "status"
                    self.yang_parent_name = "pw-template"

                    self.decoupled = YLeaf(YType.boolean, "decoupled")

                    self.disable = YLeaf(YType.boolean, "disable")

                    self.peer_topo_dual_homed = YLeaf(YType.boolean, "peer-topo-dual-homed")

                    self.redundancy_master = YLeaf(YType.boolean, "redundancy-master")

                    self.route_watch_disable = YLeaf(YType.boolean, "route-watch-disable")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("decoupled",
                                    "disable",
                                    "peer_topo_dual_homed",
                                    "redundancy_master",
                                    "route_watch_disable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PseudowireConfig.PwTemplates.PwTemplate.Status, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PseudowireConfig.PwTemplates.PwTemplate.Status, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.decoupled.is_set or
                        self.disable.is_set or
                        self.peer_topo_dual_homed.is_set or
                        self.redundancy_master.is_set or
                        self.route_watch_disable.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.decoupled.yfilter != YFilter.not_set or
                        self.disable.yfilter != YFilter.not_set or
                        self.peer_topo_dual_homed.yfilter != YFilter.not_set or
                        self.redundancy_master.yfilter != YFilter.not_set or
                        self.route_watch_disable.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "status" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.decoupled.is_set or self.decoupled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.decoupled.get_name_leafdata())
                    if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disable.get_name_leafdata())
                    if (self.peer_topo_dual_homed.is_set or self.peer_topo_dual_homed.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peer_topo_dual_homed.get_name_leafdata())
                    if (self.redundancy_master.is_set or self.redundancy_master.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.redundancy_master.get_name_leafdata())
                    if (self.route_watch_disable.is_set or self.route_watch_disable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_watch_disable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "decoupled" or name == "disable" or name == "peer-topo-dual-homed" or name == "redundancy-master" or name == "route-watch-disable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "decoupled"):
                        self.decoupled = value
                        self.decoupled.value_namespace = name_space
                        self.decoupled.value_namespace_prefix = name_space_prefix
                    if(value_path == "disable"):
                        self.disable = value
                        self.disable.value_namespace = name_space
                        self.disable.value_namespace_prefix = name_space_prefix
                    if(value_path == "peer-topo-dual-homed"):
                        self.peer_topo_dual_homed = value
                        self.peer_topo_dual_homed.value_namespace = name_space
                        self.peer_topo_dual_homed.value_namespace_prefix = name_space_prefix
                    if(value_path == "redundancy-master"):
                        self.redundancy_master = value
                        self.redundancy_master.value_namespace = name_space
                        self.redundancy_master.value_namespace_prefix = name_space_prefix
                    if(value_path == "route-watch-disable"):
                        self.route_watch_disable = value
                        self.route_watch_disable.value_namespace = name_space
                        self.route_watch_disable.value_namespace_prefix = name_space_prefix


            class PortProfileSpec(Entity):
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
                    super(PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec, self).__init__()

                    self.yang_name = "port-profile-spec"
                    self.yang_parent_name = "pw-template"

                    self.description = YLeaf(YType.str, "description")

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.max_ports = YLeaf(YType.uint16, "max-ports")

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.shut_force = YLeaf(YType.boolean, "shut-force")

                    self.shutdown = YLeaf(YType.boolean, "shutdown")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("description",
                                    "enabled",
                                    "max_ports",
                                    "mtu",
                                    "shut_force",
                                    "shutdown") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.description.is_set or
                        self.enabled.is_set or
                        self.max_ports.is_set or
                        self.mtu.is_set or
                        self.shut_force.is_set or
                        self.shutdown.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.description.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.max_ports.yfilter != YFilter.not_set or
                        self.mtu.yfilter != YFilter.not_set or
                        self.shut_force.yfilter != YFilter.not_set or
                        self.shutdown.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "port-profile-spec" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.description.get_name_leafdata())
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.max_ports.is_set or self.max_ports.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_ports.get_name_leafdata())
                    if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mtu.get_name_leafdata())
                    if (self.shut_force.is_set or self.shut_force.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.shut_force.get_name_leafdata())
                    if (self.shutdown.is_set or self.shutdown.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.shutdown.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "description" or name == "enabled" or name == "max-ports" or name == "mtu" or name == "shut-force" or name == "shutdown"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "description"):
                        self.description = value
                        self.description.value_namespace = name_space
                        self.description.value_namespace_prefix = name_space_prefix
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-ports"):
                        self.max_ports = value
                        self.max_ports.value_namespace = name_space
                        self.max_ports.value_namespace_prefix = name_space_prefix
                    if(value_path == "mtu"):
                        self.mtu = value
                        self.mtu.value_namespace = name_space
                        self.mtu.value_namespace_prefix = name_space_prefix
                    if(value_path == "shut-force"):
                        self.shut_force = value
                        self.shut_force.value_namespace = name_space
                        self.shut_force.value_namespace_prefix = name_space_prefix
                    if(value_path == "shutdown"):
                        self.shutdown = value
                        self.shutdown.value_namespace = name_space
                        self.shutdown.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.name.is_set or
                    self.control_word.is_set or
                    self.encapsulation.is_set or
                    self.mac_withdraw.is_set or
                    self.signaling_protocol.is_set or
                    self.source_ip.is_set or
                    self.switching_tlv.is_set or
                    self.tag_rewrite_ingress_vlan.is_set or
                    self.vc_type.is_set or
                    (self.load_balance is not None and self.load_balance.has_data()) or
                    (self.port_profile_spec is not None and self.port_profile_spec.has_data()) or
                    (self.preferred_path is not None and self.preferred_path.has_data()) or
                    (self.sequencing is not None and self.sequencing.has_data()) or
                    (self.status is not None and self.status.has_data()) or
                    (self.switchover_delay is not None and self.switchover_delay.has_data()) or
                    (self.vccv is not None and self.vccv.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.control_word.yfilter != YFilter.not_set or
                    self.encapsulation.yfilter != YFilter.not_set or
                    self.mac_withdraw.yfilter != YFilter.not_set or
                    self.signaling_protocol.yfilter != YFilter.not_set or
                    self.source_ip.yfilter != YFilter.not_set or
                    self.switching_tlv.yfilter != YFilter.not_set or
                    self.tag_rewrite_ingress_vlan.yfilter != YFilter.not_set or
                    self.vc_type.yfilter != YFilter.not_set or
                    (self.load_balance is not None and self.load_balance.has_operation()) or
                    (self.port_profile_spec is not None and self.port_profile_spec.has_operation()) or
                    (self.preferred_path is not None and self.preferred_path.has_operation()) or
                    (self.sequencing is not None and self.sequencing.has_operation()) or
                    (self.status is not None and self.status.has_operation()) or
                    (self.switchover_delay is not None and self.switchover_delay.has_operation()) or
                    (self.vccv is not None and self.vccv.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pw-template" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-pw:pseudowire-config/pw-templates/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.control_word.is_set or self.control_word.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.control_word.get_name_leafdata())
                if (self.encapsulation.is_set or self.encapsulation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.encapsulation.get_name_leafdata())
                if (self.mac_withdraw.is_set or self.mac_withdraw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mac_withdraw.get_name_leafdata())
                if (self.signaling_protocol.is_set or self.signaling_protocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.signaling_protocol.get_name_leafdata())
                if (self.source_ip.is_set or self.source_ip.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_ip.get_name_leafdata())
                if (self.switching_tlv.is_set or self.switching_tlv.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.switching_tlv.get_name_leafdata())
                if (self.tag_rewrite_ingress_vlan.is_set or self.tag_rewrite_ingress_vlan.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tag_rewrite_ingress_vlan.get_name_leafdata())
                if (self.vc_type.is_set or self.vc_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vc_type.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "load-balance"):
                    if (self.load_balance is None):
                        self.load_balance = PseudowireConfig.PwTemplates.PwTemplate.LoadBalance()
                        self.load_balance.parent = self
                        self._children_name_map["load_balance"] = "load-balance"
                    return self.load_balance

                if (child_yang_name == "port-profile-spec"):
                    if (self.port_profile_spec is None):
                        self.port_profile_spec = PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec()
                        self.port_profile_spec.parent = self
                        self._children_name_map["port_profile_spec"] = "port-profile-spec"
                    return self.port_profile_spec

                if (child_yang_name == "preferred-path"):
                    if (self.preferred_path is None):
                        self.preferred_path = PseudowireConfig.PwTemplates.PwTemplate.PreferredPath()
                        self.preferred_path.parent = self
                        self._children_name_map["preferred_path"] = "preferred-path"
                    return self.preferred_path

                if (child_yang_name == "sequencing"):
                    if (self.sequencing is None):
                        self.sequencing = PseudowireConfig.PwTemplates.PwTemplate.Sequencing()
                        self.sequencing.parent = self
                        self._children_name_map["sequencing"] = "sequencing"
                    return self.sequencing

                if (child_yang_name == "status"):
                    if (self.status is None):
                        self.status = PseudowireConfig.PwTemplates.PwTemplate.Status()
                        self.status.parent = self
                        self._children_name_map["status"] = "status"
                    return self.status

                if (child_yang_name == "switchover-delay"):
                    if (self.switchover_delay is None):
                        self.switchover_delay = PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay()
                        self.switchover_delay.parent = self
                        self._children_name_map["switchover_delay"] = "switchover-delay"
                    return self.switchover_delay

                if (child_yang_name == "vccv"):
                    if (self.vccv is None):
                        self.vccv = PseudowireConfig.PwTemplates.PwTemplate.Vccv()
                        self.vccv.parent = self
                        self._children_name_map["vccv"] = "vccv"
                    return self.vccv

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "load-balance" or name == "port-profile-spec" or name == "preferred-path" or name == "sequencing" or name == "status" or name == "switchover-delay" or name == "vccv" or name == "name" or name == "control-word" or name == "encapsulation" or name == "mac-withdraw" or name == "signaling-protocol" or name == "source-ip" or name == "switching-tlv" or name == "tag-rewrite-ingress-vlan" or name == "vc-type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "control-word"):
                    self.control_word = value
                    self.control_word.value_namespace = name_space
                    self.control_word.value_namespace_prefix = name_space_prefix
                if(value_path == "encapsulation"):
                    self.encapsulation = value
                    self.encapsulation.value_namespace = name_space
                    self.encapsulation.value_namespace_prefix = name_space_prefix
                if(value_path == "mac-withdraw"):
                    self.mac_withdraw = value
                    self.mac_withdraw.value_namespace = name_space
                    self.mac_withdraw.value_namespace_prefix = name_space_prefix
                if(value_path == "signaling-protocol"):
                    self.signaling_protocol = value
                    self.signaling_protocol.value_namespace = name_space
                    self.signaling_protocol.value_namespace_prefix = name_space_prefix
                if(value_path == "source-ip"):
                    self.source_ip = value
                    self.source_ip.value_namespace = name_space
                    self.source_ip.value_namespace_prefix = name_space_prefix
                if(value_path == "switching-tlv"):
                    self.switching_tlv = value
                    self.switching_tlv.value_namespace = name_space
                    self.switching_tlv.value_namespace_prefix = name_space_prefix
                if(value_path == "tag-rewrite-ingress-vlan"):
                    self.tag_rewrite_ingress_vlan = value
                    self.tag_rewrite_ingress_vlan.value_namespace = name_space
                    self.tag_rewrite_ingress_vlan.value_namespace_prefix = name_space_prefix
                if(value_path == "vc-type"):
                    self.vc_type = value
                    self.vc_type.value_namespace = name_space
                    self.vc_type.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.pw_template:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.pw_template:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "pw-templates" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-pw:pseudowire-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "pw-template"):
                for c in self.pw_template:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PseudowireConfig.PwTemplates.PwTemplate()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.pw_template.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pw-template"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class PwStaticOamClasses(Entity):
        """
        List of pseudowire static oam classes.
        
        .. attribute:: pw_static_oam_class
        
        	Pseudowire static oam class configuration
        	**type**\: list of    :py:class:`PwStaticOamClass <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwStaticOamClasses.PwStaticOamClass>`
        
        

        """

        _prefix = 'l2vpn-pw'
        _revision = '2016-12-07'

        def __init__(self):
            super(PseudowireConfig.PwStaticOamClasses, self).__init__()

            self.yang_name = "pw-static-oam-classes"
            self.yang_parent_name = "pseudowire-config"

            self.pw_static_oam_class = YList(self)

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
                        super(PseudowireConfig.PwStaticOamClasses, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PseudowireConfig.PwStaticOamClasses, self).__setattr__(name, value)


        class PwStaticOamClass(Entity):
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
                super(PseudowireConfig.PwStaticOamClasses.PwStaticOamClass, self).__init__()

                self.yang_name = "pw-static-oam-class"
                self.yang_parent_name = "pw-static-oam-classes"

                self.name = YLeaf(YType.str, "name")

                self.ack = YLeaf(YType.boolean, "ack")

                self.keepalive = YLeaf(YType.uint32, "keepalive")

                self.timeout_refresh_ack = YLeaf(YType.uint32, "timeout-refresh-ack")

                self.timeout_refresh_send = YLeaf(YType.uint32, "timeout-refresh-send")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "ack",
                                "keepalive",
                                "timeout_refresh_ack",
                                "timeout_refresh_send") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PseudowireConfig.PwStaticOamClasses.PwStaticOamClass, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PseudowireConfig.PwStaticOamClasses.PwStaticOamClass, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.name.is_set or
                    self.ack.is_set or
                    self.keepalive.is_set or
                    self.timeout_refresh_ack.is_set or
                    self.timeout_refresh_send.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.ack.yfilter != YFilter.not_set or
                    self.keepalive.yfilter != YFilter.not_set or
                    self.timeout_refresh_ack.yfilter != YFilter.not_set or
                    self.timeout_refresh_send.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pw-static-oam-class" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-pw:pseudowire-config/pw-static-oam-classes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.ack.is_set or self.ack.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ack.get_name_leafdata())
                if (self.keepalive.is_set or self.keepalive.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.keepalive.get_name_leafdata())
                if (self.timeout_refresh_ack.is_set or self.timeout_refresh_ack.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeout_refresh_ack.get_name_leafdata())
                if (self.timeout_refresh_send.is_set or self.timeout_refresh_send.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeout_refresh_send.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name" or name == "ack" or name == "keepalive" or name == "timeout-refresh-ack" or name == "timeout-refresh-send"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "ack"):
                    self.ack = value
                    self.ack.value_namespace = name_space
                    self.ack.value_namespace_prefix = name_space_prefix
                if(value_path == "keepalive"):
                    self.keepalive = value
                    self.keepalive.value_namespace = name_space
                    self.keepalive.value_namespace_prefix = name_space_prefix
                if(value_path == "timeout-refresh-ack"):
                    self.timeout_refresh_ack = value
                    self.timeout_refresh_ack.value_namespace = name_space
                    self.timeout_refresh_ack.value_namespace_prefix = name_space_prefix
                if(value_path == "timeout-refresh-send"):
                    self.timeout_refresh_send = value
                    self.timeout_refresh_send.value_namespace = name_space
                    self.timeout_refresh_send.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.pw_static_oam_class:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.pw_static_oam_class:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "pw-static-oam-classes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-pw:pseudowire-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "pw-static-oam-class"):
                for c in self.pw_static_oam_class:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PseudowireConfig.PwStaticOamClasses.PwStaticOamClass()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.pw_static_oam_class.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pw-static-oam-class"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.global_ is not None and self.global_.has_data()) or
            (self.pw_static_oam_classes is not None and self.pw_static_oam_classes.has_data()) or
            (self.pw_templates is not None and self.pw_templates.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.global_ is not None and self.global_.has_operation()) or
            (self.pw_static_oam_classes is not None and self.pw_static_oam_classes.has_operation()) or
            (self.pw_templates is not None and self.pw_templates.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "cisco-pw:pseudowire-config" + path_buffer

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

        if (child_yang_name == "global"):
            if (self.global_ is None):
                self.global_ = PseudowireConfig.Global_()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"
            return self.global_

        if (child_yang_name == "pw-static-oam-classes"):
            if (self.pw_static_oam_classes is None):
                self.pw_static_oam_classes = PseudowireConfig.PwStaticOamClasses()
                self.pw_static_oam_classes.parent = self
                self._children_name_map["pw_static_oam_classes"] = "pw-static-oam-classes"
            return self.pw_static_oam_classes

        if (child_yang_name == "pw-templates"):
            if (self.pw_templates is None):
                self.pw_templates = PseudowireConfig.PwTemplates()
                self.pw_templates.parent = self
                self._children_name_map["pw_templates"] = "pw-templates"
            return self.pw_templates

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "global" or name == "pw-static-oam-classes" or name == "pw-templates"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

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
    	**type**\: list of    :py:class:`Pseudowires <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires>`
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PseudowireState, self).__init__()
        self._top_entity = None

        self.yang_name = "pseudowire-state"
        self.yang_parent_name = "cisco-pw"

        self.pseudowires = YList(self)

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
                    super(PseudowireState, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(PseudowireState, self).__setattr__(name, value)


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
        	**type**\:   :py:class:`VcOwnerType <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires.VcOwnerType>`
        
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
        	**type**\:   :py:class:`PwOperStateType <ydk.models.cisco_ios_xe.cisco_pw.PwOperStateType>`
        
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
        	**type**\:   :py:class:`PwOperStateType <ydk.models.cisco_ios_xe.cisco_pw.PwOperStateType>`
        
        .. attribute:: vc_outbound_label
        
        	The VC label used in the outbound direction (i.e. toward the PSN). Example\: for MPLS PSN, it represents the 20 bits of VC tag, for L2TP it represent the 32 bits Session ID. If the label is not yet known (signaling in procesS), the object should return a value of 0xFFFFFFFF
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vc_outbound_oper_status
        
        	Indicates the actual operational status of this VC in the outbound direction
        	**type**\:   :py:class:`PwOperStateType <ydk.models.cisco_ios_xe.cisco_pw.PwOperStateType>`
        
        .. attribute:: vc_owner_name
        
        	Name of the L2VPN service instance that created the pseudowire VC
        	**type**\:  str
        
        .. attribute:: vc_psn_type
        
        	Indicates the type of packet\-switched network that carries this VC
        	**type**\:   :py:class:`VcPsnType <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires.VcPsnType>`
        
        .. attribute:: vc_remote_control_word
        
        	Indicates whether MPLS control words are used by the pseudowire PSN service
        	**type**\:   :py:class:`VcRemoteControlWord <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires.VcRemoteControlWord>`
        
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
        	**type**\:   :py:class:`PwVcType <ydk.models.cisco_ios_xe.cisco_pw.PwVcType>`
        
        

        """

        _prefix = 'l2vpn-pw'
        _revision = '2016-12-07'

        def __init__(self):
            super(PseudowireState.Pseudowires, self).__init__()

            self.yang_name = "pseudowires"
            self.yang_parent_name = "pseudowire-state"

            self.vc_peer_address = YLeaf(YType.str, "vc-peer-address")

            self.vc_id = YLeaf(YType.uint32, "vc-id")

            self.vc_owner_type = YLeaf(YType.enumeration, "vc-owner-type")

            self.vc_name = YLeaf(YType.str, "vc-name")

            self.vc_index = YLeaf(YType.uint32, "vc-index")

            self.vc_control_word = YLeaf(YType.boolean, "vc-control-word")

            self.vc_inbound_label = YLeaf(YType.uint32, "vc-inbound-label")

            self.vc_inbound_oper_status = YLeaf(YType.enumeration, "vc-inbound-oper-status")

            self.vc_local_group_id = YLeaf(YType.uint32, "vc-local-group-id")

            self.vc_local_if_mtu = YLeaf(YType.uint32, "vc-local-if-mtu")

            self.vc_oper_status = YLeaf(YType.enumeration, "vc-oper-status")

            self.vc_outbound_label = YLeaf(YType.uint32, "vc-outbound-label")

            self.vc_outbound_oper_status = YLeaf(YType.enumeration, "vc-outbound-oper-status")

            self.vc_owner_name = YLeaf(YType.str, "vc-owner-name")

            self.vc_psn_type = YLeaf(YType.enumeration, "vc-psn-type")

            self.vc_remote_control_word = YLeaf(YType.enumeration, "vc-remote-control-word")

            self.vc_remote_group_id = YLeaf(YType.uint32, "vc-remote-group-id")

            self.vc_remote_if_mtu = YLeaf(YType.uint32, "vc-remote-if-mtu")

            self.vc_type = YLeaf(YType.identityref, "vc-type")

            self.statistics = PseudowireState.Pseudowires.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"
            self._children_yang_names.add("statistics")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("vc_peer_address",
                            "vc_id",
                            "vc_owner_type",
                            "vc_name",
                            "vc_index",
                            "vc_control_word",
                            "vc_inbound_label",
                            "vc_inbound_oper_status",
                            "vc_local_group_id",
                            "vc_local_if_mtu",
                            "vc_oper_status",
                            "vc_outbound_label",
                            "vc_outbound_oper_status",
                            "vc_owner_name",
                            "vc_psn_type",
                            "vc_remote_control_word",
                            "vc_remote_group_id",
                            "vc_remote_if_mtu",
                            "vc_type") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(PseudowireState.Pseudowires, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PseudowireState.Pseudowires, self).__setattr__(name, value)

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
                super(PseudowireState.Pseudowires.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "pseudowires"

                self.discontinuity_time = YLeaf(YType.str, "discontinuity-time")

                self.in_errors = YLeaf(YType.uint64, "in-errors")

                self.in_octets = YLeaf(YType.uint64, "in-octets")

                self.in_pkts = YLeaf(YType.uint64, "in-pkts")

                self.out_errors = YLeaf(YType.uint64, "out-errors")

                self.out_octets = YLeaf(YType.uint64, "out-octets")

                self.out_pkts = YLeaf(YType.uint64, "out-pkts")

                self.vc_create_time = YLeaf(YType.uint32, "vc-create-time")

                self.vc_up_time = YLeaf(YType.uint32, "vc-up-time")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("discontinuity_time",
                                "in_errors",
                                "in_octets",
                                "in_pkts",
                                "out_errors",
                                "out_octets",
                                "out_pkts",
                                "vc_create_time",
                                "vc_up_time") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PseudowireState.Pseudowires.Statistics, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PseudowireState.Pseudowires.Statistics, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.discontinuity_time.is_set or
                    self.in_errors.is_set or
                    self.in_octets.is_set or
                    self.in_pkts.is_set or
                    self.out_errors.is_set or
                    self.out_octets.is_set or
                    self.out_pkts.is_set or
                    self.vc_create_time.is_set or
                    self.vc_up_time.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.discontinuity_time.yfilter != YFilter.not_set or
                    self.in_errors.yfilter != YFilter.not_set or
                    self.in_octets.yfilter != YFilter.not_set or
                    self.in_pkts.yfilter != YFilter.not_set or
                    self.out_errors.yfilter != YFilter.not_set or
                    self.out_octets.yfilter != YFilter.not_set or
                    self.out_pkts.yfilter != YFilter.not_set or
                    self.vc_create_time.yfilter != YFilter.not_set or
                    self.vc_up_time.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "statistics" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.discontinuity_time.is_set or self.discontinuity_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.discontinuity_time.get_name_leafdata())
                if (self.in_errors.is_set or self.in_errors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_errors.get_name_leafdata())
                if (self.in_octets.is_set or self.in_octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_octets.get_name_leafdata())
                if (self.in_pkts.is_set or self.in_pkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_pkts.get_name_leafdata())
                if (self.out_errors.is_set or self.out_errors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.out_errors.get_name_leafdata())
                if (self.out_octets.is_set or self.out_octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.out_octets.get_name_leafdata())
                if (self.out_pkts.is_set or self.out_pkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.out_pkts.get_name_leafdata())
                if (self.vc_create_time.is_set or self.vc_create_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vc_create_time.get_name_leafdata())
                if (self.vc_up_time.is_set or self.vc_up_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vc_up_time.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "discontinuity-time" or name == "in-errors" or name == "in-octets" or name == "in-pkts" or name == "out-errors" or name == "out-octets" or name == "out-pkts" or name == "vc-create-time" or name == "vc-up-time"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "discontinuity-time"):
                    self.discontinuity_time = value
                    self.discontinuity_time.value_namespace = name_space
                    self.discontinuity_time.value_namespace_prefix = name_space_prefix
                if(value_path == "in-errors"):
                    self.in_errors = value
                    self.in_errors.value_namespace = name_space
                    self.in_errors.value_namespace_prefix = name_space_prefix
                if(value_path == "in-octets"):
                    self.in_octets = value
                    self.in_octets.value_namespace = name_space
                    self.in_octets.value_namespace_prefix = name_space_prefix
                if(value_path == "in-pkts"):
                    self.in_pkts = value
                    self.in_pkts.value_namespace = name_space
                    self.in_pkts.value_namespace_prefix = name_space_prefix
                if(value_path == "out-errors"):
                    self.out_errors = value
                    self.out_errors.value_namespace = name_space
                    self.out_errors.value_namespace_prefix = name_space_prefix
                if(value_path == "out-octets"):
                    self.out_octets = value
                    self.out_octets.value_namespace = name_space
                    self.out_octets.value_namespace_prefix = name_space_prefix
                if(value_path == "out-pkts"):
                    self.out_pkts = value
                    self.out_pkts.value_namespace = name_space
                    self.out_pkts.value_namespace_prefix = name_space_prefix
                if(value_path == "vc-create-time"):
                    self.vc_create_time = value
                    self.vc_create_time.value_namespace = name_space
                    self.vc_create_time.value_namespace_prefix = name_space_prefix
                if(value_path == "vc-up-time"):
                    self.vc_up_time = value
                    self.vc_up_time.value_namespace = name_space
                    self.vc_up_time.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.vc_peer_address.is_set or
                self.vc_id.is_set or
                self.vc_owner_type.is_set or
                self.vc_name.is_set or
                self.vc_index.is_set or
                self.vc_control_word.is_set or
                self.vc_inbound_label.is_set or
                self.vc_inbound_oper_status.is_set or
                self.vc_local_group_id.is_set or
                self.vc_local_if_mtu.is_set or
                self.vc_oper_status.is_set or
                self.vc_outbound_label.is_set or
                self.vc_outbound_oper_status.is_set or
                self.vc_owner_name.is_set or
                self.vc_psn_type.is_set or
                self.vc_remote_control_word.is_set or
                self.vc_remote_group_id.is_set or
                self.vc_remote_if_mtu.is_set or
                self.vc_type.is_set or
                (self.statistics is not None and self.statistics.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.vc_peer_address.yfilter != YFilter.not_set or
                self.vc_id.yfilter != YFilter.not_set or
                self.vc_owner_type.yfilter != YFilter.not_set or
                self.vc_name.yfilter != YFilter.not_set or
                self.vc_index.yfilter != YFilter.not_set or
                self.vc_control_word.yfilter != YFilter.not_set or
                self.vc_inbound_label.yfilter != YFilter.not_set or
                self.vc_inbound_oper_status.yfilter != YFilter.not_set or
                self.vc_local_group_id.yfilter != YFilter.not_set or
                self.vc_local_if_mtu.yfilter != YFilter.not_set or
                self.vc_oper_status.yfilter != YFilter.not_set or
                self.vc_outbound_label.yfilter != YFilter.not_set or
                self.vc_outbound_oper_status.yfilter != YFilter.not_set or
                self.vc_owner_name.yfilter != YFilter.not_set or
                self.vc_psn_type.yfilter != YFilter.not_set or
                self.vc_remote_control_word.yfilter != YFilter.not_set or
                self.vc_remote_group_id.yfilter != YFilter.not_set or
                self.vc_remote_if_mtu.yfilter != YFilter.not_set or
                self.vc_type.yfilter != YFilter.not_set or
                (self.statistics is not None and self.statistics.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "pseudowires" + "[vc-peer-address='" + self.vc_peer_address.get() + "']" + "[vc-id='" + self.vc_id.get() + "']" + "[vc-owner-type='" + self.vc_owner_type.get() + "']" + "[vc-name='" + self.vc_name.get() + "']" + "[vc-index='" + self.vc_index.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-pw:pseudowire-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.vc_peer_address.is_set or self.vc_peer_address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_peer_address.get_name_leafdata())
            if (self.vc_id.is_set or self.vc_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_id.get_name_leafdata())
            if (self.vc_owner_type.is_set or self.vc_owner_type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_owner_type.get_name_leafdata())
            if (self.vc_name.is_set or self.vc_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_name.get_name_leafdata())
            if (self.vc_index.is_set or self.vc_index.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_index.get_name_leafdata())
            if (self.vc_control_word.is_set or self.vc_control_word.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_control_word.get_name_leafdata())
            if (self.vc_inbound_label.is_set or self.vc_inbound_label.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_inbound_label.get_name_leafdata())
            if (self.vc_inbound_oper_status.is_set or self.vc_inbound_oper_status.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_inbound_oper_status.get_name_leafdata())
            if (self.vc_local_group_id.is_set or self.vc_local_group_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_local_group_id.get_name_leafdata())
            if (self.vc_local_if_mtu.is_set or self.vc_local_if_mtu.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_local_if_mtu.get_name_leafdata())
            if (self.vc_oper_status.is_set or self.vc_oper_status.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_oper_status.get_name_leafdata())
            if (self.vc_outbound_label.is_set or self.vc_outbound_label.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_outbound_label.get_name_leafdata())
            if (self.vc_outbound_oper_status.is_set or self.vc_outbound_oper_status.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_outbound_oper_status.get_name_leafdata())
            if (self.vc_owner_name.is_set or self.vc_owner_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_owner_name.get_name_leafdata())
            if (self.vc_psn_type.is_set or self.vc_psn_type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_psn_type.get_name_leafdata())
            if (self.vc_remote_control_word.is_set or self.vc_remote_control_word.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_remote_control_word.get_name_leafdata())
            if (self.vc_remote_group_id.is_set or self.vc_remote_group_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_remote_group_id.get_name_leafdata())
            if (self.vc_remote_if_mtu.is_set or self.vc_remote_if_mtu.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_remote_if_mtu.get_name_leafdata())
            if (self.vc_type.is_set or self.vc_type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vc_type.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "statistics"):
                if (self.statistics is None):
                    self.statistics = PseudowireState.Pseudowires.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                return self.statistics

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "statistics" or name == "vc-peer-address" or name == "vc-id" or name == "vc-owner-type" or name == "vc-name" or name == "vc-index" or name == "vc-control-word" or name == "vc-inbound-label" or name == "vc-inbound-oper-status" or name == "vc-local-group-id" or name == "vc-local-if-mtu" or name == "vc-oper-status" or name == "vc-outbound-label" or name == "vc-outbound-oper-status" or name == "vc-owner-name" or name == "vc-psn-type" or name == "vc-remote-control-word" or name == "vc-remote-group-id" or name == "vc-remote-if-mtu" or name == "vc-type"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "vc-peer-address"):
                self.vc_peer_address = value
                self.vc_peer_address.value_namespace = name_space
                self.vc_peer_address.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-id"):
                self.vc_id = value
                self.vc_id.value_namespace = name_space
                self.vc_id.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-owner-type"):
                self.vc_owner_type = value
                self.vc_owner_type.value_namespace = name_space
                self.vc_owner_type.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-name"):
                self.vc_name = value
                self.vc_name.value_namespace = name_space
                self.vc_name.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-index"):
                self.vc_index = value
                self.vc_index.value_namespace = name_space
                self.vc_index.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-control-word"):
                self.vc_control_word = value
                self.vc_control_word.value_namespace = name_space
                self.vc_control_word.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-inbound-label"):
                self.vc_inbound_label = value
                self.vc_inbound_label.value_namespace = name_space
                self.vc_inbound_label.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-inbound-oper-status"):
                self.vc_inbound_oper_status = value
                self.vc_inbound_oper_status.value_namespace = name_space
                self.vc_inbound_oper_status.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-local-group-id"):
                self.vc_local_group_id = value
                self.vc_local_group_id.value_namespace = name_space
                self.vc_local_group_id.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-local-if-mtu"):
                self.vc_local_if_mtu = value
                self.vc_local_if_mtu.value_namespace = name_space
                self.vc_local_if_mtu.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-oper-status"):
                self.vc_oper_status = value
                self.vc_oper_status.value_namespace = name_space
                self.vc_oper_status.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-outbound-label"):
                self.vc_outbound_label = value
                self.vc_outbound_label.value_namespace = name_space
                self.vc_outbound_label.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-outbound-oper-status"):
                self.vc_outbound_oper_status = value
                self.vc_outbound_oper_status.value_namespace = name_space
                self.vc_outbound_oper_status.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-owner-name"):
                self.vc_owner_name = value
                self.vc_owner_name.value_namespace = name_space
                self.vc_owner_name.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-psn-type"):
                self.vc_psn_type = value
                self.vc_psn_type.value_namespace = name_space
                self.vc_psn_type.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-remote-control-word"):
                self.vc_remote_control_word = value
                self.vc_remote_control_word.value_namespace = name_space
                self.vc_remote_control_word.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-remote-group-id"):
                self.vc_remote_group_id = value
                self.vc_remote_group_id.value_namespace = name_space
                self.vc_remote_group_id.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-remote-if-mtu"):
                self.vc_remote_if_mtu = value
                self.vc_remote_if_mtu.value_namespace = name_space
                self.vc_remote_if_mtu.value_namespace_prefix = name_space_prefix
            if(value_path == "vc-type"):
                self.vc_type = value
                self.vc_type.value_namespace = name_space
                self.vc_type.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.pseudowires:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.pseudowires:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "cisco-pw:pseudowire-state" + path_buffer

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

        if (child_yang_name == "pseudowires"):
            for c in self.pseudowires:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = PseudowireState.Pseudowires()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.pseudowires.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "pseudowires"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = PseudowireState()
        return self._top_entity

class PwLbEthernetType(Identity):
    """
    Base type for load\-balancing with ethernet fields
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLbEthernetType, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-lb-ethernet-type")


class PwVcTypeVlanPassthrough(Identity):
    """
    Identity for VLAN passthrough VC type (XR)
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwVcTypeVlanPassthrough, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-vc-type-vlan-passthrough")


class PwVcTypeVlan(Identity):
    """
    Identity for VLAN VC type
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwVcTypeVlan, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-vc-type-vlan")


class PwSequencingBoth(Identity):
    """
    Receive and Transmit sequencing option for PW
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwSequencingBoth, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-sequencing-both")


class PwEncapMpls(Identity):
    """
    Use MPLS for PW encapsulation
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwEncapMpls, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-encap-mpls")


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


class PwSignalingProtocolNone(Identity):
    """
    No PW signaling protocol
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwSignalingProtocolNone, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-signaling-protocol-none")


class PwVcTypeEther(Identity):
    """
    Identity for Ethernet VC type
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwVcTypeEther, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-vc-type-ether")


class PwSequencingReceive(Identity):
    """
    Receive sequencing option for PW
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwSequencingReceive, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-sequencing-receive")


class PwSignalingProtocolBgp(Identity):
    """
    Use BGP for PW signaling protocol
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwSignalingProtocolBgp, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-signaling-protocol-bgp")


class PwSequencingTransmit(Identity):
    """
    Transmit sequencing option for PW
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwSequencingTransmit, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-sequencing-transmit")


class PwLbEthSrcMac(Identity):
    """
    Load\-balancing with ethernet source MAC field
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLbEthSrcMac, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-lb-eth-src-mac")


class PwLbIpDstIp(Identity):
    """
    Load\-balancing with IP destination IP field
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLbIpDstIp, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-lb-ip-dst-ip")


class PwLbIpSrcIp(Identity):
    """
    Load\-balancing with IP source IP field
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLbIpSrcIp, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-lb-ip-src-ip")


class PwLbEthDstMac(Identity):
    """
    Load\-balancing with ethernet destination MAC field
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLbEthDstMac, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-lb-eth-dst-mac")


class PwSignalingProtocolLdp(Identity):
    """
    Use MPLS LDP for PW signaling protocol
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwSignalingProtocolLdp, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-signaling-protocol-ldp")


class PwLbIpSrcDstIp(Identity):
    """
    Load\-balancing with IP source and destination IP fields
    
    

    """

    _prefix = 'l2vpn-pw'
    _revision = '2016-12-07'

    def __init__(self):
        super(PwLbIpSrcDstIp, self).__init__("urn:cisco:params:xml:ns:yang:pw", "cisco-pw", "cisco-pw:pw-lb-ip-src-dst-ip")



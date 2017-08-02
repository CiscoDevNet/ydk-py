""" ietf_diffserv_classifier 

This module contains a collection of YANG definitions for
configuring diffserv specification implementations.

Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC XXXX; see
the RFC itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FilterType(Identity):
    """
     This is identity of base filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(FilterType, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:filter-type")


class ClassifierEntryFilterOperationType(Identity):
    """
    Classifier entry filter logical operation
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(ClassifierEntryFilterOperationType, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:classifier-entry-filter-operation-type")


class Classifiers(Entity):
    """
    list of classifier entry
    
    .. attribute:: classifier_entry
    
    	classifier entry template
    	**type**\: list of    :py:class:`ClassifierEntry <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry>`
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(Classifiers, self).__init__()
        self._top_entity = None

        self.yang_name = "classifiers"
        self.yang_parent_name = "ietf-diffserv-classifier"

        self.classifier_entry = YList(self)

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
                    super(Classifiers, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Classifiers, self).__setattr__(name, value)


    class ClassifierEntry(Entity):
        """
        classifier entry template
        
        .. attribute:: classifier_entry_name  <key>
        
        	Diffserv classifier name
        	**type**\:  str
        
        .. attribute:: classifier_entry_descr
        
        	Description of the class template
        	**type**\:  str
        
        .. attribute:: classifier_entry_filter_operation
        
        	Filters are applicable as any or all filters
        	**type**\:   :py:class:`ClassifierEntryFilterOperationType <ydk.models.ietf.ietf_diffserv_classifier.ClassifierEntryFilterOperationType>`
        
        	**default value**\: match-any-filter
        
        .. attribute:: classifier_entry_type
        
        	Type of the class\-map
        	**type**\:   :py:class:`ClassType <ydk.models.cisco_ios_xe.policy_types.ClassType>`
        
        .. attribute:: filter_entry
        
        	Filter configuration
        	**type**\: list of    :py:class:`FilterEntry <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry>`
        
        

        """

        _prefix = 'classifier'
        _revision = '2015-04-07'

        def __init__(self):
            super(Classifiers.ClassifierEntry, self).__init__()

            self.yang_name = "classifier-entry"
            self.yang_parent_name = "classifiers"

            self.classifier_entry_name = YLeaf(YType.str, "classifier-entry-name")

            self.classifier_entry_descr = YLeaf(YType.str, "classifier-entry-descr")

            self.classifier_entry_filter_operation = YLeaf(YType.identityref, "classifier-entry-filter-operation")

            self.classifier_entry_type = YLeaf(YType.identityref, "cisco-policy-filters:classifier-entry-type")

            self.filter_entry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("classifier_entry_name",
                            "classifier_entry_descr",
                            "classifier_entry_filter_operation",
                            "classifier_entry_type") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Classifiers.ClassifierEntry, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Classifiers.ClassifierEntry, self).__setattr__(name, value)


        class FilterEntry(Entity):
            """
            Filter configuration
            
            .. attribute:: filter_type  <key>
            
            	This leaf defines type of the filter
            	**type**\:   :py:class:`FilterType <ydk.models.ietf.ietf_diffserv_classifier.FilterType>`
            
            .. attribute:: filter_logical_not  <key>
            
            	 This is logical\-not operator for a filter. When true, it  indicates filter looks for absence of a pattern defined  by the filter 
            	**type**\:  bool
            
            .. attribute:: application_cfgs
            
            	Match Type Application
            	**type**\:   :py:class:`ApplicationCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.ApplicationCfgs>`
            
            .. attribute:: atm_clp_cfg
            
            	Match ATM Cell Loss Priority (CLP)
            	**type**\:   :py:class:`AtmClpCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.AtmClpCfg>`
            
            .. attribute:: atm_vci_cfgs
            
            	Match ATM Virtual Channel Identifier  (VCI)
            	**type**\:   :py:class:`AtmVciCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.AtmVciCfgs>`
            
            .. attribute:: class_map_cfgs
            
            	Match Type cls\-map Name
            	**type**\:   :py:class:`ClassMapCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.ClassMapCfgs>`
            
            .. attribute:: cos_cfgs
            
            	
            	**type**\:   :py:class:`CosCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.CosCfgs>`
            
            .. attribute:: cos_inner_cfgs
            
            	Match Type COS\-INNER
            	**type**\:   :py:class:`CosInnerCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.CosInnerCfgs>`
            
            .. attribute:: dei_cfg
            
            	Match Type DEI Bit configuration
            	**type**\:   :py:class:`DeiCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.DeiCfg>`
            
            .. attribute:: dei_inner_cfg
            
            	Match Type Inner DEI Bit
            	**type**\:   :py:class:`DeiInnerCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.DeiInnerCfg>`
            
            .. attribute:: destination_ip_address_cfg
            
            	list of destination ip address
            	**type**\: list of    :py:class:`DestinationIpAddressCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg>`
            
            .. attribute:: destination_port_cfg
            
            	list of ranges of destination port
            	**type**\: list of    :py:class:`DestinationPortCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg>`
            
            .. attribute:: discard_class_cfgs
            
            	Match Type Discard Class
            	**type**\:   :py:class:`DiscardClassCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.DiscardClassCfgs>`
            
            .. attribute:: dscp_cfg
            
            	list of dscp ranges
            	**type**\: list of    :py:class:`DscpCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.DscpCfg>`
            
            .. attribute:: dst_mac_cfgs
            
            	Match Type Destination MAC Address
            	**type**\:   :py:class:`DstMacCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.DstMacCfgs>`
            
            .. attribute:: flow_ip_cfg
            
            	Match Type flow
            	**type**\:   :py:class:`FlowIpCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.FlowIpCfg>`
            
            .. attribute:: flow_record_cfg
            
            	Match Type flow Record Name
            	**type**\:   :py:class:`FlowRecordCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.FlowRecordCfg>`
            
            .. attribute:: fr_de_cfg
            
            	Match Frame Relay DE
            	**type**\:   :py:class:`FrDeCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.FrDeCfg>`
            
            .. attribute:: fr_dlci_cfgs
            
            	Match Frame Relay DLCI
            	**type**\:   :py:class:`FrDlciCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.FrDlciCfgs>`
            
            .. attribute:: input_interface_cfgs
            
            	Match type Input interface
            	**type**\:   :py:class:`InputInterfaceCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.InputInterfaceCfgs>`
            
            .. attribute:: ip_rtp_cfgs
            
            	Match Type IP RTP
            	**type**\:   :py:class:`IpRtpCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.IpRtpCfgs>`
            
            .. attribute:: ipv4_acl_cfgs
            
            	Match IPv4 Access\-list number
            	**type**\:   :py:class:`Ipv4AclCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.Ipv4AclCfgs>`
            
            .. attribute:: ipv4_acl_name_cfgs
            
            	Match IPv4 Access\-list name
            	**type**\:   :py:class:`Ipv4AclNameCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.Ipv4AclNameCfgs>`
            
            .. attribute:: ipv6_acl_cfgs
            
            	Match IPv6 Access\-list number
            	**type**\:   :py:class:`Ipv6AclCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.Ipv6AclCfgs>`
            
            .. attribute:: ipv6_acl_name_cfgs
            
            	Match IPv6 Access\-list name
            	**type**\:   :py:class:`Ipv6AclNameCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.Ipv6AclNameCfgs>`
            
            .. attribute:: metadata_cfg
            
            	Match Type Metadata
            	**type**\:   :py:class:`MetadataCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.MetadataCfg>`
            
            .. attribute:: mpls_exp_imp_cfgs
            
            	Match MPLS experimental Imposition
            	**type**\:   :py:class:`MplsExpImpCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.MplsExpImpCfgs>`
            
            .. attribute:: mpls_exp_top_cfgs
            
            	Match MPLS experimental Topmost
            	**type**\:   :py:class:`MplsExpTopCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.MplsExpTopCfgs>`
            
            .. attribute:: pkt_len_cfgs
            
            	Match Type Packet Length
            	**type**\:   :py:class:`PktLenCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.PktLenCfgs>`
            
            .. attribute:: prec
            
            	Match Type Precedence in  IPv4 and IPv6 packets
            	**type**\:   :py:class:`Prec <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.Prec>`
            
            .. attribute:: protocol_cfg
            
            	list of ranges of protocol values
            	**type**\: list of    :py:class:`ProtocolCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg>`
            
            .. attribute:: protocol_name_cfgs
            
            	Match Type name\-based protocol
            	**type**\:   :py:class:`ProtocolNameCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.ProtocolNameCfgs>`
            
            .. attribute:: qos_group_cfgs
            
            	Match Type QoS Group
            	**type**\:   :py:class:`QosGroupCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.QosGroupCfgs>`
            
            .. attribute:: security_group
            
            	Match Type security tag
            	**type**\:   :py:class:`SecurityGroup <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.SecurityGroup>`
            
            .. attribute:: source_ip_address_cfg
            
            	list of source ip address
            	**type**\: list of    :py:class:`SourceIpAddressCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg>`
            
            .. attribute:: source_port_cfg
            
            	list of ranges of source port
            	**type**\: list of    :py:class:`SourcePortCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg>`
            
            .. attribute:: src_mac_cfgs
            
            	Match Type Source MAC Address
            	**type**\:   :py:class:`SrcMacCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.SrcMacCfgs>`
            
            .. attribute:: vlan_cfgs
            
            	Match Type VLAN
            	**type**\:   :py:class:`VlanCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.VlanCfgs>`
            
            .. attribute:: vlan_inner_cfgs
            
            	Match Type Inner VLAN
            	**type**\:   :py:class:`VlanInnerCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.VlanInnerCfgs>`
            
            .. attribute:: vpls_cfg
            
            	Match Type VPLS
            	**type**\:   :py:class:`VplsCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.VplsCfg>`
            
            .. attribute:: wlan_user_priority_cfgs
            
            	Match Type Wlan User Priority
            	**type**\:   :py:class:`WlanUserPriorityCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.WlanUserPriorityCfgs>`
            
            

            """

            _prefix = 'classifier'
            _revision = '2015-04-07'

            def __init__(self):
                super(Classifiers.ClassifierEntry.FilterEntry, self).__init__()

                self.yang_name = "filter-entry"
                self.yang_parent_name = "classifier-entry"

                self.filter_type = YLeaf(YType.identityref, "filter-type")

                self.filter_logical_not = YLeaf(YType.boolean, "filter-logical-not")

                self.application_cfgs = Classifiers.ClassifierEntry.FilterEntry.ApplicationCfgs()
                self.application_cfgs.parent = self
                self._children_name_map["application_cfgs"] = "application-cfgs"
                self._children_yang_names.add("application-cfgs")

                self.atm_clp_cfg = Classifiers.ClassifierEntry.FilterEntry.AtmClpCfg()
                self.atm_clp_cfg.parent = self
                self._children_name_map["atm_clp_cfg"] = "atm-clp-cfg"
                self._children_yang_names.add("atm-clp-cfg")

                self.atm_vci_cfgs = Classifiers.ClassifierEntry.FilterEntry.AtmVciCfgs()
                self.atm_vci_cfgs.parent = self
                self._children_name_map["atm_vci_cfgs"] = "atm-vci-cfgs"
                self._children_yang_names.add("atm-vci-cfgs")

                self.class_map_cfgs = Classifiers.ClassifierEntry.FilterEntry.ClassMapCfgs()
                self.class_map_cfgs.parent = self
                self._children_name_map["class_map_cfgs"] = "class-map-cfgs"
                self._children_yang_names.add("class-map-cfgs")

                self.cos_cfgs = Classifiers.ClassifierEntry.FilterEntry.CosCfgs()
                self.cos_cfgs.parent = self
                self._children_name_map["cos_cfgs"] = "cos-cfgs"
                self._children_yang_names.add("cos-cfgs")

                self.cos_inner_cfgs = Classifiers.ClassifierEntry.FilterEntry.CosInnerCfgs()
                self.cos_inner_cfgs.parent = self
                self._children_name_map["cos_inner_cfgs"] = "cos-inner-cfgs"
                self._children_yang_names.add("cos-inner-cfgs")

                self.dei_cfg = Classifiers.ClassifierEntry.FilterEntry.DeiCfg()
                self.dei_cfg.parent = self
                self._children_name_map["dei_cfg"] = "dei-cfg"
                self._children_yang_names.add("dei-cfg")

                self.dei_inner_cfg = Classifiers.ClassifierEntry.FilterEntry.DeiInnerCfg()
                self.dei_inner_cfg.parent = self
                self._children_name_map["dei_inner_cfg"] = "dei-inner-cfg"
                self._children_yang_names.add("dei-inner-cfg")

                self.discard_class_cfgs = Classifiers.ClassifierEntry.FilterEntry.DiscardClassCfgs()
                self.discard_class_cfgs.parent = self
                self._children_name_map["discard_class_cfgs"] = "discard-class-cfgs"
                self._children_yang_names.add("discard-class-cfgs")

                self.dst_mac_cfgs = Classifiers.ClassifierEntry.FilterEntry.DstMacCfgs()
                self.dst_mac_cfgs.parent = self
                self._children_name_map["dst_mac_cfgs"] = "dst-mac-cfgs"
                self._children_yang_names.add("dst-mac-cfgs")

                self.flow_ip_cfg = Classifiers.ClassifierEntry.FilterEntry.FlowIpCfg()
                self.flow_ip_cfg.parent = self
                self._children_name_map["flow_ip_cfg"] = "flow-ip-cfg"
                self._children_yang_names.add("flow-ip-cfg")

                self.flow_record_cfg = Classifiers.ClassifierEntry.FilterEntry.FlowRecordCfg()
                self.flow_record_cfg.parent = self
                self._children_name_map["flow_record_cfg"] = "flow-record-cfg"
                self._children_yang_names.add("flow-record-cfg")

                self.fr_de_cfg = Classifiers.ClassifierEntry.FilterEntry.FrDeCfg()
                self.fr_de_cfg.parent = self
                self._children_name_map["fr_de_cfg"] = "fr-de-cfg"
                self._children_yang_names.add("fr-de-cfg")

                self.fr_dlci_cfgs = Classifiers.ClassifierEntry.FilterEntry.FrDlciCfgs()
                self.fr_dlci_cfgs.parent = self
                self._children_name_map["fr_dlci_cfgs"] = "fr-dlci-cfgs"
                self._children_yang_names.add("fr-dlci-cfgs")

                self.input_interface_cfgs = Classifiers.ClassifierEntry.FilterEntry.InputInterfaceCfgs()
                self.input_interface_cfgs.parent = self
                self._children_name_map["input_interface_cfgs"] = "input-interface-cfgs"
                self._children_yang_names.add("input-interface-cfgs")

                self.ip_rtp_cfgs = Classifiers.ClassifierEntry.FilterEntry.IpRtpCfgs()
                self.ip_rtp_cfgs.parent = self
                self._children_name_map["ip_rtp_cfgs"] = "ip-rtp-cfgs"
                self._children_yang_names.add("ip-rtp-cfgs")

                self.ipv4_acl_cfgs = Classifiers.ClassifierEntry.FilterEntry.Ipv4AclCfgs()
                self.ipv4_acl_cfgs.parent = self
                self._children_name_map["ipv4_acl_cfgs"] = "ipv4-acl-cfgs"
                self._children_yang_names.add("ipv4-acl-cfgs")

                self.ipv4_acl_name_cfgs = Classifiers.ClassifierEntry.FilterEntry.Ipv4AclNameCfgs()
                self.ipv4_acl_name_cfgs.parent = self
                self._children_name_map["ipv4_acl_name_cfgs"] = "ipv4-acl-name-cfgs"
                self._children_yang_names.add("ipv4-acl-name-cfgs")

                self.ipv6_acl_cfgs = Classifiers.ClassifierEntry.FilterEntry.Ipv6AclCfgs()
                self.ipv6_acl_cfgs.parent = self
                self._children_name_map["ipv6_acl_cfgs"] = "ipv6-acl-cfgs"
                self._children_yang_names.add("ipv6-acl-cfgs")

                self.ipv6_acl_name_cfgs = Classifiers.ClassifierEntry.FilterEntry.Ipv6AclNameCfgs()
                self.ipv6_acl_name_cfgs.parent = self
                self._children_name_map["ipv6_acl_name_cfgs"] = "ipv6-acl-name-cfgs"
                self._children_yang_names.add("ipv6-acl-name-cfgs")

                self.metadata_cfg = Classifiers.ClassifierEntry.FilterEntry.MetadataCfg()
                self.metadata_cfg.parent = self
                self._children_name_map["metadata_cfg"] = "metadata-cfg"
                self._children_yang_names.add("metadata-cfg")

                self.mpls_exp_imp_cfgs = Classifiers.ClassifierEntry.FilterEntry.MplsExpImpCfgs()
                self.mpls_exp_imp_cfgs.parent = self
                self._children_name_map["mpls_exp_imp_cfgs"] = "mpls-exp-imp-cfgs"
                self._children_yang_names.add("mpls-exp-imp-cfgs")

                self.mpls_exp_top_cfgs = Classifiers.ClassifierEntry.FilterEntry.MplsExpTopCfgs()
                self.mpls_exp_top_cfgs.parent = self
                self._children_name_map["mpls_exp_top_cfgs"] = "mpls-exp-top-cfgs"
                self._children_yang_names.add("mpls-exp-top-cfgs")

                self.pkt_len_cfgs = Classifiers.ClassifierEntry.FilterEntry.PktLenCfgs()
                self.pkt_len_cfgs.parent = self
                self._children_name_map["pkt_len_cfgs"] = "pkt-len-cfgs"
                self._children_yang_names.add("pkt-len-cfgs")

                self.prec = Classifiers.ClassifierEntry.FilterEntry.Prec()
                self.prec.parent = self
                self._children_name_map["prec"] = "prec"
                self._children_yang_names.add("prec")

                self.protocol_name_cfgs = Classifiers.ClassifierEntry.FilterEntry.ProtocolNameCfgs()
                self.protocol_name_cfgs.parent = self
                self._children_name_map["protocol_name_cfgs"] = "protocol-name-cfgs"
                self._children_yang_names.add("protocol-name-cfgs")

                self.qos_group_cfgs = Classifiers.ClassifierEntry.FilterEntry.QosGroupCfgs()
                self.qos_group_cfgs.parent = self
                self._children_name_map["qos_group_cfgs"] = "qos-group-cfgs"
                self._children_yang_names.add("qos-group-cfgs")

                self.security_group = Classifiers.ClassifierEntry.FilterEntry.SecurityGroup()
                self.security_group.parent = self
                self._children_name_map["security_group"] = "security-group"
                self._children_yang_names.add("security-group")

                self.src_mac_cfgs = Classifiers.ClassifierEntry.FilterEntry.SrcMacCfgs()
                self.src_mac_cfgs.parent = self
                self._children_name_map["src_mac_cfgs"] = "src-mac-cfgs"
                self._children_yang_names.add("src-mac-cfgs")

                self.vlan_cfgs = Classifiers.ClassifierEntry.FilterEntry.VlanCfgs()
                self.vlan_cfgs.parent = self
                self._children_name_map["vlan_cfgs"] = "vlan-cfgs"
                self._children_yang_names.add("vlan-cfgs")

                self.vlan_inner_cfgs = Classifiers.ClassifierEntry.FilterEntry.VlanInnerCfgs()
                self.vlan_inner_cfgs.parent = self
                self._children_name_map["vlan_inner_cfgs"] = "vlan-inner-cfgs"
                self._children_yang_names.add("vlan-inner-cfgs")

                self.vpls_cfg = Classifiers.ClassifierEntry.FilterEntry.VplsCfg()
                self.vpls_cfg.parent = self
                self._children_name_map["vpls_cfg"] = "vpls-cfg"
                self._children_yang_names.add("vpls-cfg")

                self.wlan_user_priority_cfgs = Classifiers.ClassifierEntry.FilterEntry.WlanUserPriorityCfgs()
                self.wlan_user_priority_cfgs.parent = self
                self._children_name_map["wlan_user_priority_cfgs"] = "wlan-user-priority-cfgs"
                self._children_yang_names.add("wlan-user-priority-cfgs")

                self.destination_ip_address_cfg = YList(self)
                self.destination_port_cfg = YList(self)
                self.dscp_cfg = YList(self)
                self.protocol_cfg = YList(self)
                self.source_ip_address_cfg = YList(self)
                self.source_port_cfg = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("filter_type",
                                "filter_logical_not") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Classifiers.ClassifierEntry.FilterEntry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Classifiers.ClassifierEntry.FilterEntry, self).__setattr__(name, value)


            class DscpCfg(Entity):
                """
                list of dscp ranges
                
                .. attribute:: dscp_min  <key>
                
                	Minimum value of dscp range
                	**type**\:  int
                
                	**range:** 0..63
                
                .. attribute:: dscp_max  <key>
                
                	maximum value of dscp range
                	**type**\:  int
                
                	**range:** 0..63
                
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.DscpCfg, self).__init__()

                    self.yang_name = "dscp-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.dscp_min = YLeaf(YType.uint8, "dscp-min")

                    self.dscp_max = YLeaf(YType.uint8, "dscp-max")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("dscp_min",
                                    "dscp_max") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.DscpCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.DscpCfg, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.dscp_min.is_set or
                        self.dscp_max.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.dscp_min.yfilter != YFilter.not_set or
                        self.dscp_max.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "dscp-cfg" + "[dscp-min='" + self.dscp_min.get() + "']" + "[dscp-max='" + self.dscp_max.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.dscp_min.is_set or self.dscp_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dscp_min.get_name_leafdata())
                    if (self.dscp_max.is_set or self.dscp_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dscp_max.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "dscp-min" or name == "dscp-max"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "dscp-min"):
                        self.dscp_min = value
                        self.dscp_min.value_namespace = name_space
                        self.dscp_min.value_namespace_prefix = name_space_prefix
                    if(value_path == "dscp-max"):
                        self.dscp_max = value
                        self.dscp_max.value_namespace = name_space
                        self.dscp_max.value_namespace_prefix = name_space_prefix


            class SourceIpAddressCfg(Entity):
                """
                list of source ip address
                
                .. attribute:: source_ip_addr  <key>
                
                	source ip prefix
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                
                ----
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg, self).__init__()

                    self.yang_name = "source-ip-address-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.source_ip_addr = YLeaf(YType.str, "source-ip-addr")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("source_ip_addr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg, self).__setattr__(name, value)

                def has_data(self):
                    return self.source_ip_addr.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.source_ip_addr.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "source-ip-address-cfg" + "[source-ip-addr='" + self.source_ip_addr.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.source_ip_addr.is_set or self.source_ip_addr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_ip_addr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "source-ip-addr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "source-ip-addr"):
                        self.source_ip_addr = value
                        self.source_ip_addr.value_namespace = name_space
                        self.source_ip_addr.value_namespace_prefix = name_space_prefix


            class DestinationIpAddressCfg(Entity):
                """
                list of destination ip address
                
                .. attribute:: destination_ip_addr  <key>
                
                	destination ip prefix
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                
                ----
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg, self).__init__()

                    self.yang_name = "destination-ip-address-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.destination_ip_addr = YLeaf(YType.str, "destination-ip-addr")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("destination_ip_addr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg, self).__setattr__(name, value)

                def has_data(self):
                    return self.destination_ip_addr.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.destination_ip_addr.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "destination-ip-address-cfg" + "[destination-ip-addr='" + self.destination_ip_addr.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.destination_ip_addr.is_set or self.destination_ip_addr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_ip_addr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "destination-ip-addr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "destination-ip-addr"):
                        self.destination_ip_addr = value
                        self.destination_ip_addr.value_namespace = name_space
                        self.destination_ip_addr.value_namespace_prefix = name_space_prefix


            class SourcePortCfg(Entity):
                """
                list of ranges of source port
                
                .. attribute:: source_port_min  <key>
                
                	minimum value of source port range
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: source_port_max  <key>
                
                	maximum value of source port range
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg, self).__init__()

                    self.yang_name = "source-port-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.source_port_min = YLeaf(YType.uint16, "source-port-min")

                    self.source_port_max = YLeaf(YType.uint16, "source-port-max")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("source_port_min",
                                    "source_port_max") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.source_port_min.is_set or
                        self.source_port_max.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.source_port_min.yfilter != YFilter.not_set or
                        self.source_port_max.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "source-port-cfg" + "[source-port-min='" + self.source_port_min.get() + "']" + "[source-port-max='" + self.source_port_max.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.source_port_min.is_set or self.source_port_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_port_min.get_name_leafdata())
                    if (self.source_port_max.is_set or self.source_port_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_port_max.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "source-port-min" or name == "source-port-max"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "source-port-min"):
                        self.source_port_min = value
                        self.source_port_min.value_namespace = name_space
                        self.source_port_min.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-port-max"):
                        self.source_port_max = value
                        self.source_port_max.value_namespace = name_space
                        self.source_port_max.value_namespace_prefix = name_space_prefix


            class DestinationPortCfg(Entity):
                """
                list of ranges of destination port
                
                .. attribute:: destination_port_min  <key>
                
                	minimum value of destination port range
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: destination_port_max  <key>
                
                	maximum value of destination port range
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg, self).__init__()

                    self.yang_name = "destination-port-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.destination_port_min = YLeaf(YType.uint16, "destination-port-min")

                    self.destination_port_max = YLeaf(YType.uint16, "destination-port-max")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("destination_port_min",
                                    "destination_port_max") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.destination_port_min.is_set or
                        self.destination_port_max.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.destination_port_min.yfilter != YFilter.not_set or
                        self.destination_port_max.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "destination-port-cfg" + "[destination-port-min='" + self.destination_port_min.get() + "']" + "[destination-port-max='" + self.destination_port_max.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.destination_port_min.is_set or self.destination_port_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_port_min.get_name_leafdata())
                    if (self.destination_port_max.is_set or self.destination_port_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_port_max.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "destination-port-min" or name == "destination-port-max"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "destination-port-min"):
                        self.destination_port_min = value
                        self.destination_port_min.value_namespace = name_space
                        self.destination_port_min.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-port-max"):
                        self.destination_port_max = value
                        self.destination_port_max.value_namespace = name_space
                        self.destination_port_max.value_namespace_prefix = name_space_prefix


            class ProtocolCfg(Entity):
                """
                list of ranges of protocol values
                
                .. attribute:: protocol_min  <key>
                
                	minimum value of protocol range
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: protocol_max  <key>
                
                	maximum value of protocol range
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg, self).__init__()

                    self.yang_name = "protocol-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.protocol_min = YLeaf(YType.uint8, "protocol-min")

                    self.protocol_max = YLeaf(YType.uint8, "protocol-max")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("protocol_min",
                                    "protocol_max") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.protocol_min.is_set or
                        self.protocol_max.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.protocol_min.yfilter != YFilter.not_set or
                        self.protocol_max.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "protocol-cfg" + "[protocol-min='" + self.protocol_min.get() + "']" + "[protocol-max='" + self.protocol_max.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.protocol_min.is_set or self.protocol_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.protocol_min.get_name_leafdata())
                    if (self.protocol_max.is_set or self.protocol_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.protocol_max.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "protocol-min" or name == "protocol-max"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "protocol-min"):
                        self.protocol_min = value
                        self.protocol_min.value_namespace = name_space
                        self.protocol_min.value_namespace_prefix = name_space_prefix
                    if(value_path == "protocol-max"):
                        self.protocol_max = value
                        self.protocol_max.value_namespace = name_space
                        self.protocol_max.value_namespace_prefix = name_space_prefix


            class CosCfgs(Entity):
                """
                
                
                .. attribute:: cos_cfg
                
                	Match Type COS configuration
                	**type**\: list of    :py:class:`CosCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.CosCfgs.CosCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.CosCfgs, self).__init__()

                    self.yang_name = "cos-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.cos_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.CosCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.CosCfgs, self).__setattr__(name, value)


                class CosCfg(Entity):
                    """
                    Match Type COS configuration
                    
                    .. attribute:: cos_min  <key>
                    
                    	min cos value 
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: cos_max  <key>
                    
                    	min cos value 
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.CosCfgs.CosCfg, self).__init__()

                        self.yang_name = "cos-cfg"
                        self.yang_parent_name = "cos-cfgs"

                        self.cos_min = YLeaf(YType.uint8, "cos-min")

                        self.cos_max = YLeaf(YType.uint8, "cos-max")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("cos_min",
                                        "cos_max") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.CosCfgs.CosCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.CosCfgs.CosCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.cos_min.is_set or
                            self.cos_max.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.cos_min.yfilter != YFilter.not_set or
                            self.cos_max.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "cos-cfg" + "[cos-min='" + self.cos_min.get() + "']" + "[cos-max='" + self.cos_max.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.cos_min.is_set or self.cos_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cos_min.get_name_leafdata())
                        if (self.cos_max.is_set or self.cos_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cos_max.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "cos-min" or name == "cos-max"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "cos-min"):
                            self.cos_min = value
                            self.cos_min.value_namespace = name_space
                            self.cos_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "cos-max"):
                            self.cos_max = value
                            self.cos_max.value_namespace = name_space
                            self.cos_max.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.cos_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.cos_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:cos-cfgs" + path_buffer

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

                    if (child_yang_name == "cos-cfg"):
                        for c in self.cos_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.CosCfgs.CosCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.cos_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "cos-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class CosInnerCfgs(Entity):
                """
                Match Type COS\-INNER
                
                .. attribute:: cos_inner_cfg
                
                	Match Type COS\-INNER configuration
                	**type**\: list of    :py:class:`CosInnerCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.CosInnerCfgs.CosInnerCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.CosInnerCfgs, self).__init__()

                    self.yang_name = "cos-inner-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.cos_inner_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.CosInnerCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.CosInnerCfgs, self).__setattr__(name, value)


                class CosInnerCfg(Entity):
                    """
                    Match Type COS\-INNER configuration
                    
                    .. attribute:: cos_min  <key>
                    
                    	min cos value 
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: cos_max  <key>
                    
                    	min cos value 
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.CosInnerCfgs.CosInnerCfg, self).__init__()

                        self.yang_name = "cos-inner-cfg"
                        self.yang_parent_name = "cos-inner-cfgs"

                        self.cos_min = YLeaf(YType.uint8, "cos-min")

                        self.cos_max = YLeaf(YType.uint8, "cos-max")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("cos_min",
                                        "cos_max") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.CosInnerCfgs.CosInnerCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.CosInnerCfgs.CosInnerCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.cos_min.is_set or
                            self.cos_max.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.cos_min.yfilter != YFilter.not_set or
                            self.cos_max.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "cos-inner-cfg" + "[cos-min='" + self.cos_min.get() + "']" + "[cos-max='" + self.cos_max.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.cos_min.is_set or self.cos_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cos_min.get_name_leafdata())
                        if (self.cos_max.is_set or self.cos_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cos_max.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "cos-min" or name == "cos-max"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "cos-min"):
                            self.cos_min = value
                            self.cos_min.value_namespace = name_space
                            self.cos_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "cos-max"):
                            self.cos_max = value
                            self.cos_max.value_namespace = name_space
                            self.cos_max.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.cos_inner_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.cos_inner_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:cos-inner-cfgs" + path_buffer

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

                    if (child_yang_name == "cos-inner-cfg"):
                        for c in self.cos_inner_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.CosInnerCfgs.CosInnerCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.cos_inner_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "cos-inner-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Ipv4AclNameCfgs(Entity):
                """
                Match IPv4 Access\-list name
                
                .. attribute:: ipv4_acl_name_cfg
                
                	Match IPv4 Access\-list name configuration
                	**type**\: list of    :py:class:`Ipv4AclNameCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.Ipv4AclNameCfgs.Ipv4AclNameCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.Ipv4AclNameCfgs, self).__init__()

                    self.yang_name = "ipv4-acl-name-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.ipv4_acl_name_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.Ipv4AclNameCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.Ipv4AclNameCfgs, self).__setattr__(name, value)


                class Ipv4AclNameCfg(Entity):
                    """
                    Match IPv4 Access\-list name
                    configuration
                    
                    .. attribute:: ip_acl_name  <key>
                    
                    	IP ACL name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.Ipv4AclNameCfgs.Ipv4AclNameCfg, self).__init__()

                        self.yang_name = "ipv4-acl-name-cfg"
                        self.yang_parent_name = "ipv4-acl-name-cfgs"

                        self.ip_acl_name = YLeaf(YType.str, "ip-acl-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ip_acl_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.Ipv4AclNameCfgs.Ipv4AclNameCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.Ipv4AclNameCfgs.Ipv4AclNameCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return self.ip_acl_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ip_acl_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv4-acl-name-cfg" + "[ip-acl-name='" + self.ip_acl_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ip_acl_name.is_set or self.ip_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_acl_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ip-acl-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ip-acl-name"):
                            self.ip_acl_name = value
                            self.ip_acl_name.value_namespace = name_space
                            self.ip_acl_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ipv4_acl_name_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ipv4_acl_name_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:ipv4-acl-name-cfgs" + path_buffer

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

                    if (child_yang_name == "ipv4-acl-name-cfg"):
                        for c in self.ipv4_acl_name_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.Ipv4AclNameCfgs.Ipv4AclNameCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ipv4_acl_name_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv4-acl-name-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Ipv6AclNameCfgs(Entity):
                """
                Match IPv6 Access\-list name
                
                .. attribute:: ipv6_acl_name_cfg
                
                	Match IPv6 Access\-list name configuration
                	**type**\: list of    :py:class:`Ipv6AclNameCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.Ipv6AclNameCfgs.Ipv6AclNameCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.Ipv6AclNameCfgs, self).__init__()

                    self.yang_name = "ipv6-acl-name-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.ipv6_acl_name_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.Ipv6AclNameCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.Ipv6AclNameCfgs, self).__setattr__(name, value)


                class Ipv6AclNameCfg(Entity):
                    """
                    Match IPv6 Access\-list name
                    configuration
                    
                    .. attribute:: ip_acl_name  <key>
                    
                    	IP ACL name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.Ipv6AclNameCfgs.Ipv6AclNameCfg, self).__init__()

                        self.yang_name = "ipv6-acl-name-cfg"
                        self.yang_parent_name = "ipv6-acl-name-cfgs"

                        self.ip_acl_name = YLeaf(YType.str, "ip-acl-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ip_acl_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.Ipv6AclNameCfgs.Ipv6AclNameCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.Ipv6AclNameCfgs.Ipv6AclNameCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return self.ip_acl_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ip_acl_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv6-acl-name-cfg" + "[ip-acl-name='" + self.ip_acl_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ip_acl_name.is_set or self.ip_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_acl_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ip-acl-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ip-acl-name"):
                            self.ip_acl_name = value
                            self.ip_acl_name.value_namespace = name_space
                            self.ip_acl_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ipv6_acl_name_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ipv6_acl_name_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:ipv6-acl-name-cfgs" + path_buffer

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

                    if (child_yang_name == "ipv6-acl-name-cfg"):
                        for c in self.ipv6_acl_name_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.Ipv6AclNameCfgs.Ipv6AclNameCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ipv6_acl_name_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv6-acl-name-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Ipv4AclCfgs(Entity):
                """
                Match IPv4 Access\-list number
                
                .. attribute:: ipv4_acl_cfg
                
                	Match IPv4 Access\-list number configuration
                	**type**\: list of    :py:class:`Ipv4AclCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.Ipv4AclCfgs.Ipv4AclCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.Ipv4AclCfgs, self).__init__()

                    self.yang_name = "ipv4-acl-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.ipv4_acl_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.Ipv4AclCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.Ipv4AclCfgs, self).__setattr__(name, value)


                class Ipv4AclCfg(Entity):
                    """
                    Match IPv4 Access\-list number
                    configuration
                    
                    .. attribute:: ip_acl  <key>
                    
                    	IP ACL number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.Ipv4AclCfgs.Ipv4AclCfg, self).__init__()

                        self.yang_name = "ipv4-acl-cfg"
                        self.yang_parent_name = "ipv4-acl-cfgs"

                        self.ip_acl = YLeaf(YType.uint32, "ip-acl")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ip_acl") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.Ipv4AclCfgs.Ipv4AclCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.Ipv4AclCfgs.Ipv4AclCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return self.ip_acl.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ip_acl.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv4-acl-cfg" + "[ip-acl='" + self.ip_acl.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ip_acl.is_set or self.ip_acl.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_acl.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ip-acl"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ip-acl"):
                            self.ip_acl = value
                            self.ip_acl.value_namespace = name_space
                            self.ip_acl.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ipv4_acl_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ipv4_acl_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:ipv4-acl-cfgs" + path_buffer

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

                    if (child_yang_name == "ipv4-acl-cfg"):
                        for c in self.ipv4_acl_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.Ipv4AclCfgs.Ipv4AclCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ipv4_acl_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv4-acl-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Ipv6AclCfgs(Entity):
                """
                Match IPv6 Access\-list number
                
                .. attribute:: ipv6_acl_cfg
                
                	Match IPv6 Access\-list number configuration
                	**type**\: list of    :py:class:`Ipv6AclCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.Ipv6AclCfgs.Ipv6AclCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.Ipv6AclCfgs, self).__init__()

                    self.yang_name = "ipv6-acl-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.ipv6_acl_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.Ipv6AclCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.Ipv6AclCfgs, self).__setattr__(name, value)


                class Ipv6AclCfg(Entity):
                    """
                    Match IPv6 Access\-list number
                    configuration
                    
                    .. attribute:: ip_acl  <key>
                    
                    	IP ACL number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.Ipv6AclCfgs.Ipv6AclCfg, self).__init__()

                        self.yang_name = "ipv6-acl-cfg"
                        self.yang_parent_name = "ipv6-acl-cfgs"

                        self.ip_acl = YLeaf(YType.uint32, "ip-acl")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ip_acl") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.Ipv6AclCfgs.Ipv6AclCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.Ipv6AclCfgs.Ipv6AclCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return self.ip_acl.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ip_acl.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv6-acl-cfg" + "[ip-acl='" + self.ip_acl.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ip_acl.is_set or self.ip_acl.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_acl.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ip-acl"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ip-acl"):
                            self.ip_acl = value
                            self.ip_acl.value_namespace = name_space
                            self.ip_acl.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ipv6_acl_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ipv6_acl_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:ipv6-acl-cfgs" + path_buffer

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

                    if (child_yang_name == "ipv6-acl-cfg"):
                        for c in self.ipv6_acl_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.Ipv6AclCfgs.Ipv6AclCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ipv6_acl_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv6-acl-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class InputInterfaceCfgs(Entity):
                """
                Match type Input interface
                
                .. attribute:: input_interface_cfg
                
                	Match type Input interface  configuration
                	**type**\: list of    :py:class:`InputInterfaceCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.InputInterfaceCfgs.InputInterfaceCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.InputInterfaceCfgs, self).__init__()

                    self.yang_name = "input-interface-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.input_interface_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.InputInterfaceCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.InputInterfaceCfgs, self).__setattr__(name, value)


                class InputInterfaceCfg(Entity):
                    """
                    Match type Input interface 
                    configuration
                    
                    .. attribute:: if_name  <key>
                    
                    	Input interface ID
                    	**type**\:  str
                    
                    	**length:** 1..255
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.InputInterfaceCfgs.InputInterfaceCfg, self).__init__()

                        self.yang_name = "input-interface-cfg"
                        self.yang_parent_name = "input-interface-cfgs"

                        self.if_name = YLeaf(YType.str, "if-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("if_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.InputInterfaceCfgs.InputInterfaceCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.InputInterfaceCfgs.InputInterfaceCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return self.if_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.if_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "input-interface-cfg" + "[if-name='" + self.if_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.if_name.is_set or self.if_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.if_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "if-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "if-name"):
                            self.if_name = value
                            self.if_name.value_namespace = name_space
                            self.if_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.input_interface_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.input_interface_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:input-interface-cfgs" + path_buffer

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

                    if (child_yang_name == "input-interface-cfg"):
                        for c in self.input_interface_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.InputInterfaceCfgs.InputInterfaceCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.input_interface_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "input-interface-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class SrcMacCfgs(Entity):
                """
                Match Type Source MAC Address
                
                .. attribute:: src_mac_cfg
                
                	Match Type Source MAC Address  configuration
                	**type**\: list of    :py:class:`SrcMacCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.SrcMacCfgs.SrcMacCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.SrcMacCfgs, self).__init__()

                    self.yang_name = "src-mac-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.src_mac_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.SrcMacCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.SrcMacCfgs, self).__setattr__(name, value)


                class SrcMacCfg(Entity):
                    """
                    Match Type Source MAC Address 
                    configuration
                    
                    .. attribute:: mac  <key>
                    
                    	Specifies the source/destination MAC address to be used as a match criterion
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mac_mask
                    
                    	Specifies the source/destination MAC address mask to be used as a match criterion
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.SrcMacCfgs.SrcMacCfg, self).__init__()

                        self.yang_name = "src-mac-cfg"
                        self.yang_parent_name = "src-mac-cfgs"

                        self.mac = YLeaf(YType.str, "mac")

                        self.mac_mask = YLeaf(YType.str, "mac-mask")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("mac",
                                        "mac_mask") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.SrcMacCfgs.SrcMacCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.SrcMacCfgs.SrcMacCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.mac.is_set or
                            self.mac_mask.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.mac.yfilter != YFilter.not_set or
                            self.mac_mask.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "src-mac-cfg" + "[mac='" + self.mac.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.mac.is_set or self.mac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac.get_name_leafdata())
                        if (self.mac_mask.is_set or self.mac_mask.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac_mask.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "mac" or name == "mac-mask"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "mac"):
                            self.mac = value
                            self.mac.value_namespace = name_space
                            self.mac.value_namespace_prefix = name_space_prefix
                        if(value_path == "mac-mask"):
                            self.mac_mask = value
                            self.mac_mask.value_namespace = name_space
                            self.mac_mask.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.src_mac_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.src_mac_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:src-mac-cfgs" + path_buffer

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

                    if (child_yang_name == "src-mac-cfg"):
                        for c in self.src_mac_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.SrcMacCfgs.SrcMacCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.src_mac_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "src-mac-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class DstMacCfgs(Entity):
                """
                Match Type Destination MAC Address
                
                .. attribute:: dst_mac_cfg
                
                	Match Type Destination MAC Address configuration
                	**type**\: list of    :py:class:`DstMacCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.DstMacCfgs.DstMacCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.DstMacCfgs, self).__init__()

                    self.yang_name = "dst-mac-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.dst_mac_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.DstMacCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.DstMacCfgs, self).__setattr__(name, value)


                class DstMacCfg(Entity):
                    """
                    Match Type Destination MAC Address
                    configuration
                    
                    .. attribute:: mac  <key>
                    
                    	Specifies the source/destination MAC address to be used as a match criterion
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mac_mask
                    
                    	Specifies the source/destination MAC address mask to be used as a match criterion
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.DstMacCfgs.DstMacCfg, self).__init__()

                        self.yang_name = "dst-mac-cfg"
                        self.yang_parent_name = "dst-mac-cfgs"

                        self.mac = YLeaf(YType.str, "mac")

                        self.mac_mask = YLeaf(YType.str, "mac-mask")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("mac",
                                        "mac_mask") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.DstMacCfgs.DstMacCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.DstMacCfgs.DstMacCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.mac.is_set or
                            self.mac_mask.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.mac.yfilter != YFilter.not_set or
                            self.mac_mask.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "dst-mac-cfg" + "[mac='" + self.mac.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.mac.is_set or self.mac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac.get_name_leafdata())
                        if (self.mac_mask.is_set or self.mac_mask.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac_mask.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "mac" or name == "mac-mask"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "mac"):
                            self.mac = value
                            self.mac.value_namespace = name_space
                            self.mac.value_namespace_prefix = name_space_prefix
                        if(value_path == "mac-mask"):
                            self.mac_mask = value
                            self.mac_mask.value_namespace = name_space
                            self.mac_mask.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.dst_mac_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.dst_mac_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:dst-mac-cfgs" + path_buffer

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

                    if (child_yang_name == "dst-mac-cfg"):
                        for c in self.dst_mac_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.DstMacCfgs.DstMacCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.dst_mac_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "dst-mac-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class ProtocolNameCfgs(Entity):
                """
                Match Type name\-based protocol
                
                .. attribute:: protocol_name_cfg
                
                	Match Type name\-based protocol configuration
                	**type**\: list of    :py:class:`ProtocolNameCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.ProtocolNameCfgs.ProtocolNameCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.ProtocolNameCfgs, self).__init__()

                    self.yang_name = "protocol-name-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.protocol_name_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.ProtocolNameCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.ProtocolNameCfgs, self).__setattr__(name, value)


                class ProtocolNameCfg(Entity):
                    """
                    Match Type name\-based protocol
                    configuration
                    
                    .. attribute:: protocol_name  <key>
                    
                    	protocol name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.ProtocolNameCfgs.ProtocolNameCfg, self).__init__()

                        self.yang_name = "protocol-name-cfg"
                        self.yang_parent_name = "protocol-name-cfgs"

                        self.protocol_name = YLeaf(YType.str, "protocol-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("protocol_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.ProtocolNameCfgs.ProtocolNameCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.ProtocolNameCfgs.ProtocolNameCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return self.protocol_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.protocol_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "protocol-name-cfg" + "[protocol-name='" + self.protocol_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.protocol_name.is_set or self.protocol_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "protocol-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "protocol-name"):
                            self.protocol_name = value
                            self.protocol_name.value_namespace = name_space
                            self.protocol_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.protocol_name_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.protocol_name_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:protocol-name-cfgs" + path_buffer

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

                    if (child_yang_name == "protocol-name-cfg"):
                        for c in self.protocol_name_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.ProtocolNameCfgs.ProtocolNameCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.protocol_name_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "protocol-name-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class MplsExpTopCfgs(Entity):
                """
                Match MPLS experimental Topmost
                
                .. attribute:: mpls_exp_top_cfg
                
                	Match MPLS experimental Topmost  configuration
                	**type**\: list of    :py:class:`MplsExpTopCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.MplsExpTopCfgs.MplsExpTopCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.MplsExpTopCfgs, self).__init__()

                    self.yang_name = "mpls-exp-top-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.mpls_exp_top_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.MplsExpTopCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.MplsExpTopCfgs, self).__setattr__(name, value)


                class MplsExpTopCfg(Entity):
                    """
                    Match MPLS experimental Topmost 
                    configuration
                    
                    .. attribute:: exp_min  <key>
                    
                    	The minimum EXP field value to be used as match criteria. Any number from 0 to 7
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: exp_max  <key>
                    
                    	The maximum EXP field value to be used as match criteria. Any number from 0 to 7
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.MplsExpTopCfgs.MplsExpTopCfg, self).__init__()

                        self.yang_name = "mpls-exp-top-cfg"
                        self.yang_parent_name = "mpls-exp-top-cfgs"

                        self.exp_min = YLeaf(YType.uint8, "exp-min")

                        self.exp_max = YLeaf(YType.uint8, "exp-max")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("exp_min",
                                        "exp_max") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.MplsExpTopCfgs.MplsExpTopCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.MplsExpTopCfgs.MplsExpTopCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.exp_min.is_set or
                            self.exp_max.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.exp_min.yfilter != YFilter.not_set or
                            self.exp_max.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mpls-exp-top-cfg" + "[exp-min='" + self.exp_min.get() + "']" + "[exp-max='" + self.exp_max.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.exp_min.is_set or self.exp_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.exp_min.get_name_leafdata())
                        if (self.exp_max.is_set or self.exp_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.exp_max.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "exp-min" or name == "exp-max"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "exp-min"):
                            self.exp_min = value
                            self.exp_min.value_namespace = name_space
                            self.exp_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "exp-max"):
                            self.exp_max = value
                            self.exp_max.value_namespace = name_space
                            self.exp_max.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.mpls_exp_top_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.mpls_exp_top_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:mpls-exp-top-cfgs" + path_buffer

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

                    if (child_yang_name == "mpls-exp-top-cfg"):
                        for c in self.mpls_exp_top_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.MplsExpTopCfgs.MplsExpTopCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.mpls_exp_top_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mpls-exp-top-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class MplsExpImpCfgs(Entity):
                """
                Match MPLS experimental Imposition
                
                .. attribute:: mpls_exp_imp_cfg
                
                	Match MPLS experimental Imposition  configuration
                	**type**\: list of    :py:class:`MplsExpImpCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.MplsExpImpCfgs.MplsExpImpCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.MplsExpImpCfgs, self).__init__()

                    self.yang_name = "mpls-exp-imp-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.mpls_exp_imp_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.MplsExpImpCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.MplsExpImpCfgs, self).__setattr__(name, value)


                class MplsExpImpCfg(Entity):
                    """
                    Match MPLS experimental Imposition 
                    configuration
                    
                    .. attribute:: exp_min  <key>
                    
                    	The minimum EXP field value to be used as match criteria. Any number from 0 to 7
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: exp_max  <key>
                    
                    	The maximum EXP field value to be used as match criteria. Any number from 0 to 7
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.MplsExpImpCfgs.MplsExpImpCfg, self).__init__()

                        self.yang_name = "mpls-exp-imp-cfg"
                        self.yang_parent_name = "mpls-exp-imp-cfgs"

                        self.exp_min = YLeaf(YType.uint8, "exp-min")

                        self.exp_max = YLeaf(YType.uint8, "exp-max")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("exp_min",
                                        "exp_max") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.MplsExpImpCfgs.MplsExpImpCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.MplsExpImpCfgs.MplsExpImpCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.exp_min.is_set or
                            self.exp_max.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.exp_min.yfilter != YFilter.not_set or
                            self.exp_max.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mpls-exp-imp-cfg" + "[exp-min='" + self.exp_min.get() + "']" + "[exp-max='" + self.exp_max.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.exp_min.is_set or self.exp_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.exp_min.get_name_leafdata())
                        if (self.exp_max.is_set or self.exp_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.exp_max.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "exp-min" or name == "exp-max"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "exp-min"):
                            self.exp_min = value
                            self.exp_min.value_namespace = name_space
                            self.exp_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "exp-max"):
                            self.exp_max = value
                            self.exp_max.value_namespace = name_space
                            self.exp_max.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.mpls_exp_imp_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.mpls_exp_imp_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:mpls-exp-imp-cfgs" + path_buffer

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

                    if (child_yang_name == "mpls-exp-imp-cfg"):
                        for c in self.mpls_exp_imp_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.MplsExpImpCfgs.MplsExpImpCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.mpls_exp_imp_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mpls-exp-imp-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class PktLenCfgs(Entity):
                """
                Match Type Packet Length
                
                .. attribute:: pkt_len_cfg
                
                	Match Type Packet Length  configuration
                	**type**\: list of    :py:class:`PktLenCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.PktLenCfgs.PktLenCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.PktLenCfgs, self).__init__()

                    self.yang_name = "pkt-len-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.pkt_len_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.PktLenCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.PktLenCfgs, self).__setattr__(name, value)


                class PktLenCfg(Entity):
                    """
                    Match Type Packet Length 
                    configuration
                    
                    .. attribute:: min_pkt_len  <key>
                    
                    	Minimum layer 3 packet length in bytes
                    	**type**\:  int
                    
                    	**range:** 1..9216
                    
                    .. attribute:: max_pkt_len  <key>
                    
                    	Maximum layer 3 packet length in bytes
                    	**type**\:  int
                    
                    	**range:** 1..9216
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.PktLenCfgs.PktLenCfg, self).__init__()

                        self.yang_name = "pkt-len-cfg"
                        self.yang_parent_name = "pkt-len-cfgs"

                        self.min_pkt_len = YLeaf(YType.uint16, "min-pkt-len")

                        self.max_pkt_len = YLeaf(YType.uint16, "max-pkt-len")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("min_pkt_len",
                                        "max_pkt_len") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.PktLenCfgs.PktLenCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.PktLenCfgs.PktLenCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.min_pkt_len.is_set or
                            self.max_pkt_len.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.min_pkt_len.yfilter != YFilter.not_set or
                            self.max_pkt_len.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pkt-len-cfg" + "[min-pkt-len='" + self.min_pkt_len.get() + "']" + "[max-pkt-len='" + self.max_pkt_len.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.min_pkt_len.is_set or self.min_pkt_len.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min_pkt_len.get_name_leafdata())
                        if (self.max_pkt_len.is_set or self.max_pkt_len.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_pkt_len.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "min-pkt-len" or name == "max-pkt-len"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "min-pkt-len"):
                            self.min_pkt_len = value
                            self.min_pkt_len.value_namespace = name_space
                            self.min_pkt_len.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-pkt-len"):
                            self.max_pkt_len = value
                            self.max_pkt_len.value_namespace = name_space
                            self.max_pkt_len.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.pkt_len_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.pkt_len_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:pkt-len-cfgs" + path_buffer

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

                    if (child_yang_name == "pkt-len-cfg"):
                        for c in self.pkt_len_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.PktLenCfgs.PktLenCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.pkt_len_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "pkt-len-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Prec(Entity):
                """
                Match Type Precedence in 
                IPv4 and IPv6 packets
                
                .. attribute:: prec_attr_cfgs
                
                	Match Type Precedence  based on attribute
                	**type**\:   :py:class:`PrecAttrCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.Prec.PrecAttrCfgs>`
                
                .. attribute:: prec_val_cfgs
                
                	Match Type Precedence  based on value
                	**type**\:   :py:class:`PrecValCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.Prec.PrecValCfgs>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.Prec, self).__init__()

                    self.yang_name = "prec"
                    self.yang_parent_name = "filter-entry"

                    self.prec_attr_cfgs = Classifiers.ClassifierEntry.FilterEntry.Prec.PrecAttrCfgs()
                    self.prec_attr_cfgs.parent = self
                    self._children_name_map["prec_attr_cfgs"] = "prec-attr-cfgs"
                    self._children_yang_names.add("prec-attr-cfgs")

                    self.prec_val_cfgs = Classifiers.ClassifierEntry.FilterEntry.Prec.PrecValCfgs()
                    self.prec_val_cfgs.parent = self
                    self._children_name_map["prec_val_cfgs"] = "prec-val-cfgs"
                    self._children_yang_names.add("prec-val-cfgs")


                class PrecValCfgs(Entity):
                    """
                    Match Type Precedence 
                    based on value
                    
                    .. attribute:: prec_val_cfg
                    
                    	Match Type Precedence  based on value configuration
                    	**type**\: list of    :py:class:`PrecValCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.Prec.PrecValCfgs.PrecValCfg>`
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.Prec.PrecValCfgs, self).__init__()

                        self.yang_name = "prec-val-cfgs"
                        self.yang_parent_name = "prec"

                        self.prec_val_cfg = YList(self)

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
                                    super(Classifiers.ClassifierEntry.FilterEntry.Prec.PrecValCfgs, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.Prec.PrecValCfgs, self).__setattr__(name, value)


                    class PrecValCfg(Entity):
                        """
                        Match Type Precedence 
                        based on value configuration
                        
                        .. attribute:: prec_val  <key>
                        
                        	Value from 0 to 7 used to identify an  IP precedence value
                        	**type**\:  int
                        
                        	**range:** 0..7
                        
                        

                        """

                        _prefix = 'cisco-filter'
                        _revision = '2016-03-30'

                        def __init__(self):
                            super(Classifiers.ClassifierEntry.FilterEntry.Prec.PrecValCfgs.PrecValCfg, self).__init__()

                            self.yang_name = "prec-val-cfg"
                            self.yang_parent_name = "prec-val-cfgs"

                            self.prec_val = YLeaf(YType.uint8, "prec-val")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("prec_val") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Classifiers.ClassifierEntry.FilterEntry.Prec.PrecValCfgs.PrecValCfg, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Classifiers.ClassifierEntry.FilterEntry.Prec.PrecValCfgs.PrecValCfg, self).__setattr__(name, value)

                        def has_data(self):
                            return self.prec_val.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.prec_val.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "prec-val-cfg" + "[prec-val='" + self.prec_val.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.prec_val.is_set or self.prec_val.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prec_val.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "prec-val"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "prec-val"):
                                self.prec_val = value
                                self.prec_val.value_namespace = name_space
                                self.prec_val.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.prec_val_cfg:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.prec_val_cfg:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "prec-val-cfgs" + path_buffer

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

                        if (child_yang_name == "prec-val-cfg"):
                            for c in self.prec_val_cfg:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Classifiers.ClassifierEntry.FilterEntry.Prec.PrecValCfgs.PrecValCfg()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.prec_val_cfg.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "prec-val-cfg"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class PrecAttrCfgs(Entity):
                    """
                    Match Type Precedence 
                    based on attribute
                    
                    .. attribute:: prec_attr_cfg
                    
                    	Match Type Precedence  based on attribute configuration
                    	**type**\: list of    :py:class:`PrecAttrCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.Prec.PrecAttrCfgs.PrecAttrCfg>`
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.Prec.PrecAttrCfgs, self).__init__()

                        self.yang_name = "prec-attr-cfgs"
                        self.yang_parent_name = "prec"

                        self.prec_attr_cfg = YList(self)

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
                                    super(Classifiers.ClassifierEntry.FilterEntry.Prec.PrecAttrCfgs, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.Prec.PrecAttrCfgs, self).__setattr__(name, value)


                    class PrecAttrCfg(Entity):
                        """
                        Match Type Precedence 
                        based on attribute configuration
                        
                        .. attribute:: prec_attr  <key>
                        
                        	IP precedence attribute\: critical   Match packets with critical precedence (5) flash      Match packets with flash precedence (3) flash\-override  Match packets with flash override precedence (4) immediate  Match packets with immediate precedence (2) internet   Match packets with internetwork control precedence (6) network    Match packets with network control precedence (7) priority   Match packets with priority precedence (1) routine    Match packets with routine precedence (0) 
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'cisco-filter'
                        _revision = '2016-03-30'

                        def __init__(self):
                            super(Classifiers.ClassifierEntry.FilterEntry.Prec.PrecAttrCfgs.PrecAttrCfg, self).__init__()

                            self.yang_name = "prec-attr-cfg"
                            self.yang_parent_name = "prec-attr-cfgs"

                            self.prec_attr = YLeaf(YType.str, "prec-attr")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("prec_attr") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Classifiers.ClassifierEntry.FilterEntry.Prec.PrecAttrCfgs.PrecAttrCfg, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Classifiers.ClassifierEntry.FilterEntry.Prec.PrecAttrCfgs.PrecAttrCfg, self).__setattr__(name, value)

                        def has_data(self):
                            return self.prec_attr.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.prec_attr.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "prec-attr-cfg" + "[prec-attr='" + self.prec_attr.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.prec_attr.is_set or self.prec_attr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prec_attr.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "prec-attr"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "prec-attr"):
                                self.prec_attr = value
                                self.prec_attr.value_namespace = name_space
                                self.prec_attr.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.prec_attr_cfg:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.prec_attr_cfg:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "prec-attr-cfgs" + path_buffer

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

                        if (child_yang_name == "prec-attr-cfg"):
                            for c in self.prec_attr_cfg:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Classifiers.ClassifierEntry.FilterEntry.Prec.PrecAttrCfgs.PrecAttrCfg()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.prec_attr_cfg.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "prec-attr-cfg"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.prec_attr_cfgs is not None and self.prec_attr_cfgs.has_data()) or
                        (self.prec_val_cfgs is not None and self.prec_val_cfgs.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.prec_attr_cfgs is not None and self.prec_attr_cfgs.has_operation()) or
                        (self.prec_val_cfgs is not None and self.prec_val_cfgs.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:prec" + path_buffer

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

                    if (child_yang_name == "prec-attr-cfgs"):
                        if (self.prec_attr_cfgs is None):
                            self.prec_attr_cfgs = Classifiers.ClassifierEntry.FilterEntry.Prec.PrecAttrCfgs()
                            self.prec_attr_cfgs.parent = self
                            self._children_name_map["prec_attr_cfgs"] = "prec-attr-cfgs"
                        return self.prec_attr_cfgs

                    if (child_yang_name == "prec-val-cfgs"):
                        if (self.prec_val_cfgs is None):
                            self.prec_val_cfgs = Classifiers.ClassifierEntry.FilterEntry.Prec.PrecValCfgs()
                            self.prec_val_cfgs.parent = self
                            self._children_name_map["prec_val_cfgs"] = "prec-val-cfgs"
                        return self.prec_val_cfgs

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "prec-attr-cfgs" or name == "prec-val-cfgs"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class QosGroupCfgs(Entity):
                """
                Match Type QoS Group
                
                .. attribute:: qos_group_cfg
                
                	Match Type QoS Group configuration
                	**type**\: list of    :py:class:`QosGroupCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.QosGroupCfgs.QosGroupCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.QosGroupCfgs, self).__init__()

                    self.yang_name = "qos-group-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.qos_group_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.QosGroupCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.QosGroupCfgs, self).__setattr__(name, value)


                class QosGroupCfg(Entity):
                    """
                    Match Type QoS Group configuration
                    
                    .. attribute:: qos_group_min  <key>
                    
                    	Specifies the minimum value range from 0 to 99 used to identify a QoS group value
                    	**type**\:  int
                    
                    	**range:** 0..99
                    
                    .. attribute:: qos_group_max  <key>
                    
                    	Specifies the maximum value range from 0 to 99 used to identify a QoS group value
                    	**type**\:  int
                    
                    	**range:** 0..99
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.QosGroupCfgs.QosGroupCfg, self).__init__()

                        self.yang_name = "qos-group-cfg"
                        self.yang_parent_name = "qos-group-cfgs"

                        self.qos_group_min = YLeaf(YType.uint16, "qos-group-min")

                        self.qos_group_max = YLeaf(YType.uint16, "qos-group-max")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("qos_group_min",
                                        "qos_group_max") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.QosGroupCfgs.QosGroupCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.QosGroupCfgs.QosGroupCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.qos_group_min.is_set or
                            self.qos_group_max.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.qos_group_min.yfilter != YFilter.not_set or
                            self.qos_group_max.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "qos-group-cfg" + "[qos-group-min='" + self.qos_group_min.get() + "']" + "[qos-group-max='" + self.qos_group_max.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.qos_group_min.is_set or self.qos_group_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.qos_group_min.get_name_leafdata())
                        if (self.qos_group_max.is_set or self.qos_group_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.qos_group_max.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "qos-group-min" or name == "qos-group-max"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "qos-group-min"):
                            self.qos_group_min = value
                            self.qos_group_min.value_namespace = name_space
                            self.qos_group_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "qos-group-max"):
                            self.qos_group_max = value
                            self.qos_group_max.value_namespace = name_space
                            self.qos_group_max.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.qos_group_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.qos_group_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:qos-group-cfgs" + path_buffer

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

                    if (child_yang_name == "qos-group-cfg"):
                        for c in self.qos_group_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.QosGroupCfgs.QosGroupCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.qos_group_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "qos-group-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class VlanCfgs(Entity):
                """
                Match Type VLAN
                
                .. attribute:: vlan_cfg
                
                	Match Type VLAN configuration
                	**type**\: list of    :py:class:`VlanCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.VlanCfgs.VlanCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.VlanCfgs, self).__init__()

                    self.yang_name = "vlan-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.vlan_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.VlanCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.VlanCfgs, self).__setattr__(name, value)


                class VlanCfg(Entity):
                    """
                    Match Type VLAN configuration
                    
                    .. attribute:: vlan_min  <key>
                    
                    	Vlan minimum ID
                    	**type**\:  int
                    
                    	**range:** 1..4095
                    
                    .. attribute:: vlan_max  <key>
                    
                    	Vlan maximum ID
                    	**type**\:  int
                    
                    	**range:** 1..4095
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.VlanCfgs.VlanCfg, self).__init__()

                        self.yang_name = "vlan-cfg"
                        self.yang_parent_name = "vlan-cfgs"

                        self.vlan_min = YLeaf(YType.uint16, "vlan-min")

                        self.vlan_max = YLeaf(YType.uint16, "vlan-max")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("vlan_min",
                                        "vlan_max") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.VlanCfgs.VlanCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.VlanCfgs.VlanCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.vlan_min.is_set or
                            self.vlan_max.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.vlan_min.yfilter != YFilter.not_set or
                            self.vlan_max.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vlan-cfg" + "[vlan-min='" + self.vlan_min.get() + "']" + "[vlan-max='" + self.vlan_max.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.vlan_min.is_set or self.vlan_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vlan_min.get_name_leafdata())
                        if (self.vlan_max.is_set or self.vlan_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vlan_max.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "vlan-min" or name == "vlan-max"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "vlan-min"):
                            self.vlan_min = value
                            self.vlan_min.value_namespace = name_space
                            self.vlan_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "vlan-max"):
                            self.vlan_max = value
                            self.vlan_max.value_namespace = name_space
                            self.vlan_max.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.vlan_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.vlan_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:vlan-cfgs" + path_buffer

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

                    if (child_yang_name == "vlan-cfg"):
                        for c in self.vlan_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.VlanCfgs.VlanCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.vlan_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vlan-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class VlanInnerCfgs(Entity):
                """
                Match Type Inner VLAN
                
                .. attribute:: vlan_inner_cfg
                
                	Match Type Inner VLAN  configuration
                	**type**\: list of    :py:class:`VlanInnerCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.VlanInnerCfgs.VlanInnerCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.VlanInnerCfgs, self).__init__()

                    self.yang_name = "vlan-inner-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.vlan_inner_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.VlanInnerCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.VlanInnerCfgs, self).__setattr__(name, value)


                class VlanInnerCfg(Entity):
                    """
                    Match Type Inner VLAN 
                    configuration
                    
                    .. attribute:: vlan_min  <key>
                    
                    	Vlan minimum ID
                    	**type**\:  int
                    
                    	**range:** 1..4095
                    
                    .. attribute:: vlan_max  <key>
                    
                    	Vlan maximum ID
                    	**type**\:  int
                    
                    	**range:** 1..4095
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.VlanInnerCfgs.VlanInnerCfg, self).__init__()

                        self.yang_name = "vlan-inner-cfg"
                        self.yang_parent_name = "vlan-inner-cfgs"

                        self.vlan_min = YLeaf(YType.uint16, "vlan-min")

                        self.vlan_max = YLeaf(YType.uint16, "vlan-max")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("vlan_min",
                                        "vlan_max") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.VlanInnerCfgs.VlanInnerCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.VlanInnerCfgs.VlanInnerCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.vlan_min.is_set or
                            self.vlan_max.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.vlan_min.yfilter != YFilter.not_set or
                            self.vlan_max.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vlan-inner-cfg" + "[vlan-min='" + self.vlan_min.get() + "']" + "[vlan-max='" + self.vlan_max.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.vlan_min.is_set or self.vlan_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vlan_min.get_name_leafdata())
                        if (self.vlan_max.is_set or self.vlan_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vlan_max.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "vlan-min" or name == "vlan-max"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "vlan-min"):
                            self.vlan_min = value
                            self.vlan_min.value_namespace = name_space
                            self.vlan_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "vlan-max"):
                            self.vlan_max = value
                            self.vlan_max.value_namespace = name_space
                            self.vlan_max.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.vlan_inner_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.vlan_inner_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:vlan-inner-cfgs" + path_buffer

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

                    if (child_yang_name == "vlan-inner-cfg"):
                        for c in self.vlan_inner_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.VlanInnerCfgs.VlanInnerCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.vlan_inner_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vlan-inner-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class AtmClpCfg(Entity):
                """
                Match ATM Cell Loss Priority (CLP)
                
                .. attribute:: atm_clp
                
                	ATM CLP activation
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.AtmClpCfg, self).__init__()

                    self.yang_name = "atm-clp-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.atm_clp = YLeaf(YType.empty, "atm-clp")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("atm_clp") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.AtmClpCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.AtmClpCfg, self).__setattr__(name, value)

                def has_data(self):
                    return self.atm_clp.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.atm_clp.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:atm-clp-cfg" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.atm_clp.is_set or self.atm_clp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.atm_clp.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "atm-clp"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "atm-clp"):
                        self.atm_clp = value
                        self.atm_clp.value_namespace = name_space
                        self.atm_clp.value_namespace_prefix = name_space_prefix


            class AtmVciCfgs(Entity):
                """
                Match ATM Virtual Channel Identifier 
                (VCI)
                
                .. attribute:: atm_vci_cfg
                
                	Match ATM Virtual Channel  Identifier (VCI) configuration
                	**type**\: list of    :py:class:`AtmVciCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.AtmVciCfgs.AtmVciCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.AtmVciCfgs, self).__init__()

                    self.yang_name = "atm-vci-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.atm_vci_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.AtmVciCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.AtmVciCfgs, self).__setattr__(name, value)


                class AtmVciCfg(Entity):
                    """
                    Match ATM Virtual Channel 
                    Identifier (VCI) configuration
                    
                    .. attribute:: atm_vci_min  <key>
                    
                    	ATM VCI minimum value
                    	**type**\:  int
                    
                    	**range:** 32..65535
                    
                    .. attribute:: atm_vci_max  <key>
                    
                    	ATM VCI maximum value
                    	**type**\:  int
                    
                    	**range:** 32..65535
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.AtmVciCfgs.AtmVciCfg, self).__init__()

                        self.yang_name = "atm-vci-cfg"
                        self.yang_parent_name = "atm-vci-cfgs"

                        self.atm_vci_min = YLeaf(YType.uint16, "atm-vci-min")

                        self.atm_vci_max = YLeaf(YType.uint16, "atm-vci-max")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("atm_vci_min",
                                        "atm_vci_max") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.AtmVciCfgs.AtmVciCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.AtmVciCfgs.AtmVciCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.atm_vci_min.is_set or
                            self.atm_vci_max.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.atm_vci_min.yfilter != YFilter.not_set or
                            self.atm_vci_max.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "atm-vci-cfg" + "[atm-vci-min='" + self.atm_vci_min.get() + "']" + "[atm-vci-max='" + self.atm_vci_max.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.atm_vci_min.is_set or self.atm_vci_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.atm_vci_min.get_name_leafdata())
                        if (self.atm_vci_max.is_set or self.atm_vci_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.atm_vci_max.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "atm-vci-min" or name == "atm-vci-max"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "atm-vci-min"):
                            self.atm_vci_min = value
                            self.atm_vci_min.value_namespace = name_space
                            self.atm_vci_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "atm-vci-max"):
                            self.atm_vci_max = value
                            self.atm_vci_max.value_namespace = name_space
                            self.atm_vci_max.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.atm_vci_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.atm_vci_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:atm-vci-cfgs" + path_buffer

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

                    if (child_yang_name == "atm-vci-cfg"):
                        for c in self.atm_vci_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.AtmVciCfgs.AtmVciCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.atm_vci_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "atm-vci-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class DeiCfg(Entity):
                """
                Match Type DEI Bit configuration
                
                .. attribute:: dei_cfg
                
                	DEI bit value
                	**type**\:  bool
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.DeiCfg, self).__init__()

                    self.yang_name = "dei-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.dei_cfg = YLeaf(YType.boolean, "dei-cfg")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("dei_cfg") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.DeiCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.DeiCfg, self).__setattr__(name, value)

                def has_data(self):
                    return self.dei_cfg.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.dei_cfg.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:dei-cfg" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.dei_cfg.is_set or self.dei_cfg.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dei_cfg.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "dei-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "dei-cfg"):
                        self.dei_cfg = value
                        self.dei_cfg.value_namespace = name_space
                        self.dei_cfg.value_namespace_prefix = name_space_prefix


            class DeiInnerCfg(Entity):
                """
                Match Type Inner DEI Bit
                
                .. attribute:: dei_cfg
                
                	DEI bit value
                	**type**\:  bool
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.DeiInnerCfg, self).__init__()

                    self.yang_name = "dei-inner-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.dei_cfg = YLeaf(YType.boolean, "dei-cfg")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("dei_cfg") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.DeiInnerCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.DeiInnerCfg, self).__setattr__(name, value)

                def has_data(self):
                    return self.dei_cfg.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.dei_cfg.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:dei-inner-cfg" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.dei_cfg.is_set or self.dei_cfg.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dei_cfg.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "dei-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "dei-cfg"):
                        self.dei_cfg = value
                        self.dei_cfg.value_namespace = name_space
                        self.dei_cfg.value_namespace_prefix = name_space_prefix


            class FlowIpCfg(Entity):
                """
                Match Type flow
                
                .. attribute:: dst_port
                
                	Flow destination port number
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: flow_dst_ip
                
                	Flow destination IP
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: flow_src_ip
                
                	Flow source IP
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: protocol
                
                	FLOW IP protocol
                	**type**\:   :py:class:`IpVersion <ydk.models.ietf.ietf_inet_types.IpVersion>`
                
                .. attribute:: src_port
                
                	Flow source port number
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.FlowIpCfg, self).__init__()

                    self.yang_name = "flow-ip-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.dst_port = YLeaf(YType.uint16, "dst-port")

                    self.flow_dst_ip = YLeaf(YType.str, "flow-dst-ip")

                    self.flow_src_ip = YLeaf(YType.str, "flow-src-ip")

                    self.protocol = YLeaf(YType.enumeration, "protocol")

                    self.src_port = YLeaf(YType.uint16, "src-port")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("dst_port",
                                    "flow_dst_ip",
                                    "flow_src_ip",
                                    "protocol",
                                    "src_port") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.FlowIpCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.FlowIpCfg, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.dst_port.is_set or
                        self.flow_dst_ip.is_set or
                        self.flow_src_ip.is_set or
                        self.protocol.is_set or
                        self.src_port.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.dst_port.yfilter != YFilter.not_set or
                        self.flow_dst_ip.yfilter != YFilter.not_set or
                        self.flow_src_ip.yfilter != YFilter.not_set or
                        self.protocol.yfilter != YFilter.not_set or
                        self.src_port.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:flow-ip-cfg" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.dst_port.is_set or self.dst_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dst_port.get_name_leafdata())
                    if (self.flow_dst_ip.is_set or self.flow_dst_ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flow_dst_ip.get_name_leafdata())
                    if (self.flow_src_ip.is_set or self.flow_src_ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flow_src_ip.get_name_leafdata())
                    if (self.protocol.is_set or self.protocol.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.protocol.get_name_leafdata())
                    if (self.src_port.is_set or self.src_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.src_port.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "dst-port" or name == "flow-dst-ip" or name == "flow-src-ip" or name == "protocol" or name == "src-port"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "dst-port"):
                        self.dst_port = value
                        self.dst_port.value_namespace = name_space
                        self.dst_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "flow-dst-ip"):
                        self.flow_dst_ip = value
                        self.flow_dst_ip.value_namespace = name_space
                        self.flow_dst_ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "flow-src-ip"):
                        self.flow_src_ip = value
                        self.flow_src_ip.value_namespace = name_space
                        self.flow_src_ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "protocol"):
                        self.protocol = value
                        self.protocol.value_namespace = name_space
                        self.protocol.value_namespace_prefix = name_space_prefix
                    if(value_path == "src-port"):
                        self.src_port = value
                        self.src_port.value_namespace = name_space
                        self.src_port.value_namespace_prefix = name_space_prefix


            class FlowRecordCfg(Entity):
                """
                Match Type flow Record Name
                
                .. attribute:: flow_record_name
                
                	Flow record type
                	**type**\:  str
                
                	**length:** 1..255
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.FlowRecordCfg, self).__init__()

                    self.yang_name = "flow-record-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.flow_record_name = YLeaf(YType.str, "flow-record-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("flow_record_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.FlowRecordCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.FlowRecordCfg, self).__setattr__(name, value)

                def has_data(self):
                    return self.flow_record_name.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.flow_record_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:flow-record-cfg" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.flow_record_name.is_set or self.flow_record_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flow_record_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "flow-record-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "flow-record-name"):
                        self.flow_record_name = value
                        self.flow_record_name.value_namespace = name_space
                        self.flow_record_name.value_namespace_prefix = name_space_prefix


            class FrDeCfg(Entity):
                """
                Match Frame Relay DE
                
                .. attribute:: fr_de_val
                
                	Frame Relay DE type
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.FrDeCfg, self).__init__()

                    self.yang_name = "fr-de-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.fr_de_val = YLeaf(YType.empty, "fr-de-val")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("fr_de_val") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.FrDeCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.FrDeCfg, self).__setattr__(name, value)

                def has_data(self):
                    return self.fr_de_val.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.fr_de_val.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:fr-de-cfg" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.fr_de_val.is_set or self.fr_de_val.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fr_de_val.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "fr-de-val"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "fr-de-val"):
                        self.fr_de_val = value
                        self.fr_de_val.value_namespace = name_space
                        self.fr_de_val.value_namespace_prefix = name_space_prefix


            class FrDlciCfgs(Entity):
                """
                Match Frame Relay DLCI
                
                .. attribute:: fr_dlci_cfg
                
                	Match Frame Relay DLCI  configuration
                	**type**\: list of    :py:class:`FrDlciCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.FrDlciCfgs.FrDlciCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.FrDlciCfgs, self).__init__()

                    self.yang_name = "fr-dlci-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.fr_dlci_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.FrDlciCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.FrDlciCfgs, self).__setattr__(name, value)


                class FrDlciCfg(Entity):
                    """
                    Match Frame Relay DLCI 
                    configuration
                    
                    .. attribute:: dlci_min  <key>
                    
                    	Frame Relay DLCI minimum value
                    	**type**\:  int
                    
                    	**range:** 16..1007
                    
                    .. attribute:: dlci_max  <key>
                    
                    	Frame Relay DLCI maximum value
                    	**type**\:  int
                    
                    	**range:** 16..1007
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.FrDlciCfgs.FrDlciCfg, self).__init__()

                        self.yang_name = "fr-dlci-cfg"
                        self.yang_parent_name = "fr-dlci-cfgs"

                        self.dlci_min = YLeaf(YType.uint16, "dlci-min")

                        self.dlci_max = YLeaf(YType.uint16, "dlci-max")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dlci_min",
                                        "dlci_max") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.FrDlciCfgs.FrDlciCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.FrDlciCfgs.FrDlciCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dlci_min.is_set or
                            self.dlci_max.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dlci_min.yfilter != YFilter.not_set or
                            self.dlci_max.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "fr-dlci-cfg" + "[dlci-min='" + self.dlci_min.get() + "']" + "[dlci-max='" + self.dlci_max.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dlci_min.is_set or self.dlci_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dlci_min.get_name_leafdata())
                        if (self.dlci_max.is_set or self.dlci_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dlci_max.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dlci-min" or name == "dlci-max"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dlci-min"):
                            self.dlci_min = value
                            self.dlci_min.value_namespace = name_space
                            self.dlci_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "dlci-max"):
                            self.dlci_max = value
                            self.dlci_max.value_namespace = name_space
                            self.dlci_max.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.fr_dlci_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.fr_dlci_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:fr-dlci-cfgs" + path_buffer

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

                    if (child_yang_name == "fr-dlci-cfg"):
                        for c in self.fr_dlci_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.FrDlciCfgs.FrDlciCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.fr_dlci_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "fr-dlci-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class WlanUserPriorityCfgs(Entity):
                """
                Match Type Wlan User Priority
                
                .. attribute:: wlan_user_priority_cfg
                
                	Match Type Wlan User Priority  configuration
                	**type**\: list of    :py:class:`WlanUserPriorityCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.WlanUserPriorityCfgs.WlanUserPriorityCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.WlanUserPriorityCfgs, self).__init__()

                    self.yang_name = "wlan-user-priority-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.wlan_user_priority_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.WlanUserPriorityCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.WlanUserPriorityCfgs, self).__setattr__(name, value)


                class WlanUserPriorityCfg(Entity):
                    """
                    Match Type Wlan User Priority 
                    configuration
                    
                    .. attribute:: wlan_prio_min  <key>
                    
                    	WLAN user priority minimum
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: wlan_prio_max  <key>
                    
                    	Wlan user priority maximum
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.WlanUserPriorityCfgs.WlanUserPriorityCfg, self).__init__()

                        self.yang_name = "wlan-user-priority-cfg"
                        self.yang_parent_name = "wlan-user-priority-cfgs"

                        self.wlan_prio_min = YLeaf(YType.uint8, "wlan-prio-min")

                        self.wlan_prio_max = YLeaf(YType.uint8, "wlan-prio-max")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("wlan_prio_min",
                                        "wlan_prio_max") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.WlanUserPriorityCfgs.WlanUserPriorityCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.WlanUserPriorityCfgs.WlanUserPriorityCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.wlan_prio_min.is_set or
                            self.wlan_prio_max.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.wlan_prio_min.yfilter != YFilter.not_set or
                            self.wlan_prio_max.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "wlan-user-priority-cfg" + "[wlan-prio-min='" + self.wlan_prio_min.get() + "']" + "[wlan-prio-max='" + self.wlan_prio_max.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.wlan_prio_min.is_set or self.wlan_prio_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.wlan_prio_min.get_name_leafdata())
                        if (self.wlan_prio_max.is_set or self.wlan_prio_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.wlan_prio_max.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "wlan-prio-min" or name == "wlan-prio-max"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "wlan-prio-min"):
                            self.wlan_prio_min = value
                            self.wlan_prio_min.value_namespace = name_space
                            self.wlan_prio_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "wlan-prio-max"):
                            self.wlan_prio_max = value
                            self.wlan_prio_max.value_namespace = name_space
                            self.wlan_prio_max.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.wlan_user_priority_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.wlan_user_priority_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:wlan-user-priority-cfgs" + path_buffer

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

                    if (child_yang_name == "wlan-user-priority-cfg"):
                        for c in self.wlan_user_priority_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.WlanUserPriorityCfgs.WlanUserPriorityCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.wlan_user_priority_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "wlan-user-priority-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class DiscardClassCfgs(Entity):
                """
                Match Type Discard Class
                
                .. attribute:: discard_class_cfg
                
                	Match Type Discard Class  configuration
                	**type**\: list of    :py:class:`DiscardClassCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.DiscardClassCfgs.DiscardClassCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.DiscardClassCfgs, self).__init__()

                    self.yang_name = "discard-class-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.discard_class_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.DiscardClassCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.DiscardClassCfgs, self).__setattr__(name, value)


                class DiscardClassCfg(Entity):
                    """
                    Match Type Discard Class 
                    configuration
                    
                    .. attribute:: discard_class  <key>
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.DiscardClassCfgs.DiscardClassCfg, self).__init__()

                        self.yang_name = "discard-class-cfg"
                        self.yang_parent_name = "discard-class-cfgs"

                        self.discard_class = YLeaf(YType.uint8, "discard-class")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("discard_class") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.DiscardClassCfgs.DiscardClassCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.DiscardClassCfgs.DiscardClassCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return self.discard_class.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.discard_class.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "discard-class-cfg" + "[discard-class='" + self.discard_class.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.discard_class.is_set or self.discard_class.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.discard_class.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "discard-class"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "discard-class"):
                            self.discard_class = value
                            self.discard_class.value_namespace = name_space
                            self.discard_class.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.discard_class_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.discard_class_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:discard-class-cfgs" + path_buffer

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

                    if (child_yang_name == "discard-class-cfg"):
                        for c in self.discard_class_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.DiscardClassCfgs.DiscardClassCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.discard_class_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "discard-class-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class ClassMapCfgs(Entity):
                """
                Match Type cls\-map Name
                
                .. attribute:: class_map_cfg
                
                	Match Type cls\-map Name  configuration
                	**type**\: list of    :py:class:`ClassMapCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.ClassMapCfgs.ClassMapCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.ClassMapCfgs, self).__init__()

                    self.yang_name = "class-map-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.class_map_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.ClassMapCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.ClassMapCfgs, self).__setattr__(name, value)


                class ClassMapCfg(Entity):
                    """
                    Match Type cls\-map Name 
                    configuration
                    
                    .. attribute:: class_map_name  <key>
                    
                    	
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.ClassMapCfgs.ClassMapCfg, self).__init__()

                        self.yang_name = "class-map-cfg"
                        self.yang_parent_name = "class-map-cfgs"

                        self.class_map_name = YLeaf(YType.str, "class-map-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("class_map_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.ClassMapCfgs.ClassMapCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.ClassMapCfgs.ClassMapCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return self.class_map_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.class_map_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "class-map-cfg" + "[class-map-name='" + self.class_map_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.class_map_name.is_set or self.class_map_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.class_map_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "class-map-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "class-map-name"):
                            self.class_map_name = value
                            self.class_map_name.value_namespace = name_space
                            self.class_map_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.class_map_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.class_map_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:class-map-cfgs" + path_buffer

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

                    if (child_yang_name == "class-map-cfg"):
                        for c in self.class_map_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.ClassMapCfgs.ClassMapCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.class_map_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "class-map-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class MetadataCfg(Entity):
                """
                Match Type Metadata
                
                .. attribute:: cac
                
                	Metadata CAC value
                	**type**\:   :py:class:`Cac <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.MetadataCfg.Cac>`
                
                .. attribute:: called_uri
                
                	Metadata called\-uri value
                	**type**\:  str
                
                .. attribute:: calling_uri
                
                	Metadata calling\-uri value
                	**type**\:  str
                
                .. attribute:: device_model
                
                	Metadata device\-model value
                	**type**\:  str
                
                .. attribute:: global_session_id
                
                	Metadata global session ID
                	**type**\:  str
                
                .. attribute:: multi_party_session_id
                
                	Metadata multi\-party\-session ID
                	**type**\:  str
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.MetadataCfg, self).__init__()

                    self.yang_name = "metadata-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.cac = YLeaf(YType.enumeration, "cac")

                    self.called_uri = YLeaf(YType.str, "called-uri")

                    self.calling_uri = YLeaf(YType.str, "calling-uri")

                    self.device_model = YLeaf(YType.str, "device-model")

                    self.global_session_id = YLeaf(YType.str, "global-session-id")

                    self.multi_party_session_id = YLeaf(YType.str, "multi-party-session-id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("cac",
                                    "called_uri",
                                    "calling_uri",
                                    "device_model",
                                    "global_session_id",
                                    "multi_party_session_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.MetadataCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.MetadataCfg, self).__setattr__(name, value)

                class Cac(Enum):
                    """
                    Cac

                    Metadata CAC value

                    .. data:: addmitted = 0

                    .. data:: un_addmitted = 1

                    """

                    addmitted = Enum.YLeaf(0, "addmitted")

                    un_addmitted = Enum.YLeaf(1, "un-addmitted")


                def has_data(self):
                    return (
                        self.cac.is_set or
                        self.called_uri.is_set or
                        self.calling_uri.is_set or
                        self.device_model.is_set or
                        self.global_session_id.is_set or
                        self.multi_party_session_id.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.cac.yfilter != YFilter.not_set or
                        self.called_uri.yfilter != YFilter.not_set or
                        self.calling_uri.yfilter != YFilter.not_set or
                        self.device_model.yfilter != YFilter.not_set or
                        self.global_session_id.yfilter != YFilter.not_set or
                        self.multi_party_session_id.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:metadata-cfg" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.cac.is_set or self.cac.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cac.get_name_leafdata())
                    if (self.called_uri.is_set or self.called_uri.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.called_uri.get_name_leafdata())
                    if (self.calling_uri.is_set or self.calling_uri.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.calling_uri.get_name_leafdata())
                    if (self.device_model.is_set or self.device_model.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.device_model.get_name_leafdata())
                    if (self.global_session_id.is_set or self.global_session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.global_session_id.get_name_leafdata())
                    if (self.multi_party_session_id.is_set or self.multi_party_session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.multi_party_session_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "cac" or name == "called-uri" or name == "calling-uri" or name == "device-model" or name == "global-session-id" or name == "multi-party-session-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "cac"):
                        self.cac = value
                        self.cac.value_namespace = name_space
                        self.cac.value_namespace_prefix = name_space_prefix
                    if(value_path == "called-uri"):
                        self.called_uri = value
                        self.called_uri.value_namespace = name_space
                        self.called_uri.value_namespace_prefix = name_space_prefix
                    if(value_path == "calling-uri"):
                        self.calling_uri = value
                        self.calling_uri.value_namespace = name_space
                        self.calling_uri.value_namespace_prefix = name_space_prefix
                    if(value_path == "device-model"):
                        self.device_model = value
                        self.device_model.value_namespace = name_space
                        self.device_model.value_namespace_prefix = name_space_prefix
                    if(value_path == "global-session-id"):
                        self.global_session_id = value
                        self.global_session_id.value_namespace = name_space
                        self.global_session_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "multi-party-session-id"):
                        self.multi_party_session_id = value
                        self.multi_party_session_id.value_namespace = name_space
                        self.multi_party_session_id.value_namespace_prefix = name_space_prefix


            class ApplicationCfgs(Entity):
                """
                Match Type Application
                
                .. attribute:: application_cfg
                
                	Match Type Application  configuration
                	**type**\: list of    :py:class:`ApplicationCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.ApplicationCfgs.ApplicationCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.ApplicationCfgs, self).__init__()

                    self.yang_name = "application-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.application_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.ApplicationCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.ApplicationCfgs, self).__setattr__(name, value)


                class ApplicationCfg(Entity):
                    """
                    Match Type Application 
                    configuration
                    
                    .. attribute:: application_name  <key>
                    
                    	
                    	**type**\:  str
                    
                    .. attribute:: application_cfg  <key>
                    
                    	
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.ApplicationCfgs.ApplicationCfg, self).__init__()

                        self.yang_name = "application-cfg"
                        self.yang_parent_name = "application-cfgs"

                        self.application_name = YLeaf(YType.str, "application-name")

                        self.application_cfg = YLeaf(YType.str, "application-cfg")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("application_name",
                                        "application_cfg") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.ApplicationCfgs.ApplicationCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.ApplicationCfgs.ApplicationCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.application_name.is_set or
                            self.application_cfg.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.application_name.yfilter != YFilter.not_set or
                            self.application_cfg.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "application-cfg" + "[application-name='" + self.application_name.get() + "']" + "[application-cfg='" + self.application_cfg.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.application_name.is_set or self.application_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.application_name.get_name_leafdata())
                        if (self.application_cfg.is_set or self.application_cfg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.application_cfg.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "application-name" or name == "application-cfg"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "application-name"):
                            self.application_name = value
                            self.application_name.value_namespace = name_space
                            self.application_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "application-cfg"):
                            self.application_cfg = value
                            self.application_cfg.value_namespace = name_space
                            self.application_cfg.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.application_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.application_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:application-cfgs" + path_buffer

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

                    if (child_yang_name == "application-cfg"):
                        for c in self.application_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.ApplicationCfgs.ApplicationCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.application_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "application-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class SecurityGroup(Entity):
                """
                Match Type security tag.
                
                .. attribute:: security_group_name_cfgs
                
                	Match Type security  group based on name
                	**type**\:   :py:class:`SecurityGroupNameCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupNameCfgs>`
                
                .. attribute:: security_group_tag_cfgs
                
                	Match Type security  group based on tag
                	**type**\:   :py:class:`SecurityGroupTagCfgs <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupTagCfgs>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.SecurityGroup, self).__init__()

                    self.yang_name = "security-group"
                    self.yang_parent_name = "filter-entry"

                    self.security_group_name_cfgs = Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupNameCfgs()
                    self.security_group_name_cfgs.parent = self
                    self._children_name_map["security_group_name_cfgs"] = "security-group-name-cfgs"
                    self._children_yang_names.add("security-group-name-cfgs")

                    self.security_group_tag_cfgs = Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupTagCfgs()
                    self.security_group_tag_cfgs.parent = self
                    self._children_name_map["security_group_tag_cfgs"] = "security-group-tag-cfgs"
                    self._children_yang_names.add("security-group-tag-cfgs")


                class SecurityGroupNameCfgs(Entity):
                    """
                    Match Type security 
                    group based on name
                    
                    .. attribute:: security_group_name_cfg
                    
                    	Match Type security  group based on name configuration
                    	**type**\: list of    :py:class:`SecurityGroupNameCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupNameCfgs.SecurityGroupNameCfg>`
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupNameCfgs, self).__init__()

                        self.yang_name = "security-group-name-cfgs"
                        self.yang_parent_name = "security-group"

                        self.security_group_name_cfg = YList(self)

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
                                    super(Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupNameCfgs, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupNameCfgs, self).__setattr__(name, value)


                    class SecurityGroupNameCfg(Entity):
                        """
                        Match Type security 
                        group based on name configuration
                        
                        .. attribute:: src_dst  <key>
                        
                        	Security group name source and  destination values
                        	**type**\:   :py:class:`SrcDst <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupNameCfgs.SecurityGroupNameCfg.SrcDst>`
                        
                        .. attribute:: security_name  <key>
                        
                        	Security group name value
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'cisco-filter'
                        _revision = '2016-03-30'

                        def __init__(self):
                            super(Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupNameCfgs.SecurityGroupNameCfg, self).__init__()

                            self.yang_name = "security-group-name-cfg"
                            self.yang_parent_name = "security-group-name-cfgs"

                            self.src_dst = YLeaf(YType.enumeration, "src-dst")

                            self.security_name = YLeaf(YType.str, "security-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("src_dst",
                                            "security_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupNameCfgs.SecurityGroupNameCfg, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupNameCfgs.SecurityGroupNameCfg, self).__setattr__(name, value)

                        class SrcDst(Enum):
                            """
                            SrcDst

                            Security group name source and 

                            destination values

                            .. data:: source = 0

                            .. data:: destination = 1

                            """

                            source = Enum.YLeaf(0, "source")

                            destination = Enum.YLeaf(1, "destination")


                        def has_data(self):
                            return (
                                self.src_dst.is_set or
                                self.security_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.src_dst.yfilter != YFilter.not_set or
                                self.security_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "security-group-name-cfg" + "[src-dst='" + self.src_dst.get() + "']" + "[security-name='" + self.security_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.src_dst.is_set or self.src_dst.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.src_dst.get_name_leafdata())
                            if (self.security_name.is_set or self.security_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.security_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "src-dst" or name == "security-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "src-dst"):
                                self.src_dst = value
                                self.src_dst.value_namespace = name_space
                                self.src_dst.value_namespace_prefix = name_space_prefix
                            if(value_path == "security-name"):
                                self.security_name = value
                                self.security_name.value_namespace = name_space
                                self.security_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.security_group_name_cfg:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.security_group_name_cfg:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "security-group-name-cfgs" + path_buffer

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

                        if (child_yang_name == "security-group-name-cfg"):
                            for c in self.security_group_name_cfg:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupNameCfgs.SecurityGroupNameCfg()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.security_group_name_cfg.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "security-group-name-cfg"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class SecurityGroupTagCfgs(Entity):
                    """
                    Match Type security 
                    group based on tag
                    
                    .. attribute:: security_group_tag_cfg
                    
                    	Match Type security  group based on tag configuration
                    	**type**\: list of    :py:class:`SecurityGroupTagCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupTagCfgs.SecurityGroupTagCfg>`
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupTagCfgs, self).__init__()

                        self.yang_name = "security-group-tag-cfgs"
                        self.yang_parent_name = "security-group"

                        self.security_group_tag_cfg = YList(self)

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
                                    super(Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupTagCfgs, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupTagCfgs, self).__setattr__(name, value)


                    class SecurityGroupTagCfg(Entity):
                        """
                        Match Type security 
                        group based on tag configuration
                        
                        .. attribute:: id  <key>
                        
                        	Security group tag ID
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'cisco-filter'
                        _revision = '2016-03-30'

                        def __init__(self):
                            super(Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupTagCfgs.SecurityGroupTagCfg, self).__init__()

                            self.yang_name = "security-group-tag-cfg"
                            self.yang_parent_name = "security-group-tag-cfgs"

                            self.id = YLeaf(YType.str, "id")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupTagCfgs.SecurityGroupTagCfg, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupTagCfgs.SecurityGroupTagCfg, self).__setattr__(name, value)

                        def has_data(self):
                            return self.id.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "security-group-tag-cfg" + "[id='" + self.id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "id"):
                                self.id = value
                                self.id.value_namespace = name_space
                                self.id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.security_group_tag_cfg:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.security_group_tag_cfg:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "security-group-tag-cfgs" + path_buffer

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

                        if (child_yang_name == "security-group-tag-cfg"):
                            for c in self.security_group_tag_cfg:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupTagCfgs.SecurityGroupTagCfg()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.security_group_tag_cfg.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "security-group-tag-cfg"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.security_group_name_cfgs is not None and self.security_group_name_cfgs.has_data()) or
                        (self.security_group_tag_cfgs is not None and self.security_group_tag_cfgs.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.security_group_name_cfgs is not None and self.security_group_name_cfgs.has_operation()) or
                        (self.security_group_tag_cfgs is not None and self.security_group_tag_cfgs.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:security-group" + path_buffer

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

                    if (child_yang_name == "security-group-name-cfgs"):
                        if (self.security_group_name_cfgs is None):
                            self.security_group_name_cfgs = Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupNameCfgs()
                            self.security_group_name_cfgs.parent = self
                            self._children_name_map["security_group_name_cfgs"] = "security-group-name-cfgs"
                        return self.security_group_name_cfgs

                    if (child_yang_name == "security-group-tag-cfgs"):
                        if (self.security_group_tag_cfgs is None):
                            self.security_group_tag_cfgs = Classifiers.ClassifierEntry.FilterEntry.SecurityGroup.SecurityGroupTagCfgs()
                            self.security_group_tag_cfgs.parent = self
                            self._children_name_map["security_group_tag_cfgs"] = "security-group-tag-cfgs"
                        return self.security_group_tag_cfgs

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "security-group-name-cfgs" or name == "security-group-tag-cfgs"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class IpRtpCfgs(Entity):
                """
                Match Type IP RTP.
                
                .. attribute:: ip_rtp_cfg
                
                	Match Type IP RTP configuration
                	**type**\: list of    :py:class:`IpRtpCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.IpRtpCfgs.IpRtpCfg>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.IpRtpCfgs, self).__init__()

                    self.yang_name = "ip-rtp-cfgs"
                    self.yang_parent_name = "filter-entry"

                    self.ip_rtp_cfg = YList(self)

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
                                super(Classifiers.ClassifierEntry.FilterEntry.IpRtpCfgs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.IpRtpCfgs, self).__setattr__(name, value)


                class IpRtpCfg(Entity):
                    """
                    Match Type IP RTP configuration.
                    
                    .. attribute:: starting_port_number  <key>
                    
                    	The starting RTP port number.  Values range from 2000 to 65535
                    	**type**\:  int
                    
                    	**range:** 2000..65535
                    
                    .. attribute:: port_range  <key>
                    
                    	The RTP port number range.  Values range from 0 to 16383
                    	**type**\:  int
                    
                    	**range:** 2000..65535
                    
                    

                    """

                    _prefix = 'cisco-filter'
                    _revision = '2016-03-30'

                    def __init__(self):
                        super(Classifiers.ClassifierEntry.FilterEntry.IpRtpCfgs.IpRtpCfg, self).__init__()

                        self.yang_name = "ip-rtp-cfg"
                        self.yang_parent_name = "ip-rtp-cfgs"

                        self.starting_port_number = YLeaf(YType.uint16, "starting-port-number")

                        self.port_range = YLeaf(YType.uint16, "port-range")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("starting_port_number",
                                        "port_range") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Classifiers.ClassifierEntry.FilterEntry.IpRtpCfgs.IpRtpCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Classifiers.ClassifierEntry.FilterEntry.IpRtpCfgs.IpRtpCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.starting_port_number.is_set or
                            self.port_range.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.starting_port_number.yfilter != YFilter.not_set or
                            self.port_range.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ip-rtp-cfg" + "[starting-port-number='" + self.starting_port_number.get() + "']" + "[port-range='" + self.port_range.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.starting_port_number.is_set or self.starting_port_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.starting_port_number.get_name_leafdata())
                        if (self.port_range.is_set or self.port_range.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port_range.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "starting-port-number" or name == "port-range"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "starting-port-number"):
                            self.starting_port_number = value
                            self.starting_port_number.value_namespace = name_space
                            self.starting_port_number.value_namespace_prefix = name_space_prefix
                        if(value_path == "port-range"):
                            self.port_range = value
                            self.port_range.value_namespace = name_space
                            self.port_range.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ip_rtp_cfg:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ip_rtp_cfg:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:ip-rtp-cfgs" + path_buffer

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

                    if (child_yang_name == "ip-rtp-cfg"):
                        for c in self.ip_rtp_cfg:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Classifiers.ClassifierEntry.FilterEntry.IpRtpCfgs.IpRtpCfg()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ip_rtp_cfg.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip-rtp-cfg"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class VplsCfg(Entity):
                """
                Match Type VPLS.
                
                .. attribute:: broadcast
                
                	Broadcast value
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: known
                
                	Known value
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: multicast
                
                	Multicast value
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: unknown
                
                	Unknown value
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'cisco-filter'
                _revision = '2016-03-30'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.VplsCfg, self).__init__()

                    self.yang_name = "vpls-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.broadcast = YLeaf(YType.empty, "broadcast")

                    self.known = YLeaf(YType.empty, "known")

                    self.multicast = YLeaf(YType.empty, "multicast")

                    self.unknown = YLeaf(YType.empty, "unknown")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("broadcast",
                                    "known",
                                    "multicast",
                                    "unknown") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.VplsCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.VplsCfg, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.broadcast.is_set or
                        self.known.is_set or
                        self.multicast.is_set or
                        self.unknown.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.broadcast.yfilter != YFilter.not_set or
                        self.known.yfilter != YFilter.not_set or
                        self.multicast.yfilter != YFilter.not_set or
                        self.unknown.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cisco-policy-filters:vpls-cfg" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.broadcast.is_set or self.broadcast.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.broadcast.get_name_leafdata())
                    if (self.known.is_set or self.known.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.known.get_name_leafdata())
                    if (self.multicast.is_set or self.multicast.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.multicast.get_name_leafdata())
                    if (self.unknown.is_set or self.unknown.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unknown.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "broadcast" or name == "known" or name == "multicast" or name == "unknown"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "broadcast"):
                        self.broadcast = value
                        self.broadcast.value_namespace = name_space
                        self.broadcast.value_namespace_prefix = name_space_prefix
                    if(value_path == "known"):
                        self.known = value
                        self.known.value_namespace = name_space
                        self.known.value_namespace_prefix = name_space_prefix
                    if(value_path == "multicast"):
                        self.multicast = value
                        self.multicast.value_namespace = name_space
                        self.multicast.value_namespace_prefix = name_space_prefix
                    if(value_path == "unknown"):
                        self.unknown = value
                        self.unknown.value_namespace = name_space
                        self.unknown.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.destination_ip_address_cfg:
                    if (c.has_data()):
                        return True
                for c in self.destination_port_cfg:
                    if (c.has_data()):
                        return True
                for c in self.dscp_cfg:
                    if (c.has_data()):
                        return True
                for c in self.protocol_cfg:
                    if (c.has_data()):
                        return True
                for c in self.source_ip_address_cfg:
                    if (c.has_data()):
                        return True
                for c in self.source_port_cfg:
                    if (c.has_data()):
                        return True
                return (
                    self.filter_type.is_set or
                    self.filter_logical_not.is_set or
                    (self.application_cfgs is not None and self.application_cfgs.has_data()) or
                    (self.atm_clp_cfg is not None and self.atm_clp_cfg.has_data()) or
                    (self.atm_vci_cfgs is not None and self.atm_vci_cfgs.has_data()) or
                    (self.class_map_cfgs is not None and self.class_map_cfgs.has_data()) or
                    (self.cos_cfgs is not None and self.cos_cfgs.has_data()) or
                    (self.cos_inner_cfgs is not None and self.cos_inner_cfgs.has_data()) or
                    (self.dei_cfg is not None and self.dei_cfg.has_data()) or
                    (self.dei_inner_cfg is not None and self.dei_inner_cfg.has_data()) or
                    (self.discard_class_cfgs is not None and self.discard_class_cfgs.has_data()) or
                    (self.dst_mac_cfgs is not None and self.dst_mac_cfgs.has_data()) or
                    (self.flow_ip_cfg is not None and self.flow_ip_cfg.has_data()) or
                    (self.flow_record_cfg is not None and self.flow_record_cfg.has_data()) or
                    (self.fr_de_cfg is not None and self.fr_de_cfg.has_data()) or
                    (self.fr_dlci_cfgs is not None and self.fr_dlci_cfgs.has_data()) or
                    (self.input_interface_cfgs is not None and self.input_interface_cfgs.has_data()) or
                    (self.ip_rtp_cfgs is not None and self.ip_rtp_cfgs.has_data()) or
                    (self.ipv4_acl_cfgs is not None and self.ipv4_acl_cfgs.has_data()) or
                    (self.ipv4_acl_name_cfgs is not None and self.ipv4_acl_name_cfgs.has_data()) or
                    (self.ipv6_acl_cfgs is not None and self.ipv6_acl_cfgs.has_data()) or
                    (self.ipv6_acl_name_cfgs is not None and self.ipv6_acl_name_cfgs.has_data()) or
                    (self.metadata_cfg is not None and self.metadata_cfg.has_data()) or
                    (self.mpls_exp_imp_cfgs is not None and self.mpls_exp_imp_cfgs.has_data()) or
                    (self.mpls_exp_top_cfgs is not None and self.mpls_exp_top_cfgs.has_data()) or
                    (self.pkt_len_cfgs is not None and self.pkt_len_cfgs.has_data()) or
                    (self.prec is not None and self.prec.has_data()) or
                    (self.protocol_name_cfgs is not None and self.protocol_name_cfgs.has_data()) or
                    (self.qos_group_cfgs is not None and self.qos_group_cfgs.has_data()) or
                    (self.security_group is not None and self.security_group.has_data()) or
                    (self.src_mac_cfgs is not None and self.src_mac_cfgs.has_data()) or
                    (self.vlan_cfgs is not None and self.vlan_cfgs.has_data()) or
                    (self.vlan_inner_cfgs is not None and self.vlan_inner_cfgs.has_data()) or
                    (self.vpls_cfg is not None and self.vpls_cfg.has_data()) or
                    (self.wlan_user_priority_cfgs is not None and self.wlan_user_priority_cfgs.has_data()))

            def has_operation(self):
                for c in self.destination_ip_address_cfg:
                    if (c.has_operation()):
                        return True
                for c in self.destination_port_cfg:
                    if (c.has_operation()):
                        return True
                for c in self.dscp_cfg:
                    if (c.has_operation()):
                        return True
                for c in self.protocol_cfg:
                    if (c.has_operation()):
                        return True
                for c in self.source_ip_address_cfg:
                    if (c.has_operation()):
                        return True
                for c in self.source_port_cfg:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.filter_type.yfilter != YFilter.not_set or
                    self.filter_logical_not.yfilter != YFilter.not_set or
                    (self.application_cfgs is not None and self.application_cfgs.has_operation()) or
                    (self.atm_clp_cfg is not None and self.atm_clp_cfg.has_operation()) or
                    (self.atm_vci_cfgs is not None and self.atm_vci_cfgs.has_operation()) or
                    (self.class_map_cfgs is not None and self.class_map_cfgs.has_operation()) or
                    (self.cos_cfgs is not None and self.cos_cfgs.has_operation()) or
                    (self.cos_inner_cfgs is not None and self.cos_inner_cfgs.has_operation()) or
                    (self.dei_cfg is not None and self.dei_cfg.has_operation()) or
                    (self.dei_inner_cfg is not None and self.dei_inner_cfg.has_operation()) or
                    (self.discard_class_cfgs is not None and self.discard_class_cfgs.has_operation()) or
                    (self.dst_mac_cfgs is not None and self.dst_mac_cfgs.has_operation()) or
                    (self.flow_ip_cfg is not None and self.flow_ip_cfg.has_operation()) or
                    (self.flow_record_cfg is not None and self.flow_record_cfg.has_operation()) or
                    (self.fr_de_cfg is not None and self.fr_de_cfg.has_operation()) or
                    (self.fr_dlci_cfgs is not None and self.fr_dlci_cfgs.has_operation()) or
                    (self.input_interface_cfgs is not None and self.input_interface_cfgs.has_operation()) or
                    (self.ip_rtp_cfgs is not None and self.ip_rtp_cfgs.has_operation()) or
                    (self.ipv4_acl_cfgs is not None and self.ipv4_acl_cfgs.has_operation()) or
                    (self.ipv4_acl_name_cfgs is not None and self.ipv4_acl_name_cfgs.has_operation()) or
                    (self.ipv6_acl_cfgs is not None and self.ipv6_acl_cfgs.has_operation()) or
                    (self.ipv6_acl_name_cfgs is not None and self.ipv6_acl_name_cfgs.has_operation()) or
                    (self.metadata_cfg is not None and self.metadata_cfg.has_operation()) or
                    (self.mpls_exp_imp_cfgs is not None and self.mpls_exp_imp_cfgs.has_operation()) or
                    (self.mpls_exp_top_cfgs is not None and self.mpls_exp_top_cfgs.has_operation()) or
                    (self.pkt_len_cfgs is not None and self.pkt_len_cfgs.has_operation()) or
                    (self.prec is not None and self.prec.has_operation()) or
                    (self.protocol_name_cfgs is not None and self.protocol_name_cfgs.has_operation()) or
                    (self.qos_group_cfgs is not None and self.qos_group_cfgs.has_operation()) or
                    (self.security_group is not None and self.security_group.has_operation()) or
                    (self.src_mac_cfgs is not None and self.src_mac_cfgs.has_operation()) or
                    (self.vlan_cfgs is not None and self.vlan_cfgs.has_operation()) or
                    (self.vlan_inner_cfgs is not None and self.vlan_inner_cfgs.has_operation()) or
                    (self.vpls_cfg is not None and self.vpls_cfg.has_operation()) or
                    (self.wlan_user_priority_cfgs is not None and self.wlan_user_priority_cfgs.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "filter-entry" + "[filter-type='" + self.filter_type.get() + "']" + "[filter-logical-not='" + self.filter_logical_not.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.filter_type.is_set or self.filter_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filter_type.get_name_leafdata())
                if (self.filter_logical_not.is_set or self.filter_logical_not.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filter_logical_not.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "application-cfgs"):
                    if (self.application_cfgs is None):
                        self.application_cfgs = Classifiers.ClassifierEntry.FilterEntry.ApplicationCfgs()
                        self.application_cfgs.parent = self
                        self._children_name_map["application_cfgs"] = "application-cfgs"
                    return self.application_cfgs

                if (child_yang_name == "atm-clp-cfg"):
                    if (self.atm_clp_cfg is None):
                        self.atm_clp_cfg = Classifiers.ClassifierEntry.FilterEntry.AtmClpCfg()
                        self.atm_clp_cfg.parent = self
                        self._children_name_map["atm_clp_cfg"] = "atm-clp-cfg"
                    return self.atm_clp_cfg

                if (child_yang_name == "atm-vci-cfgs"):
                    if (self.atm_vci_cfgs is None):
                        self.atm_vci_cfgs = Classifiers.ClassifierEntry.FilterEntry.AtmVciCfgs()
                        self.atm_vci_cfgs.parent = self
                        self._children_name_map["atm_vci_cfgs"] = "atm-vci-cfgs"
                    return self.atm_vci_cfgs

                if (child_yang_name == "class-map-cfgs"):
                    if (self.class_map_cfgs is None):
                        self.class_map_cfgs = Classifiers.ClassifierEntry.FilterEntry.ClassMapCfgs()
                        self.class_map_cfgs.parent = self
                        self._children_name_map["class_map_cfgs"] = "class-map-cfgs"
                    return self.class_map_cfgs

                if (child_yang_name == "cos-cfgs"):
                    if (self.cos_cfgs is None):
                        self.cos_cfgs = Classifiers.ClassifierEntry.FilterEntry.CosCfgs()
                        self.cos_cfgs.parent = self
                        self._children_name_map["cos_cfgs"] = "cos-cfgs"
                    return self.cos_cfgs

                if (child_yang_name == "cos-inner-cfgs"):
                    if (self.cos_inner_cfgs is None):
                        self.cos_inner_cfgs = Classifiers.ClassifierEntry.FilterEntry.CosInnerCfgs()
                        self.cos_inner_cfgs.parent = self
                        self._children_name_map["cos_inner_cfgs"] = "cos-inner-cfgs"
                    return self.cos_inner_cfgs

                if (child_yang_name == "dei-cfg"):
                    if (self.dei_cfg is None):
                        self.dei_cfg = Classifiers.ClassifierEntry.FilterEntry.DeiCfg()
                        self.dei_cfg.parent = self
                        self._children_name_map["dei_cfg"] = "dei-cfg"
                    return self.dei_cfg

                if (child_yang_name == "dei-inner-cfg"):
                    if (self.dei_inner_cfg is None):
                        self.dei_inner_cfg = Classifiers.ClassifierEntry.FilterEntry.DeiInnerCfg()
                        self.dei_inner_cfg.parent = self
                        self._children_name_map["dei_inner_cfg"] = "dei-inner-cfg"
                    return self.dei_inner_cfg

                if (child_yang_name == "destination-ip-address-cfg"):
                    for c in self.destination_ip_address_cfg:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.destination_ip_address_cfg.append(c)
                    return c

                if (child_yang_name == "destination-port-cfg"):
                    for c in self.destination_port_cfg:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.destination_port_cfg.append(c)
                    return c

                if (child_yang_name == "discard-class-cfgs"):
                    if (self.discard_class_cfgs is None):
                        self.discard_class_cfgs = Classifiers.ClassifierEntry.FilterEntry.DiscardClassCfgs()
                        self.discard_class_cfgs.parent = self
                        self._children_name_map["discard_class_cfgs"] = "discard-class-cfgs"
                    return self.discard_class_cfgs

                if (child_yang_name == "dscp-cfg"):
                    for c in self.dscp_cfg:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Classifiers.ClassifierEntry.FilterEntry.DscpCfg()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.dscp_cfg.append(c)
                    return c

                if (child_yang_name == "dst-mac-cfgs"):
                    if (self.dst_mac_cfgs is None):
                        self.dst_mac_cfgs = Classifiers.ClassifierEntry.FilterEntry.DstMacCfgs()
                        self.dst_mac_cfgs.parent = self
                        self._children_name_map["dst_mac_cfgs"] = "dst-mac-cfgs"
                    return self.dst_mac_cfgs

                if (child_yang_name == "flow-ip-cfg"):
                    if (self.flow_ip_cfg is None):
                        self.flow_ip_cfg = Classifiers.ClassifierEntry.FilterEntry.FlowIpCfg()
                        self.flow_ip_cfg.parent = self
                        self._children_name_map["flow_ip_cfg"] = "flow-ip-cfg"
                    return self.flow_ip_cfg

                if (child_yang_name == "flow-record-cfg"):
                    if (self.flow_record_cfg is None):
                        self.flow_record_cfg = Classifiers.ClassifierEntry.FilterEntry.FlowRecordCfg()
                        self.flow_record_cfg.parent = self
                        self._children_name_map["flow_record_cfg"] = "flow-record-cfg"
                    return self.flow_record_cfg

                if (child_yang_name == "fr-de-cfg"):
                    if (self.fr_de_cfg is None):
                        self.fr_de_cfg = Classifiers.ClassifierEntry.FilterEntry.FrDeCfg()
                        self.fr_de_cfg.parent = self
                        self._children_name_map["fr_de_cfg"] = "fr-de-cfg"
                    return self.fr_de_cfg

                if (child_yang_name == "fr-dlci-cfgs"):
                    if (self.fr_dlci_cfgs is None):
                        self.fr_dlci_cfgs = Classifiers.ClassifierEntry.FilterEntry.FrDlciCfgs()
                        self.fr_dlci_cfgs.parent = self
                        self._children_name_map["fr_dlci_cfgs"] = "fr-dlci-cfgs"
                    return self.fr_dlci_cfgs

                if (child_yang_name == "input-interface-cfgs"):
                    if (self.input_interface_cfgs is None):
                        self.input_interface_cfgs = Classifiers.ClassifierEntry.FilterEntry.InputInterfaceCfgs()
                        self.input_interface_cfgs.parent = self
                        self._children_name_map["input_interface_cfgs"] = "input-interface-cfgs"
                    return self.input_interface_cfgs

                if (child_yang_name == "ip-rtp-cfgs"):
                    if (self.ip_rtp_cfgs is None):
                        self.ip_rtp_cfgs = Classifiers.ClassifierEntry.FilterEntry.IpRtpCfgs()
                        self.ip_rtp_cfgs.parent = self
                        self._children_name_map["ip_rtp_cfgs"] = "ip-rtp-cfgs"
                    return self.ip_rtp_cfgs

                if (child_yang_name == "ipv4-acl-cfgs"):
                    if (self.ipv4_acl_cfgs is None):
                        self.ipv4_acl_cfgs = Classifiers.ClassifierEntry.FilterEntry.Ipv4AclCfgs()
                        self.ipv4_acl_cfgs.parent = self
                        self._children_name_map["ipv4_acl_cfgs"] = "ipv4-acl-cfgs"
                    return self.ipv4_acl_cfgs

                if (child_yang_name == "ipv4-acl-name-cfgs"):
                    if (self.ipv4_acl_name_cfgs is None):
                        self.ipv4_acl_name_cfgs = Classifiers.ClassifierEntry.FilterEntry.Ipv4AclNameCfgs()
                        self.ipv4_acl_name_cfgs.parent = self
                        self._children_name_map["ipv4_acl_name_cfgs"] = "ipv4-acl-name-cfgs"
                    return self.ipv4_acl_name_cfgs

                if (child_yang_name == "ipv6-acl-cfgs"):
                    if (self.ipv6_acl_cfgs is None):
                        self.ipv6_acl_cfgs = Classifiers.ClassifierEntry.FilterEntry.Ipv6AclCfgs()
                        self.ipv6_acl_cfgs.parent = self
                        self._children_name_map["ipv6_acl_cfgs"] = "ipv6-acl-cfgs"
                    return self.ipv6_acl_cfgs

                if (child_yang_name == "ipv6-acl-name-cfgs"):
                    if (self.ipv6_acl_name_cfgs is None):
                        self.ipv6_acl_name_cfgs = Classifiers.ClassifierEntry.FilterEntry.Ipv6AclNameCfgs()
                        self.ipv6_acl_name_cfgs.parent = self
                        self._children_name_map["ipv6_acl_name_cfgs"] = "ipv6-acl-name-cfgs"
                    return self.ipv6_acl_name_cfgs

                if (child_yang_name == "metadata-cfg"):
                    if (self.metadata_cfg is None):
                        self.metadata_cfg = Classifiers.ClassifierEntry.FilterEntry.MetadataCfg()
                        self.metadata_cfg.parent = self
                        self._children_name_map["metadata_cfg"] = "metadata-cfg"
                    return self.metadata_cfg

                if (child_yang_name == "mpls-exp-imp-cfgs"):
                    if (self.mpls_exp_imp_cfgs is None):
                        self.mpls_exp_imp_cfgs = Classifiers.ClassifierEntry.FilterEntry.MplsExpImpCfgs()
                        self.mpls_exp_imp_cfgs.parent = self
                        self._children_name_map["mpls_exp_imp_cfgs"] = "mpls-exp-imp-cfgs"
                    return self.mpls_exp_imp_cfgs

                if (child_yang_name == "mpls-exp-top-cfgs"):
                    if (self.mpls_exp_top_cfgs is None):
                        self.mpls_exp_top_cfgs = Classifiers.ClassifierEntry.FilterEntry.MplsExpTopCfgs()
                        self.mpls_exp_top_cfgs.parent = self
                        self._children_name_map["mpls_exp_top_cfgs"] = "mpls-exp-top-cfgs"
                    return self.mpls_exp_top_cfgs

                if (child_yang_name == "pkt-len-cfgs"):
                    if (self.pkt_len_cfgs is None):
                        self.pkt_len_cfgs = Classifiers.ClassifierEntry.FilterEntry.PktLenCfgs()
                        self.pkt_len_cfgs.parent = self
                        self._children_name_map["pkt_len_cfgs"] = "pkt-len-cfgs"
                    return self.pkt_len_cfgs

                if (child_yang_name == "prec"):
                    if (self.prec is None):
                        self.prec = Classifiers.ClassifierEntry.FilterEntry.Prec()
                        self.prec.parent = self
                        self._children_name_map["prec"] = "prec"
                    return self.prec

                if (child_yang_name == "protocol-cfg"):
                    for c in self.protocol_cfg:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.protocol_cfg.append(c)
                    return c

                if (child_yang_name == "protocol-name-cfgs"):
                    if (self.protocol_name_cfgs is None):
                        self.protocol_name_cfgs = Classifiers.ClassifierEntry.FilterEntry.ProtocolNameCfgs()
                        self.protocol_name_cfgs.parent = self
                        self._children_name_map["protocol_name_cfgs"] = "protocol-name-cfgs"
                    return self.protocol_name_cfgs

                if (child_yang_name == "qos-group-cfgs"):
                    if (self.qos_group_cfgs is None):
                        self.qos_group_cfgs = Classifiers.ClassifierEntry.FilterEntry.QosGroupCfgs()
                        self.qos_group_cfgs.parent = self
                        self._children_name_map["qos_group_cfgs"] = "qos-group-cfgs"
                    return self.qos_group_cfgs

                if (child_yang_name == "security-group"):
                    if (self.security_group is None):
                        self.security_group = Classifiers.ClassifierEntry.FilterEntry.SecurityGroup()
                        self.security_group.parent = self
                        self._children_name_map["security_group"] = "security-group"
                    return self.security_group

                if (child_yang_name == "source-ip-address-cfg"):
                    for c in self.source_ip_address_cfg:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.source_ip_address_cfg.append(c)
                    return c

                if (child_yang_name == "source-port-cfg"):
                    for c in self.source_port_cfg:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.source_port_cfg.append(c)
                    return c

                if (child_yang_name == "src-mac-cfgs"):
                    if (self.src_mac_cfgs is None):
                        self.src_mac_cfgs = Classifiers.ClassifierEntry.FilterEntry.SrcMacCfgs()
                        self.src_mac_cfgs.parent = self
                        self._children_name_map["src_mac_cfgs"] = "src-mac-cfgs"
                    return self.src_mac_cfgs

                if (child_yang_name == "vlan-cfgs"):
                    if (self.vlan_cfgs is None):
                        self.vlan_cfgs = Classifiers.ClassifierEntry.FilterEntry.VlanCfgs()
                        self.vlan_cfgs.parent = self
                        self._children_name_map["vlan_cfgs"] = "vlan-cfgs"
                    return self.vlan_cfgs

                if (child_yang_name == "vlan-inner-cfgs"):
                    if (self.vlan_inner_cfgs is None):
                        self.vlan_inner_cfgs = Classifiers.ClassifierEntry.FilterEntry.VlanInnerCfgs()
                        self.vlan_inner_cfgs.parent = self
                        self._children_name_map["vlan_inner_cfgs"] = "vlan-inner-cfgs"
                    return self.vlan_inner_cfgs

                if (child_yang_name == "vpls-cfg"):
                    if (self.vpls_cfg is None):
                        self.vpls_cfg = Classifiers.ClassifierEntry.FilterEntry.VplsCfg()
                        self.vpls_cfg.parent = self
                        self._children_name_map["vpls_cfg"] = "vpls-cfg"
                    return self.vpls_cfg

                if (child_yang_name == "wlan-user-priority-cfgs"):
                    if (self.wlan_user_priority_cfgs is None):
                        self.wlan_user_priority_cfgs = Classifiers.ClassifierEntry.FilterEntry.WlanUserPriorityCfgs()
                        self.wlan_user_priority_cfgs.parent = self
                        self._children_name_map["wlan_user_priority_cfgs"] = "wlan-user-priority-cfgs"
                    return self.wlan_user_priority_cfgs

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "application-cfgs" or name == "atm-clp-cfg" or name == "atm-vci-cfgs" or name == "class-map-cfgs" or name == "cos-cfgs" or name == "cos-inner-cfgs" or name == "dei-cfg" or name == "dei-inner-cfg" or name == "destination-ip-address-cfg" or name == "destination-port-cfg" or name == "discard-class-cfgs" or name == "dscp-cfg" or name == "dst-mac-cfgs" or name == "flow-ip-cfg" or name == "flow-record-cfg" or name == "fr-de-cfg" or name == "fr-dlci-cfgs" or name == "input-interface-cfgs" or name == "ip-rtp-cfgs" or name == "ipv4-acl-cfgs" or name == "ipv4-acl-name-cfgs" or name == "ipv6-acl-cfgs" or name == "ipv6-acl-name-cfgs" or name == "metadata-cfg" or name == "mpls-exp-imp-cfgs" or name == "mpls-exp-top-cfgs" or name == "pkt-len-cfgs" or name == "prec" or name == "protocol-cfg" or name == "protocol-name-cfgs" or name == "qos-group-cfgs" or name == "security-group" or name == "source-ip-address-cfg" or name == "source-port-cfg" or name == "src-mac-cfgs" or name == "vlan-cfgs" or name == "vlan-inner-cfgs" or name == "vpls-cfg" or name == "wlan-user-priority-cfgs" or name == "filter-type" or name == "filter-logical-not"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "filter-type"):
                    self.filter_type = value
                    self.filter_type.value_namespace = name_space
                    self.filter_type.value_namespace_prefix = name_space_prefix
                if(value_path == "filter-logical-not"):
                    self.filter_logical_not = value
                    self.filter_logical_not.value_namespace = name_space
                    self.filter_logical_not.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.filter_entry:
                if (c.has_data()):
                    return True
            return (
                self.classifier_entry_name.is_set or
                self.classifier_entry_descr.is_set or
                self.classifier_entry_filter_operation.is_set or
                self.classifier_entry_type.is_set)

        def has_operation(self):
            for c in self.filter_entry:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.classifier_entry_name.yfilter != YFilter.not_set or
                self.classifier_entry_descr.yfilter != YFilter.not_set or
                self.classifier_entry_filter_operation.yfilter != YFilter.not_set or
                self.classifier_entry_type.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "classifier-entry" + "[classifier-entry-name='" + self.classifier_entry_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-diffserv-classifier:classifiers/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.classifier_entry_name.is_set or self.classifier_entry_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.classifier_entry_name.get_name_leafdata())
            if (self.classifier_entry_descr.is_set or self.classifier_entry_descr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.classifier_entry_descr.get_name_leafdata())
            if (self.classifier_entry_filter_operation.is_set or self.classifier_entry_filter_operation.yfilter != YFilter.not_set):
                leaf_name_data.append(self.classifier_entry_filter_operation.get_name_leafdata())
            if (self.classifier_entry_type.is_set or self.classifier_entry_type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.classifier_entry_type.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "filter-entry"):
                for c in self.filter_entry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Classifiers.ClassifierEntry.FilterEntry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.filter_entry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "filter-entry" or name == "classifier-entry-name" or name == "classifier-entry-descr" or name == "classifier-entry-filter-operation" or name == "classifier-entry-type"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "classifier-entry-name"):
                self.classifier_entry_name = value
                self.classifier_entry_name.value_namespace = name_space
                self.classifier_entry_name.value_namespace_prefix = name_space_prefix
            if(value_path == "classifier-entry-descr"):
                self.classifier_entry_descr = value
                self.classifier_entry_descr.value_namespace = name_space
                self.classifier_entry_descr.value_namespace_prefix = name_space_prefix
            if(value_path == "classifier-entry-filter-operation"):
                self.classifier_entry_filter_operation = value
                self.classifier_entry_filter_operation.value_namespace = name_space
                self.classifier_entry_filter_operation.value_namespace_prefix = name_space_prefix
            if(value_path == "classifier-entry-type"):
                self.classifier_entry_type = value
                self.classifier_entry_type.value_namespace = name_space
                self.classifier_entry_type.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.classifier_entry:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.classifier_entry:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-diffserv-classifier:classifiers" + path_buffer

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

        if (child_yang_name == "classifier-entry"):
            for c in self.classifier_entry:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Classifiers.ClassifierEntry()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.classifier_entry.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "classifier-entry"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Classifiers()
        return self._top_entity

class MatchAllFilter(Identity):
    """
    Classifier entry filter logical AND operation
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(MatchAllFilter, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:match-all-filter")


class SourceIpAddress(Identity):
    """
    source\-ip\-address filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(SourceIpAddress, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:source-ip-address")


class Protocol(Identity):
    """
    protocol filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(Protocol, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:protocol")


class DestinationPort(Identity):
    """
    destination\-port filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(DestinationPort, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:destination-port")


class SourcePort(Identity):
    """
    source\-port filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(SourcePort, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:source-port")


class MatchAnyFilter(Identity):
    """
    Classifier entry filter logical OR operation
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(MatchAnyFilter, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:match-any-filter")


class Dscp(Identity):
    """
    DSCP filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(Dscp, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:dscp")


class DestinationIpAddress(Identity):
    """
    destination\-ip\-address filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(DestinationIpAddress, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:destination-ip-address")



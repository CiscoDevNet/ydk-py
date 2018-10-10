""" Cisco_IOS_XR_l2_eth_infra_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR l2\-eth\-infra package configuration.

This module contains definitions
for the following management objects\:
  ethernet\-features\: Ethernet Features Configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-l2vpn\-cfg
modules with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EgressFiltering(Enum):
    """
    EgressFiltering (Enum Class)

    Egress filtering

    .. data:: egress_filtering_type_strict = 1

    	Strict Egress Filtering

    .. data:: egress_filtering_type_disable = 2

    	Egress Filtering Disabled

    .. data:: egress_filtering_type_default = 3

    	Default Egress Filtering Behavior

    """

    egress_filtering_type_strict = Enum.YLeaf(1, "egress-filtering-type-strict")

    egress_filtering_type_disable = Enum.YLeaf(2, "egress-filtering-type-disable")

    egress_filtering_type_default = Enum.YLeaf(3, "egress-filtering-type-default")


class Filtering(Enum):
    """
    Filtering (Enum Class)

    Filtering

    .. data:: filtering_type_dot1q = 0

    	C-Vlan ingress frame filtering (Table 8-1 of

    	802.1ad standard)

    .. data:: filtering_type_dot1ad = 1

    	S-Vlan ingress frame filtering (Table 8-2 of

    	802.1ad standard)

    """

    filtering_type_dot1q = Enum.YLeaf(0, "filtering-type-dot1q")

    filtering_type_dot1ad = Enum.YLeaf(1, "filtering-type-dot1ad")


class L2ProtocolMode(Enum):
    """
    L2ProtocolMode (Enum Class)

    L2 protocol mode

    .. data:: forward = 0

    	Forward packets transparently

    .. data:: drop = 1

    	Drop the protocol's packets

    .. data:: tunnel = 2

    	Tunnel ingress frames, untunnel egress frames

    .. data:: reverse_tunnel = 3

    	Tunnel egress frames, untunnel ingress frames

    """

    forward = Enum.YLeaf(0, "forward")

    drop = Enum.YLeaf(1, "drop")

    tunnel = Enum.YLeaf(2, "tunnel")

    reverse_tunnel = Enum.YLeaf(3, "reverse-tunnel")


class L2ProtocolName(Enum):
    """
    L2ProtocolName (Enum Class)

    L2 protocol name

    .. data:: cdp = 0

    	CDP

    .. data:: stp = 1

    	STP

    .. data:: vtp = 2

    	VTP

    .. data:: pvst = 3

    	PVST+

    .. data:: cpsv = 4

    	CDP, PVST+, STP, and VTP

    """

    cdp = Enum.YLeaf(0, "cdp")

    stp = Enum.YLeaf(1, "stp")

    vtp = Enum.YLeaf(2, "vtp")

    pvst = Enum.YLeaf(3, "pvst")

    cpsv = Enum.YLeaf(4, "cpsv")



class EthernetFeatures(Entity):
    """
    Ethernet Features Configuration
    
    .. attribute:: egress_filtering
    
    	Egress Filtering Configuration
    	**type**\:  :py:class:`EgressFiltering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EgressFiltering>`
    
    .. attribute:: cfm
    
    	CFM global configuration
    	**type**\:  :py:class:`Cfm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm>`
    
    .. attribute:: ether_link_oam
    
    	Ethernet Link OAM Global Configuration
    	**type**\:  :py:class:`EtherLinkOam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam>`
    
    

    """

    _prefix = 'l2-eth-infra-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(EthernetFeatures, self).__init__()
        self._top_entity = None

        self.yang_name = "ethernet-features"
        self.yang_parent_name = "Cisco-IOS-XR-l2-eth-infra-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("egress-filtering", ("egress_filtering", EthernetFeatures.EgressFiltering)), ("Cisco-IOS-XR-ethernet-cfm-cfg:cfm", ("cfm", EthernetFeatures.Cfm)), ("Cisco-IOS-XR-ethernet-link-oam-cfg:ether-link-oam", ("ether_link_oam", EthernetFeatures.EtherLinkOam))])
        self._leafs = OrderedDict()

        self.egress_filtering = EthernetFeatures.EgressFiltering()
        self.egress_filtering.parent = self
        self._children_name_map["egress_filtering"] = "egress-filtering"

        self.cfm = EthernetFeatures.Cfm()
        self.cfm.parent = self
        self._children_name_map["cfm"] = "Cisco-IOS-XR-ethernet-cfm-cfg:cfm"

        self.ether_link_oam = EthernetFeatures.EtherLinkOam()
        self.ether_link_oam.parent = self
        self._children_name_map["ether_link_oam"] = "Cisco-IOS-XR-ethernet-link-oam-cfg:ether-link-oam"
        self._segment_path = lambda: "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(EthernetFeatures, [], name, value)


    class EgressFiltering(Entity):
        """
        Egress Filtering Configuration
        
        .. attribute:: egress_filtering_default_on
        
        	Whether Egress Filtering is on by default
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'l2-eth-infra-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(EthernetFeatures.EgressFiltering, self).__init__()

            self.yang_name = "egress-filtering"
            self.yang_parent_name = "ethernet-features"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('egress_filtering_default_on', (YLeaf(YType.empty, 'egress-filtering-default-on'), ['Empty'])),
            ])
            self.egress_filtering_default_on = None
            self._segment_path = lambda: "egress-filtering"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EthernetFeatures.EgressFiltering, [u'egress_filtering_default_on'], name, value)


    class Cfm(Entity):
        """
        CFM global configuration
        
        .. attribute:: traceroute_cache
        
        	Traceroute Cache Configuration
        	**type**\:  :py:class:`TracerouteCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.TracerouteCache>`
        
        .. attribute:: domains
        
        	Domain\-specific global configuration
        	**type**\:  :py:class:`Domains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains>`
        
        .. attribute:: nv_satellite_sla_processing_disable
        
        	Disable processing of Ethernet SLA packets on nV Satellite devices
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ethernet-cfm-cfg'
        _revision = '2017-10-06'

        def __init__(self):
            super(EthernetFeatures.Cfm, self).__init__()

            self.yang_name = "cfm"
            self.yang_parent_name = "ethernet-features"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("traceroute-cache", ("traceroute_cache", EthernetFeatures.Cfm.TracerouteCache)), ("domains", ("domains", EthernetFeatures.Cfm.Domains))])
            self._leafs = OrderedDict([
                ('nv_satellite_sla_processing_disable', (YLeaf(YType.empty, 'nv-satellite-sla-processing-disable'), ['Empty'])),
            ])
            self.nv_satellite_sla_processing_disable = None

            self.traceroute_cache = EthernetFeatures.Cfm.TracerouteCache()
            self.traceroute_cache.parent = self
            self._children_name_map["traceroute_cache"] = "traceroute-cache"

            self.domains = EthernetFeatures.Cfm.Domains()
            self.domains.parent = self
            self._children_name_map["domains"] = "domains"
            self._segment_path = lambda: "Cisco-IOS-XR-ethernet-cfm-cfg:cfm"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EthernetFeatures.Cfm, ['nv_satellite_sla_processing_disable'], name, value)


        class TracerouteCache(Entity):
            """
            Traceroute Cache Configuration
            
            .. attribute:: hold_time
            
            	Hold Time in minutes
            	**type**\: int
            
            	**range:** 1..525600
            
            	**default value**\: 100
            
            .. attribute:: cache_size
            
            	Cache Size limit (number of replies)
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**default value**\: 100
            
            

            """

            _prefix = 'ethernet-cfm-cfg'
            _revision = '2017-10-06'

            def __init__(self):
                super(EthernetFeatures.Cfm.TracerouteCache, self).__init__()

                self.yang_name = "traceroute-cache"
                self.yang_parent_name = "cfm"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('hold_time', (YLeaf(YType.uint32, 'hold-time'), ['int'])),
                    ('cache_size', (YLeaf(YType.uint32, 'cache-size'), ['int'])),
                ])
                self.hold_time = None
                self.cache_size = None
                self._segment_path = lambda: "traceroute-cache"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-cfm-cfg:cfm/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EthernetFeatures.Cfm.TracerouteCache, ['hold_time', 'cache_size'], name, value)


        class Domains(Entity):
            """
            Domain\-specific global configuration
            
            .. attribute:: domain
            
            	Configuration for a particular Maintenance Domain
            	**type**\: list of  		 :py:class:`Domain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain>`
            
            

            """

            _prefix = 'ethernet-cfm-cfg'
            _revision = '2017-10-06'

            def __init__(self):
                super(EthernetFeatures.Cfm.Domains, self).__init__()

                self.yang_name = "domains"
                self.yang_parent_name = "cfm"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("domain", ("domain", EthernetFeatures.Cfm.Domains.Domain))])
                self._leafs = OrderedDict()

                self.domain = YList(self)
                self._segment_path = lambda: "domains"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-cfm-cfg:cfm/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EthernetFeatures.Cfm.Domains, [], name, value)


            class Domain(Entity):
                """
                Configuration for a particular Maintenance
                Domain
                
                .. attribute:: domain  (key)
                
                	Maintenance Domain
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: services
                
                	Service\-specific global configuration
                	**type**\:  :py:class:`Services <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services>`
                
                .. attribute:: domain_properties
                
                	Fundamental properties of the domain
                	**type**\:  :py:class:`DomainProperties <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.DomainProperties>`
                
                

                """

                _prefix = 'ethernet-cfm-cfg'
                _revision = '2017-10-06'

                def __init__(self):
                    super(EthernetFeatures.Cfm.Domains.Domain, self).__init__()

                    self.yang_name = "domain"
                    self.yang_parent_name = "domains"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['domain']
                    self._child_classes = OrderedDict([("services", ("services", EthernetFeatures.Cfm.Domains.Domain.Services)), ("domain-properties", ("domain_properties", EthernetFeatures.Cfm.Domains.Domain.DomainProperties))])
                    self._leafs = OrderedDict([
                        ('domain', (YLeaf(YType.str, 'domain'), ['str'])),
                    ])
                    self.domain = None

                    self.services = EthernetFeatures.Cfm.Domains.Domain.Services()
                    self.services.parent = self
                    self._children_name_map["services"] = "services"

                    self.domain_properties = EthernetFeatures.Cfm.Domains.Domain.DomainProperties()
                    self.domain_properties.parent = self
                    self._children_name_map["domain_properties"] = "domain-properties"
                    self._segment_path = lambda: "domain" + "[domain='" + str(self.domain) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-cfm-cfg:cfm/domains/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(EthernetFeatures.Cfm.Domains.Domain, ['domain'], name, value)


                class Services(Entity):
                    """
                    Service\-specific global configuration
                    
                    .. attribute:: service
                    
                    	Configuration for a particular Service (Maintenance Association)
                    	**type**\: list of  		 :py:class:`Service <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-cfg'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(EthernetFeatures.Cfm.Domains.Domain.Services, self).__init__()

                        self.yang_name = "services"
                        self.yang_parent_name = "domain"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("service", ("service", EthernetFeatures.Cfm.Domains.Domain.Services.Service))])
                        self._leafs = OrderedDict()

                        self.service = YList(self)
                        self._segment_path = lambda: "services"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetFeatures.Cfm.Domains.Domain.Services, [], name, value)


                    class Service(Entity):
                        """
                        Configuration for a particular Service
                        (Maintenance Association)
                        
                        .. attribute:: service  (key)
                        
                        	Service (Maintenance Association)
                        	**type**\: str
                        
                        	**length:** 1..79
                        
                        .. attribute:: efd2
                        
                        	Enable EFD to bring down ports when MEPs detect errors
                        	**type**\:  :py:class:`Efd2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.Efd2>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: continuity_check_interval
                        
                        	Continuity Check Interval and Loss Threshold.  Configuring the interval enables Continuity Check
                        	**type**\:  :py:class:`ContinuityCheckInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.ContinuityCheckInterval>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: mip_auto_creation
                        
                        	MIP Auto\-creation Policy
                        	**type**\:  :py:class:`MipAutoCreation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.MipAutoCreation>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: ais
                        
                        	Service specific AIS configuration
                        	**type**\:  :py:class:`Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais>`
                        
                        .. attribute:: cross_check
                        
                        	Cross\-check configuration
                        	**type**\:  :py:class:`CrossCheck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck>`
                        
                        .. attribute:: service_properties
                        
                        	Fundamental properties of the service (maintenance association)
                        	**type**\:  :py:class:`ServiceProperties <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.ServiceProperties>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: maximum_meps
                        
                        	Limit on the number of MEPs in the service
                        	**type**\: int
                        
                        	**range:** 2..8190
                        
                        	**default value**\: 100
                        
                        .. attribute:: log_cross_check_errors
                        
                        	Log Cross\-check Errors detected for peer MEPs
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: continuity_check_archive_hold_time
                        
                        	How long to store information for peer MEPs that have timed out
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        	**default value**\: 100
                        
                        .. attribute:: tags
                        
                        	The number of tags to use when sending CFM packets from up MEPs in this Service
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: log_continuity_check_state_changes
                        
                        	Log peer MEPs state changes
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: log_efd
                        
                        	Enable logging
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: continuity_check_auto_traceroute
                        
                        	Automatically trigger a traceroute when a peer MEP times out
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: log_continuity_check_errors
                        
                        	Log CCM Errors detected for peer MEPs
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: log_ais
                        
                        	Log receipt of AIS and LCK messages
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-cfg'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(EthernetFeatures.Cfm.Domains.Domain.Services.Service, self).__init__()

                            self.yang_name = "service"
                            self.yang_parent_name = "services"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['service']
                            self._child_classes = OrderedDict([("efd2", ("efd2", EthernetFeatures.Cfm.Domains.Domain.Services.Service.Efd2)), ("continuity-check-interval", ("continuity_check_interval", EthernetFeatures.Cfm.Domains.Domain.Services.Service.ContinuityCheckInterval)), ("mip-auto-creation", ("mip_auto_creation", EthernetFeatures.Cfm.Domains.Domain.Services.Service.MipAutoCreation)), ("ais", ("ais", EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais)), ("cross-check", ("cross_check", EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck)), ("service-properties", ("service_properties", EthernetFeatures.Cfm.Domains.Domain.Services.Service.ServiceProperties))])
                            self._leafs = OrderedDict([
                                ('service', (YLeaf(YType.str, 'service'), ['str'])),
                                ('maximum_meps', (YLeaf(YType.uint32, 'maximum-meps'), ['int'])),
                                ('log_cross_check_errors', (YLeaf(YType.empty, 'log-cross-check-errors'), ['Empty'])),
                                ('continuity_check_archive_hold_time', (YLeaf(YType.uint32, 'continuity-check-archive-hold-time'), ['int'])),
                                ('tags', (YLeaf(YType.uint32, 'tags'), ['int'])),
                                ('log_continuity_check_state_changes', (YLeaf(YType.empty, 'log-continuity-check-state-changes'), ['Empty'])),
                                ('log_efd', (YLeaf(YType.empty, 'log-efd'), ['Empty'])),
                                ('continuity_check_auto_traceroute', (YLeaf(YType.empty, 'continuity-check-auto-traceroute'), ['Empty'])),
                                ('log_continuity_check_errors', (YLeaf(YType.empty, 'log-continuity-check-errors'), ['Empty'])),
                                ('log_ais', (YLeaf(YType.empty, 'log-ais'), ['Empty'])),
                            ])
                            self.service = None
                            self.maximum_meps = None
                            self.log_cross_check_errors = None
                            self.continuity_check_archive_hold_time = None
                            self.tags = None
                            self.log_continuity_check_state_changes = None
                            self.log_efd = None
                            self.continuity_check_auto_traceroute = None
                            self.log_continuity_check_errors = None
                            self.log_ais = None

                            self.efd2 = None
                            self._children_name_map["efd2"] = "efd2"

                            self.continuity_check_interval = None
                            self._children_name_map["continuity_check_interval"] = "continuity-check-interval"

                            self.mip_auto_creation = None
                            self._children_name_map["mip_auto_creation"] = "mip-auto-creation"

                            self.ais = EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais()
                            self.ais.parent = self
                            self._children_name_map["ais"] = "ais"

                            self.cross_check = EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck()
                            self.cross_check.parent = self
                            self._children_name_map["cross_check"] = "cross-check"

                            self.service_properties = None
                            self._children_name_map["service_properties"] = "service-properties"
                            self._segment_path = lambda: "service" + "[service='" + str(self.service) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EthernetFeatures.Cfm.Domains.Domain.Services.Service, ['service', 'maximum_meps', 'log_cross_check_errors', 'continuity_check_archive_hold_time', 'tags', 'log_continuity_check_state_changes', 'log_efd', 'continuity_check_auto_traceroute', 'log_continuity_check_errors', 'log_ais'], name, value)


                        class Efd2(Entity):
                            """
                            Enable EFD to bring down ports when MEPs
                            detect errors
                            
                            .. attribute:: enable
                            
                            	Enable EFD
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: protection_switching_enable
                            
                            	Enable protection switching notifications
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.Efd2, self).__init__()

                                self.yang_name = "efd2"
                                self.yang_parent_name = "service"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                    ('protection_switching_enable', (YLeaf(YType.empty, 'protection-switching-enable'), ['Empty'])),
                                ])
                                self.enable = None
                                self.protection_switching_enable = None
                                self._segment_path = lambda: "efd2"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EthernetFeatures.Cfm.Domains.Domain.Services.Service.Efd2, ['enable', 'protection_switching_enable'], name, value)


                        class ContinuityCheckInterval(Entity):
                            """
                            Continuity Check Interval and Loss
                            Threshold.  Configuring the interval
                            enables Continuity Check.
                            
                            .. attribute:: ccm_interval
                            
                            	CCM Interval
                            	**type**\:  :py:class:`CfmCcmInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes.CfmCcmInterval>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: loss_threshold
                            
                            	Loss Threshold (default 3)
                            	**type**\: int
                            
                            	**range:** 2..255
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.ContinuityCheckInterval, self).__init__()

                                self.yang_name = "continuity-check-interval"
                                self.yang_parent_name = "service"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('ccm_interval', (YLeaf(YType.enumeration, 'ccm-interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes', 'CfmCcmInterval', '')])),
                                    ('loss_threshold', (YLeaf(YType.uint32, 'loss-threshold'), ['int'])),
                                ])
                                self.ccm_interval = None
                                self.loss_threshold = None
                                self._segment_path = lambda: "continuity-check-interval"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EthernetFeatures.Cfm.Domains.Domain.Services.Service.ContinuityCheckInterval, ['ccm_interval', 'loss_threshold'], name, value)


                        class MipAutoCreation(Entity):
                            """
                            MIP Auto\-creation Policy
                            
                            .. attribute:: mip_policy
                            
                            	MIP Auto\-creation Policy
                            	**type**\:  :py:class:`CfmMipPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg.CfmMipPolicy>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ccm_learning_enable
                            
                            	Enable CCM Learning at MIPs in this service
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.MipAutoCreation, self).__init__()

                                self.yang_name = "mip-auto-creation"
                                self.yang_parent_name = "service"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('mip_policy', (YLeaf(YType.enumeration, 'mip-policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg', 'CfmMipPolicy', '')])),
                                    ('ccm_learning_enable', (YLeaf(YType.empty, 'ccm-learning-enable'), ['Empty'])),
                                ])
                                self.mip_policy = None
                                self.ccm_learning_enable = None
                                self._segment_path = lambda: "mip-auto-creation"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EthernetFeatures.Cfm.Domains.Domain.Services.Service.MipAutoCreation, ['mip_policy', 'ccm_learning_enable'], name, value)


                        class Ais(Entity):
                            """
                            Service specific AIS configuration
                            
                            .. attribute:: transmission
                            
                            	AIS transmission configuration
                            	**type**\:  :py:class:`Transmission <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais.Transmission>`
                            
                            	**presence node**\: True
                            
                            

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais, self).__init__()

                                self.yang_name = "ais"
                                self.yang_parent_name = "service"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("transmission", ("transmission", EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais.Transmission))])
                                self._leafs = OrderedDict()

                                self.transmission = None
                                self._children_name_map["transmission"] = "transmission"
                                self._segment_path = lambda: "ais"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais, [], name, value)


                            class Transmission(Entity):
                                """
                                AIS transmission configuration
                                
                                .. attribute:: ais_interval
                                
                                	AIS Interval
                                	**type**\:  :py:class:`CfmAisInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes.CfmAisInterval>`
                                
                                .. attribute:: cos
                                
                                	Class of Service bits
                                	**type**\: int
                                
                                	**range:** 0..7
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ethernet-cfm-cfg'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais.Transmission, self).__init__()

                                    self.yang_name = "transmission"
                                    self.yang_parent_name = "ais"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self.is_presence_container = True
                                    self._leafs = OrderedDict([
                                        ('ais_interval', (YLeaf(YType.enumeration, 'ais-interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes', 'CfmAisInterval', '')])),
                                        ('cos', (YLeaf(YType.uint32, 'cos'), ['int'])),
                                    ])
                                    self.ais_interval = None
                                    self.cos = None
                                    self._segment_path = lambda: "transmission"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais.Transmission, ['ais_interval', 'cos'], name, value)


                        class CrossCheck(Entity):
                            """
                            Cross\-check configuration
                            
                            .. attribute:: cross_check_meps
                            
                            	Cross\-check MEPs
                            	**type**\:  :py:class:`CrossCheckMeps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps>`
                            
                            .. attribute:: auto
                            
                            	Enable automatic MEP cross\-check
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck, self).__init__()

                                self.yang_name = "cross-check"
                                self.yang_parent_name = "service"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("cross-check-meps", ("cross_check_meps", EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps))])
                                self._leafs = OrderedDict([
                                    ('auto', (YLeaf(YType.empty, 'auto'), ['Empty'])),
                                ])
                                self.auto = None

                                self.cross_check_meps = EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps()
                                self.cross_check_meps.parent = self
                                self._children_name_map["cross_check_meps"] = "cross-check-meps"
                                self._segment_path = lambda: "cross-check"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck, ['auto'], name, value)


                            class CrossCheckMeps(Entity):
                                """
                                Cross\-check MEPs
                                
                                .. attribute:: cross_check_mep
                                
                                	MEP ID and optional MAC Address for Cross\-check
                                	**type**\: list of  		 :py:class:`CrossCheckMep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps.CrossCheckMep>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-cfg'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps, self).__init__()

                                    self.yang_name = "cross-check-meps"
                                    self.yang_parent_name = "cross-check"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("cross-check-mep", ("cross_check_mep", EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps.CrossCheckMep))])
                                    self._leafs = OrderedDict()

                                    self.cross_check_mep = YList(self)
                                    self._segment_path = lambda: "cross-check-meps"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps, [], name, value)


                                class CrossCheckMep(Entity):
                                    """
                                    MEP ID and optional MAC Address for
                                    Cross\-check
                                    
                                    .. attribute:: mep_id  (key)
                                    
                                    	MEP ID
                                    	**type**\: int
                                    
                                    	**range:** 1..8191
                                    
                                    .. attribute:: enable_mac_address
                                    
                                    	MAC Address is specified
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC Address
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-cfg'
                                    _revision = '2017-10-06'

                                    def __init__(self):
                                        super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps.CrossCheckMep, self).__init__()

                                        self.yang_name = "cross-check-mep"
                                        self.yang_parent_name = "cross-check-meps"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['mep_id']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mep_id', (YLeaf(YType.uint32, 'mep-id'), ['int'])),
                                            ('enable_mac_address', (YLeaf(YType.empty, 'enable-mac-address'), ['Empty'])),
                                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                        ])
                                        self.mep_id = None
                                        self.enable_mac_address = None
                                        self.mac_address = None
                                        self._segment_path = lambda: "cross-check-mep" + "[mep-id='" + str(self.mep_id) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps.CrossCheckMep, ['mep_id', 'enable_mac_address', 'mac_address'], name, value)


                        class ServiceProperties(Entity):
                            """
                            Fundamental properties of the service
                            (maintenance association)
                            
                            .. attribute:: service_type
                            
                            	Type of Service
                            	**type**\:  :py:class:`CfmService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg.CfmService>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: group_name
                            
                            	Bridge Group or Cross\-connect Group, if Service Type is BridgeDomain or CrossConnect
                            	**type**\: str
                            
                            .. attribute:: switching_name
                            
                            	Bridge Domain or Cross\-connect name, if Service Type is BridgeDomain or CrossConnect
                            	**type**\: str
                            
                            .. attribute:: ce_id
                            
                            	Local Customer Edge Identifier
                            	**type**\: int
                            
                            	**range:** 1..16384
                            
                            .. attribute:: remote_ce_id
                            
                            	Remote Customer Edge Identifier
                            	**type**\: int
                            
                            	**range:** 1..16384
                            
                            .. attribute:: evi
                            
                            	EVPN ID
                            	**type**\: int
                            
                            	**range:** 1..65534
                            
                            .. attribute:: short_ma_name_format
                            
                            	Short MA Name Format
                            	**type**\:  :py:class:`CfmShortMaNameFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg.CfmShortMaNameFormat>`
                            
                            .. attribute:: short_ma_name_string
                            
                            	String Short MA Name, if format is String
                            	**type**\: str
                            
                            	**length:** 1..45
                            
                            .. attribute:: short_ma_name_number
                            
                            	Numeric Short MA Name, if format is VlanID or Number
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: short_ma_name_oui
                            
                            	VPN OUI, if Short MA Name format is VPN\_ID
                            	**type**\: int
                            
                            	**range:** 0..16777215
                            
                            .. attribute:: short_ma_name_vpn_index
                            
                            	VPN Index, if Short MA Name format is VPN\_ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: short_ma_name_icc
                            
                            	ITU Carrier Code (ICC), if format is ICCBased
                            	**type**\: str
                            
                            	**length:** 1..6
                            
                            .. attribute:: short_ma_name_umc
                            
                            	Unique MEG ID Code (UMC), if format is ICCBased
                            	**type**\: str
                            
                            	**length:** 1..12
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.ServiceProperties, self).__init__()

                                self.yang_name = "service-properties"
                                self.yang_parent_name = "service"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('service_type', (YLeaf(YType.enumeration, 'service-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg', 'CfmService', '')])),
                                    ('group_name', (YLeaf(YType.str, 'group-name'), ['str'])),
                                    ('switching_name', (YLeaf(YType.str, 'switching-name'), ['str'])),
                                    ('ce_id', (YLeaf(YType.uint32, 'ce-id'), ['int'])),
                                    ('remote_ce_id', (YLeaf(YType.uint32, 'remote-ce-id'), ['int'])),
                                    ('evi', (YLeaf(YType.uint32, 'evi'), ['int'])),
                                    ('short_ma_name_format', (YLeaf(YType.enumeration, 'short-ma-name-format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg', 'CfmShortMaNameFormat', '')])),
                                    ('short_ma_name_string', (YLeaf(YType.str, 'short-ma-name-string'), ['str'])),
                                    ('short_ma_name_number', (YLeaf(YType.uint32, 'short-ma-name-number'), ['int'])),
                                    ('short_ma_name_oui', (YLeaf(YType.uint32, 'short-ma-name-oui'), ['int'])),
                                    ('short_ma_name_vpn_index', (YLeaf(YType.uint32, 'short-ma-name-vpn-index'), ['int'])),
                                    ('short_ma_name_icc', (YLeaf(YType.str, 'short-ma-name-icc'), ['str'])),
                                    ('short_ma_name_umc', (YLeaf(YType.str, 'short-ma-name-umc'), ['str'])),
                                ])
                                self.service_type = None
                                self.group_name = None
                                self.switching_name = None
                                self.ce_id = None
                                self.remote_ce_id = None
                                self.evi = None
                                self.short_ma_name_format = None
                                self.short_ma_name_string = None
                                self.short_ma_name_number = None
                                self.short_ma_name_oui = None
                                self.short_ma_name_vpn_index = None
                                self.short_ma_name_icc = None
                                self.short_ma_name_umc = None
                                self._segment_path = lambda: "service-properties"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EthernetFeatures.Cfm.Domains.Domain.Services.Service.ServiceProperties, ['service_type', 'group_name', 'switching_name', 'ce_id', 'remote_ce_id', 'evi', 'short_ma_name_format', 'short_ma_name_string', 'short_ma_name_number', 'short_ma_name_oui', 'short_ma_name_vpn_index', 'short_ma_name_icc', 'short_ma_name_umc'], name, value)


                class DomainProperties(Entity):
                    """
                    Fundamental properties of the domain
                    
                    .. attribute:: level
                    
                    	Maintenance Domain Level
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: mdid_format
                    
                    	Maintenance Domain ID Format
                    	**type**\:  :py:class:`CfmMdidFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg.CfmMdidFormat>`
                    
                    .. attribute:: mdid_mac_address
                    
                    	MAC Address, if MDID Format is MACAddress
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mdid_number
                    
                    	Unsigned 16\-bit Interger, if MDID Format is MACAddress
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mdid_string
                    
                    	String MDID, if MDID format is String or DNSLike
                    	**type**\: str
                    
                    	**length:** 1..43
                    
                    

                    """

                    _prefix = 'ethernet-cfm-cfg'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(EthernetFeatures.Cfm.Domains.Domain.DomainProperties, self).__init__()

                        self.yang_name = "domain-properties"
                        self.yang_parent_name = "domain"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                            ('mdid_format', (YLeaf(YType.enumeration, 'mdid-format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg', 'CfmMdidFormat', '')])),
                            ('mdid_mac_address', (YLeaf(YType.str, 'mdid-mac-address'), ['str'])),
                            ('mdid_number', (YLeaf(YType.uint32, 'mdid-number'), ['int'])),
                            ('mdid_string', (YLeaf(YType.str, 'mdid-string'), ['str'])),
                        ])
                        self.level = None
                        self.mdid_format = None
                        self.mdid_mac_address = None
                        self.mdid_number = None
                        self.mdid_string = None
                        self._segment_path = lambda: "domain-properties"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetFeatures.Cfm.Domains.Domain.DomainProperties, ['level', 'mdid_format', 'mdid_mac_address', 'mdid_number', 'mdid_string'], name, value)


    class EtherLinkOam(Entity):
        """
        Ethernet Link OAM Global Configuration
        
        .. attribute:: profiles
        
        	Table of Ethernet Link OAM profiles
        	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles>`
        
        

        """

        _prefix = 'ethernet-link-oam-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(EthernetFeatures.EtherLinkOam, self).__init__()

            self.yang_name = "ether-link-oam"
            self.yang_parent_name = "ethernet-features"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("profiles", ("profiles", EthernetFeatures.EtherLinkOam.Profiles))])
            self._leafs = OrderedDict()

            self.profiles = EthernetFeatures.EtherLinkOam.Profiles()
            self.profiles.parent = self
            self._children_name_map["profiles"] = "profiles"
            self._segment_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-cfg:ether-link-oam"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EthernetFeatures.EtherLinkOam, [], name, value)


        class Profiles(Entity):
            """
            Table of Ethernet Link OAM profiles
            
            .. attribute:: profile
            
            	Name of the profile
            	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile>`
            
            

            """

            _prefix = 'ethernet-link-oam-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(EthernetFeatures.EtherLinkOam.Profiles, self).__init__()

                self.yang_name = "profiles"
                self.yang_parent_name = "ether-link-oam"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("profile", ("profile", EthernetFeatures.EtherLinkOam.Profiles.Profile))])
                self._leafs = OrderedDict()

                self.profile = YList(self)
                self._segment_path = lambda: "profiles"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-link-oam-cfg:ether-link-oam/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EthernetFeatures.EtherLinkOam.Profiles, [], name, value)


            class Profile(Entity):
                """
                Name of the profile
                
                .. attribute:: profile  (key)
                
                	none
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: action
                
                	Configure action parameters
                	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.Action>`
                
                .. attribute:: require_remote
                
                	Configure remote requirement parameters
                	**type**\:  :py:class:`RequireRemote <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote>`
                
                .. attribute:: mib_retrieval
                
                	Enable or disable MIB retrieval support
                	**type**\: bool
                
                .. attribute:: udlf
                
                	Enable or disable uni\-directional link\-fault detection support
                	**type**\: bool
                
                .. attribute:: hello_interval
                
                	Possible Ethernet Link OAM hello intervals
                	**type**\:  :py:class:`EtherLinkOamHelloIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamHelloIntervalEnum>`
                
                .. attribute:: mode
                
                	Set the OAM mode to passive
                	**type**\:  :py:class:`EtherLinkOamModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamModeEnum>`
                
                .. attribute:: remote_loopback
                
                	Enable or disable remote loopback support
                	**type**\: bool
                
                .. attribute:: timeout
                
                	Connection timeout period in number of lost heartbeats
                	**type**\: int
                
                	**range:** 2..30
                
                .. attribute:: link_monitoring
                
                	Configure link monitor parameters
                	**type**\:  :py:class:`LinkMonitoring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring>`
                
                

                """

                _prefix = 'ethernet-link-oam-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(EthernetFeatures.EtherLinkOam.Profiles.Profile, self).__init__()

                    self.yang_name = "profile"
                    self.yang_parent_name = "profiles"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['profile']
                    self._child_classes = OrderedDict([("action", ("action", EthernetFeatures.EtherLinkOam.Profiles.Profile.Action)), ("require-remote", ("require_remote", EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote)), ("link-monitoring", ("link_monitoring", EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring))])
                    self._leafs = OrderedDict([
                        ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                        ('mib_retrieval', (YLeaf(YType.boolean, 'mib-retrieval'), ['bool'])),
                        ('udlf', (YLeaf(YType.boolean, 'udlf'), ['bool'])),
                        ('hello_interval', (YLeaf(YType.enumeration, 'hello-interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamHelloIntervalEnum', '')])),
                        ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamModeEnum', '')])),
                        ('remote_loopback', (YLeaf(YType.boolean, 'remote-loopback'), ['bool'])),
                        ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                    ])
                    self.profile = None
                    self.mib_retrieval = None
                    self.udlf = None
                    self.hello_interval = None
                    self.mode = None
                    self.remote_loopback = None
                    self.timeout = None

                    self.action = EthernetFeatures.EtherLinkOam.Profiles.Profile.Action()
                    self.action.parent = self
                    self._children_name_map["action"] = "action"

                    self.require_remote = EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote()
                    self.require_remote.parent = self
                    self._children_name_map["require_remote"] = "require-remote"

                    self.link_monitoring = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring()
                    self.link_monitoring.parent = self
                    self._children_name_map["link_monitoring"] = "link-monitoring"
                    self._segment_path = lambda: "profile" + "[profile='" + str(self.profile) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-link-oam-cfg:ether-link-oam/profiles/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(EthernetFeatures.EtherLinkOam.Profiles.Profile, ['profile', 'mib_retrieval', 'udlf', 'hello_interval', 'mode', 'remote_loopback', 'timeout'], name, value)


                class Action(Entity):
                    """
                    Configure action parameters
                    
                    .. attribute:: dying_gasp
                    
                    	Action to perform when a dying gasp occurs
                    	**type**\:  :py:class:`EtherLinkOamEventActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum>`
                    
                    .. attribute:: session_up
                    
                    	Action to perform when a session comes up
                    	**type**\:  :py:class:`EtherLinkOamEventActionPrimEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionPrimEnum>`
                    
                    .. attribute:: critical_event
                    
                    	Action to perform when a critical event occurs
                    	**type**\:  :py:class:`EtherLinkOamEventActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum>`
                    
                    .. attribute:: session_down
                    
                    	Action to perform when a session goes down
                    	**type**\:  :py:class:`EtherLinkOamEventActionEnumEfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnumEfd>`
                    
                    .. attribute:: discovery_timeout
                    
                    	Action to perform when discovery timeout occurs
                    	**type**\:  :py:class:`EtherLinkOamEventActionEnumEfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnumEfd>`
                    
                    .. attribute:: high_threshold
                    
                    	Action to perform when a high\-threshold event occurs
                    	**type**\:  :py:class:`EtherLinkOamEventActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum>`
                    
                    .. attribute:: capabilities_conflict
                    
                    	Action to perform when a capabilities conflict occurs
                    	**type**\:  :py:class:`EtherLinkOamEventActionEnumEfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnumEfd>`
                    
                    .. attribute:: remote_loopback
                    
                    	Action to perform when remote loopback is entered or exited
                    	**type**\:  :py:class:`EtherLinkOamEventActionPrimEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionPrimEnum>`
                    
                    .. attribute:: link_fault
                    
                    	Action to perform when a link fault message is received
                    	**type**\:  :py:class:`EtherLinkOamEventActionEnumEfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnumEfd>`
                    
                    .. attribute:: wiring_conflict
                    
                    	Action to perform when a wiring conflict occurs
                    	**type**\:  :py:class:`EtherLinkOamEventActionEnumEfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnumEfd>`
                    
                    

                    """

                    _prefix = 'ethernet-link-oam-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(EthernetFeatures.EtherLinkOam.Profiles.Profile.Action, self).__init__()

                        self.yang_name = "action"
                        self.yang_parent_name = "profile"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('dying_gasp', (YLeaf(YType.enumeration, 'dying-gasp'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnum', '')])),
                            ('session_up', (YLeaf(YType.enumeration, 'session-up'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionPrimEnum', '')])),
                            ('critical_event', (YLeaf(YType.enumeration, 'critical-event'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnum', '')])),
                            ('session_down', (YLeaf(YType.enumeration, 'session-down'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd', '')])),
                            ('discovery_timeout', (YLeaf(YType.enumeration, 'discovery-timeout'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd', '')])),
                            ('high_threshold', (YLeaf(YType.enumeration, 'high-threshold'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnum', '')])),
                            ('capabilities_conflict', (YLeaf(YType.enumeration, 'capabilities-conflict'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd', '')])),
                            ('remote_loopback', (YLeaf(YType.enumeration, 'remote-loopback'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionPrimEnum', '')])),
                            ('link_fault', (YLeaf(YType.enumeration, 'link-fault'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd', '')])),
                            ('wiring_conflict', (YLeaf(YType.enumeration, 'wiring-conflict'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd', '')])),
                        ])
                        self.dying_gasp = None
                        self.session_up = None
                        self.critical_event = None
                        self.session_down = None
                        self.discovery_timeout = None
                        self.high_threshold = None
                        self.capabilities_conflict = None
                        self.remote_loopback = None
                        self.link_fault = None
                        self.wiring_conflict = None
                        self._segment_path = lambda: "action"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetFeatures.EtherLinkOam.Profiles.Profile.Action, ['dying_gasp', 'session_up', 'critical_event', 'session_down', 'discovery_timeout', 'high_threshold', 'capabilities_conflict', 'remote_loopback', 'link_fault', 'wiring_conflict'], name, value)


                class RequireRemote(Entity):
                    """
                    Configure remote requirement parameters
                    
                    .. attribute:: mib_retrieval
                    
                    	Enable or disable MIB retrieval requirement
                    	**type**\: bool
                    
                    .. attribute:: mode
                    
                    	Possible required OAM modes
                    	**type**\:  :py:class:`EtherLinkOamRequireModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamRequireModeEnum>`
                    
                    .. attribute:: remote_loopback
                    
                    	Enable or disable remote loopback requirement
                    	**type**\: bool
                    
                    .. attribute:: link_monitoring
                    
                    	Enable or disable link monitoring requirement
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ethernet-link-oam-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote, self).__init__()

                        self.yang_name = "require-remote"
                        self.yang_parent_name = "profile"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('mib_retrieval', (YLeaf(YType.boolean, 'mib-retrieval'), ['bool'])),
                            ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamRequireModeEnum', '')])),
                            ('remote_loopback', (YLeaf(YType.boolean, 'remote-loopback'), ['bool'])),
                            ('link_monitoring', (YLeaf(YType.boolean, 'link-monitoring'), ['bool'])),
                        ])
                        self.mib_retrieval = None
                        self.mode = None
                        self.remote_loopback = None
                        self.link_monitoring = None
                        self._segment_path = lambda: "require-remote"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote, ['mib_retrieval', 'mode', 'remote_loopback', 'link_monitoring'], name, value)


                class LinkMonitoring(Entity):
                    """
                    Configure link monitor parameters
                    
                    .. attribute:: symbol_period
                    
                    	Symbol\-period event configuration
                    	**type**\:  :py:class:`SymbolPeriod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod>`
                    
                    .. attribute:: frame_period
                    
                    	Frame\-period event configuration
                    	**type**\:  :py:class:`FramePeriod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod>`
                    
                    .. attribute:: frame_seconds
                    
                    	Frame\-seconds event configuration
                    	**type**\:  :py:class:`FrameSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds>`
                    
                    .. attribute:: frame
                    
                    	Frame event configuration
                    	**type**\:  :py:class:`Frame <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame>`
                    
                    .. attribute:: monitoring
                    
                    	Enable or disable monitoring
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ethernet-link-oam-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring, self).__init__()

                        self.yang_name = "link-monitoring"
                        self.yang_parent_name = "profile"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("symbol-period", ("symbol_period", EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod)), ("frame-period", ("frame_period", EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod)), ("frame-seconds", ("frame_seconds", EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds)), ("frame", ("frame", EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame))])
                        self._leafs = OrderedDict([
                            ('monitoring', (YLeaf(YType.boolean, 'monitoring'), ['bool'])),
                        ])
                        self.monitoring = None

                        self.symbol_period = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod()
                        self.symbol_period.parent = self
                        self._children_name_map["symbol_period"] = "symbol-period"

                        self.frame_period = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod()
                        self.frame_period.parent = self
                        self._children_name_map["frame_period"] = "frame-period"

                        self.frame_seconds = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds()
                        self.frame_seconds.parent = self
                        self._children_name_map["frame_seconds"] = "frame-seconds"

                        self.frame = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame()
                        self.frame.parent = self
                        self._children_name_map["frame"] = "frame"
                        self._segment_path = lambda: "link-monitoring"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring, ['monitoring'], name, value)


                    class SymbolPeriod(Entity):
                        """
                        Symbol\-period event configuration
                        
                        .. attribute:: window
                        
                        	Window size configuration for symbol\-period events
                        	**type**\:  :py:class:`Window <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Window>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: threshold
                        
                        	Threshold configuration for symbol\-period events
                        	**type**\:  :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Threshold>`
                        
                        

                        """

                        _prefix = 'ethernet-link-oam-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod, self).__init__()

                            self.yang_name = "symbol-period"
                            self.yang_parent_name = "link-monitoring"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("window", ("window", EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Window)), ("threshold", ("threshold", EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Threshold))])
                            self._leafs = OrderedDict()

                            self.window = None
                            self._children_name_map["window"] = "window"

                            self.threshold = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Threshold()
                            self.threshold.parent = self
                            self._children_name_map["threshold"] = "threshold"
                            self._segment_path = lambda: "symbol-period"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod, [], name, value)


                        class Window(Entity):
                            """
                            Window size configuration for symbol\-period
                            events
                            
                            .. attribute:: window
                            
                            	Size of the symbol\-period window
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: units
                            
                            	Units to use for this window
                            	**type**\:  :py:class:`EtherLinkOamWindowUnitsSymbolsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamWindowUnitsSymbolsEnum>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: multiplier
                            
                            	The multiplier to use for this window (only valid if 'Units' is Symbols and treated as 1 if unspecified)
                            	**type**\:  :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            	**default value**\: none
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Window, self).__init__()

                                self.yang_name = "window"
                                self.yang_parent_name = "symbol-period"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('window', (YLeaf(YType.uint32, 'window'), ['int'])),
                                    ('units', (YLeaf(YType.enumeration, 'units'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamWindowUnitsSymbolsEnum', '')])),
                                    ('multiplier', (YLeaf(YType.enumeration, 'multiplier'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum', '')])),
                                ])
                                self.window = None
                                self.units = None
                                self.multiplier = None
                                self._segment_path = lambda: "window"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Window, ['window', 'units', 'multiplier'], name, value)


                        class Threshold(Entity):
                            """
                            Threshold configuration for symbol\-period
                            events
                            
                            .. attribute:: threshold_low
                            
                            	The low threshold for symbol\-period
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**default value**\: 1
                            
                            .. attribute:: threshold_high
                            
                            	The high threshold for symbol\-period
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: units
                            
                            	The units to use for these thresholds
                            	**type**\:  :py:class:`EtherLinkOamThresholdUnitsSymbolsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdUnitsSymbolsEnum>`
                            
                            	**default value**\: symbols
                            
                            .. attribute:: multiplier_low
                            
                            	The multiplier to use for the low threshold (only valid if 'Units' is Symbols and treated as 1 if unspecified)
                            	**type**\:  :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            	**default value**\: none
                            
                            .. attribute:: multiplier_high
                            
                            	The multiplier to use for the high threshold (only valid if 'Units' is Symbols and treated as 1 if unspecified)
                            	**type**\:  :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Threshold, self).__init__()

                                self.yang_name = "threshold"
                                self.yang_parent_name = "symbol-period"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('threshold_low', (YLeaf(YType.uint32, 'threshold-low'), ['int'])),
                                    ('threshold_high', (YLeaf(YType.uint32, 'threshold-high'), ['int'])),
                                    ('units', (YLeaf(YType.enumeration, 'units'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdUnitsSymbolsEnum', '')])),
                                    ('multiplier_low', (YLeaf(YType.enumeration, 'multiplier-low'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum', '')])),
                                    ('multiplier_high', (YLeaf(YType.enumeration, 'multiplier-high'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum', '')])),
                                ])
                                self.threshold_low = None
                                self.threshold_high = None
                                self.units = None
                                self.multiplier_low = None
                                self.multiplier_high = None
                                self._segment_path = lambda: "threshold"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Threshold, ['threshold_low', 'threshold_high', 'units', 'multiplier_low', 'multiplier_high'], name, value)


                    class FramePeriod(Entity):
                        """
                        Frame\-period event configuration
                        
                        .. attribute:: window
                        
                        	Window size configuration for frame\-period events
                        	**type**\:  :py:class:`Window <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Window>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: threshold
                        
                        	Threshold configuration for frame\-period events
                        	**type**\:  :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Threshold>`
                        
                        

                        """

                        _prefix = 'ethernet-link-oam-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod, self).__init__()

                            self.yang_name = "frame-period"
                            self.yang_parent_name = "link-monitoring"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("window", ("window", EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Window)), ("threshold", ("threshold", EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Threshold))])
                            self._leafs = OrderedDict()

                            self.window = None
                            self._children_name_map["window"] = "window"

                            self.threshold = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Threshold()
                            self.threshold.parent = self
                            self._children_name_map["threshold"] = "threshold"
                            self._segment_path = lambda: "frame-period"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod, [], name, value)


                        class Window(Entity):
                            """
                            Window size configuration for frame\-period
                            events
                            
                            .. attribute:: window
                            
                            	Size of the frame\-period window
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: units
                            
                            	The units to use for this window
                            	**type**\:  :py:class:`EtherLinkOamWindowUnitsFramesEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamWindowUnitsFramesEnum>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: multiplier
                            
                            	The multiplier to use for this window (only valid if 'Units' is Frames and treated as 1 if unspecified)
                            	**type**\:  :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            	**default value**\: none
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Window, self).__init__()

                                self.yang_name = "window"
                                self.yang_parent_name = "frame-period"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('window', (YLeaf(YType.uint32, 'window'), ['int'])),
                                    ('units', (YLeaf(YType.enumeration, 'units'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamWindowUnitsFramesEnum', '')])),
                                    ('multiplier', (YLeaf(YType.enumeration, 'multiplier'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum', '')])),
                                ])
                                self.window = None
                                self.units = None
                                self.multiplier = None
                                self._segment_path = lambda: "window"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Window, ['window', 'units', 'multiplier'], name, value)


                        class Threshold(Entity):
                            """
                            Threshold configuration for frame\-period
                            events
                            
                            .. attribute:: threshold_low
                            
                            	The low threshold for frame\-period events
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**default value**\: 1
                            
                            .. attribute:: threshold_high
                            
                            	The high threshold for frame\-period events
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: units
                            
                            	The units to use for these thresholds
                            	**type**\:  :py:class:`EtherLinkOamThresholdUnitsFramesEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdUnitsFramesEnum>`
                            
                            	**default value**\: ppm
                            
                            .. attribute:: multiplier_low
                            
                            	The multiplier to use for the low threshold (only valid if 'Units' is Frames and treated as 1 if unspecified)
                            	**type**\:  :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            	**default value**\: none
                            
                            .. attribute:: multiplier_high
                            
                            	The multiplier to use for the high threshold (only valid if 'Units' is Frames and treated as 1 if unspecified)
                            	**type**\:  :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Threshold, self).__init__()

                                self.yang_name = "threshold"
                                self.yang_parent_name = "frame-period"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('threshold_low', (YLeaf(YType.uint32, 'threshold-low'), ['int'])),
                                    ('threshold_high', (YLeaf(YType.uint32, 'threshold-high'), ['int'])),
                                    ('units', (YLeaf(YType.enumeration, 'units'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdUnitsFramesEnum', '')])),
                                    ('multiplier_low', (YLeaf(YType.enumeration, 'multiplier-low'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum', '')])),
                                    ('multiplier_high', (YLeaf(YType.enumeration, 'multiplier-high'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum', '')])),
                                ])
                                self.threshold_low = None
                                self.threshold_high = None
                                self.units = None
                                self.multiplier_low = None
                                self.multiplier_high = None
                                self._segment_path = lambda: "threshold"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Threshold, ['threshold_low', 'threshold_high', 'units', 'multiplier_low', 'multiplier_high'], name, value)


                    class FrameSeconds(Entity):
                        """
                        Frame\-seconds event configuration
                        
                        .. attribute:: threshold
                        
                        	Threshold configuration for frame\-seconds events
                        	**type**\:  :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds.Threshold>`
                        
                        .. attribute:: window
                        
                        	Window size configuration for frame\-seconds events
                        	**type**\: int
                        
                        	**range:** 10000..900000
                        
                        	**units**\: millisecond
                        
                        	**default value**\: 60000
                        
                        

                        """

                        _prefix = 'ethernet-link-oam-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds, self).__init__()

                            self.yang_name = "frame-seconds"
                            self.yang_parent_name = "link-monitoring"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("threshold", ("threshold", EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds.Threshold))])
                            self._leafs = OrderedDict([
                                ('window', (YLeaf(YType.uint32, 'window'), ['int'])),
                            ])
                            self.window = None

                            self.threshold = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds.Threshold()
                            self.threshold.parent = self
                            self._children_name_map["threshold"] = "threshold"
                            self._segment_path = lambda: "frame-seconds"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds, ['window'], name, value)


                        class Threshold(Entity):
                            """
                            Threshold configuration for frame\-seconds
                            events
                            
                            .. attribute:: threshold_low
                            
                            	The low threshold for frame\-seconds events
                            	**type**\: int
                            
                            	**range:** 1..900
                            
                            	**units**\: second
                            
                            	**default value**\: 1
                            
                            .. attribute:: threshold_high
                            
                            	The high threshold for frame\-seconds events
                            	**type**\: int
                            
                            	**range:** 1..900
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds.Threshold, self).__init__()

                                self.yang_name = "threshold"
                                self.yang_parent_name = "frame-seconds"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('threshold_low', (YLeaf(YType.uint32, 'threshold-low'), ['int'])),
                                    ('threshold_high', (YLeaf(YType.uint32, 'threshold-high'), ['int'])),
                                ])
                                self.threshold_low = None
                                self.threshold_high = None
                                self._segment_path = lambda: "threshold"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds.Threshold, ['threshold_low', 'threshold_high'], name, value)


                    class Frame(Entity):
                        """
                        Frame event configuration
                        
                        .. attribute:: threshold
                        
                        	Threshold configuration for frame events
                        	**type**\:  :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame.Threshold>`
                        
                        .. attribute:: window
                        
                        	Window size configuration for frame events
                        	**type**\: int
                        
                        	**range:** 1000..60000
                        
                        	**units**\: millisecond
                        
                        	**default value**\: 1000
                        
                        

                        """

                        _prefix = 'ethernet-link-oam-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame, self).__init__()

                            self.yang_name = "frame"
                            self.yang_parent_name = "link-monitoring"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("threshold", ("threshold", EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame.Threshold))])
                            self._leafs = OrderedDict([
                                ('window', (YLeaf(YType.uint32, 'window'), ['int'])),
                            ])
                            self.window = None

                            self.threshold = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame.Threshold()
                            self.threshold.parent = self
                            self._children_name_map["threshold"] = "threshold"
                            self._segment_path = lambda: "frame"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame, ['window'], name, value)


                        class Threshold(Entity):
                            """
                            Threshold configuration for frame events
                            
                            .. attribute:: threshold_low
                            
                            	The low threshold for frame events
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**default value**\: 1
                            
                            .. attribute:: threshold_high
                            
                            	The high threshold for frame events
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: multiplier_low
                            
                            	The multiplier to use for the low threshold (treated as 1 if unspecified)
                            	**type**\:  :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            	**default value**\: none
                            
                            .. attribute:: multiplier_high
                            
                            	The multiplier to use for the high threshold (treated as 1 if unspecified)
                            	**type**\:  :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame.Threshold, self).__init__()

                                self.yang_name = "threshold"
                                self.yang_parent_name = "frame"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('threshold_low', (YLeaf(YType.uint32, 'threshold-low'), ['int'])),
                                    ('threshold_high', (YLeaf(YType.uint32, 'threshold-high'), ['int'])),
                                    ('multiplier_low', (YLeaf(YType.enumeration, 'multiplier-low'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum', '')])),
                                    ('multiplier_high', (YLeaf(YType.enumeration, 'multiplier-high'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum', '')])),
                                ])
                                self.threshold_low = None
                                self.threshold_high = None
                                self.multiplier_low = None
                                self.multiplier_high = None
                                self._segment_path = lambda: "threshold"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame.Threshold, ['threshold_low', 'threshold_high', 'multiplier_low', 'multiplier_high'], name, value)

    def clone_ptr(self):
        self._top_entity = EthernetFeatures()
        return self._top_entity


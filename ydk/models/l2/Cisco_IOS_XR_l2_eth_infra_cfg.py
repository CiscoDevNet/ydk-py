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

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_cfg import CfmMdidFormatEnum
from ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_cfg import CfmMipPolicyEnum
from ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_cfg import CfmServiceEnum
from ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_cfg import CfmShortMaNameFormatEnum
from ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_datatypes import CfmAisIntervalEnum
from ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_datatypes import CfmCcmIntervalEnum
from ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg import EtherLinkOamEventActionEnum1Enum
from ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg import EtherLinkOamEventActionEnum2Enum
from ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg import EtherLinkOamEventActionEnum4Enum
from ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg import EtherLinkOamEventActionEnum5Enum
from ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg import EtherLinkOamEventActionEnum6Enum
from ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg import EtherLinkOamProfileHelloIntervalEnumEnum
from ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg import EtherLinkOamProfileModeEnumEnum
from ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg import EtherLinkOamProfileRequireModeEnumEnum

class EgressFilteringEnum(Enum):
    """
    EgressFilteringEnum

    Egress filtering

    .. data:: EGRESS_FILTERING_TYPE_STRICT = 1

    	Strict Egress Filtering

    .. data:: EGRESS_FILTERING_TYPE_DISABLE = 2

    	Egress Filtering Disabled

    .. data:: EGRESS_FILTERING_TYPE_DEFAULT = 3

    	Default Egress Filtering Behavior

    """

    EGRESS_FILTERING_TYPE_STRICT = 1

    EGRESS_FILTERING_TYPE_DISABLE = 2

    EGRESS_FILTERING_TYPE_DEFAULT = 3


    @staticmethod
    def _meta_info():
        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
        return meta._meta_table['EgressFilteringEnum']


class FilteringEnum(Enum):
    """
    FilteringEnum

    Filtering

    .. data:: FILTERING_TYPE_DOT1Q = 0

    	C-Vlan ingress frame filtering (Table 8-1 of

    	802.1ad standard)

    .. data:: FILTERING_TYPE_DOT1AD = 1

    	S-Vlan ingress frame filtering (Table 8-2 of

    	802.1ad standard)

    """

    FILTERING_TYPE_DOT1Q = 0

    FILTERING_TYPE_DOT1AD = 1


    @staticmethod
    def _meta_info():
        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
        return meta._meta_table['FilteringEnum']


class L2ProtocolModeEnum(Enum):
    """
    L2ProtocolModeEnum

    L2 protocol mode

    .. data:: FORWARD = 0

    	Forward packets transparently

    .. data:: DROP = 1

    	Drop the protocol's packets

    .. data:: TUNNEL = 2

    	Tunnel ingress frames, untunnel egress frames

    .. data:: REVERSE_TUNNEL = 3

    	Tunnel egress frames, untunnel ingress frames

    """

    FORWARD = 0

    DROP = 1

    TUNNEL = 2

    REVERSE_TUNNEL = 3


    @staticmethod
    def _meta_info():
        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
        return meta._meta_table['L2ProtocolModeEnum']


class L2ProtocolNameEnum(Enum):
    """
    L2ProtocolNameEnum

    L2 protocol name

    .. data:: CDP = 0

    	CDP

    .. data:: STP = 1

    	STP

    .. data:: VTP = 2

    	VTP

    .. data:: PVST = 3

    	PVST+

    .. data:: CPSV = 4

    	CDP, PVST+, STP, and VTP

    """

    CDP = 0

    STP = 1

    VTP = 2

    PVST = 3

    CPSV = 4


    @staticmethod
    def _meta_info():
        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
        return meta._meta_table['L2ProtocolNameEnum']



class EthernetFeatures(object):
    """
    Ethernet Features Configuration
    
    .. attribute:: cfm
    
    	CFM global configuration
    	**type**\: :py:class:`Cfm <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm>`
    
    .. attribute:: egress_filtering
    
    	Egress Filtering Configuration
    	**type**\: :py:class:`EgressFiltering <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EgressFiltering>`
    
    .. attribute:: ether_link_oam
    
    	Ethernet Link OAM Global Configuration
    	**type**\: :py:class:`EtherLinkOam <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam>`
    
    

    """

    _prefix = 'l2-eth-infra-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.cfm = EthernetFeatures.Cfm()
        self.cfm.parent = self
        self.egress_filtering = EthernetFeatures.EgressFiltering()
        self.egress_filtering.parent = self
        self.ether_link_oam = EthernetFeatures.EtherLinkOam()
        self.ether_link_oam.parent = self


    class EgressFiltering(object):
        """
        Egress Filtering Configuration
        
        .. attribute:: egress_filtering_default_on
        
        	Whether Egress Filtering is on by default
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        

        """

        _prefix = 'l2-eth-infra-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.egress_filtering_default_on = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-l2-eth-infra-cfg:egress-filtering'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.egress_filtering_default_on is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
            return meta._meta_table['EthernetFeatures.EgressFiltering']['meta_info']


    class Cfm(object):
        """
        CFM global configuration
        
        .. attribute:: domains
        
        	Domain\-specific global configuration
        	**type**\: :py:class:`Domains <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains>`
        
        .. attribute:: nv_satellite_sla_processing_disable
        
        	Disable processing of Ethernet SLA packets on nV Satellite devices
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: traceroute_cache
        
        	Traceroute Cache Configuration
        	**type**\: :py:class:`TracerouteCache <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.TracerouteCache>`
        
        

        """

        _prefix = 'ethernet-cfm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.domains = EthernetFeatures.Cfm.Domains()
            self.domains.parent = self
            self.nv_satellite_sla_processing_disable = None
            self.traceroute_cache = EthernetFeatures.Cfm.TracerouteCache()
            self.traceroute_cache.parent = self


        class TracerouteCache(object):
            """
            Traceroute Cache Configuration
            
            .. attribute:: cache_size
            
            	Cache Size limit (number of replies)
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: hold_time
            
            	Hold Time in minutes
            	**type**\: int
            
            	**range:** 1..525600
            
            

            """

            _prefix = 'ethernet-cfm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.cache_size = None
                self.hold_time = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-cfm-cfg:cfm/Cisco-IOS-XR-ethernet-cfm-cfg:traceroute-cache'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.cache_size is not None:
                    return True

                if self.hold_time is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                return meta._meta_table['EthernetFeatures.Cfm.TracerouteCache']['meta_info']


        class Domains(object):
            """
            Domain\-specific global configuration
            
            .. attribute:: domain
            
            	Configuration for a particular Maintenance Domain
            	**type**\: list of :py:class:`Domain <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain>`
            
            

            """

            _prefix = 'ethernet-cfm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.domain = YList()
                self.domain.parent = self
                self.domain.name = 'domain'


            class Domain(object):
                """
                Configuration for a particular Maintenance
                Domain
                
                .. attribute:: domain  <key>
                
                	Maintenance Domain
                	**type**\: str
                
                .. attribute:: domain_properties
                
                	Fundamental properties of the domain
                	**type**\: :py:class:`DomainProperties <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.DomainProperties>`
                
                .. attribute:: services
                
                	Service\-specific global configuration
                	**type**\: :py:class:`Services <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services>`
                
                

                """

                _prefix = 'ethernet-cfm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain = None
                    self.domain_properties = EthernetFeatures.Cfm.Domains.Domain.DomainProperties()
                    self.domain_properties.parent = self
                    self.services = EthernetFeatures.Cfm.Domains.Domain.Services()
                    self.services.parent = self


                class Services(object):
                    """
                    Service\-specific global configuration
                    
                    .. attribute:: service
                    
                    	Configuration for a particular Service (Maintenance Association)
                    	**type**\: list of :py:class:`Service <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.service = YList()
                        self.service.parent = self
                        self.service.name = 'service'


                    class Service(object):
                        """
                        Configuration for a particular Service
                        (Maintenance Association)
                        
                        .. attribute:: service  <key>
                        
                        	Service (Maintenance Association)
                        	**type**\: str
                        
                        .. attribute:: ais
                        
                        	Service specific AIS configuration
                        	**type**\: :py:class:`Ais <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais>`
                        
                        .. attribute:: continuity_check_archive_hold_time
                        
                        	How long to store information for peer MEPs that have timed out
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: continuity_check_auto_traceroute
                        
                        	Automatically trigger a traceroute when a peer MEP times out
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: continuity_check_interval
                        
                        	Continuity Check Interval and Loss Threshold.  Configuring the interval enables Continuity Check
                        	**type**\: :py:class:`ContinuityCheckInterval <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.ContinuityCheckInterval>`
                        
                        .. attribute:: cross_check
                        
                        	Cross\-check configuration
                        	**type**\: :py:class:`CrossCheck <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck>`
                        
                        .. attribute:: efd2
                        
                        	Enable EFD to bring down ports when MEPs detect errors
                        	**type**\: :py:class:`Efd2 <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.Efd2>`
                        
                        .. attribute:: log_ais
                        
                        	Log receipt of AIS and LCK messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: log_continuity_check_errors
                        
                        	Log CCM Errors detected for peer MEPs
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: log_continuity_check_state_changes
                        
                        	Log peer MEPs state changes
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: log_cross_check_errors
                        
                        	Log Cross\-check Errors detected for peer MEPs
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: log_efd
                        
                        	Enable logging
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: maximum_meps
                        
                        	Limit on the number of MEPs in the service
                        	**type**\: int
                        
                        	**range:** 2..8190
                        
                        .. attribute:: mip_auto_creation
                        
                        	MIP Auto\-creation Policy
                        	**type**\: :py:class:`MipAutoCreation <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.MipAutoCreation>`
                        
                        .. attribute:: service_properties
                        
                        	Fundamental properties of the service (maintenance association)
                        	**type**\: :py:class:`ServiceProperties <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.ServiceProperties>`
                        
                        .. attribute:: tags
                        
                        	The number of tags to use when sending CFM packets from up MEPs in this Service
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ethernet-cfm-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.service = None
                            self.ais = EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais()
                            self.ais.parent = self
                            self.continuity_check_archive_hold_time = None
                            self.continuity_check_auto_traceroute = None
                            self.continuity_check_interval = None
                            self.cross_check = EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck()
                            self.cross_check.parent = self
                            self.efd2 = None
                            self.log_ais = None
                            self.log_continuity_check_errors = None
                            self.log_continuity_check_state_changes = None
                            self.log_cross_check_errors = None
                            self.log_efd = None
                            self.maximum_meps = None
                            self.mip_auto_creation = None
                            self.service_properties = None
                            self.tags = None


                        class Efd2(object):
                            """
                            Enable EFD to bring down ports when MEPs
                            detect errors
                            
                            .. attribute:: enable
                            
                            	Enable EFD
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: protection_switching_enable
                            
                            	Enable protection switching notifications
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.protection_switching_enable = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:efd2'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.enable is not None:
                                    return True

                                if self.protection_switching_enable is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                                return meta._meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.Efd2']['meta_info']


                        class ContinuityCheckInterval(object):
                            """
                            Continuity Check Interval and Loss
                            Threshold.  Configuring the interval
                            enables Continuity Check.
                            
                            .. attribute:: ccm_interval
                            
                            	CCM Interval
                            	**type**\: :py:class:`CfmCcmIntervalEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_datatypes.CfmCcmIntervalEnum>`
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: loss_threshold
                            
                            	Loss Threshold (default 3)
                            	**type**\: int
                            
                            	**range:** 2..255
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ccm_interval = None
                                self.loss_threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:continuity-check-interval'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ccm_interval is not None:
                                    return True

                                if self.loss_threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                                return meta._meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.ContinuityCheckInterval']['meta_info']


                        class MipAutoCreation(object):
                            """
                            MIP Auto\-creation Policy
                            
                            .. attribute:: ccm_learning_enable
                            
                            	Enable CCM Learning at MIPs in this service
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: mip_policy
                            
                            	MIP Auto\-creation Policy
                            	**type**\: :py:class:`CfmMipPolicyEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_cfg.CfmMipPolicyEnum>`
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ccm_learning_enable = None
                                self.mip_policy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:mip-auto-creation'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ccm_learning_enable is not None:
                                    return True

                                if self.mip_policy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                                return meta._meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.MipAutoCreation']['meta_info']


                        class Ais(object):
                            """
                            Service specific AIS configuration
                            
                            .. attribute:: transmission
                            
                            	AIS transmission configuration
                            	**type**\: :py:class:`Transmission <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais.Transmission>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.transmission = None


                            class Transmission(object):
                                """
                                AIS transmission configuration
                                
                                .. attribute:: ais_interval
                                
                                	AIS Interval
                                	**type**\: :py:class:`CfmAisIntervalEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_datatypes.CfmAisIntervalEnum>`
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                .. attribute:: cos
                                
                                	Class of Service bits
                                	**type**\: int
                                
                                	**range:** 0..7
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ethernet-cfm-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ais_interval = None
                                    self.cos = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:transmission'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.ais_interval is not None:
                                        return True

                                    if self.cos is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                                    return meta._meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais.Transmission']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:ais'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.transmission is not None and self.transmission._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                                return meta._meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais']['meta_info']


                        class CrossCheck(object):
                            """
                            Cross\-check configuration
                            
                            .. attribute:: auto
                            
                            	Enable automatic MEP cross\-check
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: cross_check_meps
                            
                            	Cross\-check MEPs
                            	**type**\: :py:class:`CrossCheckMeps <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.auto = None
                                self.cross_check_meps = EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps()
                                self.cross_check_meps.parent = self


                            class CrossCheckMeps(object):
                                """
                                Cross\-check MEPs
                                
                                .. attribute:: cross_check_mep
                                
                                	MEP ID and optional MAC Address for Cross\-check
                                	**type**\: list of :py:class:`CrossCheckMep <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps.CrossCheckMep>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.cross_check_mep = YList()
                                    self.cross_check_mep.parent = self
                                    self.cross_check_mep.name = 'cross_check_mep'


                                class CrossCheckMep(object):
                                    """
                                    MEP ID and optional MAC Address for
                                    Cross\-check
                                    
                                    .. attribute:: mep_id  <key>
                                    
                                    	MEP ID
                                    	**type**\: int
                                    
                                    	**range:** 1..8191
                                    
                                    .. attribute:: enable_mac_address
                                    
                                    	MAC Address is specified
                                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC Address
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.mep_id = None
                                        self.enable_mac_address = None
                                        self.mac_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.mep_id is None:
                                            raise YPYModelError('Key property mep_id is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:cross-check-mep[Cisco-IOS-XR-ethernet-cfm-cfg:mep-id = ' + str(self.mep_id) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.mep_id is not None:
                                            return True

                                        if self.enable_mac_address is not None:
                                            return True

                                        if self.mac_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                                        return meta._meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps.CrossCheckMep']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:cross-check-meps'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.cross_check_mep is not None:
                                        for child_ref in self.cross_check_mep:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                                    return meta._meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:cross-check'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.auto is not None:
                                    return True

                                if self.cross_check_meps is not None and self.cross_check_meps._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                                return meta._meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck']['meta_info']


                        class ServiceProperties(object):
                            """
                            Fundamental properties of the service
                            (maintenance association)
                            
                            .. attribute:: ce_id
                            
                            	Local Customer Edge Identifier
                            	**type**\: int
                            
                            	**range:** 1..16384
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: group_name
                            
                            	Bridge Group or Cross\-connect Group, if Service Type is BridgeDomain or CrossConnect
                            	**type**\: str
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: remote_ce_id
                            
                            	Remote Customer Edge Identifier
                            	**type**\: int
                            
                            	**range:** 1..16384
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: service_type
                            
                            	Type of Service
                            	**type**\: :py:class:`CfmServiceEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_cfg.CfmServiceEnum>`
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: short_ma_name_format
                            
                            	Short MA Name Format
                            	**type**\: :py:class:`CfmShortMaNameFormatEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_cfg.CfmShortMaNameFormatEnum>`
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: short_ma_name_icc
                            
                            	ITU Carrier Code (ICC), if format is ICCBased
                            	**type**\: str
                            
                            	**range:** 0..7
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: short_ma_name_number
                            
                            	Numeric Short MA Name, if format is VlanID or Number
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: short_ma_name_oui
                            
                            	VPN OUI, if Short MA Name format is VPN\_ID
                            	**type**\: int
                            
                            	**range:** 0..16777215
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: short_ma_name_string
                            
                            	String Short MA Name, if format is String
                            	**type**\: str
                            
                            	**range:** 0..46
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: short_ma_name_umc
                            
                            	Unique MEG ID Code (UMC), if format is ICCBased
                            	**type**\: str
                            
                            	**range:** 0..13
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: short_ma_name_vpn_index
                            
                            	VPN Index, if Short MA Name format is VPN\_ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: switching_name
                            
                            	Bridge Domain or Cross\-connect name, if Service Type is BridgeDomain or CrossConnect
                            	**type**\: str
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ce_id = None
                                self.group_name = None
                                self.remote_ce_id = None
                                self.service_type = None
                                self.short_ma_name_format = None
                                self.short_ma_name_icc = None
                                self.short_ma_name_number = None
                                self.short_ma_name_oui = None
                                self.short_ma_name_string = None
                                self.short_ma_name_umc = None
                                self.short_ma_name_vpn_index = None
                                self.switching_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:service-properties'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ce_id is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.remote_ce_id is not None:
                                    return True

                                if self.service_type is not None:
                                    return True

                                if self.short_ma_name_format is not None:
                                    return True

                                if self.short_ma_name_icc is not None:
                                    return True

                                if self.short_ma_name_number is not None:
                                    return True

                                if self.short_ma_name_oui is not None:
                                    return True

                                if self.short_ma_name_string is not None:
                                    return True

                                if self.short_ma_name_umc is not None:
                                    return True

                                if self.short_ma_name_vpn_index is not None:
                                    return True

                                if self.switching_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                                return meta._meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.ServiceProperties']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.service is None:
                                raise YPYModelError('Key property service is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:service[Cisco-IOS-XR-ethernet-cfm-cfg:service = ' + str(self.service) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.service is not None:
                                return True

                            if self.ais is not None and self.ais._has_data():
                                return True

                            if self.continuity_check_archive_hold_time is not None:
                                return True

                            if self.continuity_check_auto_traceroute is not None:
                                return True

                            if self.continuity_check_interval is not None and self.continuity_check_interval._has_data():
                                return True

                            if self.cross_check is not None and self.cross_check._has_data():
                                return True

                            if self.efd2 is not None and self.efd2._has_data():
                                return True

                            if self.log_ais is not None:
                                return True

                            if self.log_continuity_check_errors is not None:
                                return True

                            if self.log_continuity_check_state_changes is not None:
                                return True

                            if self.log_cross_check_errors is not None:
                                return True

                            if self.log_efd is not None:
                                return True

                            if self.maximum_meps is not None:
                                return True

                            if self.mip_auto_creation is not None and self.mip_auto_creation._has_data():
                                return True

                            if self.service_properties is not None and self.service_properties._has_data():
                                return True

                            if self.tags is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                            return meta._meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:services'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.service is not None:
                            for child_ref in self.service:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                        return meta._meta_table['EthernetFeatures.Cfm.Domains.Domain.Services']['meta_info']


                class DomainProperties(object):
                    """
                    Fundamental properties of the domain
                    
                    .. attribute:: level
                    
                    	Maintenance Domain Level
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: mdid_format
                    
                    	Maintenance Domain ID Format
                    	**type**\: :py:class:`CfmMdidFormatEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_cfg.CfmMdidFormatEnum>`
                    
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
                    
                    	**range:** 0..44
                    
                    

                    """

                    _prefix = 'ethernet-cfm-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.mdid_format = None
                        self.mdid_mac_address = None
                        self.mdid_number = None
                        self.mdid_string = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-cfg:domain-properties'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.level is not None:
                            return True

                        if self.mdid_format is not None:
                            return True

                        if self.mdid_mac_address is not None:
                            return True

                        if self.mdid_number is not None:
                            return True

                        if self.mdid_string is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                        return meta._meta_table['EthernetFeatures.Cfm.Domains.Domain.DomainProperties']['meta_info']

                @property
                def _common_path(self):
                    if self.domain is None:
                        raise YPYModelError('Key property domain is None')

                    return '/Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-cfm-cfg:cfm/Cisco-IOS-XR-ethernet-cfm-cfg:domains/Cisco-IOS-XR-ethernet-cfm-cfg:domain[Cisco-IOS-XR-ethernet-cfm-cfg:domain = ' + str(self.domain) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.domain is not None:
                        return True

                    if self.domain_properties is not None and self.domain_properties._has_data():
                        return True

                    if self.services is not None and self.services._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                    return meta._meta_table['EthernetFeatures.Cfm.Domains.Domain']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-cfm-cfg:cfm/Cisco-IOS-XR-ethernet-cfm-cfg:domains'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.domain is not None:
                    for child_ref in self.domain:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                return meta._meta_table['EthernetFeatures.Cfm.Domains']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-cfm-cfg:cfm'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.domains is not None and self.domains._has_data():
                return True

            if self.nv_satellite_sla_processing_disable is not None:
                return True

            if self.traceroute_cache is not None and self.traceroute_cache._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
            return meta._meta_table['EthernetFeatures.Cfm']['meta_info']


    class EtherLinkOam(object):
        """
        Ethernet Link OAM Global Configuration
        
        .. attribute:: profiles
        
        	Table of Ethernet Link OAM profiles
        	**type**\: :py:class:`Profiles <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles>`
        
        

        """

        _prefix = 'ethernet-link-oam-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.profiles = EthernetFeatures.EtherLinkOam.Profiles()
            self.profiles.parent = self


        class Profiles(object):
            """
            Table of Ethernet Link OAM profiles
            
            .. attribute:: profile
            
            	Name of the profile
            	**type**\: list of :py:class:`Profile <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile>`
            
            

            """

            _prefix = 'ethernet-link-oam-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.profile = YList()
                self.profile.parent = self
                self.profile.name = 'profile'


            class Profile(object):
                """
                Name of the profile
                
                .. attribute:: profile  <key>
                
                	none
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: action
                
                	Configure action parameters
                	**type**\: :py:class:`Action <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.Action>`
                
                .. attribute:: hello_interval
                
                	Possible Ethernet Link OAM hello intervals
                	**type**\: :py:class:`EtherLinkOamProfileHelloIntervalEnumEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamProfileHelloIntervalEnumEnum>`
                
                .. attribute:: link_monitor
                
                	Configure link monitor parameters
                	**type**\: :py:class:`LinkMonitor <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor>`
                
                .. attribute:: mib_retrieval
                
                	Enable MIB retrieval support
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: mode
                
                	Set the OAM mode to passive
                	**type**\: :py:class:`EtherLinkOamProfileModeEnumEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamProfileModeEnumEnum>`
                
                .. attribute:: remote_loopback
                
                	Enable remote loopback support
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: require_remote
                
                	Configure remote requirement parameters
                	**type**\: :py:class:`RequireRemote <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote>`
                
                .. attribute:: timeout
                
                	Connection timeout period in number of lost heartbeats
                	**type**\: int
                
                	**range:** 2..30
                
                .. attribute:: udlf
                
                	Enable uni\-directional link\-fault detection support
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                

                """

                _prefix = 'ethernet-link-oam-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.profile = None
                    self.action = EthernetFeatures.EtherLinkOam.Profiles.Profile.Action()
                    self.action.parent = self
                    self.hello_interval = None
                    self.link_monitor = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor()
                    self.link_monitor.parent = self
                    self.mib_retrieval = None
                    self.mode = None
                    self.remote_loopback = None
                    self.require_remote = EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote()
                    self.require_remote.parent = self
                    self.timeout = None
                    self.udlf = None


                class LinkMonitor(object):
                    """
                    Configure link monitor parameters
                    
                    .. attribute:: frame
                    
                    	Frame event configuration
                    	**type**\: :py:class:`Frame <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.Frame>`
                    
                    .. attribute:: frame_period
                    
                    	Frame\-period event configuration
                    	**type**\: :py:class:`FramePeriod <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.FramePeriod>`
                    
                    .. attribute:: frame_seconds
                    
                    	Frame\-seconds event configuration
                    	**type**\: :py:class:`FrameSeconds <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.FrameSeconds>`
                    
                    .. attribute:: monitoring
                    
                    	Disable monitoring
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: symbol_period
                    
                    	Symbol\-period event configuration
                    	**type**\: :py:class:`SymbolPeriod <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.SymbolPeriod>`
                    
                    

                    """

                    _prefix = 'ethernet-link-oam-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.frame = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.Frame()
                        self.frame.parent = self
                        self.frame_period = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.FramePeriod()
                        self.frame_period.parent = self
                        self.frame_seconds = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.FrameSeconds()
                        self.frame_seconds.parent = self
                        self.monitoring = None
                        self.symbol_period = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.SymbolPeriod()
                        self.symbol_period.parent = self


                    class FramePeriod(object):
                        """
                        Frame\-period event configuration
                        
                        .. attribute:: threshold
                        
                        	Threshold configuration for frame\-period events
                        	**type**\: :py:class:`Threshold <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.FramePeriod.Threshold>`
                        
                        .. attribute:: window
                        
                        	Window size configuration for frame\-period events
                        	**type**\: int
                        
                        	**range:** 100..60000
                        
                        

                        """

                        _prefix = 'ethernet-link-oam-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.threshold = None
                            self.window = None


                        class Threshold(object):
                            """
                            Threshold configuration for frame\-period
                            events
                            
                            .. attribute:: threshold_high
                            
                            	The high threshold for frame\-period events
                            	**type**\: int
                            
                            	**range:** 1..1000000
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: threshold_low
                            
                            	The low threshold for frame\-period events
                            	**type**\: int
                            
                            	**range:** 1..1000000
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.threshold_high = None
                                self.threshold_low = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-cfg:threshold'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.threshold_high is not None:
                                    return True

                                if self.threshold_low is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                                return meta._meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.FramePeriod.Threshold']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-cfg:frame-period'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.threshold is not None and self.threshold._has_data():
                                return True

                            if self.window is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                            return meta._meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.FramePeriod']['meta_info']


                    class FrameSeconds(object):
                        """
                        Frame\-seconds event configuration
                        
                        .. attribute:: threshold
                        
                        	Threshold configuration for frame\-seconds events
                        	**type**\: :py:class:`Threshold <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.FrameSeconds.Threshold>`
                        
                        .. attribute:: window
                        
                        	Window size configuration for frame\-seconds events
                        	**type**\: int
                        
                        	**range:** 10000..900000
                        
                        

                        """

                        _prefix = 'ethernet-link-oam-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.threshold = None
                            self.window = None


                        class Threshold(object):
                            """
                            Threshold configuration for frame\-seconds
                            events
                            
                            .. attribute:: threshold_high
                            
                            	The high threshold for frame\-seconds events
                            	**type**\: int
                            
                            	**range:** 1..900
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: threshold_low
                            
                            	The low threshold for frame\-seconds events
                            	**type**\: int
                            
                            	**range:** 1..900
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.threshold_high = None
                                self.threshold_low = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-cfg:threshold'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.threshold_high is not None:
                                    return True

                                if self.threshold_low is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                                return meta._meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.FrameSeconds.Threshold']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-cfg:frame-seconds'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.threshold is not None and self.threshold._has_data():
                                return True

                            if self.window is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                            return meta._meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.FrameSeconds']['meta_info']


                    class Frame(object):
                        """
                        Frame event configuration
                        
                        .. attribute:: threshold
                        
                        	Threshold configuration for frame events
                        	**type**\: :py:class:`Threshold <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.Frame.Threshold>`
                        
                        .. attribute:: window
                        
                        	Window size configuration for frame events
                        	**type**\: int
                        
                        	**range:** 1000..60000
                        
                        

                        """

                        _prefix = 'ethernet-link-oam-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.threshold = None
                            self.window = None


                        class Threshold(object):
                            """
                            Threshold configuration for frame events
                            
                            .. attribute:: threshold_high
                            
                            	The high threshold for frame events
                            	**type**\: int
                            
                            	**range:** 1..12000000
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: threshold_low
                            
                            	The low threshold for frame events
                            	**type**\: int
                            
                            	**range:** 1..12000000
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.threshold_high = None
                                self.threshold_low = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-cfg:threshold'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.threshold_high is not None:
                                    return True

                                if self.threshold_low is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                                return meta._meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.Frame.Threshold']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-cfg:frame'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.threshold is not None and self.threshold._has_data():
                                return True

                            if self.window is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                            return meta._meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.Frame']['meta_info']


                    class SymbolPeriod(object):
                        """
                        Symbol\-period event configuration
                        
                        .. attribute:: threshold
                        
                        	Threshold configuration for symbol\-period events
                        	**type**\: :py:class:`Threshold <ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.SymbolPeriod.Threshold>`
                        
                        .. attribute:: window
                        
                        	Window size configuration for symbol\-period events
                        	**type**\: int
                        
                        	**range:** 1000..60000
                        
                        

                        """

                        _prefix = 'ethernet-link-oam-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.threshold = None
                            self.window = None


                        class Threshold(object):
                            """
                            Threshold configuration for symbol\-period
                            events
                            
                            .. attribute:: threshold_high
                            
                            	The high threshold for symbol\-period
                            	**type**\: int
                            
                            	**range:** 1..60000000
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            .. attribute:: threshold_low
                            
                            	The low threshold for symbol\-period
                            	**type**\: int
                            
                            	**range:** 1..60000000
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.threshold_high = None
                                self.threshold_low = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-cfg:threshold'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.threshold_high is not None:
                                    return True

                                if self.threshold_low is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                                return meta._meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.SymbolPeriod.Threshold']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-cfg:symbol-period'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.threshold is not None and self.threshold._has_data():
                                return True

                            if self.window is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                            return meta._meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor.SymbolPeriod']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-cfg:link-monitor'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.frame is not None and self.frame._has_data():
                            return True

                        if self.frame_period is not None and self.frame_period._has_data():
                            return True

                        if self.frame_seconds is not None and self.frame_seconds._has_data():
                            return True

                        if self.monitoring is not None:
                            return True

                        if self.symbol_period is not None and self.symbol_period._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                        return meta._meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitor']['meta_info']


                class Action(object):
                    """
                    Configure action parameters
                    
                    .. attribute:: capabilities_conflict
                    
                    	Action to perform when a capabilities conflict occurs
                    	**type**\: :py:class:`EtherLinkOamEventActionEnum5Enum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum5Enum>`
                    
                    .. attribute:: critical_event
                    
                    	Action to perform when a critical event occurs
                    	**type**\: :py:class:`EtherLinkOamEventActionEnum2Enum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum2Enum>`
                    
                    .. attribute:: discovery_timeout
                    
                    	Action to perform when discovery timeout occurs
                    	**type**\: :py:class:`EtherLinkOamEventActionEnum5Enum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum5Enum>`
                    
                    .. attribute:: dying_gasp
                    
                    	Action to perform when a dying gasp occurs
                    	**type**\: :py:class:`EtherLinkOamEventActionEnum2Enum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum2Enum>`
                    
                    .. attribute:: high_threshold
                    
                    	Action to perform when a high\-threshold event occurs
                    	**type**\: :py:class:`EtherLinkOamEventActionEnum1Enum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum1Enum>`
                    
                    .. attribute:: link_fault
                    
                    	Action to perform when a link fault message is received
                    	**type**\: :py:class:`EtherLinkOamEventActionEnum5Enum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum5Enum>`
                    
                    .. attribute:: remote_loopback
                    
                    	Action to perform when remote loopback is entered or exited
                    	**type**\: :py:class:`EtherLinkOamEventActionEnum4Enum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum4Enum>`
                    
                    .. attribute:: session_down
                    
                    	Action to perform when a session goes down
                    	**type**\: :py:class:`EtherLinkOamEventActionEnum5Enum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum5Enum>`
                    
                    .. attribute:: session_up
                    
                    	Action to perform when a session comes up
                    	**type**\: :py:class:`EtherLinkOamEventActionEnum4Enum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum4Enum>`
                    
                    .. attribute:: wiring_conflict
                    
                    	Action to perform when a wiring conflict occurs
                    	**type**\: :py:class:`EtherLinkOamEventActionEnum6Enum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum6Enum>`
                    
                    

                    """

                    _prefix = 'ethernet-link-oam-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.capabilities_conflict = None
                        self.critical_event = None
                        self.discovery_timeout = None
                        self.dying_gasp = None
                        self.high_threshold = None
                        self.link_fault = None
                        self.remote_loopback = None
                        self.session_down = None
                        self.session_up = None
                        self.wiring_conflict = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-cfg:action'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.capabilities_conflict is not None:
                            return True

                        if self.critical_event is not None:
                            return True

                        if self.discovery_timeout is not None:
                            return True

                        if self.dying_gasp is not None:
                            return True

                        if self.high_threshold is not None:
                            return True

                        if self.link_fault is not None:
                            return True

                        if self.remote_loopback is not None:
                            return True

                        if self.session_down is not None:
                            return True

                        if self.session_up is not None:
                            return True

                        if self.wiring_conflict is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                        return meta._meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.Action']['meta_info']


                class RequireRemote(object):
                    """
                    Configure remote requirement parameters
                    
                    .. attribute:: link_monitoring
                    
                    	Enable link monitoring requirement
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: mib_retrieval
                    
                    	Enable MIB retrieval requirement
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: mode
                    
                    	Possible required OAM modes
                    	**type**\: :py:class:`EtherLinkOamProfileRequireModeEnumEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamProfileRequireModeEnumEnum>`
                    
                    .. attribute:: remote_loopback
                    
                    	Enable remote loopback requirement
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ethernet-link-oam-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.link_monitoring = None
                        self.mib_retrieval = None
                        self.mode = None
                        self.remote_loopback = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-cfg:require-remote'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.link_monitoring is not None:
                            return True

                        if self.mib_retrieval is not None:
                            return True

                        if self.mode is not None:
                            return True

                        if self.remote_loopback is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                        return meta._meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote']['meta_info']

                @property
                def _common_path(self):
                    if self.profile is None:
                        raise YPYModelError('Key property profile is None')

                    return '/Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-link-oam-cfg:ether-link-oam/Cisco-IOS-XR-ethernet-link-oam-cfg:profiles/Cisco-IOS-XR-ethernet-link-oam-cfg:profile[Cisco-IOS-XR-ethernet-link-oam-cfg:profile = ' + str(self.profile) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.profile is not None:
                        return True

                    if self.action is not None and self.action._has_data():
                        return True

                    if self.hello_interval is not None:
                        return True

                    if self.link_monitor is not None and self.link_monitor._has_data():
                        return True

                    if self.mib_retrieval is not None:
                        return True

                    if self.mode is not None:
                        return True

                    if self.remote_loopback is not None:
                        return True

                    if self.require_remote is not None and self.require_remote._has_data():
                        return True

                    if self.timeout is not None:
                        return True

                    if self.udlf is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                    return meta._meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-link-oam-cfg:ether-link-oam/Cisco-IOS-XR-ethernet-link-oam-cfg:profiles'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.profile is not None:
                    for child_ref in self.profile:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
                return meta._meta_table['EthernetFeatures.EtherLinkOam.Profiles']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-link-oam-cfg:ether-link-oam'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.profiles is not None and self.profiles._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
            return meta._meta_table['EthernetFeatures.EtherLinkOam']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.cfm is not None and self.cfm._has_data():
            return True

        if self.egress_filtering is not None and self.egress_filtering._has_data():
            return True

        if self.ether_link_oam is not None and self.ether_link_oam._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_cfg as meta
        return meta._meta_table['EthernetFeatures']['meta_info']



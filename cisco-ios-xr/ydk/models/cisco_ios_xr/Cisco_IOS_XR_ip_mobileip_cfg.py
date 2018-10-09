""" Cisco_IOS_XR_ip_mobileip_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-mobileip package configuration.

This module contains definitions
for the following management objects\:
  mobile\-ip\: MobileIP configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EncapOpt(Enum):
    """
    EncapOpt (Enum Class)

    Encap opt

    .. data:: greipv4 = 4

    	GRE IPv4 tunnel encap

    .. data:: greipv6 = 5

    	GRE IPv6 tunnel encap

    .. data:: mgreipv4 = 7

    	mGRE IPv4 tunnel encap

    .. data:: mgreipv6 = 8

    	mGRE IPv6 tunnel encap

    """

    greipv4 = Enum.YLeaf(4, "greipv4")

    greipv6 = Enum.YLeaf(5, "greipv6")

    mgreipv4 = Enum.YLeaf(7, "mgreipv4")

    mgreipv6 = Enum.YLeaf(8, "mgreipv6")


class GreKeyType(Enum):
    """
    GreKeyType (Enum Class)

    Gre key type

    .. data:: symmetric = 1

    	Symmetric GRE Key (same Uplink and Downlink

    	key)

    """

    symmetric = Enum.YLeaf(1, "symmetric")


class LmaRat(Enum):
    """
    LmaRat (Enum Class)

    Lma rat

    .. data:: virtual = 0

    	VIRTUAL rat

    .. data:: ppp = 1

    	PPP rat

    .. data:: ethernet = 2

    	ETHERNET rat

    .. data:: wlan = 3

    	WLAN rat

    .. data:: wi_max = 4

    	WIMAX rat

    .. data:: Y_3gppgeran = 5

    	3GPP_GERAN rat

    .. data:: Y_3gpputran = 6

    	3GPP_UTRAN rat

    .. data:: Y_3gppeutran = 7

    	3GPP_E_UTRAN rat

    .. data:: Y_3gpp2ehrpd = 8

    	3GPP2_EHRPD rat

    .. data:: Y_3gpp2hrpd = 9

    	3GPP2_HRPD rat

    .. data:: Y_3gpp21rtt = 10

    	3GPP2_1RTT rat

    .. data:: Y_3gpp2umb = 11

    	3GPP2_UMB rat

    """

    virtual = Enum.YLeaf(0, "virtual")

    ppp = Enum.YLeaf(1, "ppp")

    ethernet = Enum.YLeaf(2, "ethernet")

    wlan = Enum.YLeaf(3, "wlan")

    wi_max = Enum.YLeaf(4, "wi-max")

    Y_3gppgeran = Enum.YLeaf(5, "3gppgeran")

    Y_3gpputran = Enum.YLeaf(6, "3gpputran")

    Y_3gppeutran = Enum.YLeaf(7, "3gppeutran")

    Y_3gpp2ehrpd = Enum.YLeaf(8, "3gpp2ehrpd")

    Y_3gpp2hrpd = Enum.YLeaf(9, "3gpp2hrpd")

    Y_3gpp21rtt = Enum.YLeaf(10, "3gpp21rtt")

    Y_3gpp2umb = Enum.YLeaf(11, "3gpp2umb")


class LmaRole(Enum):
    """
    LmaRole (Enum Class)

    Lma role

    .. data:: Y_3gma = 0

    	3GMA mode

    """

    Y_3gma = Enum.YLeaf(0, "3gma")


class LmaService(Enum):
    """
    LmaService (Enum Class)

    Lma service

    .. data:: service_mll = 1

    	Wireless Private Routing service

    """

    service_mll = Enum.YLeaf(1, "service-mll")


class RedistSubType(Enum):
    """
    RedistSubType (Enum Class)

    Redist sub type

    .. data:: host_prefix = 1

    	Redistribute HoA/HNP host prefix routes

    .. data:: disable = 2

    	Disable redistribution of HoA/HNP host and pool

    	refix routes

    """

    host_prefix = Enum.YLeaf(1, "host-prefix")

    disable = Enum.YLeaf(2, "disable")


class RedistType(Enum):
    """
    RedistType (Enum Class)

    Redist type

    .. data:: home_address = 1

    	Redistribute HoA/HNP routes

    """

    home_address = Enum.YLeaf(1, "home-address")


class ServiceType(Enum):
    """
    ServiceType (Enum Class)

    Service type

    .. data:: ipv4 = 1

    	ipv4 service type

    .. data:: ipv6 = 2

    	ipv6 service type

    .. data:: dual = 3

    	dual service type

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")

    dual = Enum.YLeaf(3, "dual")



class MobileIp(Entity):
    """
    MobileIP configuration
    
    .. attribute:: domains
    
    	Table of Domain
    	**type**\:  :py:class:`Domains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains>`
    
    .. attribute:: lmas
    
    	Table of LMA
    	**type**\:  :py:class:`Lmas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas>`
    
    

    """

    _prefix = 'ip-mobileip-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(MobileIp, self).__init__()
        self._top_entity = None

        self.yang_name = "mobile-ip"
        self.yang_parent_name = "Cisco-IOS-XR-ip-mobileip-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("domains", ("domains", MobileIp.Domains)), ("lmas", ("lmas", MobileIp.Lmas))])
        self._leafs = OrderedDict()

        self.domains = MobileIp.Domains()
        self.domains.parent = self
        self._children_name_map["domains"] = "domains"

        self.lmas = MobileIp.Lmas()
        self.lmas.parent = self
        self._children_name_map["lmas"] = "lmas"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-mobileip-cfg:mobile-ip"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MobileIp, [], name, value)


    class Domains(Entity):
        """
        Table of Domain
        
        .. attribute:: domain
        
        	PMIPv6 domain configuration
        	**type**\: list of  		 :py:class:`Domain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain>`
        
        

        """

        _prefix = 'ip-mobileip-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MobileIp.Domains, self).__init__()

            self.yang_name = "domains"
            self.yang_parent_name = "mobile-ip"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("domain", ("domain", MobileIp.Domains.Domain))])
            self._leafs = OrderedDict()

            self.domain = YList(self)
            self._segment_path = lambda: "domains"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-cfg:mobile-ip/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MobileIp.Domains, [], name, value)


        class Domain(Entity):
            """
            PMIPv6 domain configuration
            
            .. attribute:: domain_name  (key)
            
            	Domain Name
            	**type**\: str
            
            	**length:** 1..125
            
            .. attribute:: mags
            
            	Table of MAG
            	**type**\:  :py:class:`Mags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Mags>`
            
            .. attribute:: nais
            
            	Table of NAI
            	**type**\:  :py:class:`Nais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Nais>`
            
            .. attribute:: authenticate_option
            
            	Authentication option between PMIPV6 entities
            	**type**\:  :py:class:`AuthenticateOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.AuthenticateOption>`
            
            .. attribute:: lmas
            
            	Table of LMA
            	**type**\:  :py:class:`Lmas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Lmas>`
            
            .. attribute:: enable
            
            	Enable PMIPv6 domain configuration. Deletion of this object also causes deletion of all associated objects under Domain
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-mobileip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MobileIp.Domains.Domain, self).__init__()

                self.yang_name = "domain"
                self.yang_parent_name = "domains"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['domain_name']
                self._child_classes = OrderedDict([("mags", ("mags", MobileIp.Domains.Domain.Mags)), ("nais", ("nais", MobileIp.Domains.Domain.Nais)), ("authenticate-option", ("authenticate_option", MobileIp.Domains.Domain.AuthenticateOption)), ("lmas", ("lmas", MobileIp.Domains.Domain.Lmas))])
                self._leafs = OrderedDict([
                    ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.domain_name = None
                self.enable = None

                self.mags = MobileIp.Domains.Domain.Mags()
                self.mags.parent = self
                self._children_name_map["mags"] = "mags"

                self.nais = MobileIp.Domains.Domain.Nais()
                self.nais.parent = self
                self._children_name_map["nais"] = "nais"

                self.authenticate_option = MobileIp.Domains.Domain.AuthenticateOption()
                self.authenticate_option.parent = self
                self._children_name_map["authenticate_option"] = "authenticate-option"

                self.lmas = MobileIp.Domains.Domain.Lmas()
                self.lmas.parent = self
                self._children_name_map["lmas"] = "lmas"
                self._segment_path = lambda: "domain" + "[domain-name='" + str(self.domain_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-cfg:mobile-ip/domains/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MobileIp.Domains.Domain, ['domain_name', 'enable'], name, value)


            class Mags(Entity):
                """
                Table of MAG
                
                .. attribute:: mag
                
                	MAG within domain
                	**type**\: list of  		 :py:class:`Mag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Mags.Mag>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Domains.Domain.Mags, self).__init__()

                    self.yang_name = "mags"
                    self.yang_parent_name = "domain"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("mag", ("mag", MobileIp.Domains.Domain.Mags.Mag))])
                    self._leafs = OrderedDict()

                    self.mag = YList(self)
                    self._segment_path = lambda: "mags"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Domains.Domain.Mags, [], name, value)


                class Mag(Entity):
                    """
                    MAG within domain
                    
                    .. attribute:: mag_name  (key)
                    
                    	MAG Identifier
                    	**type**\: str
                    
                    	**length:** 1..125
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Domains.Domain.Mags.Mag, self).__init__()

                        self.yang_name = "mag"
                        self.yang_parent_name = "mags"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['mag_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('mag_name', (YLeaf(YType.str, 'mag-name'), ['str'])),
                        ])
                        self.mag_name = None
                        self._segment_path = lambda: "mag" + "[mag-name='" + str(self.mag_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MobileIp.Domains.Domain.Mags.Mag, ['mag_name'], name, value)


            class Nais(Entity):
                """
                Table of NAI
                
                .. attribute:: nai
                
                	Network access identifier or Realm
                	**type**\: list of  		 :py:class:`Nai <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Nais.Nai>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Domains.Domain.Nais, self).__init__()

                    self.yang_name = "nais"
                    self.yang_parent_name = "domain"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("nai", ("nai", MobileIp.Domains.Domain.Nais.Nai))])
                    self._leafs = OrderedDict()

                    self.nai = YList(self)
                    self._segment_path = lambda: "nais"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Domains.Domain.Nais, [], name, value)


                class Nai(Entity):
                    """
                    Network access identifier or Realm
                    
                    .. attribute:: nai_name  (key)
                    
                    	MN Identifier
                    	**type**\: str
                    
                    	**length:** 1..125
                    
                    .. attribute:: lma
                    
                    	LMA for this MN
                    	**type**\: str
                    
                    	**length:** 1..125
                    
                    .. attribute:: apn
                    
                    	Access point network for this MN
                    	**type**\: str
                    
                    	**length:** 1..125
                    
                    .. attribute:: customer
                    
                    	Customer name for this MN
                    	**type**\: str
                    
                    	**length:** 1..125
                    
                    .. attribute:: service
                    
                    	Service type for this MN
                    	**type**\:  :py:class:`ServiceType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.ServiceType>`
                    
                    .. attribute:: network
                    
                    	Network name (Address pool) for this MN
                    	**type**\: str
                    
                    	**length:** 1..125
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Domains.Domain.Nais.Nai, self).__init__()

                        self.yang_name = "nai"
                        self.yang_parent_name = "nais"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['nai_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('nai_name', (YLeaf(YType.str, 'nai-name'), ['str'])),
                            ('lma', (YLeaf(YType.str, 'lma'), ['str'])),
                            ('apn', (YLeaf(YType.str, 'apn'), ['str'])),
                            ('customer', (YLeaf(YType.str, 'customer'), ['str'])),
                            ('service', (YLeaf(YType.enumeration, 'service'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'ServiceType', '')])),
                            ('network', (YLeaf(YType.str, 'network'), ['str'])),
                        ])
                        self.nai_name = None
                        self.lma = None
                        self.apn = None
                        self.customer = None
                        self.service = None
                        self.network = None
                        self._segment_path = lambda: "nai" + "[nai-name='" + str(self.nai_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MobileIp.Domains.Domain.Nais.Nai, ['nai_name', 'lma', 'apn', 'customer', 'service', 'network'], name, value)


            class AuthenticateOption(Entity):
                """
                Authentication option between PMIPV6 entities
                
                .. attribute:: spi
                
                	SPI in hex value
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: key
                
                	ASCII string
                	**type**\: str
                
                	**length:** 1..125
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Domains.Domain.AuthenticateOption, self).__init__()

                    self.yang_name = "authenticate-option"
                    self.yang_parent_name = "domain"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('spi', (YLeaf(YType.str, 'spi'), ['str'])),
                        ('key', (YLeaf(YType.str, 'key'), ['str'])),
                    ])
                    self.spi = None
                    self.key = None
                    self._segment_path = lambda: "authenticate-option"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Domains.Domain.AuthenticateOption, ['spi', 'key'], name, value)


            class Lmas(Entity):
                """
                Table of LMA
                
                .. attribute:: lma
                
                	LMA within domain
                	**type**\: list of  		 :py:class:`Lma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Lmas.Lma>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Domains.Domain.Lmas, self).__init__()

                    self.yang_name = "lmas"
                    self.yang_parent_name = "domain"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("lma", ("lma", MobileIp.Domains.Domain.Lmas.Lma))])
                    self._leafs = OrderedDict()

                    self.lma = YList(self)
                    self._segment_path = lambda: "lmas"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Domains.Domain.Lmas, [], name, value)


                class Lma(Entity):
                    """
                    LMA within domain
                    
                    .. attribute:: lma_name  (key)
                    
                    	LMA Identifier
                    	**type**\: str
                    
                    	**length:** 1..125
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Domains.Domain.Lmas.Lma, self).__init__()

                        self.yang_name = "lma"
                        self.yang_parent_name = "lmas"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['lma_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lma_name', (YLeaf(YType.str, 'lma-name'), ['str'])),
                        ])
                        self.lma_name = None
                        self._segment_path = lambda: "lma" + "[lma-name='" + str(self.lma_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MobileIp.Domains.Domain.Lmas.Lma, ['lma_name'], name, value)


    class Lmas(Entity):
        """
        Table of LMA
        
        .. attribute:: lma
        
        	PMIPv6 LMA configuration
        	**type**\: list of  		 :py:class:`Lma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma>`
        
        

        """

        _prefix = 'ip-mobileip-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MobileIp.Lmas, self).__init__()

            self.yang_name = "lmas"
            self.yang_parent_name = "mobile-ip"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lma", ("lma", MobileIp.Lmas.Lma))])
            self._leafs = OrderedDict()

            self.lma = YList(self)
            self._segment_path = lambda: "lmas"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-cfg:mobile-ip/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MobileIp.Lmas, [], name, value)


        class Lma(Entity):
            """
            PMIPv6 LMA configuration
            
            .. attribute:: lma_name  (key)
            
            	LMA name
            	**type**\: str
            
            	**length:** 1..125
            
            .. attribute:: domain_name  (key)
            
            	Domain name
            	**type**\: str
            
            	**length:** 1..125
            
            .. attribute:: binding_revocation_attributes
            
            	LMA Binding Revocation Attributes
            	**type**\:  :py:class:`BindingRevocationAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.BindingRevocationAttributes>`
            
            .. attribute:: rat_attributes
            
            	Radio access technology type config  this LMA
            	**type**\:  :py:class:`RatAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.RatAttributes>`
            
            .. attribute:: heart_beat_attributes
            
            	heartbeat config for this LMA
            	**type**\:  :py:class:`HeartBeatAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.HeartBeatAttributes>`
            
            .. attribute:: lmaipv6_addresses
            
            	Table of LMAIPv6Address
            	**type**\:  :py:class:`Lmaipv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Lmaipv6Addresses>`
            
            .. attribute:: hnp
            
            	LMA HNP options
            	**type**\:  :py:class:`Hnp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Hnp>`
            
            .. attribute:: redistribute
            
            	Redistribute routes
            	**type**\:  :py:class:`Redistribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Redistribute>`
            
            .. attribute:: aaa
            
            	AAA configuration for this LMA
            	**type**\:  :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Aaa>`
            
            .. attribute:: dscp
            
            	DSCP for packets originating from this LMA
            	**type**\:  :py:class:`Dscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Dscp>`
            
            .. attribute:: lmaipv4_addresses
            
            	Table of LMAIPv4Address
            	**type**\:  :py:class:`Lmaipv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Lmaipv4Addresses>`
            
            .. attribute:: roles
            
            	Table of Role
            	**type**\:  :py:class:`Roles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Roles>`
            
            .. attribute:: binding_attributes
            
            	LMA binding attributes
            	**type**\:  :py:class:`BindingAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.BindingAttributes>`
            
            .. attribute:: mags
            
            	Table of MAG
            	**type**\:  :py:class:`Mags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Mags>`
            
            .. attribute:: tunnel_attributes
            
            	tunnel attributes
            	**type**\:  :py:class:`TunnelAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.TunnelAttributes>`
            
            .. attribute:: services
            
            	Table of Service
            	**type**\:  :py:class:`Services <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services>`
            
            .. attribute:: networks
            
            	Table of Network
            	**type**\:  :py:class:`Networks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks>`
            
            .. attribute:: replay_protection
            
            	Replay Protection Method
            	**type**\:  :py:class:`ReplayProtection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.ReplayProtection>`
            
            .. attribute:: generate
            
            	generate gre key for LMA bindings
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: mobile_route_ad
            
            	Specify the Admin Distance value
            	**type**\: int
            
            	**range:** 1..254
            
            .. attribute:: ani
            
            	enable ani option processing in LMA
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: multipath
            
            	enable multipath support for LMA
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: dynamic
            
            	enable dynamic mag learning for LMA
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enforce
            
            	enforce heartbeat values to MAG
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: default_profile
            
            	Default MN profile for LMA
            	**type**\: str
            
            	**length:** 1..125
            
            .. attribute:: interface
            
            	CN facing interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: mobile_map
            
            	Mobile Map for this LMA
            	**type**\: str
            
            	**length:** 1..125
            
            .. attribute:: pgw_subs_cont
            
            	Feature related to interface with PGW
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-mobileip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MobileIp.Lmas.Lma, self).__init__()

                self.yang_name = "lma"
                self.yang_parent_name = "lmas"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lma_name','domain_name']
                self._child_classes = OrderedDict([("binding-revocation-attributes", ("binding_revocation_attributes", MobileIp.Lmas.Lma.BindingRevocationAttributes)), ("rat-attributes", ("rat_attributes", MobileIp.Lmas.Lma.RatAttributes)), ("heart-beat-attributes", ("heart_beat_attributes", MobileIp.Lmas.Lma.HeartBeatAttributes)), ("lmaipv6-addresses", ("lmaipv6_addresses", MobileIp.Lmas.Lma.Lmaipv6Addresses)), ("hnp", ("hnp", MobileIp.Lmas.Lma.Hnp)), ("redistribute", ("redistribute", MobileIp.Lmas.Lma.Redistribute)), ("aaa", ("aaa", MobileIp.Lmas.Lma.Aaa)), ("dscp", ("dscp", MobileIp.Lmas.Lma.Dscp)), ("lmaipv4-addresses", ("lmaipv4_addresses", MobileIp.Lmas.Lma.Lmaipv4Addresses)), ("roles", ("roles", MobileIp.Lmas.Lma.Roles)), ("binding-attributes", ("binding_attributes", MobileIp.Lmas.Lma.BindingAttributes)), ("mags", ("mags", MobileIp.Lmas.Lma.Mags)), ("tunnel-attributes", ("tunnel_attributes", MobileIp.Lmas.Lma.TunnelAttributes)), ("services", ("services", MobileIp.Lmas.Lma.Services)), ("networks", ("networks", MobileIp.Lmas.Lma.Networks)), ("replay-protection", ("replay_protection", MobileIp.Lmas.Lma.ReplayProtection))])
                self._leafs = OrderedDict([
                    ('lma_name', (YLeaf(YType.str, 'lma-name'), ['str'])),
                    ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                    ('generate', (YLeaf(YType.empty, 'generate'), ['Empty'])),
                    ('mobile_route_ad', (YLeaf(YType.uint32, 'mobile-route-ad'), ['int'])),
                    ('ani', (YLeaf(YType.empty, 'ani'), ['Empty'])),
                    ('multipath', (YLeaf(YType.empty, 'multipath'), ['Empty'])),
                    ('dynamic', (YLeaf(YType.empty, 'dynamic'), ['Empty'])),
                    ('enforce', (YLeaf(YType.empty, 'enforce'), ['Empty'])),
                    ('default_profile', (YLeaf(YType.str, 'default-profile'), ['str'])),
                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                    ('mobile_map', (YLeaf(YType.str, 'mobile-map'), ['str'])),
                    ('pgw_subs_cont', (YLeaf(YType.empty, 'pgw-subs-cont'), ['Empty'])),
                ])
                self.lma_name = None
                self.domain_name = None
                self.generate = None
                self.mobile_route_ad = None
                self.ani = None
                self.multipath = None
                self.dynamic = None
                self.enforce = None
                self.default_profile = None
                self.interface = None
                self.mobile_map = None
                self.pgw_subs_cont = None

                self.binding_revocation_attributes = MobileIp.Lmas.Lma.BindingRevocationAttributes()
                self.binding_revocation_attributes.parent = self
                self._children_name_map["binding_revocation_attributes"] = "binding-revocation-attributes"

                self.rat_attributes = MobileIp.Lmas.Lma.RatAttributes()
                self.rat_attributes.parent = self
                self._children_name_map["rat_attributes"] = "rat-attributes"

                self.heart_beat_attributes = MobileIp.Lmas.Lma.HeartBeatAttributes()
                self.heart_beat_attributes.parent = self
                self._children_name_map["heart_beat_attributes"] = "heart-beat-attributes"

                self.lmaipv6_addresses = MobileIp.Lmas.Lma.Lmaipv6Addresses()
                self.lmaipv6_addresses.parent = self
                self._children_name_map["lmaipv6_addresses"] = "lmaipv6-addresses"

                self.hnp = MobileIp.Lmas.Lma.Hnp()
                self.hnp.parent = self
                self._children_name_map["hnp"] = "hnp"

                self.redistribute = MobileIp.Lmas.Lma.Redistribute()
                self.redistribute.parent = self
                self._children_name_map["redistribute"] = "redistribute"

                self.aaa = MobileIp.Lmas.Lma.Aaa()
                self.aaa.parent = self
                self._children_name_map["aaa"] = "aaa"

                self.dscp = MobileIp.Lmas.Lma.Dscp()
                self.dscp.parent = self
                self._children_name_map["dscp"] = "dscp"

                self.lmaipv4_addresses = MobileIp.Lmas.Lma.Lmaipv4Addresses()
                self.lmaipv4_addresses.parent = self
                self._children_name_map["lmaipv4_addresses"] = "lmaipv4-addresses"

                self.roles = MobileIp.Lmas.Lma.Roles()
                self.roles.parent = self
                self._children_name_map["roles"] = "roles"

                self.binding_attributes = MobileIp.Lmas.Lma.BindingAttributes()
                self.binding_attributes.parent = self
                self._children_name_map["binding_attributes"] = "binding-attributes"

                self.mags = MobileIp.Lmas.Lma.Mags()
                self.mags.parent = self
                self._children_name_map["mags"] = "mags"

                self.tunnel_attributes = MobileIp.Lmas.Lma.TunnelAttributes()
                self.tunnel_attributes.parent = self
                self._children_name_map["tunnel_attributes"] = "tunnel-attributes"

                self.services = MobileIp.Lmas.Lma.Services()
                self.services.parent = self
                self._children_name_map["services"] = "services"

                self.networks = MobileIp.Lmas.Lma.Networks()
                self.networks.parent = self
                self._children_name_map["networks"] = "networks"

                self.replay_protection = MobileIp.Lmas.Lma.ReplayProtection()
                self.replay_protection.parent = self
                self._children_name_map["replay_protection"] = "replay-protection"
                self._segment_path = lambda: "lma" + "[lma-name='" + str(self.lma_name) + "']" + "[domain-name='" + str(self.domain_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-cfg:mobile-ip/lmas/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MobileIp.Lmas.Lma, ['lma_name', 'domain_name', 'generate', 'mobile_route_ad', 'ani', 'multipath', 'dynamic', 'enforce', 'default_profile', 'interface', 'mobile_map', 'pgw_subs_cont'], name, value)


            class BindingRevocationAttributes(Entity):
                """
                LMA Binding Revocation Attributes
                
                .. attribute:: delay
                
                	Time to wait before Retransmitting BRI Message
                	**type**\:  :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay>`
                
                .. attribute:: retry
                
                	Number of Retransmissons Allowed for BRI Message
                	**type**\: int
                
                	**range:** 1..10
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.BindingRevocationAttributes, self).__init__()

                    self.yang_name = "binding-revocation-attributes"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("delay", ("delay", MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay))])
                    self._leafs = OrderedDict([
                        ('retry', (YLeaf(YType.uint32, 'retry'), ['int'])),
                    ])
                    self.retry = None

                    self.delay = MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay()
                    self.delay.parent = self
                    self._children_name_map["delay"] = "delay"
                    self._segment_path = lambda: "binding-revocation-attributes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.BindingRevocationAttributes, ['retry'], name, value)


                class Delay(Entity):
                    """
                    Time to wait before Retransmitting BRI
                    Message
                    
                    .. attribute:: br_min
                    
                    	Specify in millisec
                    	**type**\: int
                    
                    	**range:** 500..65535
                    
                    .. attribute:: br_max
                    
                    	Specify in millisec
                    	**type**\: int
                    
                    	**range:** 500..65535
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay, self).__init__()

                        self.yang_name = "delay"
                        self.yang_parent_name = "binding-revocation-attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('br_min', (YLeaf(YType.uint32, 'br-min'), ['int'])),
                            ('br_max', (YLeaf(YType.uint32, 'br-max'), ['int'])),
                        ])
                        self.br_min = None
                        self.br_max = None
                        self._segment_path = lambda: "delay"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay, ['br_min', 'br_max'], name, value)


            class RatAttributes(Entity):
                """
                Radio access technology type config  this LMA
                
                .. attribute:: lma_rat
                
                	LMA rat type
                	**type**\:  :py:class:`LmaRat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.LmaRat>`
                
                .. attribute:: priority_value
                
                	Specify the priority value
                	**type**\: int
                
                	**range:** 1..255
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.RatAttributes, self).__init__()

                    self.yang_name = "rat-attributes"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('lma_rat', (YLeaf(YType.enumeration, 'lma-rat'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'LmaRat', '')])),
                        ('priority_value', (YLeaf(YType.uint32, 'priority-value'), ['int'])),
                    ])
                    self.lma_rat = None
                    self.priority_value = None
                    self._segment_path = lambda: "rat-attributes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.RatAttributes, ['lma_rat', 'priority_value'], name, value)


            class HeartBeatAttributes(Entity):
                """
                heartbeat config for this LMA
                
                .. attribute:: interval
                
                	Specify the interval value in second
                	**type**\: int
                
                	**range:** 10..3600
                
                .. attribute:: retries
                
                	Specify the retry value
                	**type**\: int
                
                	**range:** 1..10
                
                .. attribute:: timeout
                
                	Specify the timeout value
                	**type**\: int
                
                	**range:** 1..3600
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.HeartBeatAttributes, self).__init__()

                    self.yang_name = "heart-beat-attributes"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                        ('retries', (YLeaf(YType.uint32, 'retries'), ['int'])),
                        ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                    ])
                    self.interval = None
                    self.retries = None
                    self.timeout = None
                    self._segment_path = lambda: "heart-beat-attributes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.HeartBeatAttributes, ['interval', 'retries', 'timeout'], name, value)


            class Lmaipv6Addresses(Entity):
                """
                Table of LMAIPv6Address
                
                .. attribute:: lmaipv6_address
                
                	Configure IPv6 address for this LMA
                	**type**\: list of  		 :py:class:`Lmaipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Lmaipv6Addresses.Lmaipv6Address>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Lmaipv6Addresses, self).__init__()

                    self.yang_name = "lmaipv6-addresses"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("lmaipv6-address", ("lmaipv6_address", MobileIp.Lmas.Lma.Lmaipv6Addresses.Lmaipv6Address))])
                    self._leafs = OrderedDict()

                    self.lmaipv6_address = YList(self)
                    self._segment_path = lambda: "lmaipv6-addresses"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.Lmaipv6Addresses, [], name, value)


                class Lmaipv6Address(Entity):
                    """
                    Configure IPv6 address for this LMA
                    
                    .. attribute:: address  (key)
                    
                    	LMA IPv6 address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.Lmaipv6Addresses.Lmaipv6Address, self).__init__()

                        self.yang_name = "lmaipv6-address"
                        self.yang_parent_name = "lmaipv6-addresses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                        ])
                        self.address = None
                        self._segment_path = lambda: "lmaipv6-address" + "[address='" + str(self.address) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MobileIp.Lmas.Lma.Lmaipv6Addresses.Lmaipv6Address, ['address'], name, value)


            class Hnp(Entity):
                """
                LMA HNP options
                
                .. attribute:: maximum
                
                	maximum HNPs allowed per MN interface
                	**type**\: int
                
                	**range:** 1..3
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Hnp, self).__init__()

                    self.yang_name = "hnp"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                    ])
                    self.maximum = None
                    self._segment_path = lambda: "hnp"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.Hnp, ['maximum'], name, value)


            class Redistribute(Entity):
                """
                Redistribute routes
                
                .. attribute:: redist_type
                
                	Redistribute type
                	**type**\:  :py:class:`RedistType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.RedistType>`
                
                .. attribute:: redist_sub_type
                
                	Redistribute sub\-type
                	**type**\:  :py:class:`RedistSubType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.RedistSubType>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Redistribute, self).__init__()

                    self.yang_name = "redistribute"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('redist_type', (YLeaf(YType.enumeration, 'redist-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'RedistType', '')])),
                        ('redist_sub_type', (YLeaf(YType.enumeration, 'redist-sub-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'RedistSubType', '')])),
                    ])
                    self.redist_type = None
                    self.redist_sub_type = None
                    self._segment_path = lambda: "redistribute"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.Redistribute, ['redist_type', 'redist_sub_type'], name, value)


            class Aaa(Entity):
                """
                AAA configuration for this LMA
                
                .. attribute:: accounting
                
                	AAA accounting for this LMA
                	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Aaa.Accounting>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Aaa, self).__init__()

                    self.yang_name = "aaa"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("accounting", ("accounting", MobileIp.Lmas.Lma.Aaa.Accounting))])
                    self._leafs = OrderedDict()

                    self.accounting = MobileIp.Lmas.Lma.Aaa.Accounting()
                    self.accounting.parent = self
                    self._children_name_map["accounting"] = "accounting"
                    self._segment_path = lambda: "aaa"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.Aaa, [], name, value)


                class Accounting(Entity):
                    """
                    AAA accounting for this LMA
                    
                    .. attribute:: enable
                    
                    	Set constant integer
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interim_interval
                    
                    	Interim acounting interval (in minutes)
                    	**type**\: int
                    
                    	**range:** 1..86400
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.Aaa.Accounting, self).__init__()

                        self.yang_name = "accounting"
                        self.yang_parent_name = "aaa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ('interim_interval', (YLeaf(YType.uint32, 'interim-interval'), ['int'])),
                        ])
                        self.enable = None
                        self.interim_interval = None
                        self._segment_path = lambda: "accounting"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MobileIp.Lmas.Lma.Aaa.Accounting, ['enable', 'interim_interval'], name, value)


            class Dscp(Entity):
                """
                DSCP for packets originating from this LMA
                
                .. attribute:: value
                
                	Specify the DSCP value
                	**type**\: int
                
                	**range:** 1..63
                
                .. attribute:: force
                
                	Set constant integer
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Dscp, self).__init__()

                    self.yang_name = "dscp"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                        ('force', (YLeaf(YType.empty, 'force'), ['Empty'])),
                    ])
                    self.value = None
                    self.force = None
                    self._segment_path = lambda: "dscp"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.Dscp, ['value', 'force'], name, value)


            class Lmaipv4Addresses(Entity):
                """
                Table of LMAIPv4Address
                
                .. attribute:: lmaipv4_address
                
                	Configure IPv4 address for this LMA
                	**type**\: list of  		 :py:class:`Lmaipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Lmaipv4Addresses.Lmaipv4Address>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Lmaipv4Addresses, self).__init__()

                    self.yang_name = "lmaipv4-addresses"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("lmaipv4-address", ("lmaipv4_address", MobileIp.Lmas.Lma.Lmaipv4Addresses.Lmaipv4Address))])
                    self._leafs = OrderedDict()

                    self.lmaipv4_address = YList(self)
                    self._segment_path = lambda: "lmaipv4-addresses"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.Lmaipv4Addresses, [], name, value)


                class Lmaipv4Address(Entity):
                    """
                    Configure IPv4 address for this LMA
                    
                    .. attribute:: address  (key)
                    
                    	LMA IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.Lmaipv4Addresses.Lmaipv4Address, self).__init__()

                        self.yang_name = "lmaipv4-address"
                        self.yang_parent_name = "lmaipv4-addresses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                        ])
                        self.address = None
                        self._segment_path = lambda: "lmaipv4-address" + "[address='" + str(self.address) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MobileIp.Lmas.Lma.Lmaipv4Addresses.Lmaipv4Address, ['address'], name, value)


            class Roles(Entity):
                """
                Table of Role
                
                .. attribute:: role
                
                	Role of this LMA
                	**type**\: list of  		 :py:class:`Role <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Roles.Role>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Roles, self).__init__()

                    self.yang_name = "roles"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("role", ("role", MobileIp.Lmas.Lma.Roles.Role))])
                    self._leafs = OrderedDict()

                    self.role = YList(self)
                    self._segment_path = lambda: "roles"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.Roles, [], name, value)


                class Role(Entity):
                    """
                    Role of this LMA
                    
                    .. attribute:: lma_role  (key)
                    
                    	LMA role mode
                    	**type**\:  :py:class:`LmaRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.LmaRole>`
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.Roles.Role, self).__init__()

                        self.yang_name = "role"
                        self.yang_parent_name = "roles"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['lma_role']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lma_role', (YLeaf(YType.enumeration, 'lma-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'LmaRole', '')])),
                        ])
                        self.lma_role = None
                        self._segment_path = lambda: "role" + "[lma-role='" + str(self.lma_role) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MobileIp.Lmas.Lma.Roles.Role, ['lma_role'], name, value)


            class BindingAttributes(Entity):
                """
                LMA binding attributes
                
                .. attribute:: refresh_time
                
                	Specify in seconds, (multiples of 4)
                	**type**\: int
                
                	**range:** 4..65000
                
                	**units**\: second
                
                .. attribute:: delete_wait_interval
                
                	bce delete wait time interval
                	**type**\: int
                
                	**range:** 100..65535
                
                .. attribute:: create_wait_interval
                
                	bce create wait time interval
                	**type**\: int
                
                	**range:** 100..65535
                
                .. attribute:: max_life_time
                
                	Maximum bce lifetime permitted
                	**type**\: int
                
                	**range:** 10..65535
                
                	**units**\: second
                
                .. attribute:: maximum
                
                	Specify max. number of bindings
                	**type**\: int
                
                	**range:** 1..128000
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.BindingAttributes, self).__init__()

                    self.yang_name = "binding-attributes"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('refresh_time', (YLeaf(YType.uint32, 'refresh-time'), ['int'])),
                        ('delete_wait_interval', (YLeaf(YType.uint32, 'delete-wait-interval'), ['int'])),
                        ('create_wait_interval', (YLeaf(YType.uint32, 'create-wait-interval'), ['int'])),
                        ('max_life_time', (YLeaf(YType.uint32, 'max-life-time'), ['int'])),
                        ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                    ])
                    self.refresh_time = None
                    self.delete_wait_interval = None
                    self.create_wait_interval = None
                    self.max_life_time = None
                    self.maximum = None
                    self._segment_path = lambda: "binding-attributes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.BindingAttributes, ['refresh_time', 'delete_wait_interval', 'create_wait_interval', 'max_life_time', 'maximum'], name, value)


            class Mags(Entity):
                """
                Table of MAG
                
                .. attribute:: mag
                
                	MAG within LMA
                	**type**\: list of  		 :py:class:`Mag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Mags.Mag>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Mags, self).__init__()

                    self.yang_name = "mags"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("mag", ("mag", MobileIp.Lmas.Lma.Mags.Mag))])
                    self._leafs = OrderedDict()

                    self.mag = YList(self)
                    self._segment_path = lambda: "mags"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.Mags, [], name, value)


                class Mag(Entity):
                    """
                    MAG within LMA
                    
                    .. attribute:: mag_name  (key)
                    
                    	MAG identifier
                    	**type**\: str
                    
                    	**length:** 1..125
                    
                    .. attribute:: domain_name  (key)
                    
                    	Domain name
                    	**type**\: str
                    
                    	**length:** 1..125
                    
                    .. attribute:: authenticate_option
                    
                    	Authentication option between PMIPV6 entities
                    	**type**\:  :py:class:`AuthenticateOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption>`
                    
                    .. attribute:: dscp
                    
                    	DSCP for packets originating from this MAG
                    	**type**\:  :py:class:`Dscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Mags.Mag.Dscp>`
                    
                    .. attribute:: encap_option
                    
                    	Encapsulation option between PMIPV6 entities
                    	**type**\:  :py:class:`EncapOpt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.EncapOpt>`
                    
                    .. attribute:: ipv4_address
                    
                    	Configure IPv4 address for this MAG
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_address
                    
                    	Configure IPv6 address for this MAG
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: tunnel
                    
                    	static tunnel for this peer MAG
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.Mags.Mag, self).__init__()

                        self.yang_name = "mag"
                        self.yang_parent_name = "mags"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['mag_name','domain_name']
                        self._child_classes = OrderedDict([("authenticate-option", ("authenticate_option", MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption)), ("dscp", ("dscp", MobileIp.Lmas.Lma.Mags.Mag.Dscp))])
                        self._leafs = OrderedDict([
                            ('mag_name', (YLeaf(YType.str, 'mag-name'), ['str'])),
                            ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                            ('encap_option', (YLeaf(YType.enumeration, 'encap-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'EncapOpt', '')])),
                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ('tunnel', (YLeaf(YType.str, 'tunnel'), ['str'])),
                        ])
                        self.mag_name = None
                        self.domain_name = None
                        self.encap_option = None
                        self.ipv4_address = None
                        self.ipv6_address = None
                        self.tunnel = None

                        self.authenticate_option = MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption()
                        self.authenticate_option.parent = self
                        self._children_name_map["authenticate_option"] = "authenticate-option"

                        self.dscp = MobileIp.Lmas.Lma.Mags.Mag.Dscp()
                        self.dscp.parent = self
                        self._children_name_map["dscp"] = "dscp"
                        self._segment_path = lambda: "mag" + "[mag-name='" + str(self.mag_name) + "']" + "[domain-name='" + str(self.domain_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MobileIp.Lmas.Lma.Mags.Mag, ['mag_name', 'domain_name', 'encap_option', 'ipv4_address', 'ipv6_address', 'tunnel'], name, value)


                    class AuthenticateOption(Entity):
                        """
                        Authentication option between PMIPV6
                        entities
                        
                        .. attribute:: spi
                        
                        	SPI in hex value
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: key
                        
                        	ASCII string
                        	**type**\: str
                        
                        	**length:** 1..125
                        
                        

                        """

                        _prefix = 'ip-mobileip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption, self).__init__()

                            self.yang_name = "authenticate-option"
                            self.yang_parent_name = "mag"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('spi', (YLeaf(YType.str, 'spi'), ['str'])),
                                ('key', (YLeaf(YType.str, 'key'), ['str'])),
                            ])
                            self.spi = None
                            self.key = None
                            self._segment_path = lambda: "authenticate-option"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption, ['spi', 'key'], name, value)


                    class Dscp(Entity):
                        """
                        DSCP for packets originating from this MAG
                        
                        .. attribute:: value
                        
                        	Specify the DSCP value
                        	**type**\: int
                        
                        	**range:** 1..63
                        
                        .. attribute:: force
                        
                        	Set constant integer
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ip-mobileip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MobileIp.Lmas.Lma.Mags.Mag.Dscp, self).__init__()

                            self.yang_name = "dscp"
                            self.yang_parent_name = "mag"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('force', (YLeaf(YType.empty, 'force'), ['Empty'])),
                            ])
                            self.value = None
                            self.force = None
                            self._segment_path = lambda: "dscp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MobileIp.Lmas.Lma.Mags.Mag.Dscp, ['value', 'force'], name, value)


            class TunnelAttributes(Entity):
                """
                tunnel attributes
                
                .. attribute:: mtu
                
                	maximum transmission unit for tunnel
                	**type**\: int
                
                	**range:** 68..17916
                
                .. attribute:: acl
                
                	access list to apply for tunnel
                	**type**\: str
                
                	**length:** 1..125
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.TunnelAttributes, self).__init__()

                    self.yang_name = "tunnel-attributes"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                        ('acl', (YLeaf(YType.str, 'acl'), ['str'])),
                    ])
                    self.mtu = None
                    self.acl = None
                    self._segment_path = lambda: "tunnel-attributes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.TunnelAttributes, ['mtu', 'acl'], name, value)


            class Services(Entity):
                """
                Table of Service
                
                .. attribute:: service
                
                	Service of this LMA
                	**type**\: list of  		 :py:class:`Service <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Services, self).__init__()

                    self.yang_name = "services"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("service", ("service", MobileIp.Lmas.Lma.Services.Service))])
                    self._leafs = OrderedDict()

                    self.service = YList(self)
                    self._segment_path = lambda: "services"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.Services, [], name, value)


                class Service(Entity):
                    """
                    Service of this LMA
                    
                    .. attribute:: lma_service  (key)
                    
                    	LMA service mode
                    	**type**\:  :py:class:`LmaService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.LmaService>`
                    
                    .. attribute:: customers
                    
                    	Table of Customer
                    	**type**\:  :py:class:`Customers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers>`
                    
                    .. attribute:: mnp_customer
                    
                    	mnp limit config for all customer's
                    	**type**\: int
                    
                    	**range:** 1..4000000
                    
                    .. attribute:: mnp_ipv4_lmn
                    
                    	mnp limit config for all logical mn's
                    	**type**\: int
                    
                    	**range:** 1..32
                    
                    .. attribute:: mnp_ipv6_lmn
                    
                    	mnp limit config for all logical mn's
                    	**type**\: int
                    
                    	**range:** 1..32
                    
                    .. attribute:: mnp_lmn
                    
                    	mnp limit config for all logical mn's
                    	**type**\: int
                    
                    	**range:** 1..32
                    
                    .. attribute:: ignore_home_address
                    
                    	Ignore HoA/HNP option
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: mnp_ipv4_customer
                    
                    	mnp limit config for all customer's
                    	**type**\: int
                    
                    	**range:** 1..4000000
                    
                    .. attribute:: mnp_ipv6_customer
                    
                    	mnp limit config for all customer's
                    	**type**\: int
                    
                    	**range:** 1..4000000
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.Services.Service, self).__init__()

                        self.yang_name = "service"
                        self.yang_parent_name = "services"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['lma_service']
                        self._child_classes = OrderedDict([("customers", ("customers", MobileIp.Lmas.Lma.Services.Service.Customers))])
                        self._leafs = OrderedDict([
                            ('lma_service', (YLeaf(YType.enumeration, 'lma-service'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'LmaService', '')])),
                            ('mnp_customer', (YLeaf(YType.uint32, 'mnp-customer'), ['int'])),
                            ('mnp_ipv4_lmn', (YLeaf(YType.uint32, 'mnp-ipv4-lmn'), ['int'])),
                            ('mnp_ipv6_lmn', (YLeaf(YType.uint32, 'mnp-ipv6-lmn'), ['int'])),
                            ('mnp_lmn', (YLeaf(YType.uint32, 'mnp-lmn'), ['int'])),
                            ('ignore_home_address', (YLeaf(YType.empty, 'ignore-home-address'), ['Empty'])),
                            ('mnp_ipv4_customer', (YLeaf(YType.uint32, 'mnp-ipv4-customer'), ['int'])),
                            ('mnp_ipv6_customer', (YLeaf(YType.uint32, 'mnp-ipv6-customer'), ['int'])),
                        ])
                        self.lma_service = None
                        self.mnp_customer = None
                        self.mnp_ipv4_lmn = None
                        self.mnp_ipv6_lmn = None
                        self.mnp_lmn = None
                        self.ignore_home_address = None
                        self.mnp_ipv4_customer = None
                        self.mnp_ipv6_customer = None

                        self.customers = MobileIp.Lmas.Lma.Services.Service.Customers()
                        self.customers.parent = self
                        self._children_name_map["customers"] = "customers"
                        self._segment_path = lambda: "service" + "[lma-service='" + str(self.lma_service) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MobileIp.Lmas.Lma.Services.Service, ['lma_service', 'mnp_customer', 'mnp_ipv4_lmn', 'mnp_ipv6_lmn', 'mnp_lmn', 'ignore_home_address', 'mnp_ipv4_customer', 'mnp_ipv6_customer'], name, value)


                    class Customers(Entity):
                        """
                        Table of Customer
                        
                        .. attribute:: customer
                        
                        	customer configuration on this mobile local loop service
                        	**type**\: list of  		 :py:class:`Customer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer>`
                        
                        

                        """

                        _prefix = 'ip-mobileip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MobileIp.Lmas.Lma.Services.Service.Customers, self).__init__()

                            self.yang_name = "customers"
                            self.yang_parent_name = "service"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("customer", ("customer", MobileIp.Lmas.Lma.Services.Service.Customers.Customer))])
                            self._leafs = OrderedDict()

                            self.customer = YList(self)
                            self._segment_path = lambda: "customers"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers, [], name, value)


                        class Customer(Entity):
                            """
                            customer configuration on this mobile local
                            loop service
                            
                            .. attribute:: customer_name  (key)
                            
                            	Customer name
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            .. attribute:: vrf_name  (key)
                            
                            	VRF name
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            .. attribute:: authenticate_option
                            
                            	Authentication option between PMIPV6 entities
                            	**type**\:  :py:class:`AuthenticateOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption>`
                            
                            .. attribute:: heart_beat_attributes
                            
                            	heartbeat config for this Customer
                            	**type**\:  :py:class:`HeartBeatAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes>`
                            
                            .. attribute:: transports
                            
                            	Table of Transport
                            	**type**\:  :py:class:`Transports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports>`
                            
                            .. attribute:: network_attributes
                            
                            	network parameters for the customer
                            	**type**\:  :py:class:`NetworkAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes>`
                            
                            .. attribute:: gre_key
                            
                            	Customer specific GRE key
                            	**type**\:  :py:class:`GreKey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey>`
                            
                            .. attribute:: binding_attributes
                            
                            	Customer specific binding attributes
                            	**type**\:  :py:class:`BindingAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes>`
                            
                            .. attribute:: mnp_customer
                            
                            	mnp limit config for customer
                            	**type**\: int
                            
                            	**range:** 1..4000000
                            
                            .. attribute:: mnp_ipv4_lmn
                            
                            	mnp limit config for customer specific logical mn
                            	**type**\: int
                            
                            	**range:** 1..32
                            
                            .. attribute:: mnp_ipv6_lmn
                            
                            	mnp limit config for customer specific logical mn
                            	**type**\: int
                            
                            	**range:** 1..32
                            
                            .. attribute:: mnp_lmn
                            
                            	mnp limit config for customer specific logical mn
                            	**type**\: int
                            
                            	**range:** 1..32
                            
                            .. attribute:: mnp_ipv4_customer
                            
                            	mnp limit config for customer
                            	**type**\: int
                            
                            	**range:** 1..4000000
                            
                            .. attribute:: mnp_ipv6_customer
                            
                            	mnp limit config for customer
                            	**type**\: int
                            
                            	**range:** 1..4000000
                            
                            .. attribute:: mobile_route_ad
                            
                            	Specify the Admin Distance value
                            	**type**\: int
                            
                            	**range:** 1..254
                            
                            .. attribute:: bandwidth_aggregate
                            
                            	Aggregate bandwidth across all logical MNs
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**units**\: kbit/s
                            
                            

                            """

                            _prefix = 'ip-mobileip-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer, self).__init__()

                                self.yang_name = "customer"
                                self.yang_parent_name = "customers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['customer_name','vrf_name']
                                self._child_classes = OrderedDict([("authenticate-option", ("authenticate_option", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption)), ("heart-beat-attributes", ("heart_beat_attributes", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes)), ("transports", ("transports", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports)), ("network-attributes", ("network_attributes", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes)), ("gre-key", ("gre_key", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey)), ("binding-attributes", ("binding_attributes", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes))])
                                self._leafs = OrderedDict([
                                    ('customer_name', (YLeaf(YType.str, 'customer-name'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ('mnp_customer', (YLeaf(YType.uint32, 'mnp-customer'), ['int'])),
                                    ('mnp_ipv4_lmn', (YLeaf(YType.uint32, 'mnp-ipv4-lmn'), ['int'])),
                                    ('mnp_ipv6_lmn', (YLeaf(YType.uint32, 'mnp-ipv6-lmn'), ['int'])),
                                    ('mnp_lmn', (YLeaf(YType.uint32, 'mnp-lmn'), ['int'])),
                                    ('mnp_ipv4_customer', (YLeaf(YType.uint32, 'mnp-ipv4-customer'), ['int'])),
                                    ('mnp_ipv6_customer', (YLeaf(YType.uint32, 'mnp-ipv6-customer'), ['int'])),
                                    ('mobile_route_ad', (YLeaf(YType.uint32, 'mobile-route-ad'), ['int'])),
                                    ('bandwidth_aggregate', (YLeaf(YType.uint32, 'bandwidth-aggregate'), ['int'])),
                                ])
                                self.customer_name = None
                                self.vrf_name = None
                                self.mnp_customer = None
                                self.mnp_ipv4_lmn = None
                                self.mnp_ipv6_lmn = None
                                self.mnp_lmn = None
                                self.mnp_ipv4_customer = None
                                self.mnp_ipv6_customer = None
                                self.mobile_route_ad = None
                                self.bandwidth_aggregate = None

                                self.authenticate_option = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption()
                                self.authenticate_option.parent = self
                                self._children_name_map["authenticate_option"] = "authenticate-option"

                                self.heart_beat_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes()
                                self.heart_beat_attributes.parent = self
                                self._children_name_map["heart_beat_attributes"] = "heart-beat-attributes"

                                self.transports = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports()
                                self.transports.parent = self
                                self._children_name_map["transports"] = "transports"

                                self.network_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes()
                                self.network_attributes.parent = self
                                self._children_name_map["network_attributes"] = "network-attributes"

                                self.gre_key = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey()
                                self.gre_key.parent = self
                                self._children_name_map["gre_key"] = "gre-key"

                                self.binding_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes()
                                self.binding_attributes.parent = self
                                self._children_name_map["binding_attributes"] = "binding-attributes"
                                self._segment_path = lambda: "customer" + "[customer-name='" + str(self.customer_name) + "']" + "[vrf-name='" + str(self.vrf_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer, ['customer_name', 'vrf_name', 'mnp_customer', 'mnp_ipv4_lmn', 'mnp_ipv6_lmn', 'mnp_lmn', 'mnp_ipv4_customer', 'mnp_ipv6_customer', 'mobile_route_ad', 'bandwidth_aggregate'], name, value)


                            class AuthenticateOption(Entity):
                                """
                                Authentication option between PMIPV6
                                entities
                                
                                .. attribute:: spi
                                
                                	SPI in hex value
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{1,8}
                                
                                .. attribute:: key
                                
                                	ASCII string
                                	**type**\: str
                                
                                	**length:** 1..125
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption, self).__init__()

                                    self.yang_name = "authenticate-option"
                                    self.yang_parent_name = "customer"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('spi', (YLeaf(YType.str, 'spi'), ['str'])),
                                        ('key', (YLeaf(YType.str, 'key'), ['str'])),
                                    ])
                                    self.spi = None
                                    self.key = None
                                    self._segment_path = lambda: "authenticate-option"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption, ['spi', 'key'], name, value)


                            class HeartBeatAttributes(Entity):
                                """
                                heartbeat config for this Customer
                                
                                .. attribute:: interval
                                
                                	Specify the interval value in second
                                	**type**\: int
                                
                                	**range:** 10..3600
                                
                                .. attribute:: retries
                                
                                	Specify the retry value
                                	**type**\: int
                                
                                	**range:** 1..10
                                
                                .. attribute:: timeout
                                
                                	Specify the timeout value
                                	**type**\: int
                                
                                	**range:** 1..3600
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes, self).__init__()

                                    self.yang_name = "heart-beat-attributes"
                                    self.yang_parent_name = "customer"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                        ('retries', (YLeaf(YType.uint32, 'retries'), ['int'])),
                                        ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                                    ])
                                    self.interval = None
                                    self.retries = None
                                    self.timeout = None
                                    self._segment_path = lambda: "heart-beat-attributes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes, ['interval', 'retries', 'timeout'], name, value)


                            class Transports(Entity):
                                """
                                Table of Transport
                                
                                .. attribute:: transport
                                
                                	Customer transport attributes
                                	**type**\: list of  		 :py:class:`Transport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports.Transport>`
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports, self).__init__()

                                    self.yang_name = "transports"
                                    self.yang_parent_name = "customer"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("transport", ("transport", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports.Transport))])
                                    self._leafs = OrderedDict()

                                    self.transport = YList(self)
                                    self._segment_path = lambda: "transports"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports, [], name, value)


                                class Transport(Entity):
                                    """
                                    Customer transport attributes
                                    
                                    .. attribute:: vrf_name  (key)
                                    
                                    	VRF Name
                                    	**type**\: str
                                    
                                    	**length:** 1..125
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	Configure IPv4 address for this LMA
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	Configure IPv6 address for this LMA
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-mobileip-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports.Transport, self).__init__()

                                        self.yang_name = "transport"
                                        self.yang_parent_name = "transports"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['vrf_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                        ])
                                        self.vrf_name = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None
                                        self._segment_path = lambda: "transport" + "[vrf-name='" + str(self.vrf_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports.Transport, ['vrf_name', 'ipv4_address', 'ipv6_address'], name, value)


                            class NetworkAttributes(Entity):
                                """
                                network parameters for the customer
                                
                                .. attribute:: authorizes
                                
                                	Table of Authorize
                                	**type**\:  :py:class:`Authorizes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes>`
                                
                                .. attribute:: unauthorize
                                
                                	not authorize the network prefixes
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes, self).__init__()

                                    self.yang_name = "network-attributes"
                                    self.yang_parent_name = "customer"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("authorizes", ("authorizes", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes))])
                                    self._leafs = OrderedDict([
                                        ('unauthorize', (YLeaf(YType.empty, 'unauthorize'), ['Empty'])),
                                    ])
                                    self.unauthorize = None

                                    self.authorizes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes()
                                    self.authorizes.parent = self
                                    self._children_name_map["authorizes"] = "authorizes"
                                    self._segment_path = lambda: "network-attributes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes, ['unauthorize'], name, value)


                                class Authorizes(Entity):
                                    """
                                    Table of Authorize
                                    
                                    .. attribute:: authorize
                                    
                                    	not authorize the network prefixes
                                    	**type**\: list of  		 :py:class:`Authorize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize>`
                                    
                                    

                                    """

                                    _prefix = 'ip-mobileip-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes, self).__init__()

                                        self.yang_name = "authorizes"
                                        self.yang_parent_name = "network-attributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("authorize", ("authorize", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize))])
                                        self._leafs = OrderedDict()

                                        self.authorize = YList(self)
                                        self._segment_path = lambda: "authorizes"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes, [], name, value)


                                    class Authorize(Entity):
                                        """
                                        not authorize the network prefixes
                                        
                                        .. attribute:: name  (key)
                                        
                                        	ASCII string
                                        	**type**\: str
                                        
                                        	**length:** 1..125
                                        
                                        .. attribute:: pool_attributes
                                        
                                        	Pool configs for this network
                                        	**type**\:  :py:class:`PoolAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes>`
                                        
                                        

                                        """

                                        _prefix = 'ip-mobileip-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize, self).__init__()

                                            self.yang_name = "authorize"
                                            self.yang_parent_name = "authorizes"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['name']
                                            self._child_classes = OrderedDict([("pool-attributes", ("pool_attributes", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes))])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ])
                                            self.name = None

                                            self.pool_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes()
                                            self.pool_attributes.parent = self
                                            self._children_name_map["pool_attributes"] = "pool-attributes"
                                            self._segment_path = lambda: "authorize" + "[name='" + str(self.name) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize, ['name'], name, value)


                                        class PoolAttributes(Entity):
                                            """
                                            Pool configs for this network
                                            
                                            .. attribute:: mobile_node
                                            
                                            	pool configs for the mobile nodes
                                            	**type**\:  :py:class:`MobileNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode>`
                                            
                                            .. attribute:: mobile_network
                                            
                                            	pool configs for the mobile network
                                            	**type**\:  :py:class:`MobileNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork>`
                                            
                                            

                                            """

                                            _prefix = 'ip-mobileip-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes, self).__init__()

                                                self.yang_name = "pool-attributes"
                                                self.yang_parent_name = "authorize"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("mobile-node", ("mobile_node", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode)), ("mobile-network", ("mobile_network", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork))])
                                                self._leafs = OrderedDict()

                                                self.mobile_node = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode()
                                                self.mobile_node.parent = self
                                                self._children_name_map["mobile_node"] = "mobile-node"

                                                self.mobile_network = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork()
                                                self.mobile_network.parent = self
                                                self._children_name_map["mobile_network"] = "mobile-network"
                                                self._segment_path = lambda: "pool-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes, [], name, value)


                                            class MobileNode(Entity):
                                                """
                                                pool configs for the mobile nodes
                                                
                                                .. attribute:: ipv4_pool
                                                
                                                	None
                                                	**type**\:  :py:class:`Ipv4Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool>`
                                                
                                                .. attribute:: ipv6_pool
                                                
                                                	None
                                                	**type**\:  :py:class:`Ipv6Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool>`
                                                
                                                

                                                """

                                                _prefix = 'ip-mobileip-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode, self).__init__()

                                                    self.yang_name = "mobile-node"
                                                    self.yang_parent_name = "pool-attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("ipv4-pool", ("ipv4_pool", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool)), ("ipv6-pool", ("ipv6_pool", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool))])
                                                    self._leafs = OrderedDict()

                                                    self.ipv4_pool = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool()
                                                    self.ipv4_pool.parent = self
                                                    self._children_name_map["ipv4_pool"] = "ipv4-pool"

                                                    self.ipv6_pool = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool()
                                                    self.ipv6_pool.parent = self
                                                    self._children_name_map["ipv6_pool"] = "ipv6-pool"
                                                    self._segment_path = lambda: "mobile-node"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode, [], name, value)


                                                class Ipv4Pool(Entity):
                                                    """
                                                    None
                                                    
                                                    .. attribute:: start_address
                                                    
                                                    	Pool IPv4 start address
                                                    	**type**\: str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: pool_prefix
                                                    
                                                    	IPv4 Pool Prefix value
                                                    	**type**\: int
                                                    
                                                    	**range:** 8..30
                                                    
                                                    

                                                    """

                                                    _prefix = 'ip-mobileip-cfg'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool, self).__init__()

                                                        self.yang_name = "ipv4-pool"
                                                        self.yang_parent_name = "mobile-node"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('start_address', (YLeaf(YType.str, 'start-address'), ['str'])),
                                                            ('pool_prefix', (YLeaf(YType.uint32, 'pool-prefix'), ['int'])),
                                                        ])
                                                        self.start_address = None
                                                        self.pool_prefix = None
                                                        self._segment_path = lambda: "ipv4-pool"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool, ['start_address', 'pool_prefix'], name, value)


                                                class Ipv6Pool(Entity):
                                                    """
                                                    None
                                                    
                                                    .. attribute:: start_address
                                                    
                                                    	Pool IPv6 start address
                                                    	**type**\: str
                                                    
                                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: pool_prefix
                                                    
                                                    	IPv6 Pool Prefix value
                                                    	**type**\: int
                                                    
                                                    	**range:** 8..62
                                                    
                                                    

                                                    """

                                                    _prefix = 'ip-mobileip-cfg'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool, self).__init__()

                                                        self.yang_name = "ipv6-pool"
                                                        self.yang_parent_name = "mobile-node"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('start_address', (YLeaf(YType.str, 'start-address'), ['str'])),
                                                            ('pool_prefix', (YLeaf(YType.uint32, 'pool-prefix'), ['int'])),
                                                        ])
                                                        self.start_address = None
                                                        self.pool_prefix = None
                                                        self._segment_path = lambda: "ipv6-pool"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool, ['start_address', 'pool_prefix'], name, value)


                                            class MobileNetwork(Entity):
                                                """
                                                pool configs for the mobile network
                                                
                                                .. attribute:: mripv6_pools
                                                
                                                	Table of MRIPV6Pool
                                                	**type**\:  :py:class:`Mripv6Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools>`
                                                
                                                .. attribute:: mripv4_pools
                                                
                                                	Table of MRIPV4Pool
                                                	**type**\:  :py:class:`Mripv4Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools>`
                                                
                                                

                                                """

                                                _prefix = 'ip-mobileip-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork, self).__init__()

                                                    self.yang_name = "mobile-network"
                                                    self.yang_parent_name = "pool-attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("mripv6-pools", ("mripv6_pools", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools)), ("mripv4-pools", ("mripv4_pools", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools))])
                                                    self._leafs = OrderedDict()

                                                    self.mripv6_pools = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools()
                                                    self.mripv6_pools.parent = self
                                                    self._children_name_map["mripv6_pools"] = "mripv6-pools"

                                                    self.mripv4_pools = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools()
                                                    self.mripv4_pools.parent = self
                                                    self._children_name_map["mripv4_pools"] = "mripv4-pools"
                                                    self._segment_path = lambda: "mobile-network"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork, [], name, value)


                                                class Mripv6Pools(Entity):
                                                    """
                                                    Table of MRIPV6Pool
                                                    
                                                    .. attribute:: mripv6_pool
                                                    
                                                    	ipv6 pool
                                                    	**type**\: list of  		 :py:class:`Mripv6Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ip-mobileip-cfg'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools, self).__init__()

                                                        self.yang_name = "mripv6-pools"
                                                        self.yang_parent_name = "mobile-network"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("mripv6-pool", ("mripv6_pool", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool))])
                                                        self._leafs = OrderedDict()

                                                        self.mripv6_pool = YList(self)
                                                        self._segment_path = lambda: "mripv6-pools"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools, [], name, value)


                                                    class Mripv6Pool(Entity):
                                                        """
                                                        ipv6 pool
                                                        
                                                        .. attribute:: start_address  (key)
                                                        
                                                        	Pool IPv6 start address
                                                        	**type**\: str
                                                        
                                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: pool_prefix
                                                        
                                                        	IPv6 Pool Prefix value
                                                        	**type**\: int
                                                        
                                                        	**range:** 8..64
                                                        
                                                        .. attribute:: network_prefix
                                                        
                                                        	IPv4 Network Prefix value
                                                        	**type**\: int
                                                        
                                                        	**range:** 8..64
                                                        
                                                        

                                                        """

                                                        _prefix = 'ip-mobileip-cfg'
                                                        _revision = '2015-11-09'

                                                        def __init__(self):
                                                            super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool, self).__init__()

                                                            self.yang_name = "mripv6-pool"
                                                            self.yang_parent_name = "mripv6-pools"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = ['start_address']
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('start_address', (YLeaf(YType.str, 'start-address'), ['str'])),
                                                                ('pool_prefix', (YLeaf(YType.uint32, 'pool-prefix'), ['int'])),
                                                                ('network_prefix', (YLeaf(YType.uint32, 'network-prefix'), ['int'])),
                                                            ])
                                                            self.start_address = None
                                                            self.pool_prefix = None
                                                            self.network_prefix = None
                                                            self._segment_path = lambda: "mripv6-pool" + "[start-address='" + str(self.start_address) + "']"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool, ['start_address', 'pool_prefix', 'network_prefix'], name, value)


                                                class Mripv4Pools(Entity):
                                                    """
                                                    Table of MRIPV4Pool
                                                    
                                                    .. attribute:: mripv4_pool
                                                    
                                                    	ipv4 pool
                                                    	**type**\: list of  		 :py:class:`Mripv4Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ip-mobileip-cfg'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools, self).__init__()

                                                        self.yang_name = "mripv4-pools"
                                                        self.yang_parent_name = "mobile-network"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("mripv4-pool", ("mripv4_pool", MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool))])
                                                        self._leafs = OrderedDict()

                                                        self.mripv4_pool = YList(self)
                                                        self._segment_path = lambda: "mripv4-pools"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools, [], name, value)


                                                    class Mripv4Pool(Entity):
                                                        """
                                                        ipv4 pool
                                                        
                                                        .. attribute:: start_address  (key)
                                                        
                                                        	Pool IPv4 start address
                                                        	**type**\: str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: pool_prefix
                                                        
                                                        	IPv4 Pool Prefix value
                                                        	**type**\: int
                                                        
                                                        	**range:** 8..30
                                                        
                                                        .. attribute:: network_prefix
                                                        
                                                        	IPv4 Network Prefix value
                                                        	**type**\: int
                                                        
                                                        	**range:** 8..32
                                                        
                                                        

                                                        """

                                                        _prefix = 'ip-mobileip-cfg'
                                                        _revision = '2015-11-09'

                                                        def __init__(self):
                                                            super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool, self).__init__()

                                                            self.yang_name = "mripv4-pool"
                                                            self.yang_parent_name = "mripv4-pools"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = ['start_address']
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('start_address', (YLeaf(YType.str, 'start-address'), ['str'])),
                                                                ('pool_prefix', (YLeaf(YType.uint32, 'pool-prefix'), ['int'])),
                                                                ('network_prefix', (YLeaf(YType.uint32, 'network-prefix'), ['int'])),
                                                            ])
                                                            self.start_address = None
                                                            self.pool_prefix = None
                                                            self.network_prefix = None
                                                            self._segment_path = lambda: "mripv4-pool" + "[start-address='" + str(self.start_address) + "']"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool, ['start_address', 'pool_prefix', 'network_prefix'], name, value)


                            class GreKey(Entity):
                                """
                                Customer specific GRE key
                                
                                .. attribute:: gre_key_type
                                
                                	GRE key type
                                	**type**\:  :py:class:`GreKeyType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.GreKeyType>`
                                
                                .. attribute:: gre_key_value
                                
                                	GRE key value
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey, self).__init__()

                                    self.yang_name = "gre-key"
                                    self.yang_parent_name = "customer"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('gre_key_type', (YLeaf(YType.enumeration, 'gre-key-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'GreKeyType', '')])),
                                        ('gre_key_value', (YLeaf(YType.uint32, 'gre-key-value'), ['int'])),
                                    ])
                                    self.gre_key_type = None
                                    self.gre_key_value = None
                                    self._segment_path = lambda: "gre-key"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey, ['gre_key_type', 'gre_key_value'], name, value)


                            class BindingAttributes(Entity):
                                """
                                Customer specific binding attributes
                                
                                .. attribute:: max_life_time
                                
                                	Maximum bce lifetime permitted
                                	**type**\: int
                                
                                	**range:** 10..65535
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes, self).__init__()

                                    self.yang_name = "binding-attributes"
                                    self.yang_parent_name = "customer"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_life_time', (YLeaf(YType.uint32, 'max-life-time'), ['int'])),
                                    ])
                                    self.max_life_time = None
                                    self._segment_path = lambda: "binding-attributes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes, ['max_life_time'], name, value)


            class Networks(Entity):
                """
                Table of Network
                
                .. attribute:: network
                
                	network for this LMA
                	**type**\: list of  		 :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Networks, self).__init__()

                    self.yang_name = "networks"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("network", ("network", MobileIp.Lmas.Lma.Networks.Network))])
                    self._leafs = OrderedDict()

                    self.network = YList(self)
                    self._segment_path = lambda: "networks"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.Networks, [], name, value)


                class Network(Entity):
                    """
                    network for this LMA
                    
                    .. attribute:: lma_network  (key)
                    
                    	Network name
                    	**type**\: str
                    
                    	**length:** 1..125
                    
                    .. attribute:: pool_attributes
                    
                    	Pool configs for this network
                    	**type**\:  :py:class:`PoolAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes>`
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.Networks.Network, self).__init__()

                        self.yang_name = "network"
                        self.yang_parent_name = "networks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['lma_network']
                        self._child_classes = OrderedDict([("pool-attributes", ("pool_attributes", MobileIp.Lmas.Lma.Networks.Network.PoolAttributes))])
                        self._leafs = OrderedDict([
                            ('lma_network', (YLeaf(YType.str, 'lma-network'), ['str'])),
                        ])
                        self.lma_network = None

                        self.pool_attributes = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes()
                        self.pool_attributes.parent = self
                        self._children_name_map["pool_attributes"] = "pool-attributes"
                        self._segment_path = lambda: "network" + "[lma-network='" + str(self.lma_network) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MobileIp.Lmas.Lma.Networks.Network, ['lma_network'], name, value)


                    class PoolAttributes(Entity):
                        """
                        Pool configs for this network
                        
                        .. attribute:: mobile_node
                        
                        	pool configs for the mobile nodes
                        	**type**\:  :py:class:`MobileNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode>`
                        
                        .. attribute:: mobile_network
                        
                        	pool configs for the mobile network
                        	**type**\:  :py:class:`MobileNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork>`
                        
                        

                        """

                        _prefix = 'ip-mobileip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes, self).__init__()

                            self.yang_name = "pool-attributes"
                            self.yang_parent_name = "network"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("mobile-node", ("mobile_node", MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode)), ("mobile-network", ("mobile_network", MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork))])
                            self._leafs = OrderedDict()

                            self.mobile_node = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode()
                            self.mobile_node.parent = self
                            self._children_name_map["mobile_node"] = "mobile-node"

                            self.mobile_network = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork()
                            self.mobile_network.parent = self
                            self._children_name_map["mobile_network"] = "mobile-network"
                            self._segment_path = lambda: "pool-attributes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes, [], name, value)


                        class MobileNode(Entity):
                            """
                            pool configs for the mobile nodes
                            
                            .. attribute:: ipv4_pool
                            
                            	None
                            	**type**\:  :py:class:`Ipv4Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool>`
                            
                            .. attribute:: ipv6_pool
                            
                            	None
                            	**type**\:  :py:class:`Ipv6Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool>`
                            
                            

                            """

                            _prefix = 'ip-mobileip-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode, self).__init__()

                                self.yang_name = "mobile-node"
                                self.yang_parent_name = "pool-attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("ipv4-pool", ("ipv4_pool", MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool)), ("ipv6-pool", ("ipv6_pool", MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool))])
                                self._leafs = OrderedDict()

                                self.ipv4_pool = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool()
                                self.ipv4_pool.parent = self
                                self._children_name_map["ipv4_pool"] = "ipv4-pool"

                                self.ipv6_pool = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool()
                                self.ipv6_pool.parent = self
                                self._children_name_map["ipv6_pool"] = "ipv6-pool"
                                self._segment_path = lambda: "mobile-node"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode, [], name, value)


                            class Ipv4Pool(Entity):
                                """
                                None
                                
                                .. attribute:: start_address
                                
                                	Pool IPv4 start address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: pool_prefix
                                
                                	IPv4 Pool Prefix value
                                	**type**\: int
                                
                                	**range:** 8..30
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool, self).__init__()

                                    self.yang_name = "ipv4-pool"
                                    self.yang_parent_name = "mobile-node"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('start_address', (YLeaf(YType.str, 'start-address'), ['str'])),
                                        ('pool_prefix', (YLeaf(YType.uint32, 'pool-prefix'), ['int'])),
                                    ])
                                    self.start_address = None
                                    self.pool_prefix = None
                                    self._segment_path = lambda: "ipv4-pool"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool, ['start_address', 'pool_prefix'], name, value)


                            class Ipv6Pool(Entity):
                                """
                                None
                                
                                .. attribute:: start_address
                                
                                	Pool IPv6 start address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: pool_prefix
                                
                                	IPv6 Pool Prefix value
                                	**type**\: int
                                
                                	**range:** 8..62
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool, self).__init__()

                                    self.yang_name = "ipv6-pool"
                                    self.yang_parent_name = "mobile-node"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('start_address', (YLeaf(YType.str, 'start-address'), ['str'])),
                                        ('pool_prefix', (YLeaf(YType.uint32, 'pool-prefix'), ['int'])),
                                    ])
                                    self.start_address = None
                                    self.pool_prefix = None
                                    self._segment_path = lambda: "ipv6-pool"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool, ['start_address', 'pool_prefix'], name, value)


                        class MobileNetwork(Entity):
                            """
                            pool configs for the mobile network
                            
                            .. attribute:: mripv6_pools
                            
                            	Table of MRIPV6Pool
                            	**type**\:  :py:class:`Mripv6Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools>`
                            
                            .. attribute:: mripv4_pools
                            
                            	Table of MRIPV4Pool
                            	**type**\:  :py:class:`Mripv4Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools>`
                            
                            

                            """

                            _prefix = 'ip-mobileip-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork, self).__init__()

                                self.yang_name = "mobile-network"
                                self.yang_parent_name = "pool-attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("mripv6-pools", ("mripv6_pools", MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools)), ("mripv4-pools", ("mripv4_pools", MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools))])
                                self._leafs = OrderedDict()

                                self.mripv6_pools = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools()
                                self.mripv6_pools.parent = self
                                self._children_name_map["mripv6_pools"] = "mripv6-pools"

                                self.mripv4_pools = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools()
                                self.mripv4_pools.parent = self
                                self._children_name_map["mripv4_pools"] = "mripv4-pools"
                                self._segment_path = lambda: "mobile-network"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork, [], name, value)


                            class Mripv6Pools(Entity):
                                """
                                Table of MRIPV6Pool
                                
                                .. attribute:: mripv6_pool
                                
                                	ipv6 pool
                                	**type**\: list of  		 :py:class:`Mripv6Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool>`
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools, self).__init__()

                                    self.yang_name = "mripv6-pools"
                                    self.yang_parent_name = "mobile-network"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("mripv6-pool", ("mripv6_pool", MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool))])
                                    self._leafs = OrderedDict()

                                    self.mripv6_pool = YList(self)
                                    self._segment_path = lambda: "mripv6-pools"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools, [], name, value)


                                class Mripv6Pool(Entity):
                                    """
                                    ipv6 pool
                                    
                                    .. attribute:: start_address  (key)
                                    
                                    	Pool IPv6 start address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: pool_prefix
                                    
                                    	IPv6 Pool Prefix value
                                    	**type**\: int
                                    
                                    	**range:** 8..64
                                    
                                    .. attribute:: network_prefix
                                    
                                    	IPv4 Network Prefix value
                                    	**type**\: int
                                    
                                    	**range:** 8..64
                                    
                                    

                                    """

                                    _prefix = 'ip-mobileip-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool, self).__init__()

                                        self.yang_name = "mripv6-pool"
                                        self.yang_parent_name = "mripv6-pools"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['start_address']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('start_address', (YLeaf(YType.str, 'start-address'), ['str'])),
                                            ('pool_prefix', (YLeaf(YType.uint32, 'pool-prefix'), ['int'])),
                                            ('network_prefix', (YLeaf(YType.uint32, 'network-prefix'), ['int'])),
                                        ])
                                        self.start_address = None
                                        self.pool_prefix = None
                                        self.network_prefix = None
                                        self._segment_path = lambda: "mripv6-pool" + "[start-address='" + str(self.start_address) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool, ['start_address', 'pool_prefix', 'network_prefix'], name, value)


                            class Mripv4Pools(Entity):
                                """
                                Table of MRIPV4Pool
                                
                                .. attribute:: mripv4_pool
                                
                                	ipv4 pool
                                	**type**\: list of  		 :py:class:`Mripv4Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool>`
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools, self).__init__()

                                    self.yang_name = "mripv4-pools"
                                    self.yang_parent_name = "mobile-network"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("mripv4-pool", ("mripv4_pool", MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool))])
                                    self._leafs = OrderedDict()

                                    self.mripv4_pool = YList(self)
                                    self._segment_path = lambda: "mripv4-pools"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools, [], name, value)


                                class Mripv4Pool(Entity):
                                    """
                                    ipv4 pool
                                    
                                    .. attribute:: start_address  (key)
                                    
                                    	Pool IPv4 start address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: pool_prefix
                                    
                                    	IPv4 Pool Prefix value
                                    	**type**\: int
                                    
                                    	**range:** 8..30
                                    
                                    .. attribute:: network_prefix
                                    
                                    	IPv4 Network Prefix value
                                    	**type**\: int
                                    
                                    	**range:** 8..32
                                    
                                    

                                    """

                                    _prefix = 'ip-mobileip-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool, self).__init__()

                                        self.yang_name = "mripv4-pool"
                                        self.yang_parent_name = "mripv4-pools"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['start_address']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('start_address', (YLeaf(YType.str, 'start-address'), ['str'])),
                                            ('pool_prefix', (YLeaf(YType.uint32, 'pool-prefix'), ['int'])),
                                            ('network_prefix', (YLeaf(YType.uint32, 'network-prefix'), ['int'])),
                                        ])
                                        self.start_address = None
                                        self.pool_prefix = None
                                        self.network_prefix = None
                                        self._segment_path = lambda: "mripv4-pool" + "[start-address='" + str(self.start_address) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool, ['start_address', 'pool_prefix', 'network_prefix'], name, value)


            class ReplayProtection(Entity):
                """
                Replay Protection Method
                
                .. attribute:: timestamp_window
                
                	Specify timestamp window value in seconds
                	**type**\: int
                
                	**range:** 1..255
                
                	**units**\: second
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.ReplayProtection, self).__init__()

                    self.yang_name = "replay-protection"
                    self.yang_parent_name = "lma"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('timestamp_window', (YLeaf(YType.uint32, 'timestamp-window'), ['int'])),
                    ])
                    self.timestamp_window = None
                    self._segment_path = lambda: "replay-protection"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MobileIp.Lmas.Lma.ReplayProtection, ['timestamp_window'], name, value)

    def clone_ptr(self):
        self._top_entity = MobileIp()
        return self._top_entity


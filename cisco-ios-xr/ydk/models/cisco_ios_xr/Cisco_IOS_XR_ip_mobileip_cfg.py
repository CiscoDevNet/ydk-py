""" Cisco_IOS_XR_ip_mobileip_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-mobileip package configuration.

This module contains definitions
for the following management objects\:
  mobile\-ip\: MobileIP configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EncapOptEnum(Enum):
    """
    EncapOptEnum

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

    greipv4 = 4

    greipv6 = 5

    mgreipv4 = 7

    mgreipv6 = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
        return meta._meta_table['EncapOptEnum']


class LmaRatEnum(Enum):
    """
    LmaRatEnum

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

    virtual = 0

    ppp = 1

    ethernet = 2

    wlan = 3

    wi_max = 4

    Y_3gppgeran = 5

    Y_3gpputran = 6

    Y_3gppeutran = 7

    Y_3gpp2ehrpd = 8

    Y_3gpp2hrpd = 9

    Y_3gpp21rtt = 10

    Y_3gpp2umb = 11


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
        return meta._meta_table['LmaRatEnum']


class LmaRoleEnum(Enum):
    """
    LmaRoleEnum

    Lma role

    .. data:: Y_3gma = 0

    	3GMA mode

    """

    Y_3gma = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
        return meta._meta_table['LmaRoleEnum']


class LmaServiceEnum(Enum):
    """
    LmaServiceEnum

    Lma service

    .. data:: service_mll = 1

    	Wireless Private Routing service

    """

    service_mll = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
        return meta._meta_table['LmaServiceEnum']


class ServiceTypeEnum(Enum):
    """
    ServiceTypeEnum

    Service type

    .. data:: ipv4 = 1

    	ipv4 service type

    .. data:: ipv6 = 2

    	ipv6 service type

    .. data:: dual = 3

    	dual service type

    """

    ipv4 = 1

    ipv6 = 2

    dual = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
        return meta._meta_table['ServiceTypeEnum']



class MobileIp(object):
    """
    MobileIP configuration
    
    .. attribute:: domains
    
    	Table of Domain
    	**type**\:   :py:class:`Domains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains>`
    
    .. attribute:: lmas
    
    	Table of LMA
    	**type**\:   :py:class:`Lmas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas>`
    
    

    """

    _prefix = 'ip-mobileip-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.domains = MobileIp.Domains()
        self.domains.parent = self
        self.lmas = MobileIp.Lmas()
        self.lmas.parent = self


    class Domains(object):
        """
        Table of Domain
        
        .. attribute:: domain
        
        	PMIPv6 domain configuration
        	**type**\: list of    :py:class:`Domain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain>`
        
        

        """

        _prefix = 'ip-mobileip-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.domain = YList()
            self.domain.parent = self
            self.domain.name = 'domain'


        class Domain(object):
            """
            PMIPv6 domain configuration
            
            .. attribute:: domain_name  <key>
            
            	Domain Name
            	**type**\:  str
            
            	**length:** 1..125
            
            .. attribute:: authenticate_option
            
            	Authentication option between PMIPV6 entities
            	**type**\:   :py:class:`AuthenticateOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.AuthenticateOption>`
            
            .. attribute:: enable
            
            	Enable PMIPv6 domain configuration. Deletion of this object also causes deletion of all associated objects under Domain
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: lmas
            
            	Table of LMA
            	**type**\:   :py:class:`Lmas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Lmas>`
            
            .. attribute:: mags
            
            	Table of MAG
            	**type**\:   :py:class:`Mags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Mags>`
            
            .. attribute:: nais
            
            	Table of NAI
            	**type**\:   :py:class:`Nais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Nais>`
            
            

            """

            _prefix = 'ip-mobileip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.domain_name = None
                self.authenticate_option = MobileIp.Domains.Domain.AuthenticateOption()
                self.authenticate_option.parent = self
                self.enable = None
                self.lmas = MobileIp.Domains.Domain.Lmas()
                self.lmas.parent = self
                self.mags = MobileIp.Domains.Domain.Mags()
                self.mags.parent = self
                self.nais = MobileIp.Domains.Domain.Nais()
                self.nais.parent = self


            class Mags(object):
                """
                Table of MAG
                
                .. attribute:: mag
                
                	MAG within domain
                	**type**\: list of    :py:class:`Mag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Mags.Mag>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.mag = YList()
                    self.mag.parent = self
                    self.mag.name = 'mag'


                class Mag(object):
                    """
                    MAG within domain
                    
                    .. attribute:: mag_name  <key>
                    
                    	MAG Identifier
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mag_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.mag_name is None:
                            raise YPYModelError('Key property mag_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mag[Cisco-IOS-XR-ip-mobileip-cfg:mag-name = ' + str(self.mag_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.mag_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                        return meta._meta_table['MobileIp.Domains.Domain.Mags.Mag']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mags'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.mag is not None:
                        for child_ref in self.mag:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Domains.Domain.Mags']['meta_info']


            class Nais(object):
                """
                Table of NAI
                
                .. attribute:: nai
                
                	Network access identifier or Realm
                	**type**\: list of    :py:class:`Nai <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Nais.Nai>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.nai = YList()
                    self.nai.parent = self
                    self.nai.name = 'nai'


                class Nai(object):
                    """
                    Network access identifier or Realm
                    
                    .. attribute:: nai_name  <key>
                    
                    	MN Identifier
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: apn
                    
                    	Access point network for this MN
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: customer
                    
                    	Customer name for this MN
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: lma
                    
                    	LMA for this MN
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: network
                    
                    	Network name (Address pool) for this MN
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: service
                    
                    	Service type for this MN
                    	**type**\:   :py:class:`ServiceTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.ServiceTypeEnum>`
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.nai_name = None
                        self.apn = None
                        self.customer = None
                        self.lma = None
                        self.network = None
                        self.service = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.nai_name is None:
                            raise YPYModelError('Key property nai_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:nai[Cisco-IOS-XR-ip-mobileip-cfg:nai-name = ' + str(self.nai_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.nai_name is not None:
                            return True

                        if self.apn is not None:
                            return True

                        if self.customer is not None:
                            return True

                        if self.lma is not None:
                            return True

                        if self.network is not None:
                            return True

                        if self.service is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                        return meta._meta_table['MobileIp.Domains.Domain.Nais.Nai']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:nais'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.nai is not None:
                        for child_ref in self.nai:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Domains.Domain.Nais']['meta_info']


            class AuthenticateOption(object):
                """
                Authentication option between PMIPV6 entities
                
                .. attribute:: key
                
                	ASCII string
                	**type**\:  str
                
                	**length:** 1..125
                
                .. attribute:: spi
                
                	SPI in hex value
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.key = None
                    self.spi = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:authenticate-option'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.key is not None:
                        return True

                    if self.spi is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Domains.Domain.AuthenticateOption']['meta_info']


            class Lmas(object):
                """
                Table of LMA
                
                .. attribute:: lma
                
                	LMA within domain
                	**type**\: list of    :py:class:`Lma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Lmas.Lma>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lma = YList()
                    self.lma.parent = self
                    self.lma.name = 'lma'


                class Lma(object):
                    """
                    LMA within domain
                    
                    .. attribute:: lma_name  <key>
                    
                    	LMA Identifier
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.lma_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.lma_name is None:
                            raise YPYModelError('Key property lma_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:lma[Cisco-IOS-XR-ip-mobileip-cfg:lma-name = ' + str(self.lma_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.lma_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                        return meta._meta_table['MobileIp.Domains.Domain.Lmas.Lma']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:lmas'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lma is not None:
                        for child_ref in self.lma:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Domains.Domain.Lmas']['meta_info']

            @property
            def _common_path(self):
                if self.domain_name is None:
                    raise YPYModelError('Key property domain_name is None')

                return '/Cisco-IOS-XR-ip-mobileip-cfg:mobile-ip/Cisco-IOS-XR-ip-mobileip-cfg:domains/Cisco-IOS-XR-ip-mobileip-cfg:domain[Cisco-IOS-XR-ip-mobileip-cfg:domain-name = ' + str(self.domain_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.domain_name is not None:
                    return True

                if self.authenticate_option is not None and self.authenticate_option._has_data():
                    return True

                if self.enable is not None:
                    return True

                if self.lmas is not None and self.lmas._has_data():
                    return True

                if self.mags is not None and self.mags._has_data():
                    return True

                if self.nais is not None and self.nais._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                return meta._meta_table['MobileIp.Domains.Domain']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-mobileip-cfg:mobile-ip/Cisco-IOS-XR-ip-mobileip-cfg:domains'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.domain is not None:
                for child_ref in self.domain:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
            return meta._meta_table['MobileIp.Domains']['meta_info']


    class Lmas(object):
        """
        Table of LMA
        
        .. attribute:: lma
        
        	PMIPv6 LMA configuration
        	**type**\: list of    :py:class:`Lma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma>`
        
        

        """

        _prefix = 'ip-mobileip-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.lma = YList()
            self.lma.parent = self
            self.lma.name = 'lma'


        class Lma(object):
            """
            PMIPv6 LMA configuration
            
            .. attribute:: lma_name  <key>
            
            	LMA name
            	**type**\:  str
            
            	**length:** 1..125
            
            .. attribute:: domain_name  <key>
            
            	Domain name
            	**type**\:  str
            
            	**length:** 1..125
            
            .. attribute:: aaa
            
            	aaa config attributes for this LMA
            	**type**\:   :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Aaa>`
            
            .. attribute:: ani
            
            	enable ani option processing in LMA
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: binding_attributes
            
            	LMA binding attributes
            	**type**\:   :py:class:`BindingAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.BindingAttributes>`
            
            .. attribute:: binding_revocation_attributes
            
            	LMA Binding Revocation Attributes
            	**type**\:   :py:class:`BindingRevocationAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.BindingRevocationAttributes>`
            
            .. attribute:: default_profile
            
            	Default MN profile for LMA
            	**type**\:  str
            
            	**length:** 1..125
            
            .. attribute:: dscp
            
            	DSCP for packets originating from this LMA
            	**type**\:   :py:class:`Dscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Dscp>`
            
            .. attribute:: dynamic
            
            	enable dynamic mag learning for LMA
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enforce
            
            	enforce heartbeat values to MAG
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: generate
            
            	generate gre key for LMA bindings
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: heart_beat_attributes
            
            	heartbeat config for this LMA
            	**type**\:   :py:class:`HeartBeatAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.HeartBeatAttributes>`
            
            .. attribute:: hnp
            
            	LMA HNP options
            	**type**\:   :py:class:`Hnp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Hnp>`
            
            .. attribute:: interface
            
            	CN facing interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: lmaipv4_addresses
            
            	Table of LMAIPv4Address
            	**type**\:   :py:class:`Lmaipv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Lmaipv4Addresses>`
            
            .. attribute:: lmaipv6_addresses
            
            	Table of LMAIPv6Address
            	**type**\:   :py:class:`Lmaipv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Lmaipv6Addresses>`
            
            .. attribute:: mags
            
            	Table of MAG
            	**type**\:   :py:class:`Mags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Mags>`
            
            .. attribute:: mobile_map
            
            	Mobile Map for this LMA
            	**type**\:  str
            
            	**length:** 1..125
            
            .. attribute:: mobile_route_ad
            
            	Specify the Admin Distance value
            	**type**\:  int
            
            	**range:** 1..254
            
            .. attribute:: multipath
            
            	enable multipath support for LMA
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: networks
            
            	Table of Network
            	**type**\:   :py:class:`Networks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks>`
            
            .. attribute:: pgw_subs_cont
            
            	Feature related to interface with PGW
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: rat_attributes
            
            	Radio access technology type config  this LMA
            	**type**\:   :py:class:`RatAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.RatAttributes>`
            
            .. attribute:: redistribute
            
            	Redistribute routes
            	**type**\:   :py:class:`Redistribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Redistribute>`
            
            .. attribute:: replay_protection
            
            	Replay Protection Method
            	**type**\:   :py:class:`ReplayProtection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.ReplayProtection>`
            
            .. attribute:: roles
            
            	Table of Role
            	**type**\:   :py:class:`Roles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Roles>`
            
            .. attribute:: services
            
            	Table of Service
            	**type**\:   :py:class:`Services <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services>`
            
            .. attribute:: tunnel_attributes
            
            	tunnel attributes
            	**type**\:   :py:class:`TunnelAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.TunnelAttributes>`
            
            

            """

            _prefix = 'ip-mobileip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.lma_name = None
                self.domain_name = None
                self.aaa = MobileIp.Lmas.Lma.Aaa()
                self.aaa.parent = self
                self.ani = None
                self.binding_attributes = MobileIp.Lmas.Lma.BindingAttributes()
                self.binding_attributes.parent = self
                self.binding_revocation_attributes = MobileIp.Lmas.Lma.BindingRevocationAttributes()
                self.binding_revocation_attributes.parent = self
                self.default_profile = None
                self.dscp = MobileIp.Lmas.Lma.Dscp()
                self.dscp.parent = self
                self.dynamic = None
                self.enforce = None
                self.generate = None
                self.heart_beat_attributes = MobileIp.Lmas.Lma.HeartBeatAttributes()
                self.heart_beat_attributes.parent = self
                self.hnp = MobileIp.Lmas.Lma.Hnp()
                self.hnp.parent = self
                self.interface = None
                self.lmaipv4_addresses = MobileIp.Lmas.Lma.Lmaipv4Addresses()
                self.lmaipv4_addresses.parent = self
                self.lmaipv6_addresses = MobileIp.Lmas.Lma.Lmaipv6Addresses()
                self.lmaipv6_addresses.parent = self
                self.mags = MobileIp.Lmas.Lma.Mags()
                self.mags.parent = self
                self.mobile_map = None
                self.mobile_route_ad = None
                self.multipath = None
                self.networks = MobileIp.Lmas.Lma.Networks()
                self.networks.parent = self
                self.pgw_subs_cont = None
                self.rat_attributes = MobileIp.Lmas.Lma.RatAttributes()
                self.rat_attributes.parent = self
                self.redistribute = MobileIp.Lmas.Lma.Redistribute()
                self.redistribute.parent = self
                self.replay_protection = MobileIp.Lmas.Lma.ReplayProtection()
                self.replay_protection.parent = self
                self.roles = MobileIp.Lmas.Lma.Roles()
                self.roles.parent = self
                self.services = MobileIp.Lmas.Lma.Services()
                self.services.parent = self
                self.tunnel_attributes = MobileIp.Lmas.Lma.TunnelAttributes()
                self.tunnel_attributes.parent = self


            class BindingRevocationAttributes(object):
                """
                LMA Binding Revocation Attributes
                
                .. attribute:: delay
                
                	Time to wait before Retransmitting BRI Message
                	**type**\:   :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay>`
                
                .. attribute:: retry
                
                	Number of Retransmissons Allowed for BRI Message
                	**type**\:  int
                
                	**range:** 1..10
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.delay = MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay()
                    self.delay.parent = self
                    self.retry = None


                class Delay(object):
                    """
                    Time to wait before Retransmitting BRI
                    Message
                    
                    .. attribute:: maximum
                    
                    	Maximum time delay to send BRI
                    	**type**\:  int
                    
                    	**range:** 500..65535
                    
                    .. attribute:: minimum
                    
                    	Minimum time delay to send BRI
                    	**type**\:  int
                    
                    	**range:** 500..65535
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.maximum = None
                        self.minimum = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:delay'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.maximum is not None:
                            return True

                        if self.minimum is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                        return meta._meta_table['MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:binding-revocation-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.delay is not None and self.delay._has_data():
                        return True

                    if self.retry is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.BindingRevocationAttributes']['meta_info']


            class RatAttributes(object):
                """
                Radio access technology type config  this LMA
                
                .. attribute:: lma_rat
                
                	LMA rat type
                	**type**\:   :py:class:`LmaRatEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.LmaRatEnum>`
                
                .. attribute:: priority_value
                
                	Specify the priority value
                	**type**\:  int
                
                	**range:** 1..255
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lma_rat = None
                    self.priority_value = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:rat-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lma_rat is not None:
                        return True

                    if self.priority_value is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.RatAttributes']['meta_info']


            class HeartBeatAttributes(object):
                """
                heartbeat config for this LMA
                
                .. attribute:: interval
                
                	Specify the interval value in second
                	**type**\:  int
                
                	**range:** 10..3600
                
                .. attribute:: retries
                
                	Specify the retry value
                	**type**\:  int
                
                	**range:** 1..10
                
                .. attribute:: timeout
                
                	Specify the timeout value
                	**type**\:  int
                
                	**range:** 1..3600
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interval = None
                    self.retries = None
                    self.timeout = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:heart-beat-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interval is not None:
                        return True

                    if self.retries is not None:
                        return True

                    if self.timeout is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.HeartBeatAttributes']['meta_info']


            class Lmaipv6Addresses(object):
                """
                Table of LMAIPv6Address
                
                .. attribute:: lmaipv6_address
                
                	Configure IPv6 address for this LMA
                	**type**\: list of    :py:class:`Lmaipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Lmaipv6Addresses.Lmaipv6Address>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lmaipv6_address = YList()
                    self.lmaipv6_address.parent = self
                    self.lmaipv6_address.name = 'lmaipv6_address'


                class Lmaipv6Address(object):
                    """
                    Configure IPv6 address for this LMA
                    
                    .. attribute:: address  <key>
                    
                    	LMA IPv6 address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:lmaipv6-address[Cisco-IOS-XR-ip-mobileip-cfg:address = ' + str(self.address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                        return meta._meta_table['MobileIp.Lmas.Lma.Lmaipv6Addresses.Lmaipv6Address']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:lmaipv6-addresses'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lmaipv6_address is not None:
                        for child_ref in self.lmaipv6_address:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.Lmaipv6Addresses']['meta_info']


            class Hnp(object):
                """
                LMA HNP options
                
                .. attribute:: maximum
                
                	maximum HNPs allowed per MN interface
                	**type**\:  int
                
                	**range:** 1..3
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.maximum = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:hnp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.maximum is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.Hnp']['meta_info']


            class Redistribute(object):
                """
                Redistribute routes
                
                .. attribute:: redist_sub_type
                
                	Set constant integer
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: redist_type
                
                	Set constant integer
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.redist_sub_type = None
                    self.redist_type = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:redistribute'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.redist_sub_type is not None:
                        return True

                    if self.redist_type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.Redistribute']['meta_info']


            class Dscp(object):
                """
                DSCP for packets originating from this LMA
                
                .. attribute:: force
                
                	Set constant integer
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: value
                
                	Specify the DSCP value
                	**type**\:  int
                
                	**range:** 1..63
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.force = None
                    self.value = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:dscp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.force is not None:
                        return True

                    if self.value is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.Dscp']['meta_info']


            class Lmaipv4Addresses(object):
                """
                Table of LMAIPv4Address
                
                .. attribute:: lmaipv4_address
                
                	Configure IPv4 address for this LMA
                	**type**\: list of    :py:class:`Lmaipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Lmaipv4Addresses.Lmaipv4Address>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lmaipv4_address = YList()
                    self.lmaipv4_address.parent = self
                    self.lmaipv4_address.name = 'lmaipv4_address'


                class Lmaipv4Address(object):
                    """
                    Configure IPv4 address for this LMA
                    
                    .. attribute:: address  <key>
                    
                    	LMA IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:lmaipv4-address[Cisco-IOS-XR-ip-mobileip-cfg:address = ' + str(self.address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                        return meta._meta_table['MobileIp.Lmas.Lma.Lmaipv4Addresses.Lmaipv4Address']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:lmaipv4-addresses'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lmaipv4_address is not None:
                        for child_ref in self.lmaipv4_address:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.Lmaipv4Addresses']['meta_info']


            class Roles(object):
                """
                Table of Role
                
                .. attribute:: role
                
                	Role of this LMA
                	**type**\: list of    :py:class:`Role <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Roles.Role>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.role = YList()
                    self.role.parent = self
                    self.role.name = 'role'


                class Role(object):
                    """
                    Role of this LMA
                    
                    .. attribute:: lma_role  <key>
                    
                    	LMA role mode
                    	**type**\:   :py:class:`LmaRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.LmaRoleEnum>`
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.lma_role = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.lma_role is None:
                            raise YPYModelError('Key property lma_role is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:role[Cisco-IOS-XR-ip-mobileip-cfg:lma-role = ' + str(self.lma_role) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.lma_role is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                        return meta._meta_table['MobileIp.Lmas.Lma.Roles.Role']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:roles'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.role is not None:
                        for child_ref in self.role:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.Roles']['meta_info']


            class BindingAttributes(object):
                """
                LMA binding attributes
                
                .. attribute:: create_wait_interval
                
                	bce create wait time interval
                	**type**\:  int
                
                	**range:** 100..65535
                
                .. attribute:: delete_wait_interval
                
                	bce delete wait time interval
                	**type**\:  int
                
                	**range:** 100..65535
                
                .. attribute:: max_life_time
                
                	Maximum bce lifetime permitted
                	**type**\:  int
                
                	**range:** 10..65535
                
                	**units**\: second
                
                .. attribute:: maximum
                
                	Specify max. number of bindings
                	**type**\:  int
                
                	**range:** 1..128000
                
                .. attribute:: refresh_time
                
                	Specify in seconds, (multiples of 4)
                	**type**\:  int
                
                	**range:** 4..65000
                
                	**units**\: second
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.create_wait_interval = None
                    self.delete_wait_interval = None
                    self.max_life_time = None
                    self.maximum = None
                    self.refresh_time = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:binding-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.create_wait_interval is not None:
                        return True

                    if self.delete_wait_interval is not None:
                        return True

                    if self.max_life_time is not None:
                        return True

                    if self.maximum is not None:
                        return True

                    if self.refresh_time is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.BindingAttributes']['meta_info']


            class Aaa(object):
                """
                aaa config attributes for this LMA
                
                .. attribute:: enable
                
                	Set constant integer
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: interim_interval
                
                	Set constant integer
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.enable = None
                    self.interim_interval = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:aaa'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.enable is not None:
                        return True

                    if self.interim_interval is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.Aaa']['meta_info']


            class Mags(object):
                """
                Table of MAG
                
                .. attribute:: mag
                
                	MAG within LMA
                	**type**\: list of    :py:class:`Mag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Mags.Mag>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.mag = YList()
                    self.mag.parent = self
                    self.mag.name = 'mag'


                class Mag(object):
                    """
                    MAG within LMA
                    
                    .. attribute:: mag_name  <key>
                    
                    	MAG identifier
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: domain_name  <key>
                    
                    	Domain name
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: authenticate_option
                    
                    	Authentication option between PMIPV6 entities
                    	**type**\:   :py:class:`AuthenticateOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption>`
                    
                    .. attribute:: dscp
                    
                    	DSCP for packets originating from this MAG
                    	**type**\:   :py:class:`Dscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Mags.Mag.Dscp>`
                    
                    .. attribute:: encap_option
                    
                    	Encapsulation option between PMIPV6 entities
                    	**type**\:   :py:class:`EncapOptEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.EncapOptEnum>`
                    
                    .. attribute:: ipv4_address
                    
                    	Configure IPv4 address for this MAG
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_address
                    
                    	Configure IPv6 address for this MAG
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: tunnel
                    
                    	static tunnel for this peer MAG
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mag_name = None
                        self.domain_name = None
                        self.authenticate_option = MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption()
                        self.authenticate_option.parent = self
                        self.dscp = MobileIp.Lmas.Lma.Mags.Mag.Dscp()
                        self.dscp.parent = self
                        self.encap_option = None
                        self.ipv4_address = None
                        self.ipv6_address = None
                        self.tunnel = None


                    class AuthenticateOption(object):
                        """
                        Authentication option between PMIPV6
                        entities
                        
                        .. attribute:: key
                        
                        	ASCII string
                        	**type**\:  str
                        
                        	**length:** 1..125
                        
                        .. attribute:: spi
                        
                        	SPI in hex value
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        

                        """

                        _prefix = 'ip-mobileip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.key = None
                            self.spi = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:authenticate-option'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.key is not None:
                                return True

                            if self.spi is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                            return meta._meta_table['MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption']['meta_info']


                    class Dscp(object):
                        """
                        DSCP for packets originating from this MAG
                        
                        .. attribute:: force
                        
                        	Set constant integer
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: value
                        
                        	Specify the DSCP value
                        	**type**\:  int
                        
                        	**range:** 1..63
                        
                        

                        """

                        _prefix = 'ip-mobileip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.force = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:dscp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.force is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                            return meta._meta_table['MobileIp.Lmas.Lma.Mags.Mag.Dscp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.mag_name is None:
                            raise YPYModelError('Key property mag_name is None')
                        if self.domain_name is None:
                            raise YPYModelError('Key property domain_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mag[Cisco-IOS-XR-ip-mobileip-cfg:mag-name = ' + str(self.mag_name) + '][Cisco-IOS-XR-ip-mobileip-cfg:domain-name = ' + str(self.domain_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.mag_name is not None:
                            return True

                        if self.domain_name is not None:
                            return True

                        if self.authenticate_option is not None and self.authenticate_option._has_data():
                            return True

                        if self.dscp is not None and self.dscp._has_data():
                            return True

                        if self.encap_option is not None:
                            return True

                        if self.ipv4_address is not None:
                            return True

                        if self.ipv6_address is not None:
                            return True

                        if self.tunnel is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                        return meta._meta_table['MobileIp.Lmas.Lma.Mags.Mag']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mags'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.mag is not None:
                        for child_ref in self.mag:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.Mags']['meta_info']


            class TunnelAttributes(object):
                """
                tunnel attributes
                
                .. attribute:: acl
                
                	access list to apply for tunnel
                	**type**\:  str
                
                	**length:** 1..125
                
                .. attribute:: mtu
                
                	maximum transmission unit for tunnel
                	**type**\:  int
                
                	**range:** 68..17916
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.acl = None
                    self.mtu = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:tunnel-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.acl is not None:
                        return True

                    if self.mtu is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.TunnelAttributes']['meta_info']


            class Services(object):
                """
                Table of Service
                
                .. attribute:: service
                
                	Service of this LMA
                	**type**\: list of    :py:class:`Service <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.service = YList()
                    self.service.parent = self
                    self.service.name = 'service'


                class Service(object):
                    """
                    Service of this LMA
                    
                    .. attribute:: lma_service  <key>
                    
                    	LMA service mode
                    	**type**\:   :py:class:`LmaServiceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.LmaServiceEnum>`
                    
                    .. attribute:: customers
                    
                    	Table of Customer
                    	**type**\:   :py:class:`Customers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers>`
                    
                    .. attribute:: ignore
                    
                    	ignore options for mobile local loop service
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: mnp_customer
                    
                    	mnp limit config for all customer's
                    	**type**\:  int
                    
                    	**range:** 1..4000000
                    
                    .. attribute:: mnp_ipv4_customer
                    
                    	mnp limit config for all customer's
                    	**type**\:  int
                    
                    	**range:** 1..4000000
                    
                    .. attribute:: mnp_ipv4_lmn
                    
                    	mnp limit config for all logical mn's
                    	**type**\:  int
                    
                    	**range:** 1..32
                    
                    .. attribute:: mnp_ipv6_customer
                    
                    	mnp limit config for all customer's
                    	**type**\:  int
                    
                    	**range:** 1..4000000
                    
                    .. attribute:: mnp_ipv6_lmn
                    
                    	mnp limit config for all logical mn's
                    	**type**\:  int
                    
                    	**range:** 1..32
                    
                    .. attribute:: mnp_lmn
                    
                    	mnp limit config for all logical mn's
                    	**type**\:  int
                    
                    	**range:** 1..32
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.lma_service = None
                        self.customers = MobileIp.Lmas.Lma.Services.Service.Customers()
                        self.customers.parent = self
                        self.ignore = None
                        self.mnp_customer = None
                        self.mnp_ipv4_customer = None
                        self.mnp_ipv4_lmn = None
                        self.mnp_ipv6_customer = None
                        self.mnp_ipv6_lmn = None
                        self.mnp_lmn = None


                    class Customers(object):
                        """
                        Table of Customer
                        
                        .. attribute:: customer
                        
                        	customer configuration on this mobile local loop service
                        	**type**\: list of    :py:class:`Customer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer>`
                        
                        

                        """

                        _prefix = 'ip-mobileip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.customer = YList()
                            self.customer.parent = self
                            self.customer.name = 'customer'


                        class Customer(object):
                            """
                            customer configuration on this mobile local
                            loop service
                            
                            .. attribute:: customer_name  <key>
                            
                            	Customer name
                            	**type**\:  str
                            
                            	**length:** 1..125
                            
                            .. attribute:: vrf_name  <key>
                            
                            	VRF name
                            	**type**\:  str
                            
                            	**length:** 1..125
                            
                            .. attribute:: authenticate_option
                            
                            	Authentication option between PMIPV6 entities
                            	**type**\:   :py:class:`AuthenticateOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption>`
                            
                            .. attribute:: bandwidth_aggregate
                            
                            	Aggregate bandwidth across all logical MNs
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: binding_attributes
                            
                            	Customer specific binding attributes
                            	**type**\:   :py:class:`BindingAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes>`
                            
                            .. attribute:: gre_key
                            
                            	Customer specific GRE key
                            	**type**\:   :py:class:`GreKey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey>`
                            
                            .. attribute:: heart_beat_attributes
                            
                            	heartbeat config for this Customer
                            	**type**\:   :py:class:`HeartBeatAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes>`
                            
                            .. attribute:: mnp_customer
                            
                            	mnp limit config for customer
                            	**type**\:  int
                            
                            	**range:** 1..4000000
                            
                            .. attribute:: mnp_ipv4_customer
                            
                            	mnp limit config for customer
                            	**type**\:  int
                            
                            	**range:** 1..4000000
                            
                            .. attribute:: mnp_ipv4_lmn
                            
                            	mnp limit config for customer specific logical mn
                            	**type**\:  int
                            
                            	**range:** 1..32
                            
                            .. attribute:: mnp_ipv6_customer
                            
                            	mnp limit config for customer
                            	**type**\:  int
                            
                            	**range:** 1..4000000
                            
                            .. attribute:: mnp_ipv6_lmn
                            
                            	mnp limit config for customer specific logical mn
                            	**type**\:  int
                            
                            	**range:** 1..32
                            
                            .. attribute:: mnp_lmn
                            
                            	mnp limit config for customer specific logical mn
                            	**type**\:  int
                            
                            	**range:** 1..32
                            
                            .. attribute:: mobile_route_ad
                            
                            	Specify the Admin Distance value
                            	**type**\:  int
                            
                            	**range:** 1..254
                            
                            .. attribute:: network_attributes
                            
                            	network parameters for the customer
                            	**type**\:   :py:class:`NetworkAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes>`
                            
                            .. attribute:: transports
                            
                            	Table of Transport
                            	**type**\:   :py:class:`Transports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports>`
                            
                            

                            """

                            _prefix = 'ip-mobileip-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.customer_name = None
                                self.vrf_name = None
                                self.authenticate_option = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption()
                                self.authenticate_option.parent = self
                                self.bandwidth_aggregate = None
                                self.binding_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes()
                                self.binding_attributes.parent = self
                                self.gre_key = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey()
                                self.gre_key.parent = self
                                self.heart_beat_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes()
                                self.heart_beat_attributes.parent = self
                                self.mnp_customer = None
                                self.mnp_ipv4_customer = None
                                self.mnp_ipv4_lmn = None
                                self.mnp_ipv6_customer = None
                                self.mnp_ipv6_lmn = None
                                self.mnp_lmn = None
                                self.mobile_route_ad = None
                                self.network_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes()
                                self.network_attributes.parent = self
                                self.transports = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports()
                                self.transports.parent = self


                            class AuthenticateOption(object):
                                """
                                Authentication option between PMIPV6
                                entities
                                
                                .. attribute:: key
                                
                                	ASCII string
                                	**type**\:  str
                                
                                	**length:** 1..125
                                
                                .. attribute:: spi
                                
                                	SPI in hex value
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{1,8}
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.key = None
                                    self.spi = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:authenticate-option'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.key is not None:
                                        return True

                                    if self.spi is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                    return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption']['meta_info']


                            class HeartBeatAttributes(object):
                                """
                                heartbeat config for this Customer
                                
                                .. attribute:: interval
                                
                                	Specify the interval value in second
                                	**type**\:  int
                                
                                	**range:** 10..3600
                                
                                .. attribute:: retries
                                
                                	Specify the retry value
                                	**type**\:  int
                                
                                	**range:** 1..10
                                
                                .. attribute:: timeout
                                
                                	Specify the timeout value
                                	**type**\:  int
                                
                                	**range:** 1..3600
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.interval = None
                                    self.retries = None
                                    self.timeout = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:heart-beat-attributes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.interval is not None:
                                        return True

                                    if self.retries is not None:
                                        return True

                                    if self.timeout is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                    return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes']['meta_info']


                            class Transports(object):
                                """
                                Table of Transport
                                
                                .. attribute:: transport
                                
                                	Customer transport attributes
                                	**type**\: list of    :py:class:`Transport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports.Transport>`
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.transport = YList()
                                    self.transport.parent = self
                                    self.transport.name = 'transport'


                                class Transport(object):
                                    """
                                    Customer transport attributes
                                    
                                    .. attribute:: vrf_name  <key>
                                    
                                    	VRF Name
                                    	**type**\:  str
                                    
                                    	**length:** 1..125
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	Configure IPv4 address for this LMA
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	Configure IPv6 address for this LMA
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-mobileip-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.vrf_name = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.vrf_name is None:
                                            raise YPYModelError('Key property vrf_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:transport[Cisco-IOS-XR-ip-mobileip-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.vrf_name is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.ipv6_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                        return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports.Transport']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:transports'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.transport is not None:
                                        for child_ref in self.transport:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                    return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports']['meta_info']


                            class NetworkAttributes(object):
                                """
                                network parameters for the customer
                                
                                .. attribute:: authorizes
                                
                                	Table of Authorize
                                	**type**\:   :py:class:`Authorizes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes>`
                                
                                .. attribute:: unauthorize
                                
                                	not authorize the network prefixes
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.authorizes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes()
                                    self.authorizes.parent = self
                                    self.unauthorize = None


                                class Authorizes(object):
                                    """
                                    Table of Authorize
                                    
                                    .. attribute:: authorize
                                    
                                    	not authorize the network prefixes
                                    	**type**\: list of    :py:class:`Authorize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize>`
                                    
                                    

                                    """

                                    _prefix = 'ip-mobileip-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.authorize = YList()
                                        self.authorize.parent = self
                                        self.authorize.name = 'authorize'


                                    class Authorize(object):
                                        """
                                        not authorize the network prefixes
                                        
                                        .. attribute:: name  <key>
                                        
                                        	ASCII string
                                        	**type**\:  str
                                        
                                        	**length:** 1..125
                                        
                                        .. attribute:: pool_attributes
                                        
                                        	Pool configs for this network
                                        	**type**\:   :py:class:`PoolAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes>`
                                        
                                        

                                        """

                                        _prefix = 'ip-mobileip-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.name = None
                                            self.pool_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes()
                                            self.pool_attributes.parent = self


                                        class PoolAttributes(object):
                                            """
                                            Pool configs for this network
                                            
                                            .. attribute:: mobile_network
                                            
                                            	pool configs for the mobile network
                                            	**type**\:   :py:class:`MobileNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork>`
                                            
                                            .. attribute:: mobile_node
                                            
                                            	pool configs for the mobile nodes
                                            	**type**\:   :py:class:`MobileNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode>`
                                            
                                            

                                            """

                                            _prefix = 'ip-mobileip-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.mobile_network = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork()
                                                self.mobile_network.parent = self
                                                self.mobile_node = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode()
                                                self.mobile_node.parent = self


                                            class MobileNode(object):
                                                """
                                                pool configs for the mobile nodes
                                                
                                                .. attribute:: ipv4_pool
                                                
                                                	None
                                                	**type**\:   :py:class:`Ipv4Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool>`
                                                
                                                .. attribute:: ipv6_pool
                                                
                                                	None
                                                	**type**\:   :py:class:`Ipv6Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool>`
                                                
                                                

                                                """

                                                _prefix = 'ip-mobileip-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.ipv4_pool = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool()
                                                    self.ipv4_pool.parent = self
                                                    self.ipv6_pool = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool()
                                                    self.ipv6_pool.parent = self


                                                class Ipv4Pool(object):
                                                    """
                                                    None
                                                    
                                                    .. attribute:: pool_prefix
                                                    
                                                    	IPv4 Pool Prefix value
                                                    	**type**\:  int
                                                    
                                                    	**range:** 8..30
                                                    
                                                    .. attribute:: start_address
                                                    
                                                    	Pool IPv4 start address
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    

                                                    """

                                                    _prefix = 'ip-mobileip-cfg'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.pool_prefix = None
                                                        self.start_address = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:ipv4-pool'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return True

                                                    def _has_data(self):
                                                        if self.pool_prefix is not None:
                                                            return True

                                                        if self.start_address is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                                        return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool']['meta_info']


                                                class Ipv6Pool(object):
                                                    """
                                                    None
                                                    
                                                    .. attribute:: pool_prefix
                                                    
                                                    	IPv6 Pool Prefix value
                                                    	**type**\:  int
                                                    
                                                    	**range:** 8..62
                                                    
                                                    .. attribute:: start_address
                                                    
                                                    	Pool IPv6 start address
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                    
                                                    

                                                    """

                                                    _prefix = 'ip-mobileip-cfg'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.pool_prefix = None
                                                        self.start_address = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:ipv6-pool'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return True

                                                    def _has_data(self):
                                                        if self.pool_prefix is not None:
                                                            return True

                                                        if self.start_address is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                                        return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mobile-node'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if self.ipv4_pool is not None and self.ipv4_pool._has_data():
                                                        return True

                                                    if self.ipv6_pool is not None and self.ipv6_pool._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                                    return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode']['meta_info']


                                            class MobileNetwork(object):
                                                """
                                                pool configs for the mobile network
                                                
                                                .. attribute:: mripv4_pools
                                                
                                                	Table of MRIPV4Pool
                                                	**type**\:   :py:class:`Mripv4Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools>`
                                                
                                                .. attribute:: mripv6_pools
                                                
                                                	Table of MRIPV6Pool
                                                	**type**\:   :py:class:`Mripv6Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools>`
                                                
                                                

                                                """

                                                _prefix = 'ip-mobileip-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.mripv4_pools = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools()
                                                    self.mripv4_pools.parent = self
                                                    self.mripv6_pools = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools()
                                                    self.mripv6_pools.parent = self


                                                class Mripv4Pools(object):
                                                    """
                                                    Table of MRIPV4Pool
                                                    
                                                    .. attribute:: mripv4_pool
                                                    
                                                    	ipv4 pool
                                                    	**type**\: list of    :py:class:`Mripv4Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ip-mobileip-cfg'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.mripv4_pool = YList()
                                                        self.mripv4_pool.parent = self
                                                        self.mripv4_pool.name = 'mripv4_pool'


                                                    class Mripv4Pool(object):
                                                        """
                                                        ipv4 pool
                                                        
                                                        .. attribute:: start_address  <key>
                                                        
                                                        	Pool IPv4 start address
                                                        	**type**\:  str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: network_prefix
                                                        
                                                        	IPv4 Network Prefix value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 8..32
                                                        
                                                        .. attribute:: pool_prefix
                                                        
                                                        	IPv4 Pool Prefix value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 8..30
                                                        
                                                        

                                                        """

                                                        _prefix = 'ip-mobileip-cfg'
                                                        _revision = '2015-11-09'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.start_address = None
                                                            self.network_prefix = None
                                                            self.pool_prefix = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                                            if self.start_address is None:
                                                                raise YPYModelError('Key property start_address is None')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mripv4-pool[Cisco-IOS-XR-ip-mobileip-cfg:start-address = ' + str(self.start_address) + ']'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return True

                                                        def _has_data(self):
                                                            if self.start_address is not None:
                                                                return True

                                                            if self.network_prefix is not None:
                                                                return True

                                                            if self.pool_prefix is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                                            return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mripv4-pools'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return True

                                                    def _has_data(self):
                                                        if self.mripv4_pool is not None:
                                                            for child_ref in self.mripv4_pool:
                                                                if child_ref._has_data():
                                                                    return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                                        return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools']['meta_info']


                                                class Mripv6Pools(object):
                                                    """
                                                    Table of MRIPV6Pool
                                                    
                                                    .. attribute:: mripv6_pool
                                                    
                                                    	ipv6 pool
                                                    	**type**\: list of    :py:class:`Mripv6Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ip-mobileip-cfg'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.mripv6_pool = YList()
                                                        self.mripv6_pool.parent = self
                                                        self.mripv6_pool.name = 'mripv6_pool'


                                                    class Mripv6Pool(object):
                                                        """
                                                        ipv6 pool
                                                        
                                                        .. attribute:: start_address  <key>
                                                        
                                                        	Pool IPv6 start address
                                                        	**type**\:  str
                                                        
                                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: network_prefix
                                                        
                                                        	IPv4 Network Prefix value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 8..64
                                                        
                                                        .. attribute:: pool_prefix
                                                        
                                                        	IPv6 Pool Prefix value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 8..64
                                                        
                                                        

                                                        """

                                                        _prefix = 'ip-mobileip-cfg'
                                                        _revision = '2015-11-09'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.start_address = None
                                                            self.network_prefix = None
                                                            self.pool_prefix = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                                            if self.start_address is None:
                                                                raise YPYModelError('Key property start_address is None')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mripv6-pool[Cisco-IOS-XR-ip-mobileip-cfg:start-address = ' + str(self.start_address) + ']'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return True

                                                        def _has_data(self):
                                                            if self.start_address is not None:
                                                                return True

                                                            if self.network_prefix is not None:
                                                                return True

                                                            if self.pool_prefix is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                                            return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mripv6-pools'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return True

                                                    def _has_data(self):
                                                        if self.mripv6_pool is not None:
                                                            for child_ref in self.mripv6_pool:
                                                                if child_ref._has_data():
                                                                    return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                                        return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mobile-network'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if self.mripv4_pools is not None and self.mripv4_pools._has_data():
                                                        return True

                                                    if self.mripv6_pools is not None and self.mripv6_pools._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                                    return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:pool-attributes'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.mobile_network is not None and self.mobile_network._has_data():
                                                    return True

                                                if self.mobile_node is not None and self.mobile_node._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                                return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.name is None:
                                                raise YPYModelError('Key property name is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:authorize[Cisco-IOS-XR-ip-mobileip-cfg:name = ' + str(self.name) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.name is not None:
                                                return True

                                            if self.pool_attributes is not None and self.pool_attributes._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                            return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:authorizes'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.authorize is not None:
                                            for child_ref in self.authorize:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                        return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:network-attributes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.authorizes is not None and self.authorizes._has_data():
                                        return True

                                    if self.unauthorize is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                    return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes']['meta_info']


                            class GreKey(object):
                                """
                                Customer specific GRE key
                                
                                .. attribute:: gre_key_type
                                
                                	Set constant integer
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: gre_key_value
                                
                                	GRE key value
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.gre_key_type = None
                                    self.gre_key_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:gre-key'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.gre_key_type is not None:
                                        return True

                                    if self.gre_key_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                    return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey']['meta_info']


                            class BindingAttributes(object):
                                """
                                Customer specific binding attributes
                                
                                .. attribute:: max_life_time
                                
                                	Maximum bce lifetime permitted
                                	**type**\:  int
                                
                                	**range:** 10..65535
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.max_life_time = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:binding-attributes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.max_life_time is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                    return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.customer_name is None:
                                    raise YPYModelError('Key property customer_name is None')
                                if self.vrf_name is None:
                                    raise YPYModelError('Key property vrf_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:customer[Cisco-IOS-XR-ip-mobileip-cfg:customer-name = ' + str(self.customer_name) + '][Cisco-IOS-XR-ip-mobileip-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.customer_name is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                if self.authenticate_option is not None and self.authenticate_option._has_data():
                                    return True

                                if self.bandwidth_aggregate is not None:
                                    return True

                                if self.binding_attributes is not None and self.binding_attributes._has_data():
                                    return True

                                if self.gre_key is not None and self.gre_key._has_data():
                                    return True

                                if self.heart_beat_attributes is not None and self.heart_beat_attributes._has_data():
                                    return True

                                if self.mnp_customer is not None:
                                    return True

                                if self.mnp_ipv4_customer is not None:
                                    return True

                                if self.mnp_ipv4_lmn is not None:
                                    return True

                                if self.mnp_ipv6_customer is not None:
                                    return True

                                if self.mnp_ipv6_lmn is not None:
                                    return True

                                if self.mnp_lmn is not None:
                                    return True

                                if self.mobile_route_ad is not None:
                                    return True

                                if self.network_attributes is not None and self.network_attributes._has_data():
                                    return True

                                if self.transports is not None and self.transports._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:customers'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.customer is not None:
                                for child_ref in self.customer:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                            return meta._meta_table['MobileIp.Lmas.Lma.Services.Service.Customers']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.lma_service is None:
                            raise YPYModelError('Key property lma_service is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:service[Cisco-IOS-XR-ip-mobileip-cfg:lma-service = ' + str(self.lma_service) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.lma_service is not None:
                            return True

                        if self.customers is not None and self.customers._has_data():
                            return True

                        if self.ignore is not None:
                            return True

                        if self.mnp_customer is not None:
                            return True

                        if self.mnp_ipv4_customer is not None:
                            return True

                        if self.mnp_ipv4_lmn is not None:
                            return True

                        if self.mnp_ipv6_customer is not None:
                            return True

                        if self.mnp_ipv6_lmn is not None:
                            return True

                        if self.mnp_lmn is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                        return meta._meta_table['MobileIp.Lmas.Lma.Services.Service']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:services'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.service is not None:
                        for child_ref in self.service:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.Services']['meta_info']


            class ReplayProtection(object):
                """
                Replay Protection Method
                
                .. attribute:: ignore
                
                	Set constant integer
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: validity_window
                
                	Specify window value in seconds
                	**type**\:  int
                
                	**range:** 1..255
                
                	**units**\: second
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ignore = None
                    self.validity_window = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:replay-protection'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ignore is not None:
                        return True

                    if self.validity_window is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.ReplayProtection']['meta_info']


            class Networks(object):
                """
                Table of Network
                
                .. attribute:: network
                
                	network for this LMA
                	**type**\: list of    :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.network = YList()
                    self.network.parent = self
                    self.network.name = 'network'


                class Network(object):
                    """
                    network for this LMA
                    
                    .. attribute:: lma_network  <key>
                    
                    	Network name
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: pool_attributes
                    
                    	Pool configs for this network
                    	**type**\:   :py:class:`PoolAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes>`
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.lma_network = None
                        self.pool_attributes = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes()
                        self.pool_attributes.parent = self


                    class PoolAttributes(object):
                        """
                        Pool configs for this network
                        
                        .. attribute:: mobile_network
                        
                        	pool configs for the mobile network
                        	**type**\:   :py:class:`MobileNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork>`
                        
                        .. attribute:: mobile_node
                        
                        	pool configs for the mobile nodes
                        	**type**\:   :py:class:`MobileNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode>`
                        
                        

                        """

                        _prefix = 'ip-mobileip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.mobile_network = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork()
                            self.mobile_network.parent = self
                            self.mobile_node = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode()
                            self.mobile_node.parent = self


                        class MobileNode(object):
                            """
                            pool configs for the mobile nodes
                            
                            .. attribute:: ipv4_pool
                            
                            	None
                            	**type**\:   :py:class:`Ipv4Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool>`
                            
                            .. attribute:: ipv6_pool
                            
                            	None
                            	**type**\:   :py:class:`Ipv6Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool>`
                            
                            

                            """

                            _prefix = 'ip-mobileip-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_pool = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool()
                                self.ipv4_pool.parent = self
                                self.ipv6_pool = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool()
                                self.ipv6_pool.parent = self


                            class Ipv4Pool(object):
                                """
                                None
                                
                                .. attribute:: pool_prefix
                                
                                	IPv4 Pool Prefix value
                                	**type**\:  int
                                
                                	**range:** 8..30
                                
                                .. attribute:: start_address
                                
                                	Pool IPv4 start address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.pool_prefix = None
                                    self.start_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:ipv4-pool'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.pool_prefix is not None:
                                        return True

                                    if self.start_address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                    return meta._meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool']['meta_info']


                            class Ipv6Pool(object):
                                """
                                None
                                
                                .. attribute:: pool_prefix
                                
                                	IPv6 Pool Prefix value
                                	**type**\:  int
                                
                                	**range:** 8..62
                                
                                .. attribute:: start_address
                                
                                	Pool IPv6 start address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.pool_prefix = None
                                    self.start_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:ipv6-pool'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.pool_prefix is not None:
                                        return True

                                    if self.start_address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                    return meta._meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mobile-node'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.ipv4_pool is not None and self.ipv4_pool._has_data():
                                    return True

                                if self.ipv6_pool is not None and self.ipv6_pool._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                return meta._meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode']['meta_info']


                        class MobileNetwork(object):
                            """
                            pool configs for the mobile network
                            
                            .. attribute:: mripv4_pools
                            
                            	Table of MRIPV4Pool
                            	**type**\:   :py:class:`Mripv4Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools>`
                            
                            .. attribute:: mripv6_pools
                            
                            	Table of MRIPV6Pool
                            	**type**\:   :py:class:`Mripv6Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools>`
                            
                            

                            """

                            _prefix = 'ip-mobileip-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mripv4_pools = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools()
                                self.mripv4_pools.parent = self
                                self.mripv6_pools = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools()
                                self.mripv6_pools.parent = self


                            class Mripv6Pools(object):
                                """
                                Table of MRIPV6Pool
                                
                                .. attribute:: mripv6_pool
                                
                                	ipv6 pool
                                	**type**\: list of    :py:class:`Mripv6Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool>`
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.mripv6_pool = YList()
                                    self.mripv6_pool.parent = self
                                    self.mripv6_pool.name = 'mripv6_pool'


                                class Mripv6Pool(object):
                                    """
                                    ipv6 pool
                                    
                                    .. attribute:: start_address  <key>
                                    
                                    	Pool IPv6 start address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: network_prefix
                                    
                                    	IPv4 Network Prefix value
                                    	**type**\:  int
                                    
                                    	**range:** 8..64
                                    
                                    .. attribute:: pool_prefix
                                    
                                    	IPv6 Pool Prefix value
                                    	**type**\:  int
                                    
                                    	**range:** 8..64
                                    
                                    

                                    """

                                    _prefix = 'ip-mobileip-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.start_address = None
                                        self.network_prefix = None
                                        self.pool_prefix = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.start_address is None:
                                            raise YPYModelError('Key property start_address is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mripv6-pool[Cisco-IOS-XR-ip-mobileip-cfg:start-address = ' + str(self.start_address) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.start_address is not None:
                                            return True

                                        if self.network_prefix is not None:
                                            return True

                                        if self.pool_prefix is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                        return meta._meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mripv6-pools'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.mripv6_pool is not None:
                                        for child_ref in self.mripv6_pool:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                    return meta._meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools']['meta_info']


                            class Mripv4Pools(object):
                                """
                                Table of MRIPV4Pool
                                
                                .. attribute:: mripv4_pool
                                
                                	ipv4 pool
                                	**type**\: list of    :py:class:`Mripv4Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool>`
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.mripv4_pool = YList()
                                    self.mripv4_pool.parent = self
                                    self.mripv4_pool.name = 'mripv4_pool'


                                class Mripv4Pool(object):
                                    """
                                    ipv4 pool
                                    
                                    .. attribute:: start_address  <key>
                                    
                                    	Pool IPv4 start address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: network_prefix
                                    
                                    	IPv4 Network Prefix value
                                    	**type**\:  int
                                    
                                    	**range:** 8..32
                                    
                                    .. attribute:: pool_prefix
                                    
                                    	IPv4 Pool Prefix value
                                    	**type**\:  int
                                    
                                    	**range:** 8..30
                                    
                                    

                                    """

                                    _prefix = 'ip-mobileip-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.start_address = None
                                        self.network_prefix = None
                                        self.pool_prefix = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.start_address is None:
                                            raise YPYModelError('Key property start_address is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mripv4-pool[Cisco-IOS-XR-ip-mobileip-cfg:start-address = ' + str(self.start_address) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.start_address is not None:
                                            return True

                                        if self.network_prefix is not None:
                                            return True

                                        if self.pool_prefix is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                        return meta._meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mripv4-pools'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.mripv4_pool is not None:
                                        for child_ref in self.mripv4_pool:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                    return meta._meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:mobile-network'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.mripv4_pools is not None and self.mripv4_pools._has_data():
                                    return True

                                if self.mripv6_pools is not None and self.mripv6_pools._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                                return meta._meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:pool-attributes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.mobile_network is not None and self.mobile_network._has_data():
                                return True

                            if self.mobile_node is not None and self.mobile_node._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                            return meta._meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.lma_network is None:
                            raise YPYModelError('Key property lma_network is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:network[Cisco-IOS-XR-ip-mobileip-cfg:lma-network = ' + str(self.lma_network) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.lma_network is not None:
                            return True

                        if self.pool_attributes is not None and self.pool_attributes._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                        return meta._meta_table['MobileIp.Lmas.Lma.Networks.Network']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-mobileip-cfg:networks'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.network is not None:
                        for child_ref in self.network:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                    return meta._meta_table['MobileIp.Lmas.Lma.Networks']['meta_info']

            @property
            def _common_path(self):
                if self.lma_name is None:
                    raise YPYModelError('Key property lma_name is None')
                if self.domain_name is None:
                    raise YPYModelError('Key property domain_name is None')

                return '/Cisco-IOS-XR-ip-mobileip-cfg:mobile-ip/Cisco-IOS-XR-ip-mobileip-cfg:lmas/Cisco-IOS-XR-ip-mobileip-cfg:lma[Cisco-IOS-XR-ip-mobileip-cfg:lma-name = ' + str(self.lma_name) + '][Cisco-IOS-XR-ip-mobileip-cfg:domain-name = ' + str(self.domain_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.lma_name is not None:
                    return True

                if self.domain_name is not None:
                    return True

                if self.aaa is not None and self.aaa._has_data():
                    return True

                if self.ani is not None:
                    return True

                if self.binding_attributes is not None and self.binding_attributes._has_data():
                    return True

                if self.binding_revocation_attributes is not None and self.binding_revocation_attributes._has_data():
                    return True

                if self.default_profile is not None:
                    return True

                if self.dscp is not None and self.dscp._has_data():
                    return True

                if self.dynamic is not None:
                    return True

                if self.enforce is not None:
                    return True

                if self.generate is not None:
                    return True

                if self.heart_beat_attributes is not None and self.heart_beat_attributes._has_data():
                    return True

                if self.hnp is not None and self.hnp._has_data():
                    return True

                if self.interface is not None:
                    return True

                if self.lmaipv4_addresses is not None and self.lmaipv4_addresses._has_data():
                    return True

                if self.lmaipv6_addresses is not None and self.lmaipv6_addresses._has_data():
                    return True

                if self.mags is not None and self.mags._has_data():
                    return True

                if self.mobile_map is not None:
                    return True

                if self.mobile_route_ad is not None:
                    return True

                if self.multipath is not None:
                    return True

                if self.networks is not None and self.networks._has_data():
                    return True

                if self.pgw_subs_cont is not None:
                    return True

                if self.rat_attributes is not None and self.rat_attributes._has_data():
                    return True

                if self.redistribute is not None and self.redistribute._has_data():
                    return True

                if self.replay_protection is not None and self.replay_protection._has_data():
                    return True

                if self.roles is not None and self.roles._has_data():
                    return True

                if self.services is not None and self.services._has_data():
                    return True

                if self.tunnel_attributes is not None and self.tunnel_attributes._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
                return meta._meta_table['MobileIp.Lmas.Lma']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-mobileip-cfg:mobile-ip/Cisco-IOS-XR-ip-mobileip-cfg:lmas'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.lma is not None:
                for child_ref in self.lma:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
            return meta._meta_table['MobileIp.Lmas']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-mobileip-cfg:mobile-ip'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.domains is not None and self.domains._has_data():
            return True

        if self.lmas is not None and self.lmas._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_mobileip_cfg as meta
        return meta._meta_table['MobileIp']['meta_info']



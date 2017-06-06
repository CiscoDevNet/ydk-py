""" Cisco_IOS_XR_crypto_macsec_mka_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-macsec\-mka package configuration.

This module contains definitions
for the following management objects\:
  macsec\: MACSec MKA

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MacsecMkaCipherSuiteEnum(Enum):
    """
    MacsecMkaCipherSuiteEnum

    Macsec mka cipher suite

    .. data:: gcm_aes_128 = 1

    	GCM AES 128

    .. data:: gcm_aes_256 = 2

    	GCM AES 256

    .. data:: gcm_aes_xpn_128 = 3

    	GCM AES XPN 128

    .. data:: gcm_aes_xpn_256 = 4

    	GCM AES XPN 256

    """

    gcm_aes_128 = 1

    gcm_aes_256 = 2

    gcm_aes_xpn_128 = 3

    gcm_aes_xpn_256 = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_cfg as meta
        return meta._meta_table['MacsecMkaCipherSuiteEnum']


class MacsecMkaConfOffsetEnum(Enum):
    """
    MacsecMkaConfOffsetEnum

    Macsec mka conf offset

    .. data:: conf_off_set_0 = 0

    	CONF OFFSET 0

    .. data:: conf_off_set_30 = 30

    	CONF OFFSET 30

    .. data:: conf_off_set_50 = 50

    	CONF OFFSET 50

    """

    conf_off_set_0 = 0

    conf_off_set_30 = 30

    conf_off_set_50 = 50


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_cfg as meta
        return meta._meta_table['MacsecMkaConfOffsetEnum']


class MacsecMkaPolicyExceptionEnum(Enum):
    """
    MacsecMkaPolicyExceptionEnum

    Macsec mka policy exception

    .. data:: lacp_in_clear = 1

    	lacp in clear

    """

    lacp_in_clear = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_cfg as meta
        return meta._meta_table['MacsecMkaPolicyExceptionEnum']


class MacsecMkaSecurityPolicyEnum(Enum):
    """
    MacsecMkaSecurityPolicyEnum

    Macsec mka security policy

    .. data:: should_secure = 0

    	should secure

    .. data:: must_secure = 1

    	must secure

    """

    should_secure = 0

    must_secure = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_cfg as meta
        return meta._meta_table['MacsecMkaSecurityPolicyEnum']



class Macsec(object):
    """
    MACSec MKA
    
    .. attribute:: policy
    
    	MACSec Policy
    	**type**\: list of    :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.Macsec.Policy>`
    
    

    """

    _prefix = 'crypto-macsec-mka-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.policy = YList()
        self.policy.parent = self
        self.policy.name = 'policy'


    class Policy(object):
        """
        MACSec Policy
        
        .. attribute:: name  <key>
        
        	Name of the Policy of maximum length 16
        	**type**\:  str
        
        	**length:** 1..16
        
        .. attribute:: cipher_suite
        
        	Cipher\-suite of Policy
        	**type**\:   :py:class:`MacsecMkaCipherSuiteEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.MacsecMkaCipherSuiteEnum>`
        
        .. attribute:: conf_offset
        
        	Conf\-Offset of Policy
        	**type**\:   :py:class:`MacsecMkaConfOffsetEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.MacsecMkaConfOffsetEnum>`
        
        .. attribute:: delay_protection
        
        	TRUE enables data delay protection
        	**type**\:  bool
        
        .. attribute:: include_icv_indicator
        
        	TRUE enables Include ICV Indicator paramset in MKPDU
        	**type**\:  bool
        
        .. attribute:: key_server_priority
        
        	Key\-Server\-Priority of Policy
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: policy_exception
        
        	Macsec policy exception for packets to be in clear
        	**type**\:   :py:class:`MacsecMkaPolicyExceptionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.MacsecMkaPolicyExceptionEnum>`
        
        .. attribute:: sak_rekey_interval
        
        	Interval after which key\-server generates new SAK for a Secured Session
        	**type**\:  int
        
        	**range:** 0..43200
        
        	**units**\: minute
        
        .. attribute:: security_policy
        
        	Security\-Policy of Policy
        	**type**\:   :py:class:`MacsecMkaSecurityPolicyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.MacsecMkaSecurityPolicyEnum>`
        
        .. attribute:: vlan_tags_in_clear
        
        	VLAN\-Tags\-In\-Clear of Policy
        	**type**\:  int
        
        	**range:** 1..2
        
        .. attribute:: window_size
        
        	Window\-Size of Policy
        	**type**\:  int
        
        	**range:** 0..1024
        
        

        """

        _prefix = 'crypto-macsec-mka-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.name = None
            self.cipher_suite = None
            self.conf_offset = None
            self.delay_protection = None
            self.include_icv_indicator = None
            self.key_server_priority = None
            self.policy_exception = None
            self.sak_rekey_interval = None
            self.security_policy = None
            self.vlan_tags_in_clear = None
            self.window_size = None

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/Cisco-IOS-XR-crypto-macsec-mka-cfg:macsec/Cisco-IOS-XR-crypto-macsec-mka-cfg:policy[Cisco-IOS-XR-crypto-macsec-mka-cfg:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.name is not None:
                return True

            if self.cipher_suite is not None:
                return True

            if self.conf_offset is not None:
                return True

            if self.delay_protection is not None:
                return True

            if self.include_icv_indicator is not None:
                return True

            if self.key_server_priority is not None:
                return True

            if self.policy_exception is not None:
                return True

            if self.sak_rekey_interval is not None:
                return True

            if self.security_policy is not None:
                return True

            if self.vlan_tags_in_clear is not None:
                return True

            if self.window_size is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_cfg as meta
            return meta._meta_table['Macsec.Policy']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-macsec-mka-cfg:macsec'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.policy is not None:
            for child_ref in self.policy:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_cfg as meta
        return meta._meta_table['Macsec']['meta_info']



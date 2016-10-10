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

    .. data:: GCM_AES_128 = 1

    	GCM AES 128

    .. data:: GCM_AES_256 = 2

    	GCM AES 256

    .. data:: GCM_AES_XPN_128 = 3

    	GCM AES XPN 128

    .. data:: GCM_AES_XPN_256 = 4

    	GCM AES XPN 256

    """

    GCM_AES_128 = 1

    GCM_AES_256 = 2

    GCM_AES_XPN_128 = 3

    GCM_AES_XPN_256 = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_cfg as meta
        return meta._meta_table['MacsecMkaCipherSuiteEnum']


class MacsecMkaConfOffsetEnum(Enum):
    """
    MacsecMkaConfOffsetEnum

    Macsec mka conf offset

    .. data:: CONF_OFF_SET_0 = 0

    	CONF OFFSET 0

    .. data:: CONF_OFF_SET_30 = 30

    	CONF OFFSET 30

    .. data:: CONF_OFF_SET_50 = 50

    	CONF OFFSET 50

    """

    CONF_OFF_SET_0 = 0

    CONF_OFF_SET_30 = 30

    CONF_OFF_SET_50 = 50


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_cfg as meta
        return meta._meta_table['MacsecMkaConfOffsetEnum']


class MacsecMkaSecurityPolicyEnum(Enum):
    """
    MacsecMkaSecurityPolicyEnum

    Macsec mka security policy

    .. data:: SHOULD_SECURE = 0

    	should secure

    .. data:: MUST_SECURE = 1

    	must secure

    """

    SHOULD_SECURE = 0

    MUST_SECURE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_cfg as meta
        return meta._meta_table['MacsecMkaSecurityPolicyEnum']



class Macsec(object):
    """
    MACSec MKA
    
    .. attribute:: policy
    
    	MACSec Policy
    	**type**\: list of  :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.Macsec.Policy>`
    
    

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
        
        	Name of the Policy
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: cipher_suite
        
        	Cipher\-suite of Policy
        	**type**\:  :py:class:`MacsecMkaCipherSuiteEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.MacsecMkaCipherSuiteEnum>`
        
        .. attribute:: conf_offset
        
        	Conf\-Offset of Policy
        	**type**\:  :py:class:`MacsecMkaConfOffsetEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.MacsecMkaConfOffsetEnum>`
        
        .. attribute:: key_server_priority
        
        	Key\-Server\-Priority of Policy
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: security_policy
        
        	Security\-Policy of Policy
        	**type**\:  :py:class:`MacsecMkaSecurityPolicyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.MacsecMkaSecurityPolicyEnum>`
        
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
            self.key_server_priority = None
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
            if not self.is_config():
                return False
            if self.name is not None:
                return True

            if self.cipher_suite is not None:
                return True

            if self.conf_offset is not None:
                return True

            if self.key_server_priority is not None:
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
        if not self.is_config():
            return False
        if self.policy is not None:
            for child_ref in self.policy:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_cfg as meta
        return meta._meta_table['Macsec']['meta_info']



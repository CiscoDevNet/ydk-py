""" Cisco_IOS_XR_crypto_macsec_mka_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-macsec\-mka package configuration.

This module contains definitions
for the following management objects\:
  macsec\: MACSec MKA

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MacsecMkaCipherSuite(Enum):
    """
    MacsecMkaCipherSuite (Enum Class)

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

    gcm_aes_128 = Enum.YLeaf(1, "gcm-aes-128")

    gcm_aes_256 = Enum.YLeaf(2, "gcm-aes-256")

    gcm_aes_xpn_128 = Enum.YLeaf(3, "gcm-aes-xpn-128")

    gcm_aes_xpn_256 = Enum.YLeaf(4, "gcm-aes-xpn-256")


class MacsecMkaConfOffset(Enum):
    """
    MacsecMkaConfOffset (Enum Class)

    Macsec mka conf offset

    .. data:: conf_off_set_0 = 0

    	CONF OFFSET 0

    .. data:: conf_off_set_30 = 30

    	CONF OFFSET 30

    .. data:: conf_off_set_50 = 50

    	CONF OFFSET 50

    """

    conf_off_set_0 = Enum.YLeaf(0, "conf-off-set-0")

    conf_off_set_30 = Enum.YLeaf(30, "conf-off-set-30")

    conf_off_set_50 = Enum.YLeaf(50, "conf-off-set-50")


class MacsecMkaPolicyException(Enum):
    """
    MacsecMkaPolicyException (Enum Class)

    Macsec mka policy exception

    .. data:: lacp_in_clear = 1

    	lacp in clear

    """

    lacp_in_clear = Enum.YLeaf(1, "lacp-in-clear")


class MacsecMkaSecurityPolicy(Enum):
    """
    MacsecMkaSecurityPolicy (Enum Class)

    Macsec mka security policy

    .. data:: should_secure = 0

    	should secure

    .. data:: must_secure = 1

    	must secure

    """

    should_secure = Enum.YLeaf(0, "should-secure")

    must_secure = Enum.YLeaf(1, "must-secure")



class Macsec(Entity):
    """
    MACSec MKA
    
    .. attribute:: policy
    
    	MACSec Policy
    	**type**\: list of  		 :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.Macsec.Policy>`
    
    

    """

    _prefix = 'crypto-macsec-mka-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Macsec, self).__init__()
        self._top_entity = None

        self.yang_name = "macsec"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-macsec-mka-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("policy", ("policy", Macsec.Policy))])
        self._leafs = OrderedDict()

        self.policy = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-macsec-mka-cfg:macsec"

    def __setattr__(self, name, value):
        self._perform_setattr(Macsec, [], name, value)


    class Policy(Entity):
        """
        MACSec Policy
        
        .. attribute:: name  (key)
        
        	Name of the Policy of maximum length 16
        	**type**\: str
        
        	**length:** 1..16
        
        .. attribute:: delay_protection
        
        	TRUE enables data delay protection
        	**type**\: bool
        
        .. attribute:: security_policy
        
        	Security\-Policy of Policy
        	**type**\:  :py:class:`MacsecMkaSecurityPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.MacsecMkaSecurityPolicy>`
        
        .. attribute:: key_server_priority
        
        	Key\-Server\-Priority of Policy
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: conf_offset
        
        	Conf\-Offset of Policy
        	**type**\:  :py:class:`MacsecMkaConfOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.MacsecMkaConfOffset>`
        
        .. attribute:: sak_rekey_interval
        
        	Interval after which key\-server generates new SAK for a Secured Session
        	**type**\: int
        
        	**range:** 0..43200
        
        	**units**\: minute
        
        .. attribute:: policy_exception
        
        	Macsec policy exception for packets to be in clear
        	**type**\:  :py:class:`MacsecMkaPolicyException <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.MacsecMkaPolicyException>`
        
        .. attribute:: window_size
        
        	Window\-Size of Policy
        	**type**\: int
        
        	**range:** 0..1024
        
        .. attribute:: cipher_suite
        
        	Cipher\-suite of Policy
        	**type**\:  :py:class:`MacsecMkaCipherSuite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.MacsecMkaCipherSuite>`
        
        .. attribute:: include_icv_indicator
        
        	TRUE enables Include ICV Indicator paramset in MKPDU
        	**type**\: bool
        
        .. attribute:: vlan_tags_in_clear
        
        	VLAN\-Tags\-In\-Clear of Policy
        	**type**\: int
        
        	**range:** 1..2
        
        

        """

        _prefix = 'crypto-macsec-mka-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Macsec.Policy, self).__init__()

            self.yang_name = "policy"
            self.yang_parent_name = "macsec"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', YLeaf(YType.str, 'name')),
                ('delay_protection', YLeaf(YType.boolean, 'delay-protection')),
                ('security_policy', YLeaf(YType.enumeration, 'security-policy')),
                ('key_server_priority', YLeaf(YType.uint32, 'key-server-priority')),
                ('conf_offset', YLeaf(YType.enumeration, 'conf-offset')),
                ('sak_rekey_interval', YLeaf(YType.uint32, 'sak-rekey-interval')),
                ('policy_exception', YLeaf(YType.enumeration, 'policy-exception')),
                ('window_size', YLeaf(YType.uint32, 'window-size')),
                ('cipher_suite', YLeaf(YType.enumeration, 'cipher-suite')),
                ('include_icv_indicator', YLeaf(YType.boolean, 'include-icv-indicator')),
                ('vlan_tags_in_clear', YLeaf(YType.uint32, 'vlan-tags-in-clear')),
            ])
            self.name = None
            self.delay_protection = None
            self.security_policy = None
            self.key_server_priority = None
            self.conf_offset = None
            self.sak_rekey_interval = None
            self.policy_exception = None
            self.window_size = None
            self.cipher_suite = None
            self.include_icv_indicator = None
            self.vlan_tags_in_clear = None
            self._segment_path = lambda: "policy" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-mka-cfg:macsec/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Macsec.Policy, ['name', 'delay_protection', 'security_policy', 'key_server_priority', 'conf_offset', 'sak_rekey_interval', 'policy_exception', 'window_size', 'cipher_suite', 'include_icv_indicator', 'vlan_tags_in_clear'], name, value)

    def clone_ptr(self):
        self._top_entity = Macsec()
        return self._top_entity


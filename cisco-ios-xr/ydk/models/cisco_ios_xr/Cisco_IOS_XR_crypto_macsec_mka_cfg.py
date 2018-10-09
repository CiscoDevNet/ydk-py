""" Cisco_IOS_XR_crypto_macsec_mka_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-macsec\-mka package configuration.

This module contains definitions
for the following management objects\:
  macsec\: MACSec MKA

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
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
    
    .. attribute:: policy_names
    
    	MACSec Policy
    	**type**\:  :py:class:`PolicyNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.Macsec.PolicyNames>`
    
    .. attribute:: shutdown
    
    	Disable macsec on all data ports(system wide), has no impact on macsec configs
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

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
        self._child_classes = OrderedDict([("policy-names", ("policy_names", Macsec.PolicyNames))])
        self._leafs = OrderedDict([
            ('shutdown', (YLeaf(YType.empty, 'shutdown'), ['Empty'])),
        ])
        self.shutdown = None

        self.policy_names = Macsec.PolicyNames()
        self.policy_names.parent = self
        self._children_name_map["policy_names"] = "policy-names"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-macsec-mka-cfg:macsec"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Macsec, ['shutdown'], name, value)


    class PolicyNames(Entity):
        """
        MACSec Policy
        
        .. attribute:: policy_name
        
        	MACsec Policy Name
        	**type**\: list of  		 :py:class:`PolicyName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.Macsec.PolicyNames.PolicyName>`
        
        

        """

        _prefix = 'crypto-macsec-mka-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Macsec.PolicyNames, self).__init__()

            self.yang_name = "policy-names"
            self.yang_parent_name = "macsec"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("policy-name", ("policy_name", Macsec.PolicyNames.PolicyName))])
            self._leafs = OrderedDict()

            self.policy_name = YList(self)
            self._segment_path = lambda: "policy-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-mka-cfg:macsec/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Macsec.PolicyNames, [], name, value)


        class PolicyName(Entity):
            """
            MACsec Policy Name
            
            .. attribute:: name  (key)
            
            	Name of the Policy of maximum length 16
            	**type**\: str
            
            	**length:** 1..16
            
            .. attribute:: delay_protection
            
            	Enables data delay protection
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
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
            
            	DEPRECATED\-Interval(in minutes) after which key\-server generates new SAK for a Secured Session, Default\: OFF, recommended to use seconds option
            	**type**\: int
            
            	**range:** 1..43200
            
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
            
            	Enables Include ICV Indicator paramset in MKPDU
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: sak_rekey_interval_sec
            
            	Interval(in seconds) after which key\-server generates new SAK for a Secured Session, Default\: OFF
            	**type**\: int
            
            	**range:** 60..2592000
            
            	**units**\: second
            
            .. attribute:: vlan_tags_in_clear
            
            	VLAN\-Tags\-In\-Clear of Policy
            	**type**\: int
            
            	**range:** 1..2
            
            

            """

            _prefix = 'crypto-macsec-mka-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Macsec.PolicyNames.PolicyName, self).__init__()

                self.yang_name = "policy-name"
                self.yang_parent_name = "policy-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('delay_protection', (YLeaf(YType.empty, 'delay-protection'), ['Empty'])),
                    ('security_policy', (YLeaf(YType.enumeration, 'security-policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaSecurityPolicy', '')])),
                    ('key_server_priority', (YLeaf(YType.uint32, 'key-server-priority'), ['int'])),
                    ('conf_offset', (YLeaf(YType.enumeration, 'conf-offset'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaConfOffset', '')])),
                    ('sak_rekey_interval', (YLeaf(YType.uint32, 'sak-rekey-interval'), ['int'])),
                    ('policy_exception', (YLeaf(YType.enumeration, 'policy-exception'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaPolicyException', '')])),
                    ('window_size', (YLeaf(YType.uint32, 'window-size'), ['int'])),
                    ('cipher_suite', (YLeaf(YType.enumeration, 'cipher-suite'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaCipherSuite', '')])),
                    ('include_icv_indicator', (YLeaf(YType.empty, 'include-icv-indicator'), ['Empty'])),
                    ('sak_rekey_interval_sec', (YLeaf(YType.uint32, 'sak-rekey-interval-sec'), ['int'])),
                    ('vlan_tags_in_clear', (YLeaf(YType.uint32, 'vlan-tags-in-clear'), ['int'])),
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
                self.sak_rekey_interval_sec = None
                self.vlan_tags_in_clear = None
                self._segment_path = lambda: "policy-name" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-mka-cfg:macsec/policy-names/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Macsec.PolicyNames.PolicyName, ['name', 'delay_protection', 'security_policy', 'key_server_priority', 'conf_offset', 'sak_rekey_interval', 'policy_exception', 'window_size', 'cipher_suite', 'include_icv_indicator', 'sak_rekey_interval_sec', 'vlan_tags_in_clear'], name, value)

    def clone_ptr(self):
        self._top_entity = Macsec()
        return self._top_entity


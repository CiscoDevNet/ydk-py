""" Cisco_IOS_XR_crypto_macsec_mka_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-macsec\-mka package configuration.

This module contains definitions
for the following management objects\:
  macsec\: MACSec MKA

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MacsecMkaCipherSuite(Enum):
    """
    MacsecMkaCipherSuite

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
    MacsecMkaConfOffset

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
    MacsecMkaPolicyException

    Macsec mka policy exception

    .. data:: lacp_in_clear = 1

    	lacp in clear

    """

    lacp_in_clear = Enum.YLeaf(1, "lacp-in-clear")


class MacsecMkaSecurityPolicy(Enum):
    """
    MacsecMkaSecurityPolicy

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
    	**type**\: list of    :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.Macsec.Policy>`
    
    

    """

    _prefix = 'crypto-macsec-mka-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Macsec, self).__init__()
        self._top_entity = None

        self.yang_name = "macsec"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-macsec-mka-cfg"

        self.policy = YList(self)

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
                    super(Macsec, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Macsec, self).__setattr__(name, value)


    class Policy(Entity):
        """
        MACSec Policy
        
        .. attribute:: name  <key>
        
        	Name of the Policy of maximum length 16
        	**type**\:  str
        
        	**length:** 1..16
        
        .. attribute:: cipher_suite
        
        	Cipher\-suite of Policy
        	**type**\:   :py:class:`MacsecMkaCipherSuite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.MacsecMkaCipherSuite>`
        
        .. attribute:: conf_offset
        
        	Conf\-Offset of Policy
        	**type**\:   :py:class:`MacsecMkaConfOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.MacsecMkaConfOffset>`
        
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
        	**type**\:   :py:class:`MacsecMkaPolicyException <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.MacsecMkaPolicyException>`
        
        .. attribute:: sak_rekey_interval
        
        	Interval after which key\-server generates new SAK for a Secured Session
        	**type**\:  int
        
        	**range:** 0..43200
        
        	**units**\: minute
        
        .. attribute:: security_policy
        
        	Security\-Policy of Policy
        	**type**\:   :py:class:`MacsecMkaSecurityPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg.MacsecMkaSecurityPolicy>`
        
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
            super(Macsec.Policy, self).__init__()

            self.yang_name = "policy"
            self.yang_parent_name = "macsec"

            self.name = YLeaf(YType.str, "name")

            self.cipher_suite = YLeaf(YType.enumeration, "cipher-suite")

            self.conf_offset = YLeaf(YType.enumeration, "conf-offset")

            self.delay_protection = YLeaf(YType.boolean, "delay-protection")

            self.include_icv_indicator = YLeaf(YType.boolean, "include-icv-indicator")

            self.key_server_priority = YLeaf(YType.uint32, "key-server-priority")

            self.policy_exception = YLeaf(YType.enumeration, "policy-exception")

            self.sak_rekey_interval = YLeaf(YType.uint32, "sak-rekey-interval")

            self.security_policy = YLeaf(YType.enumeration, "security-policy")

            self.vlan_tags_in_clear = YLeaf(YType.uint32, "vlan-tags-in-clear")

            self.window_size = YLeaf(YType.uint32, "window-size")

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
                            "cipher_suite",
                            "conf_offset",
                            "delay_protection",
                            "include_icv_indicator",
                            "key_server_priority",
                            "policy_exception",
                            "sak_rekey_interval",
                            "security_policy",
                            "vlan_tags_in_clear",
                            "window_size") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Macsec.Policy, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Macsec.Policy, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.name.is_set or
                self.cipher_suite.is_set or
                self.conf_offset.is_set or
                self.delay_protection.is_set or
                self.include_icv_indicator.is_set or
                self.key_server_priority.is_set or
                self.policy_exception.is_set or
                self.sak_rekey_interval.is_set or
                self.security_policy.is_set or
                self.vlan_tags_in_clear.is_set or
                self.window_size.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                self.cipher_suite.yfilter != YFilter.not_set or
                self.conf_offset.yfilter != YFilter.not_set or
                self.delay_protection.yfilter != YFilter.not_set or
                self.include_icv_indicator.yfilter != YFilter.not_set or
                self.key_server_priority.yfilter != YFilter.not_set or
                self.policy_exception.yfilter != YFilter.not_set or
                self.sak_rekey_interval.yfilter != YFilter.not_set or
                self.security_policy.yfilter != YFilter.not_set or
                self.vlan_tags_in_clear.yfilter != YFilter.not_set or
                self.window_size.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "policy" + "[name='" + self.name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-macsec-mka-cfg:macsec/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())
            if (self.cipher_suite.is_set or self.cipher_suite.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipher_suite.get_name_leafdata())
            if (self.conf_offset.is_set or self.conf_offset.yfilter != YFilter.not_set):
                leaf_name_data.append(self.conf_offset.get_name_leafdata())
            if (self.delay_protection.is_set or self.delay_protection.yfilter != YFilter.not_set):
                leaf_name_data.append(self.delay_protection.get_name_leafdata())
            if (self.include_icv_indicator.is_set or self.include_icv_indicator.yfilter != YFilter.not_set):
                leaf_name_data.append(self.include_icv_indicator.get_name_leafdata())
            if (self.key_server_priority.is_set or self.key_server_priority.yfilter != YFilter.not_set):
                leaf_name_data.append(self.key_server_priority.get_name_leafdata())
            if (self.policy_exception.is_set or self.policy_exception.yfilter != YFilter.not_set):
                leaf_name_data.append(self.policy_exception.get_name_leafdata())
            if (self.sak_rekey_interval.is_set or self.sak_rekey_interval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sak_rekey_interval.get_name_leafdata())
            if (self.security_policy.is_set or self.security_policy.yfilter != YFilter.not_set):
                leaf_name_data.append(self.security_policy.get_name_leafdata())
            if (self.vlan_tags_in_clear.is_set or self.vlan_tags_in_clear.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vlan_tags_in_clear.get_name_leafdata())
            if (self.window_size.is_set or self.window_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.window_size.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "name" or name == "cipher-suite" or name == "conf-offset" or name == "delay-protection" or name == "include-icv-indicator" or name == "key-server-priority" or name == "policy-exception" or name == "sak-rekey-interval" or name == "security-policy" or name == "vlan-tags-in-clear" or name == "window-size"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix
            if(value_path == "cipher-suite"):
                self.cipher_suite = value
                self.cipher_suite.value_namespace = name_space
                self.cipher_suite.value_namespace_prefix = name_space_prefix
            if(value_path == "conf-offset"):
                self.conf_offset = value
                self.conf_offset.value_namespace = name_space
                self.conf_offset.value_namespace_prefix = name_space_prefix
            if(value_path == "delay-protection"):
                self.delay_protection = value
                self.delay_protection.value_namespace = name_space
                self.delay_protection.value_namespace_prefix = name_space_prefix
            if(value_path == "include-icv-indicator"):
                self.include_icv_indicator = value
                self.include_icv_indicator.value_namespace = name_space
                self.include_icv_indicator.value_namespace_prefix = name_space_prefix
            if(value_path == "key-server-priority"):
                self.key_server_priority = value
                self.key_server_priority.value_namespace = name_space
                self.key_server_priority.value_namespace_prefix = name_space_prefix
            if(value_path == "policy-exception"):
                self.policy_exception = value
                self.policy_exception.value_namespace = name_space
                self.policy_exception.value_namespace_prefix = name_space_prefix
            if(value_path == "sak-rekey-interval"):
                self.sak_rekey_interval = value
                self.sak_rekey_interval.value_namespace = name_space
                self.sak_rekey_interval.value_namespace_prefix = name_space_prefix
            if(value_path == "security-policy"):
                self.security_policy = value
                self.security_policy.value_namespace = name_space
                self.security_policy.value_namespace_prefix = name_space_prefix
            if(value_path == "vlan-tags-in-clear"):
                self.vlan_tags_in_clear = value
                self.vlan_tags_in_clear.value_namespace = name_space
                self.vlan_tags_in_clear.value_namespace_prefix = name_space_prefix
            if(value_path == "window-size"):
                self.window_size = value
                self.window_size.value_namespace = name_space
                self.window_size.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.policy:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.policy:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-macsec-mka-cfg:macsec" + path_buffer

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

        if (child_yang_name == "policy"):
            for c in self.policy:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Macsec.Policy()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.policy.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "policy"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Macsec()
        return self._top_entity


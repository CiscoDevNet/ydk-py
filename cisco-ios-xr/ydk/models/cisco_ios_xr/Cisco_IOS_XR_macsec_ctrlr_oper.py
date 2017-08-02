""" Cisco_IOS_XR_macsec_ctrlr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR macsec\-ctrlr package operational data.

This module contains definitions
for the following management objects\:
  macsec\-ctrlr\-oper\: Macsec controller data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MacsecCtrlrCiphersuit(Enum):
    """
    MacsecCtrlrCiphersuit

    Macsec ctrlr ciphersuit

    .. data:: gcm_aes_256 = 0

    	GCM AES 256

    .. data:: gcm_aes_128 = 1

    	GCM AES 128

    .. data:: gcm_aes_xpn_256 = 2

    	GCM AES XPN 256

    """

    gcm_aes_256 = Enum.YLeaf(0, "gcm-aes-256")

    gcm_aes_128 = Enum.YLeaf(1, "gcm-aes-128")

    gcm_aes_xpn_256 = Enum.YLeaf(2, "gcm-aes-xpn-256")


class MacsecCtrlrState(Enum):
    """
    MacsecCtrlrState

    Macsec ctrlr state

    .. data:: macsec_ctrlr_state_up = 0

    	Up

    .. data:: macsec_ctrlr_state_down = 1

    	Down

    .. data:: macsec_ctrlr_state_admin_down = 2

    	Administratively Down

    """

    macsec_ctrlr_state_up = Enum.YLeaf(0, "macsec-ctrlr-state-up")

    macsec_ctrlr_state_down = Enum.YLeaf(1, "macsec-ctrlr-state-down")

    macsec_ctrlr_state_admin_down = Enum.YLeaf(2, "macsec-ctrlr-state-admin-down")



class MacsecCtrlrOper(Entity):
    """
    Macsec controller data
    
    .. attribute:: macsec_ctrlr_ports
    
    	All Macsec Controller Port operational data
    	**type**\:   :py:class:`MacsecCtrlrPorts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts>`
    
    

    """

    _prefix = 'macsec-ctrlr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(MacsecCtrlrOper, self).__init__()
        self._top_entity = None

        self.yang_name = "macsec-ctrlr-oper"
        self.yang_parent_name = "Cisco-IOS-XR-macsec-ctrlr-oper"

        self.macsec_ctrlr_ports = MacsecCtrlrOper.MacsecCtrlrPorts()
        self.macsec_ctrlr_ports.parent = self
        self._children_name_map["macsec_ctrlr_ports"] = "macsec-ctrlr-ports"
        self._children_yang_names.add("macsec-ctrlr-ports")


    class MacsecCtrlrPorts(Entity):
        """
        All Macsec Controller Port operational data
        
        .. attribute:: macsec_ctrlr_port
        
        	Controller name
        	**type**\: list of    :py:class:`MacsecCtrlrPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort>`
        
        

        """

        _prefix = 'macsec-ctrlr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MacsecCtrlrOper.MacsecCtrlrPorts, self).__init__()

            self.yang_name = "macsec-ctrlr-ports"
            self.yang_parent_name = "macsec-ctrlr-oper"

            self.macsec_ctrlr_port = YList(self)

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
                        super(MacsecCtrlrOper.MacsecCtrlrPorts, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MacsecCtrlrOper.MacsecCtrlrPorts, self).__setattr__(name, value)


        class MacsecCtrlrPort(Entity):
            """
            Controller name
            
            .. attribute:: name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: macsec_ctrlr_info
            
            	Macsec Controller operational data
            	**type**\:   :py:class:`MacsecCtrlrInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo>`
            
            

            """

            _prefix = 'macsec-ctrlr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort, self).__init__()

                self.yang_name = "macsec-ctrlr-port"
                self.yang_parent_name = "macsec-ctrlr-ports"

                self.name = YLeaf(YType.str, "name")

                self.macsec_ctrlr_info = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo()
                self.macsec_ctrlr_info.parent = self
                self._children_name_map["macsec_ctrlr_info"] = "macsec-ctrlr-info"
                self._children_yang_names.add("macsec-ctrlr-info")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort, self).__setattr__(name, value)


            class MacsecCtrlrInfo(Entity):
                """
                Macsec Controller operational data
                
                .. attribute:: decrypt_sc_status
                
                	Decrypt Secure Channel Status
                	**type**\:   :py:class:`DecryptScStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus>`
                
                .. attribute:: encrypt_sc_status
                
                	Encrypt Secure Channel Status
                	**type**\:   :py:class:`EncryptScStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus>`
                
                .. attribute:: must_secure
                
                	Must Secure
                	**type**\:  bool
                
                .. attribute:: replay_window_size
                
                	Replay Window Size
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: secure_mode
                
                	Secure Mode
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state
                
                	State
                	**type**\:   :py:class:`MacsecCtrlrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrState>`
                
                

                """

                _prefix = 'macsec-ctrlr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo, self).__init__()

                    self.yang_name = "macsec-ctrlr-info"
                    self.yang_parent_name = "macsec-ctrlr-port"

                    self.must_secure = YLeaf(YType.boolean, "must-secure")

                    self.replay_window_size = YLeaf(YType.uint32, "replay-window-size")

                    self.secure_mode = YLeaf(YType.uint32, "secure-mode")

                    self.state = YLeaf(YType.enumeration, "state")

                    self.decrypt_sc_status = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus()
                    self.decrypt_sc_status.parent = self
                    self._children_name_map["decrypt_sc_status"] = "decrypt-sc-status"
                    self._children_yang_names.add("decrypt-sc-status")

                    self.encrypt_sc_status = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus()
                    self.encrypt_sc_status.parent = self
                    self._children_name_map["encrypt_sc_status"] = "encrypt-sc-status"
                    self._children_yang_names.add("encrypt-sc-status")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("must_secure",
                                    "replay_window_size",
                                    "secure_mode",
                                    "state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo, self).__setattr__(name, value)


                class EncryptScStatus(Entity):
                    """
                    Encrypt Secure Channel Status
                    
                    .. attribute:: active_association
                    
                    	Active Associations
                    	**type**\: list of    :py:class:`ActiveAssociation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation>`
                    
                    .. attribute:: cipher_suite
                    
                    	Cipher Suite
                    	**type**\:   :py:class:`MacsecCtrlrCiphersuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrCiphersuit>`
                    
                    .. attribute:: confidentiality_offset
                    
                    	Confidentiality offset
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_packet_number
                    
                    	Max packet Number
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: protection_enabled
                    
                    	Protection Enabled
                    	**type**\:  bool
                    
                    .. attribute:: recent_packet_number
                    
                    	Recent Packet Number
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: secure_channel_id
                    
                    	Secure Channel Id
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'macsec-ctrlr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus, self).__init__()

                        self.yang_name = "encrypt-sc-status"
                        self.yang_parent_name = "macsec-ctrlr-info"

                        self.cipher_suite = YLeaf(YType.enumeration, "cipher-suite")

                        self.confidentiality_offset = YLeaf(YType.uint32, "confidentiality-offset")

                        self.max_packet_number = YLeaf(YType.uint64, "max-packet-number")

                        self.protection_enabled = YLeaf(YType.boolean, "protection-enabled")

                        self.recent_packet_number = YLeaf(YType.uint64, "recent-packet-number")

                        self.secure_channel_id = YLeaf(YType.str, "secure-channel-id")

                        self.active_association = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("cipher_suite",
                                        "confidentiality_offset",
                                        "max_packet_number",
                                        "protection_enabled",
                                        "recent_packet_number",
                                        "secure_channel_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus, self).__setattr__(name, value)


                    class ActiveAssociation(Entity):
                        """
                        Active Associations
                        
                        .. attribute:: association_number
                        
                        	Association Number
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: short_secure_channel_id
                        
                        	Short secure channel id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'macsec-ctrlr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation, self).__init__()

                            self.yang_name = "active-association"
                            self.yang_parent_name = "encrypt-sc-status"

                            self.association_number = YLeaf(YType.uint8, "association-number")

                            self.short_secure_channel_id = YLeaf(YType.uint32, "short-secure-channel-id")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("association_number",
                                            "short_secure_channel_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.association_number.is_set or
                                self.short_secure_channel_id.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.association_number.yfilter != YFilter.not_set or
                                self.short_secure_channel_id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "active-association" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.association_number.is_set or self.association_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.association_number.get_name_leafdata())
                            if (self.short_secure_channel_id.is_set or self.short_secure_channel_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.short_secure_channel_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "association-number" or name == "short-secure-channel-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "association-number"):
                                self.association_number = value
                                self.association_number.value_namespace = name_space
                                self.association_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "short-secure-channel-id"):
                                self.short_secure_channel_id = value
                                self.short_secure_channel_id.value_namespace = name_space
                                self.short_secure_channel_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.active_association:
                            if (c.has_data()):
                                return True
                        return (
                            self.cipher_suite.is_set or
                            self.confidentiality_offset.is_set or
                            self.max_packet_number.is_set or
                            self.protection_enabled.is_set or
                            self.recent_packet_number.is_set or
                            self.secure_channel_id.is_set)

                    def has_operation(self):
                        for c in self.active_association:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.cipher_suite.yfilter != YFilter.not_set or
                            self.confidentiality_offset.yfilter != YFilter.not_set or
                            self.max_packet_number.yfilter != YFilter.not_set or
                            self.protection_enabled.yfilter != YFilter.not_set or
                            self.recent_packet_number.yfilter != YFilter.not_set or
                            self.secure_channel_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "encrypt-sc-status" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.cipher_suite.is_set or self.cipher_suite.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cipher_suite.get_name_leafdata())
                        if (self.confidentiality_offset.is_set or self.confidentiality_offset.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.confidentiality_offset.get_name_leafdata())
                        if (self.max_packet_number.is_set or self.max_packet_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_packet_number.get_name_leafdata())
                        if (self.protection_enabled.is_set or self.protection_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protection_enabled.get_name_leafdata())
                        if (self.recent_packet_number.is_set or self.recent_packet_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.recent_packet_number.get_name_leafdata())
                        if (self.secure_channel_id.is_set or self.secure_channel_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.secure_channel_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "active-association"):
                            for c in self.active_association:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.active_association.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "active-association" or name == "cipher-suite" or name == "confidentiality-offset" or name == "max-packet-number" or name == "protection-enabled" or name == "recent-packet-number" or name == "secure-channel-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "cipher-suite"):
                            self.cipher_suite = value
                            self.cipher_suite.value_namespace = name_space
                            self.cipher_suite.value_namespace_prefix = name_space_prefix
                        if(value_path == "confidentiality-offset"):
                            self.confidentiality_offset = value
                            self.confidentiality_offset.value_namespace = name_space
                            self.confidentiality_offset.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-packet-number"):
                            self.max_packet_number = value
                            self.max_packet_number.value_namespace = name_space
                            self.max_packet_number.value_namespace_prefix = name_space_prefix
                        if(value_path == "protection-enabled"):
                            self.protection_enabled = value
                            self.protection_enabled.value_namespace = name_space
                            self.protection_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "recent-packet-number"):
                            self.recent_packet_number = value
                            self.recent_packet_number.value_namespace = name_space
                            self.recent_packet_number.value_namespace_prefix = name_space_prefix
                        if(value_path == "secure-channel-id"):
                            self.secure_channel_id = value
                            self.secure_channel_id.value_namespace = name_space
                            self.secure_channel_id.value_namespace_prefix = name_space_prefix


                class DecryptScStatus(Entity):
                    """
                    Decrypt Secure Channel Status
                    
                    .. attribute:: active_association
                    
                    	Active Associations
                    	**type**\: list of    :py:class:`ActiveAssociation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation>`
                    
                    .. attribute:: cipher_suite
                    
                    	Cipher Suite
                    	**type**\:   :py:class:`MacsecCtrlrCiphersuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrCiphersuit>`
                    
                    .. attribute:: confidentiality_offset
                    
                    	Confidentiality offset
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_packet_number
                    
                    	Max packet Number
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: protection_enabled
                    
                    	Protection Enabled
                    	**type**\:  bool
                    
                    .. attribute:: recent_packet_number
                    
                    	Recent Packet Number
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: secure_channel_id
                    
                    	Secure Channel Id
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'macsec-ctrlr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus, self).__init__()

                        self.yang_name = "decrypt-sc-status"
                        self.yang_parent_name = "macsec-ctrlr-info"

                        self.cipher_suite = YLeaf(YType.enumeration, "cipher-suite")

                        self.confidentiality_offset = YLeaf(YType.uint32, "confidentiality-offset")

                        self.max_packet_number = YLeaf(YType.uint64, "max-packet-number")

                        self.protection_enabled = YLeaf(YType.boolean, "protection-enabled")

                        self.recent_packet_number = YLeaf(YType.uint64, "recent-packet-number")

                        self.secure_channel_id = YLeaf(YType.str, "secure-channel-id")

                        self.active_association = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("cipher_suite",
                                        "confidentiality_offset",
                                        "max_packet_number",
                                        "protection_enabled",
                                        "recent_packet_number",
                                        "secure_channel_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus, self).__setattr__(name, value)


                    class ActiveAssociation(Entity):
                        """
                        Active Associations
                        
                        .. attribute:: association_number
                        
                        	Association Number
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: short_secure_channel_id
                        
                        	Short secure channel id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'macsec-ctrlr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation, self).__init__()

                            self.yang_name = "active-association"
                            self.yang_parent_name = "decrypt-sc-status"

                            self.association_number = YLeaf(YType.uint8, "association-number")

                            self.short_secure_channel_id = YLeaf(YType.uint32, "short-secure-channel-id")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("association_number",
                                            "short_secure_channel_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.association_number.is_set or
                                self.short_secure_channel_id.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.association_number.yfilter != YFilter.not_set or
                                self.short_secure_channel_id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "active-association" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.association_number.is_set or self.association_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.association_number.get_name_leafdata())
                            if (self.short_secure_channel_id.is_set or self.short_secure_channel_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.short_secure_channel_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "association-number" or name == "short-secure-channel-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "association-number"):
                                self.association_number = value
                                self.association_number.value_namespace = name_space
                                self.association_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "short-secure-channel-id"):
                                self.short_secure_channel_id = value
                                self.short_secure_channel_id.value_namespace = name_space
                                self.short_secure_channel_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.active_association:
                            if (c.has_data()):
                                return True
                        return (
                            self.cipher_suite.is_set or
                            self.confidentiality_offset.is_set or
                            self.max_packet_number.is_set or
                            self.protection_enabled.is_set or
                            self.recent_packet_number.is_set or
                            self.secure_channel_id.is_set)

                    def has_operation(self):
                        for c in self.active_association:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.cipher_suite.yfilter != YFilter.not_set or
                            self.confidentiality_offset.yfilter != YFilter.not_set or
                            self.max_packet_number.yfilter != YFilter.not_set or
                            self.protection_enabled.yfilter != YFilter.not_set or
                            self.recent_packet_number.yfilter != YFilter.not_set or
                            self.secure_channel_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "decrypt-sc-status" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.cipher_suite.is_set or self.cipher_suite.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cipher_suite.get_name_leafdata())
                        if (self.confidentiality_offset.is_set or self.confidentiality_offset.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.confidentiality_offset.get_name_leafdata())
                        if (self.max_packet_number.is_set or self.max_packet_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_packet_number.get_name_leafdata())
                        if (self.protection_enabled.is_set or self.protection_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protection_enabled.get_name_leafdata())
                        if (self.recent_packet_number.is_set or self.recent_packet_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.recent_packet_number.get_name_leafdata())
                        if (self.secure_channel_id.is_set or self.secure_channel_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.secure_channel_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "active-association"):
                            for c in self.active_association:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.active_association.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "active-association" or name == "cipher-suite" or name == "confidentiality-offset" or name == "max-packet-number" or name == "protection-enabled" or name == "recent-packet-number" or name == "secure-channel-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "cipher-suite"):
                            self.cipher_suite = value
                            self.cipher_suite.value_namespace = name_space
                            self.cipher_suite.value_namespace_prefix = name_space_prefix
                        if(value_path == "confidentiality-offset"):
                            self.confidentiality_offset = value
                            self.confidentiality_offset.value_namespace = name_space
                            self.confidentiality_offset.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-packet-number"):
                            self.max_packet_number = value
                            self.max_packet_number.value_namespace = name_space
                            self.max_packet_number.value_namespace_prefix = name_space_prefix
                        if(value_path == "protection-enabled"):
                            self.protection_enabled = value
                            self.protection_enabled.value_namespace = name_space
                            self.protection_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "recent-packet-number"):
                            self.recent_packet_number = value
                            self.recent_packet_number.value_namespace = name_space
                            self.recent_packet_number.value_namespace_prefix = name_space_prefix
                        if(value_path == "secure-channel-id"):
                            self.secure_channel_id = value
                            self.secure_channel_id.value_namespace = name_space
                            self.secure_channel_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.must_secure.is_set or
                        self.replay_window_size.is_set or
                        self.secure_mode.is_set or
                        self.state.is_set or
                        (self.decrypt_sc_status is not None and self.decrypt_sc_status.has_data()) or
                        (self.encrypt_sc_status is not None and self.encrypt_sc_status.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.must_secure.yfilter != YFilter.not_set or
                        self.replay_window_size.yfilter != YFilter.not_set or
                        self.secure_mode.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set or
                        (self.decrypt_sc_status is not None and self.decrypt_sc_status.has_operation()) or
                        (self.encrypt_sc_status is not None and self.encrypt_sc_status.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "macsec-ctrlr-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.must_secure.is_set or self.must_secure.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.must_secure.get_name_leafdata())
                    if (self.replay_window_size.is_set or self.replay_window_size.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.replay_window_size.get_name_leafdata())
                    if (self.secure_mode.is_set or self.secure_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.secure_mode.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "decrypt-sc-status"):
                        if (self.decrypt_sc_status is None):
                            self.decrypt_sc_status = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus()
                            self.decrypt_sc_status.parent = self
                            self._children_name_map["decrypt_sc_status"] = "decrypt-sc-status"
                        return self.decrypt_sc_status

                    if (child_yang_name == "encrypt-sc-status"):
                        if (self.encrypt_sc_status is None):
                            self.encrypt_sc_status = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus()
                            self.encrypt_sc_status.parent = self
                            self._children_name_map["encrypt_sc_status"] = "encrypt-sc-status"
                        return self.encrypt_sc_status

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "decrypt-sc-status" or name == "encrypt-sc-status" or name == "must-secure" or name == "replay-window-size" or name == "secure-mode" or name == "state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "must-secure"):
                        self.must_secure = value
                        self.must_secure.value_namespace = name_space
                        self.must_secure.value_namespace_prefix = name_space_prefix
                    if(value_path == "replay-window-size"):
                        self.replay_window_size = value
                        self.replay_window_size.value_namespace = name_space
                        self.replay_window_size.value_namespace_prefix = name_space_prefix
                    if(value_path == "secure-mode"):
                        self.secure_mode = value
                        self.secure_mode.value_namespace = name_space
                        self.secure_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.name.is_set or
                    (self.macsec_ctrlr_info is not None and self.macsec_ctrlr_info.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    (self.macsec_ctrlr_info is not None and self.macsec_ctrlr_info.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "macsec-ctrlr-port" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-oper/macsec-ctrlr-ports/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "macsec-ctrlr-info"):
                    if (self.macsec_ctrlr_info is None):
                        self.macsec_ctrlr_info = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo()
                        self.macsec_ctrlr_info.parent = self
                        self._children_name_map["macsec_ctrlr_info"] = "macsec-ctrlr-info"
                    return self.macsec_ctrlr_info

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "macsec-ctrlr-info" or name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.macsec_ctrlr_port:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.macsec_ctrlr_port:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "macsec-ctrlr-ports" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-oper/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "macsec-ctrlr-port"):
                for c in self.macsec_ctrlr_port:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.macsec_ctrlr_port.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "macsec-ctrlr-port"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.macsec_ctrlr_ports is not None and self.macsec_ctrlr_ports.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.macsec_ctrlr_ports is not None and self.macsec_ctrlr_ports.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-oper" + path_buffer

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

        if (child_yang_name == "macsec-ctrlr-ports"):
            if (self.macsec_ctrlr_ports is None):
                self.macsec_ctrlr_ports = MacsecCtrlrOper.MacsecCtrlrPorts()
                self.macsec_ctrlr_ports.parent = self
                self._children_name_map["macsec_ctrlr_ports"] = "macsec-ctrlr-ports"
            return self.macsec_ctrlr_ports

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "macsec-ctrlr-ports"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MacsecCtrlrOper()
        return self._top_entity


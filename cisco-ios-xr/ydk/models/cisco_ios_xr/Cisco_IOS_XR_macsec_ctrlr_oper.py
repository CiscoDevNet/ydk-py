""" Cisco_IOS_XR_macsec_ctrlr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR macsec\-ctrlr package operational data.

This module contains definitions
for the following management objects\:
  macsec\-ctrlr\-oper\: Macsec controller data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"macsec-ctrlr-ports" : ("macsec_ctrlr_ports", MacsecCtrlrOper.MacsecCtrlrPorts)}
        self._child_list_classes = {}

        self.macsec_ctrlr_ports = MacsecCtrlrOper.MacsecCtrlrPorts()
        self.macsec_ctrlr_ports.parent = self
        self._children_name_map["macsec_ctrlr_ports"] = "macsec-ctrlr-ports"
        self._children_yang_names.add("macsec-ctrlr-ports")
        self._segment_path = lambda: "Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-oper"


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"macsec-ctrlr-port" : ("macsec_ctrlr_port", MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort)}

            self.macsec_ctrlr_port = YList(self)
            self._segment_path = lambda: "macsec-ctrlr-ports"
            self._absolute_path = lambda: "Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-oper/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MacsecCtrlrOper.MacsecCtrlrPorts, [], name, value)


        class MacsecCtrlrPort(Entity):
            """
            Controller name
            
            .. attribute:: name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"macsec-ctrlr-info" : ("macsec_ctrlr_info", MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo)}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.macsec_ctrlr_info = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo()
                self.macsec_ctrlr_info.parent = self
                self._children_name_map["macsec_ctrlr_info"] = "macsec-ctrlr-info"
                self._children_yang_names.add("macsec-ctrlr-info")
                self._segment_path = lambda: "macsec-ctrlr-port" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-oper/macsec-ctrlr-ports/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort, ['name'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"decrypt-sc-status" : ("decrypt_sc_status", MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus), "encrypt-sc-status" : ("encrypt_sc_status", MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus)}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "macsec-ctrlr-info"

                def __setattr__(self, name, value):
                    self._perform_setattr(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo, ['must_secure', 'replay_window_size', 'secure_mode', 'state'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"active-association" : ("active_association", MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation)}

                        self.cipher_suite = YLeaf(YType.enumeration, "cipher-suite")

                        self.confidentiality_offset = YLeaf(YType.uint32, "confidentiality-offset")

                        self.max_packet_number = YLeaf(YType.uint64, "max-packet-number")

                        self.protection_enabled = YLeaf(YType.boolean, "protection-enabled")

                        self.recent_packet_number = YLeaf(YType.uint64, "recent-packet-number")

                        self.secure_channel_id = YLeaf(YType.str, "secure-channel-id")

                        self.active_association = YList(self)
                        self._segment_path = lambda: "decrypt-sc-status"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus, ['cipher_suite', 'confidentiality_offset', 'max_packet_number', 'protection_enabled', 'recent_packet_number', 'secure_channel_id'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.association_number = YLeaf(YType.uint8, "association-number")

                            self.short_secure_channel_id = YLeaf(YType.uint32, "short-secure-channel-id")
                            self._segment_path = lambda: "active-association"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation, ['association_number', 'short_secure_channel_id'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"active-association" : ("active_association", MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation)}

                        self.cipher_suite = YLeaf(YType.enumeration, "cipher-suite")

                        self.confidentiality_offset = YLeaf(YType.uint32, "confidentiality-offset")

                        self.max_packet_number = YLeaf(YType.uint64, "max-packet-number")

                        self.protection_enabled = YLeaf(YType.boolean, "protection-enabled")

                        self.recent_packet_number = YLeaf(YType.uint64, "recent-packet-number")

                        self.secure_channel_id = YLeaf(YType.str, "secure-channel-id")

                        self.active_association = YList(self)
                        self._segment_path = lambda: "encrypt-sc-status"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus, ['cipher_suite', 'confidentiality_offset', 'max_packet_number', 'protection_enabled', 'recent_packet_number', 'secure_channel_id'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.association_number = YLeaf(YType.uint8, "association-number")

                            self.short_secure_channel_id = YLeaf(YType.uint32, "short-secure-channel-id")
                            self._segment_path = lambda: "active-association"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation, ['association_number', 'short_secure_channel_id'], name, value)

    def clone_ptr(self):
        self._top_entity = MacsecCtrlrOper()
        return self._top_entity


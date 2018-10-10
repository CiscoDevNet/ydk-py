""" Cisco_IOS_XR_macsec_ctrlr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR macsec\-ctrlr package operational data.

This module contains definitions
for the following management objects\:
  macsec\-ctrlr\-oper\: Macsec controller data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MacsecCtrlrCiphersuit(Enum):
    """
    MacsecCtrlrCiphersuit (Enum Class)

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
    MacsecCtrlrState (Enum Class)

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
    	**type**\:  :py:class:`MacsecCtrlrPorts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts>`
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("macsec-ctrlr-ports", ("macsec_ctrlr_ports", MacsecCtrlrOper.MacsecCtrlrPorts))])
        self._leafs = OrderedDict()

        self.macsec_ctrlr_ports = MacsecCtrlrOper.MacsecCtrlrPorts()
        self.macsec_ctrlr_ports.parent = self
        self._children_name_map["macsec_ctrlr_ports"] = "macsec-ctrlr-ports"
        self._segment_path = lambda: "Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-oper"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MacsecCtrlrOper, [], name, value)


    class MacsecCtrlrPorts(Entity):
        """
        All Macsec Controller Port operational data
        
        .. attribute:: macsec_ctrlr_port
        
        	Controller name
        	**type**\: list of  		 :py:class:`MacsecCtrlrPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort>`
        
        

        """

        _prefix = 'macsec-ctrlr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MacsecCtrlrOper.MacsecCtrlrPorts, self).__init__()

            self.yang_name = "macsec-ctrlr-ports"
            self.yang_parent_name = "macsec-ctrlr-oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("macsec-ctrlr-port", ("macsec_ctrlr_port", MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort))])
            self._leafs = OrderedDict()

            self.macsec_ctrlr_port = YList(self)
            self._segment_path = lambda: "macsec-ctrlr-ports"
            self._absolute_path = lambda: "Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-oper/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MacsecCtrlrOper.MacsecCtrlrPorts, [], name, value)


        class MacsecCtrlrPort(Entity):
            """
            Controller name
            
            .. attribute:: name  (key)
            
            	Port name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: macsec_ctrlr_info
            
            	Macsec Controller operational data
            	**type**\:  :py:class:`MacsecCtrlrInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo>`
            
            

            """

            _prefix = 'macsec-ctrlr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort, self).__init__()

                self.yang_name = "macsec-ctrlr-port"
                self.yang_parent_name = "macsec-ctrlr-ports"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("macsec-ctrlr-info", ("macsec_ctrlr_info", MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.macsec_ctrlr_info = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo()
                self.macsec_ctrlr_info.parent = self
                self._children_name_map["macsec_ctrlr_info"] = "macsec-ctrlr-info"
                self._segment_path = lambda: "macsec-ctrlr-port" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-oper/macsec-ctrlr-ports/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort, ['name'], name, value)


            class MacsecCtrlrInfo(Entity):
                """
                Macsec Controller operational data
                
                .. attribute:: encrypt_sc_status
                
                	Encrypt Secure Channel Status
                	**type**\:  :py:class:`EncryptScStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus>`
                
                .. attribute:: decrypt_sc_status
                
                	Decrypt Secure Channel Status
                	**type**\:  :py:class:`DecryptScStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus>`
                
                .. attribute:: state
                
                	State
                	**type**\:  :py:class:`MacsecCtrlrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrState>`
                
                .. attribute:: replay_window_size
                
                	Replay Window Size
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: must_secure
                
                	Must Secure
                	**type**\: bool
                
                .. attribute:: secure_mode
                
                	Secure Mode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'macsec-ctrlr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo, self).__init__()

                    self.yang_name = "macsec-ctrlr-info"
                    self.yang_parent_name = "macsec-ctrlr-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("encrypt-sc-status", ("encrypt_sc_status", MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus)), ("decrypt-sc-status", ("decrypt_sc_status", MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus))])
                    self._leafs = OrderedDict([
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper', 'MacsecCtrlrState', '')])),
                        ('replay_window_size', (YLeaf(YType.uint32, 'replay-window-size'), ['int'])),
                        ('must_secure', (YLeaf(YType.boolean, 'must-secure'), ['bool'])),
                        ('secure_mode', (YLeaf(YType.uint32, 'secure-mode'), ['int'])),
                    ])
                    self.state = None
                    self.replay_window_size = None
                    self.must_secure = None
                    self.secure_mode = None

                    self.encrypt_sc_status = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus()
                    self.encrypt_sc_status.parent = self
                    self._children_name_map["encrypt_sc_status"] = "encrypt-sc-status"

                    self.decrypt_sc_status = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus()
                    self.decrypt_sc_status.parent = self
                    self._children_name_map["decrypt_sc_status"] = "decrypt-sc-status"
                    self._segment_path = lambda: "macsec-ctrlr-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo, [u'state', u'replay_window_size', u'must_secure', u'secure_mode'], name, value)


                class EncryptScStatus(Entity):
                    """
                    Encrypt Secure Channel Status
                    
                    .. attribute:: protection_enabled
                    
                    	Protection Enabled
                    	**type**\: bool
                    
                    .. attribute:: secure_channel_id
                    
                    	Secure Channel Id
                    	**type**\: str
                    
                    .. attribute:: confidentiality_offset
                    
                    	Confidentiality offset
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cipher_suite
                    
                    	Cipher Suite
                    	**type**\:  :py:class:`MacsecCtrlrCiphersuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrCiphersuit>`
                    
                    .. attribute:: max_packet_number
                    
                    	Max packet Number
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: recent_packet_number
                    
                    	Recent Packet Number
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: active_association
                    
                    	Active Associations
                    	**type**\: list of  		 :py:class:`ActiveAssociation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation>`
                    
                    

                    """

                    _prefix = 'macsec-ctrlr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus, self).__init__()

                        self.yang_name = "encrypt-sc-status"
                        self.yang_parent_name = "macsec-ctrlr-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("active-association", ("active_association", MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation))])
                        self._leafs = OrderedDict([
                            ('protection_enabled', (YLeaf(YType.boolean, 'protection-enabled'), ['bool'])),
                            ('secure_channel_id', (YLeaf(YType.str, 'secure-channel-id'), ['str'])),
                            ('confidentiality_offset', (YLeaf(YType.uint32, 'confidentiality-offset'), ['int'])),
                            ('cipher_suite', (YLeaf(YType.enumeration, 'cipher-suite'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper', 'MacsecCtrlrCiphersuit', '')])),
                            ('max_packet_number', (YLeaf(YType.uint64, 'max-packet-number'), ['int'])),
                            ('recent_packet_number', (YLeaf(YType.uint64, 'recent-packet-number'), ['int'])),
                        ])
                        self.protection_enabled = None
                        self.secure_channel_id = None
                        self.confidentiality_offset = None
                        self.cipher_suite = None
                        self.max_packet_number = None
                        self.recent_packet_number = None

                        self.active_association = YList(self)
                        self._segment_path = lambda: "encrypt-sc-status"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus, [u'protection_enabled', u'secure_channel_id', u'confidentiality_offset', u'cipher_suite', u'max_packet_number', u'recent_packet_number'], name, value)


                    class ActiveAssociation(Entity):
                        """
                        Active Associations
                        
                        .. attribute:: association_number
                        
                        	Association Number
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: short_secure_channel_id
                        
                        	Short secure channel id
                        	**type**\: int
                        
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
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('association_number', (YLeaf(YType.uint8, 'association-number'), ['int'])),
                                ('short_secure_channel_id', (YLeaf(YType.uint32, 'short-secure-channel-id'), ['int'])),
                            ])
                            self.association_number = None
                            self.short_secure_channel_id = None
                            self._segment_path = lambda: "active-association"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation, [u'association_number', u'short_secure_channel_id'], name, value)


                class DecryptScStatus(Entity):
                    """
                    Decrypt Secure Channel Status
                    
                    .. attribute:: protection_enabled
                    
                    	Protection Enabled
                    	**type**\: bool
                    
                    .. attribute:: secure_channel_id
                    
                    	Secure Channel Id
                    	**type**\: str
                    
                    .. attribute:: confidentiality_offset
                    
                    	Confidentiality offset
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cipher_suite
                    
                    	Cipher Suite
                    	**type**\:  :py:class:`MacsecCtrlrCiphersuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrCiphersuit>`
                    
                    .. attribute:: max_packet_number
                    
                    	Max packet Number
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: recent_packet_number
                    
                    	Recent Packet Number
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: active_association
                    
                    	Active Associations
                    	**type**\: list of  		 :py:class:`ActiveAssociation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation>`
                    
                    

                    """

                    _prefix = 'macsec-ctrlr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus, self).__init__()

                        self.yang_name = "decrypt-sc-status"
                        self.yang_parent_name = "macsec-ctrlr-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("active-association", ("active_association", MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation))])
                        self._leafs = OrderedDict([
                            ('protection_enabled', (YLeaf(YType.boolean, 'protection-enabled'), ['bool'])),
                            ('secure_channel_id', (YLeaf(YType.str, 'secure-channel-id'), ['str'])),
                            ('confidentiality_offset', (YLeaf(YType.uint32, 'confidentiality-offset'), ['int'])),
                            ('cipher_suite', (YLeaf(YType.enumeration, 'cipher-suite'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper', 'MacsecCtrlrCiphersuit', '')])),
                            ('max_packet_number', (YLeaf(YType.uint64, 'max-packet-number'), ['int'])),
                            ('recent_packet_number', (YLeaf(YType.uint64, 'recent-packet-number'), ['int'])),
                        ])
                        self.protection_enabled = None
                        self.secure_channel_id = None
                        self.confidentiality_offset = None
                        self.cipher_suite = None
                        self.max_packet_number = None
                        self.recent_packet_number = None

                        self.active_association = YList(self)
                        self._segment_path = lambda: "decrypt-sc-status"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus, [u'protection_enabled', u'secure_channel_id', u'confidentiality_offset', u'cipher_suite', u'max_packet_number', u'recent_packet_number'], name, value)


                    class ActiveAssociation(Entity):
                        """
                        Active Associations
                        
                        .. attribute:: association_number
                        
                        	Association Number
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: short_secure_channel_id
                        
                        	Short secure channel id
                        	**type**\: int
                        
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
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('association_number', (YLeaf(YType.uint8, 'association-number'), ['int'])),
                                ('short_secure_channel_id', (YLeaf(YType.uint32, 'short-secure-channel-id'), ['int'])),
                            ])
                            self.association_number = None
                            self.short_secure_channel_id = None
                            self._segment_path = lambda: "active-association"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation, [u'association_number', u'short_secure_channel_id'], name, value)

    def clone_ptr(self):
        self._top_entity = MacsecCtrlrOper()
        return self._top_entity


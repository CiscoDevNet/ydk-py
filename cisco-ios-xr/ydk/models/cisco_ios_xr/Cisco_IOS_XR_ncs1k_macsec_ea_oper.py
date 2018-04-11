""" Cisco_IOS_XR_ncs1k_macsec_ea_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-macsec\-ea package operational data.

This module contains definitions
for the following management objects\:
  ncs1k\-macsec\-oper\: Macsec data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ncs1kCipherSuit(Enum):
    """
    Ncs1kCipherSuit (Enum Class)

    Ncs1k cipher suit

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



class Ncs1KMacsecOper(Entity):
    """
    Macsec data
    
    .. attribute:: ncs1k_macsec_ctrlr_names
    
    	All Macsec operational data
    	**type**\:  :py:class:`Ncs1KMacsecCtrlrNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames>`
    
    

    """

    _prefix = 'ncs1k-macsec-ea-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ncs1KMacsecOper, self).__init__()
        self._top_entity = None

        self.yang_name = "ncs1k-macsec-oper"
        self.yang_parent_name = "Cisco-IOS-XR-ncs1k-macsec-ea-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ncs1k-macsec-ctrlr-names", ("ncs1k_macsec_ctrlr_names", Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ncs1k_macsec_ctrlr_names = Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames()
        self.ncs1k_macsec_ctrlr_names.parent = self
        self._children_name_map["ncs1k_macsec_ctrlr_names"] = "ncs1k-macsec-ctrlr-names"
        self._children_yang_names.add("ncs1k-macsec-ctrlr-names")
        self._segment_path = lambda: "Cisco-IOS-XR-ncs1k-macsec-ea-oper:ncs1k-macsec-oper"


    class Ncs1KMacsecCtrlrNames(Entity):
        """
        All Macsec operational data
        
        .. attribute:: ncs1k_macsec_ctrlr_name
        
        	Interface name
        	**type**\: list of  		 :py:class:`Ncs1KMacsecCtrlrName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName>`
        
        

        """

        _prefix = 'ncs1k-macsec-ea-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames, self).__init__()

            self.yang_name = "ncs1k-macsec-ctrlr-names"
            self.yang_parent_name = "ncs1k-macsec-oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ncs1k-macsec-ctrlr-name", ("ncs1k_macsec_ctrlr_name", Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName))])
            self._leafs = OrderedDict()

            self.ncs1k_macsec_ctrlr_name = YList(self)
            self._segment_path = lambda: "ncs1k-macsec-ctrlr-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-macsec-ea-oper:ncs1k-macsec-oper/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames, [], name, value)


        class Ncs1KMacsecCtrlrName(Entity):
            """
            Interface name
            
            .. attribute:: name  (key)
            
            	Port name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: ncs1k_status_info
            
            	controller data
            	**type**\:  :py:class:`Ncs1KStatusInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo>`
            
            

            """

            _prefix = 'ncs1k-macsec-ea-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName, self).__init__()

                self.yang_name = "ncs1k-macsec-ctrlr-name"
                self.yang_parent_name = "ncs1k-macsec-ctrlr-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_container_classes = OrderedDict([("ncs1k-status-info", ("ncs1k_status_info", Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                ])
                self.name = None

                self.ncs1k_status_info = Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo()
                self.ncs1k_status_info.parent = self
                self._children_name_map["ncs1k_status_info"] = "ncs1k-status-info"
                self._children_yang_names.add("ncs1k-status-info")
                self._segment_path = lambda: "ncs1k-macsec-ctrlr-name" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-macsec-ea-oper:ncs1k-macsec-oper/ncs1k-macsec-ctrlr-names/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName, ['name'], name, value)


            class Ncs1KStatusInfo(Entity):
                """
                controller data
                
                .. attribute:: encrypt_sc_status
                
                	Encrypt Secure Channel Status
                	**type**\:  :py:class:`EncryptScStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus>`
                
                .. attribute:: decrypt_sc_status
                
                	Decrypt Secure Channel Status
                	**type**\:  :py:class:`DecryptScStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus>`
                
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

                _prefix = 'ncs1k-macsec-ea-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo, self).__init__()

                    self.yang_name = "ncs1k-status-info"
                    self.yang_parent_name = "ncs1k-macsec-ctrlr-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("encrypt-sc-status", ("encrypt_sc_status", Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus)), ("decrypt-sc-status", ("decrypt_sc_status", Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('replay_window_size', YLeaf(YType.uint32, 'replay-window-size')),
                        ('must_secure', YLeaf(YType.boolean, 'must-secure')),
                        ('secure_mode', YLeaf(YType.uint32, 'secure-mode')),
                    ])
                    self.replay_window_size = None
                    self.must_secure = None
                    self.secure_mode = None

                    self.encrypt_sc_status = Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus()
                    self.encrypt_sc_status.parent = self
                    self._children_name_map["encrypt_sc_status"] = "encrypt-sc-status"
                    self._children_yang_names.add("encrypt-sc-status")

                    self.decrypt_sc_status = Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus()
                    self.decrypt_sc_status.parent = self
                    self._children_name_map["decrypt_sc_status"] = "decrypt-sc-status"
                    self._children_yang_names.add("decrypt-sc-status")
                    self._segment_path = lambda: "ncs1k-status-info"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo, ['replay_window_size', 'must_secure', 'secure_mode'], name, value)


                class EncryptScStatus(Entity):
                    """
                    Encrypt Secure Channel Status
                    
                    .. attribute:: protection_enabled
                    
                    	Protection Enabled
                    	**type**\: bool
                    
                    .. attribute:: secure_channel_id
                    
                    	Secure Channel Id
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: confidentiality_offset
                    
                    	Confidentiality offset
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cipher_suite
                    
                    	Cipher Suite
                    	**type**\:  :py:class:`Ncs1kCipherSuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1kCipherSuit>`
                    
                    .. attribute:: initial_packet_number
                    
                    	Initial Packet Number
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: secure_tag_length
                    
                    	Secure Tag Length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_packet_number
                    
                    	Maximum Packet Number
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: recent_packet_number
                    
                    	Recent Packet Number
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: active_association
                    
                    	Active Associations
                    	**type**\: list of  		 :py:class:`ActiveAssociation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus.ActiveAssociation>`
                    
                    

                    """

                    _prefix = 'ncs1k-macsec-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus, self).__init__()

                        self.yang_name = "encrypt-sc-status"
                        self.yang_parent_name = "ncs1k-status-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("active-association", ("active_association", Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus.ActiveAssociation))])
                        self._leafs = OrderedDict([
                            ('protection_enabled', YLeaf(YType.boolean, 'protection-enabled')),
                            ('secure_channel_id', YLeaf(YType.uint64, 'secure-channel-id')),
                            ('confidentiality_offset', YLeaf(YType.uint32, 'confidentiality-offset')),
                            ('cipher_suite', YLeaf(YType.enumeration, 'cipher-suite')),
                            ('initial_packet_number', YLeaf(YType.uint64, 'initial-packet-number')),
                            ('secure_tag_length', YLeaf(YType.uint32, 'secure-tag-length')),
                            ('max_packet_number', YLeaf(YType.uint64, 'max-packet-number')),
                            ('recent_packet_number', YLeaf(YType.uint64, 'recent-packet-number')),
                        ])
                        self.protection_enabled = None
                        self.secure_channel_id = None
                        self.confidentiality_offset = None
                        self.cipher_suite = None
                        self.initial_packet_number = None
                        self.secure_tag_length = None
                        self.max_packet_number = None
                        self.recent_packet_number = None

                        self.active_association = YList(self)
                        self._segment_path = lambda: "encrypt-sc-status"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus, ['protection_enabled', 'secure_channel_id', 'confidentiality_offset', 'cipher_suite', 'initial_packet_number', 'secure_tag_length', 'max_packet_number', 'recent_packet_number'], name, value)


                    class ActiveAssociation(Entity):
                        """
                        Active Associations
                        
                        .. attribute:: association_number
                        
                        	Assocition Number
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: device_association_number
                        
                        	Devive Association Number
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: short_secure_channel_id
                        
                        	Short Secure Channel Id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: programmed_time
                        
                        	Key Programmed Time
                        	**type**\: str
                        
                        	**length:** 0..30
                        
                        .. attribute:: key_crc
                        
                        	32bit CRC of Programmed Key
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: xpn_salt
                        
                        	XPN Salt
                        	**type**\: list of str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        

                        """

                        _prefix = 'ncs1k-macsec-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus.ActiveAssociation, self).__init__()

                            self.yang_name = "active-association"
                            self.yang_parent_name = "encrypt-sc-status"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('association_number', YLeaf(YType.uint8, 'association-number')),
                                ('device_association_number', YLeaf(YType.uint8, 'device-association-number')),
                                ('short_secure_channel_id', YLeaf(YType.uint32, 'short-secure-channel-id')),
                                ('programmed_time', YLeaf(YType.str, 'programmed-time')),
                                ('key_crc', YLeaf(YType.str, 'key-crc')),
                                ('xpn_salt', YLeafList(YType.str, 'xpn-salt')),
                            ])
                            self.association_number = None
                            self.device_association_number = None
                            self.short_secure_channel_id = None
                            self.programmed_time = None
                            self.key_crc = None
                            self.xpn_salt = []
                            self._segment_path = lambda: "active-association"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus.ActiveAssociation, ['association_number', 'device_association_number', 'short_secure_channel_id', 'programmed_time', 'key_crc', 'xpn_salt'], name, value)


                class DecryptScStatus(Entity):
                    """
                    Decrypt Secure Channel Status
                    
                    .. attribute:: protection_enabled
                    
                    	Protection Enabled
                    	**type**\: bool
                    
                    .. attribute:: secure_channel_id
                    
                    	Secure Channel Id
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: confidentiality_offset
                    
                    	Confidentiality offset
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cipher_suite
                    
                    	Cipher Suite
                    	**type**\:  :py:class:`Ncs1kCipherSuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1kCipherSuit>`
                    
                    .. attribute:: initial_packet_number
                    
                    	Initial Packet Number
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: secure_tag_length
                    
                    	Secure Tag Length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_packet_number
                    
                    	Maximum Packet Number
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: recent_packet_number
                    
                    	Recent Packet Number
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: active_association
                    
                    	Active Associations
                    	**type**\: list of  		 :py:class:`ActiveAssociation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus.ActiveAssociation>`
                    
                    

                    """

                    _prefix = 'ncs1k-macsec-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus, self).__init__()

                        self.yang_name = "decrypt-sc-status"
                        self.yang_parent_name = "ncs1k-status-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("active-association", ("active_association", Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus.ActiveAssociation))])
                        self._leafs = OrderedDict([
                            ('protection_enabled', YLeaf(YType.boolean, 'protection-enabled')),
                            ('secure_channel_id', YLeaf(YType.uint64, 'secure-channel-id')),
                            ('confidentiality_offset', YLeaf(YType.uint32, 'confidentiality-offset')),
                            ('cipher_suite', YLeaf(YType.enumeration, 'cipher-suite')),
                            ('initial_packet_number', YLeaf(YType.uint64, 'initial-packet-number')),
                            ('secure_tag_length', YLeaf(YType.uint32, 'secure-tag-length')),
                            ('max_packet_number', YLeaf(YType.uint64, 'max-packet-number')),
                            ('recent_packet_number', YLeaf(YType.uint64, 'recent-packet-number')),
                        ])
                        self.protection_enabled = None
                        self.secure_channel_id = None
                        self.confidentiality_offset = None
                        self.cipher_suite = None
                        self.initial_packet_number = None
                        self.secure_tag_length = None
                        self.max_packet_number = None
                        self.recent_packet_number = None

                        self.active_association = YList(self)
                        self._segment_path = lambda: "decrypt-sc-status"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus, ['protection_enabled', 'secure_channel_id', 'confidentiality_offset', 'cipher_suite', 'initial_packet_number', 'secure_tag_length', 'max_packet_number', 'recent_packet_number'], name, value)


                    class ActiveAssociation(Entity):
                        """
                        Active Associations
                        
                        .. attribute:: association_number
                        
                        	Assocition Number
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: device_association_number
                        
                        	Devive Association Number
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: short_secure_channel_id
                        
                        	Short Secure Channel Id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: programmed_time
                        
                        	Key Programmed Time
                        	**type**\: str
                        
                        	**length:** 0..30
                        
                        .. attribute:: key_crc
                        
                        	32bit CRC of Programmed Key
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: xpn_salt
                        
                        	XPN Salt
                        	**type**\: list of str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        

                        """

                        _prefix = 'ncs1k-macsec-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus.ActiveAssociation, self).__init__()

                            self.yang_name = "active-association"
                            self.yang_parent_name = "decrypt-sc-status"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('association_number', YLeaf(YType.uint8, 'association-number')),
                                ('device_association_number', YLeaf(YType.uint8, 'device-association-number')),
                                ('short_secure_channel_id', YLeaf(YType.uint32, 'short-secure-channel-id')),
                                ('programmed_time', YLeaf(YType.str, 'programmed-time')),
                                ('key_crc', YLeaf(YType.str, 'key-crc')),
                                ('xpn_salt', YLeafList(YType.str, 'xpn-salt')),
                            ])
                            self.association_number = None
                            self.device_association_number = None
                            self.short_secure_channel_id = None
                            self.programmed_time = None
                            self.key_crc = None
                            self.xpn_salt = []
                            self._segment_path = lambda: "active-association"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus.ActiveAssociation, ['association_number', 'device_association_number', 'short_secure_channel_id', 'programmed_time', 'key_crc', 'xpn_salt'], name, value)

    def clone_ptr(self):
        self._top_entity = Ncs1KMacsecOper()
        return self._top_entity


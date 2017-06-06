""" Cisco_IOS_XR_ncs1k_macsec_ea_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-macsec\-ea package operational data.

This module contains definitions
for the following management objects\:
  ncs1k\-macsec\-oper\: Macsec data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class Ncs1KCipherSuitEnum(Enum):
    """
    Ncs1KCipherSuitEnum

    Ncs1k cipher suit

    .. data:: gcm_aes_256 = 0

    	GCM AES 256

    .. data:: gcm_aes_128 = 1

    	GCM AES 128

    .. data:: gcm_aes_xpn_256 = 2

    	GCM AES XPN 256

    """

    gcm_aes_256 = 0

    gcm_aes_128 = 1

    gcm_aes_xpn_256 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_macsec_ea_oper as meta
        return meta._meta_table['Ncs1KCipherSuitEnum']



class Ncs1KMacsecOper(object):
    """
    Macsec data
    
    .. attribute:: ncs1k_macsec_ctrlr_names
    
    	All Macsec operational data
    	**type**\:   :py:class:`Ncs1KMacsecCtrlrNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames>`
    
    

    """

    _prefix = 'ncs1k-macsec-ea-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.ncs1k_macsec_ctrlr_names = Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames()
        self.ncs1k_macsec_ctrlr_names.parent = self


    class Ncs1KMacsecCtrlrNames(object):
        """
        All Macsec operational data
        
        .. attribute:: ncs1k_macsec_ctrlr_name
        
        	Interface name
        	**type**\: list of    :py:class:`Ncs1KMacsecCtrlrName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName>`
        
        

        """

        _prefix = 'ncs1k-macsec-ea-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.ncs1k_macsec_ctrlr_name = YList()
            self.ncs1k_macsec_ctrlr_name.parent = self
            self.ncs1k_macsec_ctrlr_name.name = 'ncs1k_macsec_ctrlr_name'


        class Ncs1KMacsecCtrlrName(object):
            """
            Interface name
            
            .. attribute:: name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: ncs1k_status_info
            
            	controller data
            	**type**\:   :py:class:`Ncs1KStatusInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo>`
            
            

            """

            _prefix = 'ncs1k-macsec-ea-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.ncs1k_status_info = Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo()
                self.ncs1k_status_info.parent = self


            class Ncs1KStatusInfo(object):
                """
                controller data
                
                .. attribute:: decrypt_sc_status
                
                	Decrypt Secure Channel Status
                	**type**\:   :py:class:`DecryptScStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus>`
                
                .. attribute:: encrypt_sc_status
                
                	Encrypt Secure Channel Status
                	**type**\:   :py:class:`EncryptScStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus>`
                
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
                
                

                """

                _prefix = 'ncs1k-macsec-ea-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.decrypt_sc_status = Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus()
                    self.decrypt_sc_status.parent = self
                    self.encrypt_sc_status = Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus()
                    self.encrypt_sc_status.parent = self
                    self.must_secure = None
                    self.replay_window_size = None
                    self.secure_mode = None


                class EncryptScStatus(object):
                    """
                    Encrypt Secure Channel Status
                    
                    .. attribute:: active_association
                    
                    	Active Associations
                    	**type**\: list of    :py:class:`ActiveAssociation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus.ActiveAssociation>`
                    
                    .. attribute:: cipher_suite
                    
                    	Cipher Suite
                    	**type**\:   :py:class:`Ncs1KCipherSuitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KCipherSuitEnum>`
                    
                    .. attribute:: confidentiality_offset
                    
                    	Confidentiality offset
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: initial_packet_number
                    
                    	Initial Packet Number
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: max_packet_number
                    
                    	Maximum Packet Number
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
                    
                    	**length:** 0..20
                    
                    .. attribute:: secure_tag_length
                    
                    	Secure Tag Length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ncs1k-macsec-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.active_association = YList()
                        self.active_association.parent = self
                        self.active_association.name = 'active_association'
                        self.cipher_suite = None
                        self.confidentiality_offset = None
                        self.initial_packet_number = None
                        self.max_packet_number = None
                        self.protection_enabled = None
                        self.recent_packet_number = None
                        self.secure_channel_id = None
                        self.secure_tag_length = None


                    class ActiveAssociation(object):
                        """
                        Active Associations
                        
                        .. attribute:: association_number
                        
                        	Assocition Number
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: device_association_number
                        
                        	Devive Association Number
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: key_crc
                        
                        	32bit CRC of Programmed Key
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: programmed_time
                        
                        	Key Programmed Time
                        	**type**\:  str
                        
                        	**length:** 0..30
                        
                        .. attribute:: short_secure_channel_id
                        
                        	Short Secure Channel Id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: xpn_salt
                        
                        	XPN Salt
                        	**type**\:  list of str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        

                        """

                        _prefix = 'ncs1k-macsec-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.association_number = None
                            self.device_association_number = None
                            self.key_crc = None
                            self.programmed_time = None
                            self.short_secure_channel_id = None
                            self.xpn_salt = YLeafList()
                            self.xpn_salt.parent = self
                            self.xpn_salt.name = 'xpn_salt'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-macsec-ea-oper:active-association'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.association_number is not None:
                                return True

                            if self.device_association_number is not None:
                                return True

                            if self.key_crc is not None:
                                return True

                            if self.programmed_time is not None:
                                return True

                            if self.short_secure_channel_id is not None:
                                return True

                            if self.xpn_salt is not None:
                                for child in self.xpn_salt:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_macsec_ea_oper as meta
                            return meta._meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus.ActiveAssociation']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-macsec-ea-oper:encrypt-sc-status'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.active_association is not None:
                            for child_ref in self.active_association:
                                if child_ref._has_data():
                                    return True

                        if self.cipher_suite is not None:
                            return True

                        if self.confidentiality_offset is not None:
                            return True

                        if self.initial_packet_number is not None:
                            return True

                        if self.max_packet_number is not None:
                            return True

                        if self.protection_enabled is not None:
                            return True

                        if self.recent_packet_number is not None:
                            return True

                        if self.secure_channel_id is not None:
                            return True

                        if self.secure_tag_length is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_macsec_ea_oper as meta
                        return meta._meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus']['meta_info']


                class DecryptScStatus(object):
                    """
                    Decrypt Secure Channel Status
                    
                    .. attribute:: active_association
                    
                    	Active Associations
                    	**type**\: list of    :py:class:`ActiveAssociation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus.ActiveAssociation>`
                    
                    .. attribute:: cipher_suite
                    
                    	Cipher Suite
                    	**type**\:   :py:class:`Ncs1KCipherSuitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper.Ncs1KCipherSuitEnum>`
                    
                    .. attribute:: confidentiality_offset
                    
                    	Confidentiality offset
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: initial_packet_number
                    
                    	Initial Packet Number
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: max_packet_number
                    
                    	Maximum Packet Number
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
                    
                    	**length:** 0..20
                    
                    .. attribute:: secure_tag_length
                    
                    	Secure Tag Length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ncs1k-macsec-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.active_association = YList()
                        self.active_association.parent = self
                        self.active_association.name = 'active_association'
                        self.cipher_suite = None
                        self.confidentiality_offset = None
                        self.initial_packet_number = None
                        self.max_packet_number = None
                        self.protection_enabled = None
                        self.recent_packet_number = None
                        self.secure_channel_id = None
                        self.secure_tag_length = None


                    class ActiveAssociation(object):
                        """
                        Active Associations
                        
                        .. attribute:: association_number
                        
                        	Assocition Number
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: device_association_number
                        
                        	Devive Association Number
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: key_crc
                        
                        	32bit CRC of Programmed Key
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: programmed_time
                        
                        	Key Programmed Time
                        	**type**\:  str
                        
                        	**length:** 0..30
                        
                        .. attribute:: short_secure_channel_id
                        
                        	Short Secure Channel Id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: xpn_salt
                        
                        	XPN Salt
                        	**type**\:  list of str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        

                        """

                        _prefix = 'ncs1k-macsec-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.association_number = None
                            self.device_association_number = None
                            self.key_crc = None
                            self.programmed_time = None
                            self.short_secure_channel_id = None
                            self.xpn_salt = YLeafList()
                            self.xpn_salt.parent = self
                            self.xpn_salt.name = 'xpn_salt'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-macsec-ea-oper:active-association'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.association_number is not None:
                                return True

                            if self.device_association_number is not None:
                                return True

                            if self.key_crc is not None:
                                return True

                            if self.programmed_time is not None:
                                return True

                            if self.short_secure_channel_id is not None:
                                return True

                            if self.xpn_salt is not None:
                                for child in self.xpn_salt:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_macsec_ea_oper as meta
                            return meta._meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus.ActiveAssociation']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-macsec-ea-oper:decrypt-sc-status'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.active_association is not None:
                            for child_ref in self.active_association:
                                if child_ref._has_data():
                                    return True

                        if self.cipher_suite is not None:
                            return True

                        if self.confidentiality_offset is not None:
                            return True

                        if self.initial_packet_number is not None:
                            return True

                        if self.max_packet_number is not None:
                            return True

                        if self.protection_enabled is not None:
                            return True

                        if self.recent_packet_number is not None:
                            return True

                        if self.secure_channel_id is not None:
                            return True

                        if self.secure_tag_length is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_macsec_ea_oper as meta
                        return meta._meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-macsec-ea-oper:ncs1k-status-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.decrypt_sc_status is not None and self.decrypt_sc_status._has_data():
                        return True

                    if self.encrypt_sc_status is not None and self.encrypt_sc_status._has_data():
                        return True

                    if self.must_secure is not None:
                        return True

                    if self.replay_window_size is not None:
                        return True

                    if self.secure_mode is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_macsec_ea_oper as meta
                    return meta._meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-ncs1k-macsec-ea-oper:ncs1k-macsec-oper/Cisco-IOS-XR-ncs1k-macsec-ea-oper:ncs1k-macsec-ctrlr-names/Cisco-IOS-XR-ncs1k-macsec-ea-oper:ncs1k-macsec-ctrlr-name[Cisco-IOS-XR-ncs1k-macsec-ea-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.ncs1k_status_info is not None and self.ncs1k_status_info._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_macsec_ea_oper as meta
                return meta._meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ncs1k-macsec-ea-oper:ncs1k-macsec-oper/Cisco-IOS-XR-ncs1k-macsec-ea-oper:ncs1k-macsec-ctrlr-names'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ncs1k_macsec_ctrlr_name is not None:
                for child_ref in self.ncs1k_macsec_ctrlr_name:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_macsec_ea_oper as meta
            return meta._meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ncs1k-macsec-ea-oper:ncs1k-macsec-oper'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ncs1k_macsec_ctrlr_names is not None and self.ncs1k_macsec_ctrlr_names._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_macsec_ea_oper as meta
        return meta._meta_table['Ncs1KMacsecOper']['meta_info']



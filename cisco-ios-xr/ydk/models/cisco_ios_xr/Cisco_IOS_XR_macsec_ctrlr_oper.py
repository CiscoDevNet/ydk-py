""" Cisco_IOS_XR_macsec_ctrlr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR macsec\-ctrlr package operational data.

This module contains definitions
for the following management objects\:
  macsec\-ctrlr\-oper\: Macsec controller data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MacsecCtrlrCiphersuitEnum(Enum):
    """
    MacsecCtrlrCiphersuitEnum

    Macsec ctrlr ciphersuit

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_macsec_ctrlr_oper as meta
        return meta._meta_table['MacsecCtrlrCiphersuitEnum']


class MacsecCtrlrStateEnum(Enum):
    """
    MacsecCtrlrStateEnum

    Macsec ctrlr state

    .. data:: macsec_ctrlr_state_up = 0

    	Up

    .. data:: macsec_ctrlr_state_down = 1

    	Down

    .. data:: macsec_ctrlr_state_admin_down = 2

    	Administratively Down

    """

    macsec_ctrlr_state_up = 0

    macsec_ctrlr_state_down = 1

    macsec_ctrlr_state_admin_down = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_macsec_ctrlr_oper as meta
        return meta._meta_table['MacsecCtrlrStateEnum']



class MacsecCtrlrOper(object):
    """
    Macsec controller data
    
    .. attribute:: macsec_ctrlr_ports
    
    	All Macsec Controller Port operational data
    	**type**\:   :py:class:`MacsecCtrlrPorts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts>`
    
    

    """

    _prefix = 'macsec-ctrlr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.macsec_ctrlr_ports = MacsecCtrlrOper.MacsecCtrlrPorts()
        self.macsec_ctrlr_ports.parent = self


    class MacsecCtrlrPorts(object):
        """
        All Macsec Controller Port operational data
        
        .. attribute:: macsec_ctrlr_port
        
        	Controller name
        	**type**\: list of    :py:class:`MacsecCtrlrPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort>`
        
        

        """

        _prefix = 'macsec-ctrlr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.macsec_ctrlr_port = YList()
            self.macsec_ctrlr_port.parent = self
            self.macsec_ctrlr_port.name = 'macsec_ctrlr_port'


        class MacsecCtrlrPort(object):
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
                self.parent = None
                self.name = None
                self.macsec_ctrlr_info = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo()
                self.macsec_ctrlr_info.parent = self


            class MacsecCtrlrInfo(object):
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
                	**type**\:   :py:class:`MacsecCtrlrStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrStateEnum>`
                
                

                """

                _prefix = 'macsec-ctrlr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.decrypt_sc_status = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus()
                    self.decrypt_sc_status.parent = self
                    self.encrypt_sc_status = MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus()
                    self.encrypt_sc_status.parent = self
                    self.must_secure = None
                    self.replay_window_size = None
                    self.secure_mode = None
                    self.state = None


                class EncryptScStatus(object):
                    """
                    Encrypt Secure Channel Status
                    
                    .. attribute:: active_association
                    
                    	Active Associations
                    	**type**\: list of    :py:class:`ActiveAssociation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation>`
                    
                    .. attribute:: cipher_suite
                    
                    	Cipher Suite
                    	**type**\:   :py:class:`MacsecCtrlrCiphersuitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrCiphersuitEnum>`
                    
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
                        self.parent = None
                        self.active_association = YList()
                        self.active_association.parent = self
                        self.active_association.name = 'active_association'
                        self.cipher_suite = None
                        self.confidentiality_offset = None
                        self.max_packet_number = None
                        self.protection_enabled = None
                        self.recent_packet_number = None
                        self.secure_channel_id = None


                    class ActiveAssociation(object):
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
                            self.parent = None
                            self.association_number = None
                            self.short_secure_channel_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-macsec-ctrlr-oper:active-association'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.association_number is not None:
                                return True

                            if self.short_secure_channel_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_macsec_ctrlr_oper as meta
                            return meta._meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-macsec-ctrlr-oper:encrypt-sc-status'

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

                        if self.max_packet_number is not None:
                            return True

                        if self.protection_enabled is not None:
                            return True

                        if self.recent_packet_number is not None:
                            return True

                        if self.secure_channel_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_macsec_ctrlr_oper as meta
                        return meta._meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus']['meta_info']


                class DecryptScStatus(object):
                    """
                    Decrypt Secure Channel Status
                    
                    .. attribute:: active_association
                    
                    	Active Associations
                    	**type**\: list of    :py:class:`ActiveAssociation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation>`
                    
                    .. attribute:: cipher_suite
                    
                    	Cipher Suite
                    	**type**\:   :py:class:`MacsecCtrlrCiphersuitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper.MacsecCtrlrCiphersuitEnum>`
                    
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
                        self.parent = None
                        self.active_association = YList()
                        self.active_association.parent = self
                        self.active_association.name = 'active_association'
                        self.cipher_suite = None
                        self.confidentiality_offset = None
                        self.max_packet_number = None
                        self.protection_enabled = None
                        self.recent_packet_number = None
                        self.secure_channel_id = None


                    class ActiveAssociation(object):
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
                            self.parent = None
                            self.association_number = None
                            self.short_secure_channel_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-macsec-ctrlr-oper:active-association'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.association_number is not None:
                                return True

                            if self.short_secure_channel_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_macsec_ctrlr_oper as meta
                            return meta._meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-macsec-ctrlr-oper:decrypt-sc-status'

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

                        if self.max_packet_number is not None:
                            return True

                        if self.protection_enabled is not None:
                            return True

                        if self.recent_packet_number is not None:
                            return True

                        if self.secure_channel_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_macsec_ctrlr_oper as meta
                        return meta._meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-info'

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

                    if self.state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_macsec_ctrlr_oper as meta
                    return meta._meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-oper/Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-ports/Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-port[Cisco-IOS-XR-macsec-ctrlr-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.macsec_ctrlr_info is not None and self.macsec_ctrlr_info._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_macsec_ctrlr_oper as meta
                return meta._meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-oper/Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-ports'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.macsec_ctrlr_port is not None:
                for child_ref in self.macsec_ctrlr_port:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_macsec_ctrlr_oper as meta
            return meta._meta_table['MacsecCtrlrOper.MacsecCtrlrPorts']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-macsec-ctrlr-oper:macsec-ctrlr-oper'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.macsec_ctrlr_ports is not None and self.macsec_ctrlr_ports._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_macsec_ctrlr_oper as meta
        return meta._meta_table['MacsecCtrlrOper']['meta_info']



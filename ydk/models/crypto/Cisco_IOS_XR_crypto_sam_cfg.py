""" Cisco_IOS_XR_crypto_sam_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-sam package configuration.

This module contains definitions
for the following management objects\:
  crypto\: Crypto configuration

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CryptoSamActionEnum(Enum):
    """
    CryptoSamActionEnum

    Crypto sam action

    .. data:: PROCEED = 1

    	To respond YES to the SAM prompt

    .. data:: TERMINATE = 2

    	To respond NO to the SAM prompt

    """

    PROCEED = 1

    TERMINATE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_sam_cfg as meta
        return meta._meta_table['CryptoSamActionEnum']



class Crypto(object):
    """
    Crypto configuration
    
    .. attribute:: sam
    
    	Software Authentication Manager (SAM) Config
    	**type**\: :py:class:`Sam <ydk.models.crypto.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Sam>`
    
    .. attribute:: ssh
    
    	Secure Shell configuration
    	**type**\: :py:class:`Ssh <ydk.models.crypto.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh>`
    
    

    """

    _prefix = 'crypto-sam-cfg'
    _revision = '2015-01-07'

    def __init__(self):
        self.sam = Crypto.Sam()
        self.sam.parent = self
        self.ssh = Crypto.Ssh()
        self.ssh.parent = self


    class Sam(object):
        """
        Software Authentication Manager (SAM) Config
        
        .. attribute:: prompt_interval
        
        	Set prompt interval at reboot time
        	**type**\: :py:class:`PromptInterval <ydk.models.crypto.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Sam.PromptInterval>`
        
        

        """

        _prefix = 'crypto-sam-cfg'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.prompt_interval = None


        class PromptInterval(object):
            """
            Set prompt interval at reboot time
            
            .. attribute:: action
            
            	Respond to SAM prompt either Proceed/Terminate
            	**type**\: :py:class:`CryptoSamActionEnum <ydk.models.crypto.Cisco_IOS_XR_crypto_sam_cfg.CryptoSamActionEnum>`
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            .. attribute:: prompt_time
            
            	Prompt time from 0 \- 300 seconds
            	**type**\: int
            
            	**range:** 0..300
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'crypto-sam-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.action = None
                self.prompt_time = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-sam-cfg:sam/Cisco-IOS-XR-crypto-sam-cfg:prompt-interval'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.action is not None:
                    return True

                if self.prompt_time is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_sam_cfg as meta
                return meta._meta_table['Crypto.Sam.PromptInterval']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-sam-cfg:sam'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.prompt_interval is not None and self.prompt_interval._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_sam_cfg as meta
            return meta._meta_table['Crypto.Sam']['meta_info']


    class Ssh(object):
        """
        Secure Shell configuration
        
        .. attribute:: client
        
        	Provide SSH client service
        	**type**\: :py:class:`Client <ydk.models.crypto.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Client>`
        
        .. attribute:: server
        
        	Provide SSH server service
        	**type**\: :py:class:`Server <ydk.models.crypto.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server>`
        
        

        """

        _prefix = 'crypto-ssh-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.client = Crypto.Ssh.Client()
            self.client.parent = self
            self.server = Crypto.Ssh.Server()
            self.server.parent = self


        class Client(object):
            """
            Provide SSH client service
            
            .. attribute:: host_public_key
            
            	Filename \- where to store known host file
            	**type**\: str
            
            .. attribute:: client_vrf
            
            	Source interface VRF for ssh client sessions
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: source_interface
            
            	Source interface for ssh client sessions
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: dscp
            
            	Cisco sshd DSCP value
            	**type**\: int
            
            	**range:** 0..63
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.host_public_key = None
                self.client_vrf = None
                self.source_interface = None
                self.dscp = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/Cisco-IOS-XR-crypto-ssh-cfg:client'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.host_public_key is not None:
                    return True

                if self.client_vrf is not None:
                    return True

                if self.source_interface is not None:
                    return True

                if self.dscp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_sam_cfg as meta
                return meta._meta_table['Crypto.Ssh.Client']['meta_info']


        class Server(object):
            """
            Provide SSH server service
            
            .. attribute:: vrf_table
            
            	Cisco sshd VRF name
            	**type**\: :py:class:`VrfTable <ydk.models.crypto.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.VrfTable>`
            
            .. attribute:: netconf_vrf_table
            
            	Cisco sshd Netconf VRF name
            	**type**\: :py:class:`NetconfVrfTable <ydk.models.crypto.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.NetconfVrfTable>`
            
            .. attribute:: session_limit
            
            	Cisco sshd session\-limit of service requests
            	**type**\: int
            
            	**range:** 1..1024
            
            .. attribute:: netconf
            
            	port number on which ssh service to be started for netconf
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: v2
            
            	Cisco sshd force protocol version 2 only
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: logging
            
            	Enable ssh server logging
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: rate_limit
            
            	Cisco sshd rate\-limit of service requests
            	**type**\: int
            
            	**range:** 1..600
            
            .. attribute:: timeout
            
            	Timeout value between 5\-120 seconds defalut 30
            	**type**\: int
            
            	**range:** 5..120
            
            .. attribute:: dscp
            
            	Cisco sshd DSCP value
            	**type**\: int
            
            	**range:** 0..63
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.vrf_table = Crypto.Ssh.Server.VrfTable()
                self.vrf_table.parent = self
                self.netconf_vrf_table = Crypto.Ssh.Server.NetconfVrfTable()
                self.netconf_vrf_table.parent = self
                self.session_limit = None
                self.netconf = None
                self.v2 = None
                self.logging = None
                self.rate_limit = None
                self.timeout = None
                self.dscp = None


            class VrfTable(object):
                """
                Cisco sshd VRF name
                
                .. attribute:: vrf
                
                	Enter VRF name
                	**type**\: list of :py:class:`Vrf <ydk.models.crypto.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.VrfTable.Vrf>`
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.vrf = YList()
                    self.vrf.parent = self
                    self.vrf.name = 'vrf'


                class Vrf(object):
                    """
                    Enter VRF name
                    
                    .. attribute:: vrf_name  <key>
                    
                    	Enter VRF name
                    	**type**\: str
                    
                    	**range:** 0..32
                    
                    .. attribute:: enable
                    
                    	Enable to use VRF
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: ipv4_access_list
                    
                    	SSH v4 access\-list name
                    	**type**\: str
                    
                    	**range:** 0..32
                    
                    .. attribute:: ipv6_access_list
                    
                    	SSH v6 access\-list name
                    	**type**\: str
                    
                    	**range:** 0..32
                    
                    

                    """

                    _prefix = 'crypto-ssh-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.vrf_name = None
                        self.enable = None
                        self.ipv4_access_list = None
                        self.ipv6_access_list = None

                    @property
                    def _common_path(self):
                        if self.vrf_name is None:
                            raise YPYDataValidationError('Key property vrf_name is None')

                        return '/Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/Cisco-IOS-XR-crypto-ssh-cfg:server/Cisco-IOS-XR-crypto-ssh-cfg:vrf-table/Cisco-IOS-XR-crypto-ssh-cfg:vrf[Cisco-IOS-XR-crypto-ssh-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.vrf_name is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.ipv4_access_list is not None:
                            return True

                        if self.ipv6_access_list is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_sam_cfg as meta
                        return meta._meta_table['Crypto.Ssh.Server.VrfTable.Vrf']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/Cisco-IOS-XR-crypto-ssh-cfg:server/Cisco-IOS-XR-crypto-ssh-cfg:vrf-table'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.vrf is not None:
                        for child_ref in self.vrf:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_sam_cfg as meta
                    return meta._meta_table['Crypto.Ssh.Server.VrfTable']['meta_info']


            class NetconfVrfTable(object):
                """
                Cisco sshd Netconf VRF name
                
                .. attribute:: vrf
                
                	Enter VRF name
                	**type**\: list of :py:class:`Vrf <ydk.models.crypto.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.NetconfVrfTable.Vrf>`
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.vrf = YList()
                    self.vrf.parent = self
                    self.vrf.name = 'vrf'


                class Vrf(object):
                    """
                    Enter VRF name
                    
                    .. attribute:: vrf_name  <key>
                    
                    	Enter VRF name
                    	**type**\: str
                    
                    	**range:** 0..32
                    
                    .. attribute:: enable
                    
                    	Enable to use VRF
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: ipv4_access_list
                    
                    	SSH v4 access\-list name
                    	**type**\: str
                    
                    	**range:** 0..32
                    
                    .. attribute:: ipv6_access_list
                    
                    	SSH v6 access\-list name
                    	**type**\: str
                    
                    	**range:** 0..32
                    
                    

                    """

                    _prefix = 'crypto-ssh-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.vrf_name = None
                        self.enable = None
                        self.ipv4_access_list = None
                        self.ipv6_access_list = None

                    @property
                    def _common_path(self):
                        if self.vrf_name is None:
                            raise YPYDataValidationError('Key property vrf_name is None')

                        return '/Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/Cisco-IOS-XR-crypto-ssh-cfg:server/Cisco-IOS-XR-crypto-ssh-cfg:netconf-vrf-table/Cisco-IOS-XR-crypto-ssh-cfg:vrf[Cisco-IOS-XR-crypto-ssh-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.vrf_name is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.ipv4_access_list is not None:
                            return True

                        if self.ipv6_access_list is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_sam_cfg as meta
                        return meta._meta_table['Crypto.Ssh.Server.NetconfVrfTable.Vrf']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/Cisco-IOS-XR-crypto-ssh-cfg:server/Cisco-IOS-XR-crypto-ssh-cfg:netconf-vrf-table'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.vrf is not None:
                        for child_ref in self.vrf:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_sam_cfg as meta
                    return meta._meta_table['Crypto.Ssh.Server.NetconfVrfTable']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/Cisco-IOS-XR-crypto-ssh-cfg:server'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.vrf_table is not None and self.vrf_table._has_data():
                    return True

                if self.netconf_vrf_table is not None and self.netconf_vrf_table._has_data():
                    return True

                if self.session_limit is not None:
                    return True

                if self.netconf is not None:
                    return True

                if self.v2 is not None:
                    return True

                if self.logging is not None:
                    return True

                if self.rate_limit is not None:
                    return True

                if self.timeout is not None:
                    return True

                if self.dscp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_sam_cfg as meta
                return meta._meta_table['Crypto.Ssh.Server']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.client is not None and self.client._has_data():
                return True

            if self.server is not None and self.server._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_sam_cfg as meta
            return meta._meta_table['Crypto.Ssh']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-sam-cfg:crypto'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.sam is not None and self.sam._has_data():
            return True

        if self.ssh is not None and self.ssh._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_sam_cfg as meta
        return meta._meta_table['Crypto']['meta_info']



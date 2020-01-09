""" Cisco_IOS_XR_crypto_ssh_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-ssh package configuration.

This module contains definitions
for the following management objects\:
  ssh\: Secure Shell configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Ssh(_Entity_):
    """
    Secure Shell configuration
    
    .. attribute:: client
    
    	Provide SSH client service
    	**type**\:  :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Client>`
    
    .. attribute:: server
    
    	Provide SSH server service
    	**type**\:  :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server>`
    
    .. attribute:: backup_server
    
    	Provide SSH server service
    	**type**\:  :py:class:`BackupServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.BackupServer>`
    
    

    """

    _prefix = 'crypto-ssh-cfg'
    _revision = '2019-03-28'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Ssh, self).__init__()
        self._top_entity = None

        self.yang_name = "ssh"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-ssh-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("client", ("client", Ssh.Client)), ("server", ("server", Ssh.Server)), ("backup-server", ("backup_server", Ssh.BackupServer))])
        self._leafs = OrderedDict()

        self.client = Ssh.Client()
        self.client.parent = self
        self._children_name_map["client"] = "client"

        self.server = Ssh.Server()
        self.server.parent = self
        self._children_name_map["server"] = "server"

        self.backup_server = Ssh.BackupServer()
        self.backup_server.parent = self
        self._children_name_map["backup_server"] = "backup-server"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ssh, [], name, value)


    class Client(_Entity_):
        """
        Provide SSH client service
        
        .. attribute:: client_disable
        
        	disable
        	**type**\:  :py:class:`ClientDisable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Client.ClientDisable>`
        
        .. attribute:: client_algo
        
        	Cisco ssh algorithms
        	**type**\:  :py:class:`ClientAlgo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Client.ClientAlgo>`
        
        .. attribute:: client_enable
        
        	clientenable
        	**type**\:  :py:class:`ClientEnable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Client.ClientEnable>`
        
        .. attribute:: rekey_volume
        
        	Configure client volume\-based rekey for SSH
        	**type**\: int
        
        	**range:** 1024..4095
        
        	**default value**\: 1024
        
        .. attribute:: host_public_key
        
        	Filename \- where to store known host file
        	**type**\: str
        
        .. attribute:: client_vrf
        
        	Source interface VRF for ssh client sessions
        	**type**\: str
        
        	**length:** 1..32
        
        .. attribute:: v2
        
        	Cisco ssh client force protocol version 2 only
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: tcp_window_scale
        
        	Set SSH Client Tcp Window Scale factor
        	**type**\: int
        
        	**range:** 1..14
        
        	**default value**\: 1
        
        .. attribute:: rekey_time
        
        	Configure client time\-based rekey for SSH
        	**type**\: int
        
        	**range:** 30..1440
        
        	**units**\: minute
        
        	**default value**\: 60
        
        .. attribute:: source_interface
        
        	Source interface for ssh client sessions
        	**type**\: str
        
        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
        
        .. attribute:: dscp
        
        	Cisco sshd DSCP value
        	**type**\: int
        
        	**range:** 0..63
        
        

        """

        _prefix = 'crypto-ssh-cfg'
        _revision = '2019-03-28'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ssh.Client, self).__init__()

            self.yang_name = "client"
            self.yang_parent_name = "ssh"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("client-disable", ("client_disable", Ssh.Client.ClientDisable)), ("client-algo", ("client_algo", Ssh.Client.ClientAlgo)), ("client-enable", ("client_enable", Ssh.Client.ClientEnable))])
            self._leafs = OrderedDict([
                ('rekey_volume', (YLeaf(YType.uint32, 'rekey-volume'), ['int'])),
                ('host_public_key', (YLeaf(YType.str, 'host-public-key'), ['str'])),
                ('client_vrf', (YLeaf(YType.str, 'client-vrf'), ['str'])),
                ('v2', (YLeaf(YType.empty, 'v2'), ['Empty'])),
                ('tcp_window_scale', (YLeaf(YType.uint32, 'tcp-window-scale'), ['int'])),
                ('rekey_time', (YLeaf(YType.uint32, 'rekey-time'), ['int'])),
                ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                ('dscp', (YLeaf(YType.uint32, 'dscp'), ['int'])),
            ])
            self.rekey_volume = None
            self.host_public_key = None
            self.client_vrf = None
            self.v2 = None
            self.tcp_window_scale = None
            self.rekey_time = None
            self.source_interface = None
            self.dscp = None

            self.client_disable = Ssh.Client.ClientDisable()
            self.client_disable.parent = self
            self._children_name_map["client_disable"] = "client-disable"

            self.client_algo = Ssh.Client.ClientAlgo()
            self.client_algo.parent = self
            self._children_name_map["client_algo"] = "client-algo"

            self.client_enable = Ssh.Client.ClientEnable()
            self.client_enable.parent = self
            self._children_name_map["client_enable"] = "client-enable"
            self._segment_path = lambda: "client"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ssh.Client, ['rekey_volume', 'host_public_key', 'client_vrf', 'v2', 'tcp_window_scale', 'rekey_time', 'source_interface', 'dscp'], name, value)


        class ClientDisable(_Entity_):
            """
            disable
            
            .. attribute:: client_hmac
            
            	hmac
            	**type**\:  :py:class:`ClientHmac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Client.ClientDisable.ClientHmac>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2019-03-28'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh.Client.ClientDisable, self).__init__()

                self.yang_name = "client-disable"
                self.yang_parent_name = "client"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("client-hmac", ("client_hmac", Ssh.Client.ClientDisable.ClientHmac))])
                self._leafs = OrderedDict()

                self.client_hmac = Ssh.Client.ClientDisable.ClientHmac()
                self.client_hmac.parent = self
                self._children_name_map["client_hmac"] = "client-hmac"
                self._segment_path = lambda: "client-disable"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/client/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Client.ClientDisable, [], name, value)


            class ClientHmac(_Entity_):
                """
                hmac
                
                .. attribute:: client_hmac_sha1
                
                	Disable Hmac\-sha1 negotiation
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2019-03-28'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Client.ClientDisable.ClientHmac, self).__init__()

                    self.yang_name = "client-hmac"
                    self.yang_parent_name = "client-disable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('client_hmac_sha1', (YLeaf(YType.boolean, 'client-hmac-sha1'), ['bool'])),
                    ])
                    self.client_hmac_sha1 = None
                    self._segment_path = lambda: "client-hmac"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/client/client-disable/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Client.ClientDisable.ClientHmac, ['client_hmac_sha1'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                    return meta._meta_table['Ssh.Client.ClientDisable.ClientHmac']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                return meta._meta_table['Ssh.Client.ClientDisable']['meta_info']


        class ClientAlgo(_Entity_):
            """
            Cisco ssh algorithms
            
            .. attribute:: key_exchanges
            
            	Key exchange algorithm
            	**type**\:  :py:class:`KeyExchanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Client.ClientAlgo.KeyExchanges>`
            
            .. attribute:: ciphers
            
            	cipher algorithm
            	**type**\:  :py:class:`Ciphers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Client.ClientAlgo.Ciphers>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2019-03-28'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh.Client.ClientAlgo, self).__init__()

                self.yang_name = "client-algo"
                self.yang_parent_name = "client"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("key-exchanges", ("key_exchanges", Ssh.Client.ClientAlgo.KeyExchanges)), ("ciphers", ("ciphers", Ssh.Client.ClientAlgo.Ciphers))])
                self._leafs = OrderedDict()

                self.key_exchanges = Ssh.Client.ClientAlgo.KeyExchanges()
                self.key_exchanges.parent = self
                self._children_name_map["key_exchanges"] = "key-exchanges"

                self.ciphers = Ssh.Client.ClientAlgo.Ciphers()
                self.ciphers.parent = self
                self._children_name_map["ciphers"] = "ciphers"
                self._segment_path = lambda: "client-algo"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/client/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Client.ClientAlgo, [], name, value)


            class KeyExchanges(_Entity_):
                """
                Key exchange algorithm
                
                .. attribute:: key_exchange
                
                	key exchange algorithm
                	**type**\: list of str
                
                	**length:** 1..32
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2019-03-28'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Client.ClientAlgo.KeyExchanges, self).__init__()

                    self.yang_name = "key-exchanges"
                    self.yang_parent_name = "client-algo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('key_exchange', (YLeafList(YType.str, 'key-exchange'), ['str'])),
                    ])
                    self.key_exchange = []
                    self._segment_path = lambda: "key-exchanges"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/client/client-algo/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Client.ClientAlgo.KeyExchanges, ['key_exchange'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                    return meta._meta_table['Ssh.Client.ClientAlgo.KeyExchanges']['meta_info']


            class Ciphers(_Entity_):
                """
                cipher algorithm
                
                .. attribute:: cipher
                
                	Cipher algorithm
                	**type**\: list of str
                
                	**length:** 1..32
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2019-03-28'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Client.ClientAlgo.Ciphers, self).__init__()

                    self.yang_name = "ciphers"
                    self.yang_parent_name = "client-algo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('cipher', (YLeafList(YType.str, 'cipher'), ['str'])),
                    ])
                    self.cipher = []
                    self._segment_path = lambda: "ciphers"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/client/client-algo/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Client.ClientAlgo.Ciphers, ['cipher'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                    return meta._meta_table['Ssh.Client.ClientAlgo.Ciphers']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                return meta._meta_table['Ssh.Client.ClientAlgo']['meta_info']


        class ClientEnable(_Entity_):
            """
            clientenable
            
            .. attribute:: client_cipher
            
            	Enable AES\-CBC and 3DES\_CBC for ssh client
            	**type**\:  :py:class:`ClientCipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Client.ClientEnable.ClientCipher>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2019-03-28'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh.Client.ClientEnable, self).__init__()

                self.yang_name = "client-enable"
                self.yang_parent_name = "client"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("client-cipher", ("client_cipher", Ssh.Client.ClientEnable.ClientCipher))])
                self._leafs = OrderedDict()

                self.client_cipher = Ssh.Client.ClientEnable.ClientCipher()
                self.client_cipher.parent = self
                self._children_name_map["client_cipher"] = "client-cipher"
                self._segment_path = lambda: "client-enable"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/client/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Client.ClientEnable, [], name, value)


            class ClientCipher(_Entity_):
                """
                Enable AES\-CBC and 3DES\_CBC for ssh client
                
                .. attribute:: aes_cbc
                
                	Enable AES\-CBC ciphers
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: tripledes_cbc
                
                	Enable 3DES\-CBC cipher
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2019-03-28'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Client.ClientEnable.ClientCipher, self).__init__()

                    self.yang_name = "client-cipher"
                    self.yang_parent_name = "client-enable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('aes_cbc', (YLeaf(YType.boolean, 'aes-cbc'), ['bool'])),
                        ('tripledes_cbc', (YLeaf(YType.boolean, 'tripledes-cbc'), ['bool'])),
                    ])
                    self.aes_cbc = None
                    self.tripledes_cbc = None
                    self._segment_path = lambda: "client-cipher"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/client/client-enable/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Client.ClientEnable.ClientCipher, ['aes_cbc', 'tripledes_cbc'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                    return meta._meta_table['Ssh.Client.ClientEnable.ClientCipher']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                return meta._meta_table['Ssh.Client.ClientEnable']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
            return meta._meta_table['Ssh.Client']['meta_info']


    class Server(_Entity_):
        """
        Provide SSH server service
        
        .. attribute:: disable
        
        	disable
        	**type**\:  :py:class:`Disable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.Disable>`
        
        .. attribute:: enable
        
        	enable
        	**type**\:  :py:class:`Enable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.Enable>`
        
        .. attribute:: vrf_table
        
        	Cisco sshd VRF name
        	**type**\:  :py:class:`VrfTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.VrfTable>`
        
        .. attribute:: server_algo
        
        	Cisco ssh algorithms
        	**type**\:  :py:class:`ServerAlgo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.ServerAlgo>`
        
        .. attribute:: capability
        
        	Capability
        	**type**\:  :py:class:`Capability <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.Capability>`
        
        .. attribute:: netconf_vrf_table
        
        	Cisco sshd Netconf VRF name
        	**type**\:  :py:class:`NetconfVrfTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.NetconfVrfTable>`
        
        .. attribute:: rekey_volume
        
        	Configure volume\-based rekey for SSH
        	**type**\: int
        
        	**range:** 1024..4095
        
        	**default value**\: 1024
        
        .. attribute:: session_limit
        
        	Cisco sshd session\-limit of service requests
        	**type**\: int
        
        	**range:** 1..110
        
        .. attribute:: netconf
        
        	port number on which ssh service to be started for netconf
        	**type**\: int
        
        	**range:** 1..65535
        
        	**default value**\: 830
        
        .. attribute:: v2
        
        	Cisco sshd force protocol version 2 only
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: tcp_window_scale
        
        	Set SSH Server Tcp Window Scale factor
        	**type**\: int
        
        	**range:** 1..14
        
        	**default value**\: 1
        
        .. attribute:: rekey_time
        
        	Time Period in minutes, defalut 60
        	**type**\: int
        
        	**range:** 30..1440
        
        	**units**\: minute
        
        	**default value**\: 60
        
        .. attribute:: logging
        
        	Enable ssh server logging
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: rate_limit
        
        	Cisco sshd rate\-limit of service requests
        	**type**\: int
        
        	**range:** 1..600
        
        	**default value**\: 60
        
        .. attribute:: timeout
        
        	Timeout value between 5\-120 seconds defalut 30
        	**type**\: int
        
        	**range:** 5..120
        
        	**units**\: second
        
        	**default value**\: 30
        
        .. attribute:: dscp
        
        	Cisco sshd DSCP value
        	**type**\: int
        
        	**range:** 0..63
        
        

        """

        _prefix = 'crypto-ssh-cfg'
        _revision = '2019-03-28'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ssh.Server, self).__init__()

            self.yang_name = "server"
            self.yang_parent_name = "ssh"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("disable", ("disable", Ssh.Server.Disable)), ("enable", ("enable", Ssh.Server.Enable)), ("vrf-table", ("vrf_table", Ssh.Server.VrfTable)), ("server-algo", ("server_algo", Ssh.Server.ServerAlgo)), ("capability", ("capability", Ssh.Server.Capability)), ("netconf-vrf-table", ("netconf_vrf_table", Ssh.Server.NetconfVrfTable))])
            self._leafs = OrderedDict([
                ('rekey_volume', (YLeaf(YType.uint32, 'rekey-volume'), ['int'])),
                ('session_limit', (YLeaf(YType.uint32, 'session-limit'), ['int'])),
                ('netconf', (YLeaf(YType.uint32, 'netconf'), ['int'])),
                ('v2', (YLeaf(YType.empty, 'v2'), ['Empty'])),
                ('tcp_window_scale', (YLeaf(YType.uint32, 'tcp-window-scale'), ['int'])),
                ('rekey_time', (YLeaf(YType.uint32, 'rekey-time'), ['int'])),
                ('logging', (YLeaf(YType.empty, 'logging'), ['Empty'])),
                ('rate_limit', (YLeaf(YType.uint32, 'rate-limit'), ['int'])),
                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                ('dscp', (YLeaf(YType.uint32, 'dscp'), ['int'])),
            ])
            self.rekey_volume = None
            self.session_limit = None
            self.netconf = None
            self.v2 = None
            self.tcp_window_scale = None
            self.rekey_time = None
            self.logging = None
            self.rate_limit = None
            self.timeout = None
            self.dscp = None

            self.disable = Ssh.Server.Disable()
            self.disable.parent = self
            self._children_name_map["disable"] = "disable"

            self.enable = Ssh.Server.Enable()
            self.enable.parent = self
            self._children_name_map["enable"] = "enable"

            self.vrf_table = Ssh.Server.VrfTable()
            self.vrf_table.parent = self
            self._children_name_map["vrf_table"] = "vrf-table"

            self.server_algo = Ssh.Server.ServerAlgo()
            self.server_algo.parent = self
            self._children_name_map["server_algo"] = "server-algo"

            self.capability = Ssh.Server.Capability()
            self.capability.parent = self
            self._children_name_map["capability"] = "capability"

            self.netconf_vrf_table = Ssh.Server.NetconfVrfTable()
            self.netconf_vrf_table.parent = self
            self._children_name_map["netconf_vrf_table"] = "netconf-vrf-table"
            self._segment_path = lambda: "server"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ssh.Server, ['rekey_volume', 'session_limit', 'netconf', 'v2', 'tcp_window_scale', 'rekey_time', 'logging', 'rate_limit', 'timeout', 'dscp'], name, value)


        class Disable(_Entity_):
            """
            disable
            
            .. attribute:: hmac
            
            	hmac
            	**type**\:  :py:class:`Hmac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.Disable.Hmac>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2019-03-28'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh.Server.Disable, self).__init__()

                self.yang_name = "disable"
                self.yang_parent_name = "server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("hmac", ("hmac", Ssh.Server.Disable.Hmac))])
                self._leafs = OrderedDict()

                self.hmac = Ssh.Server.Disable.Hmac()
                self.hmac.parent = self
                self._children_name_map["hmac"] = "hmac"
                self._segment_path = lambda: "disable"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Server.Disable, [], name, value)


            class Hmac(_Entity_):
                """
                hmac
                
                .. attribute:: hmac_sha512
                
                	Disable Hmac\-sha2\-512 negotiation
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: hmac_sha1
                
                	Disable Hmac\-sha1 negotiation
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2019-03-28'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Server.Disable.Hmac, self).__init__()

                    self.yang_name = "hmac"
                    self.yang_parent_name = "disable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('hmac_sha512', (YLeaf(YType.boolean, 'hmac-sha512'), ['bool'])),
                        ('hmac_sha1', (YLeaf(YType.boolean, 'hmac-sha1'), ['bool'])),
                    ])
                    self.hmac_sha512 = None
                    self.hmac_sha1 = None
                    self._segment_path = lambda: "hmac"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/disable/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Server.Disable.Hmac, ['hmac_sha512', 'hmac_sha1'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                    return meta._meta_table['Ssh.Server.Disable.Hmac']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                return meta._meta_table['Ssh.Server.Disable']['meta_info']


        class Enable(_Entity_):
            """
            enable
            
            .. attribute:: cipher
            
            	Enable AES\-CBC and 3DES\-CBC ciphers
            	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.Enable.Cipher>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2019-03-28'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh.Server.Enable, self).__init__()

                self.yang_name = "enable"
                self.yang_parent_name = "server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("cipher", ("cipher", Ssh.Server.Enable.Cipher))])
                self._leafs = OrderedDict()

                self.cipher = Ssh.Server.Enable.Cipher()
                self.cipher.parent = self
                self._children_name_map["cipher"] = "cipher"
                self._segment_path = lambda: "enable"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Server.Enable, [], name, value)


            class Cipher(_Entity_):
                """
                Enable AES\-CBC and 3DES\-CBC ciphers
                
                .. attribute:: aes_cbc
                
                	Enable aes\-cbc ciphers
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: tripledes_cbc
                
                	Enable 3des\-cbc cipher
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2019-03-28'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Server.Enable.Cipher, self).__init__()

                    self.yang_name = "cipher"
                    self.yang_parent_name = "enable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('aes_cbc', (YLeaf(YType.boolean, 'aes-cbc'), ['bool'])),
                        ('tripledes_cbc', (YLeaf(YType.boolean, 'tripledes-cbc'), ['bool'])),
                    ])
                    self.aes_cbc = None
                    self.tripledes_cbc = None
                    self._segment_path = lambda: "cipher"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/enable/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Server.Enable.Cipher, ['aes_cbc', 'tripledes_cbc'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                    return meta._meta_table['Ssh.Server.Enable.Cipher']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                return meta._meta_table['Ssh.Server.Enable']['meta_info']


        class VrfTable(_Entity_):
            """
            Cisco sshd VRF name
            
            .. attribute:: vrf
            
            	Enter VRF name
            	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.VrfTable.Vrf>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2019-03-28'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh.Server.VrfTable, self).__init__()

                self.yang_name = "vrf-table"
                self.yang_parent_name = "server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("vrf", ("vrf", Ssh.Server.VrfTable.Vrf))])
                self._leafs = OrderedDict()

                self.vrf = YList(self)
                self._segment_path = lambda: "vrf-table"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Server.VrfTable, [], name, value)


            class Vrf(_Entity_):
                """
                Enter VRF name
                
                .. attribute:: vrf_name  (key)
                
                	Enter VRF name
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: enable
                
                	Enable to use VRF
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: ipv4_access_list
                
                	SSH v4 access\-list name
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: ipv6_access_list
                
                	SSH v6 access\-list name
                	**type**\: str
                
                	**length:** 1..32
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2019-03-28'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Server.VrfTable.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrf-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ('ipv4_access_list', (YLeaf(YType.str, 'ipv4-access-list'), ['str'])),
                        ('ipv6_access_list', (YLeaf(YType.str, 'ipv6-access-list'), ['str'])),
                    ])
                    self.vrf_name = None
                    self.enable = None
                    self.ipv4_access_list = None
                    self.ipv6_access_list = None
                    self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/vrf-table/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Server.VrfTable.Vrf, ['vrf_name', 'enable', 'ipv4_access_list', 'ipv6_access_list'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                    return meta._meta_table['Ssh.Server.VrfTable.Vrf']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                return meta._meta_table['Ssh.Server.VrfTable']['meta_info']


        class ServerAlgo(_Entity_):
            """
            Cisco ssh algorithms
            
            .. attribute:: key_exchanges
            
            	Key exchange algorithm
            	**type**\:  :py:class:`KeyExchanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.ServerAlgo.KeyExchanges>`
            
            .. attribute:: ciphers
            
            	cipher algorithm
            	**type**\:  :py:class:`Ciphers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.ServerAlgo.Ciphers>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2019-03-28'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh.Server.ServerAlgo, self).__init__()

                self.yang_name = "server-algo"
                self.yang_parent_name = "server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("key-exchanges", ("key_exchanges", Ssh.Server.ServerAlgo.KeyExchanges)), ("ciphers", ("ciphers", Ssh.Server.ServerAlgo.Ciphers))])
                self._leafs = OrderedDict()

                self.key_exchanges = Ssh.Server.ServerAlgo.KeyExchanges()
                self.key_exchanges.parent = self
                self._children_name_map["key_exchanges"] = "key-exchanges"

                self.ciphers = Ssh.Server.ServerAlgo.Ciphers()
                self.ciphers.parent = self
                self._children_name_map["ciphers"] = "ciphers"
                self._segment_path = lambda: "server-algo"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Server.ServerAlgo, [], name, value)


            class KeyExchanges(_Entity_):
                """
                Key exchange algorithm
                
                .. attribute:: key_exchange
                
                	key exchange algorithm
                	**type**\: list of str
                
                	**length:** 1..32
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2019-03-28'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Server.ServerAlgo.KeyExchanges, self).__init__()

                    self.yang_name = "key-exchanges"
                    self.yang_parent_name = "server-algo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('key_exchange', (YLeafList(YType.str, 'key-exchange'), ['str'])),
                    ])
                    self.key_exchange = []
                    self._segment_path = lambda: "key-exchanges"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/server-algo/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Server.ServerAlgo.KeyExchanges, ['key_exchange'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                    return meta._meta_table['Ssh.Server.ServerAlgo.KeyExchanges']['meta_info']


            class Ciphers(_Entity_):
                """
                cipher algorithm
                
                .. attribute:: cipher
                
                	Cipher algorithm
                	**type**\: list of str
                
                	**length:** 1..32
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2019-03-28'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Server.ServerAlgo.Ciphers, self).__init__()

                    self.yang_name = "ciphers"
                    self.yang_parent_name = "server-algo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('cipher', (YLeafList(YType.str, 'cipher'), ['str'])),
                    ])
                    self.cipher = []
                    self._segment_path = lambda: "ciphers"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/server-algo/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Server.ServerAlgo.Ciphers, ['cipher'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                    return meta._meta_table['Ssh.Server.ServerAlgo.Ciphers']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                return meta._meta_table['Ssh.Server.ServerAlgo']['meta_info']


        class Capability(_Entity_):
            """
            Capability
            
            .. attribute:: netconf_xml
            
            	Enable Netconf\-XML stack on port 22
            	**type**\: bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2019-03-28'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh.Server.Capability, self).__init__()

                self.yang_name = "capability"
                self.yang_parent_name = "server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('netconf_xml', (YLeaf(YType.boolean, 'netconf-xml'), ['bool'])),
                ])
                self.netconf_xml = None
                self._segment_path = lambda: "capability"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Server.Capability, ['netconf_xml'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                return meta._meta_table['Ssh.Server.Capability']['meta_info']


        class NetconfVrfTable(_Entity_):
            """
            Cisco sshd Netconf VRF name
            
            .. attribute:: vrf
            
            	Enter VRF name
            	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.NetconfVrfTable.Vrf>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2019-03-28'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh.Server.NetconfVrfTable, self).__init__()

                self.yang_name = "netconf-vrf-table"
                self.yang_parent_name = "server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("vrf", ("vrf", Ssh.Server.NetconfVrfTable.Vrf))])
                self._leafs = OrderedDict()

                self.vrf = YList(self)
                self._segment_path = lambda: "netconf-vrf-table"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Server.NetconfVrfTable, [], name, value)


            class Vrf(_Entity_):
                """
                Enter VRF name
                
                .. attribute:: vrf_name  (key)
                
                	Enter VRF name
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: enable
                
                	Enable to use VRF
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: ipv4_access_list
                
                	SSH v4 access\-list name
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: ipv6_access_list
                
                	SSH v6 access\-list name
                	**type**\: str
                
                	**length:** 1..32
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2019-03-28'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Server.NetconfVrfTable.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "netconf-vrf-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ('ipv4_access_list', (YLeaf(YType.str, 'ipv4-access-list'), ['str'])),
                        ('ipv6_access_list', (YLeaf(YType.str, 'ipv6-access-list'), ['str'])),
                    ])
                    self.vrf_name = None
                    self.enable = None
                    self.ipv4_access_list = None
                    self.ipv6_access_list = None
                    self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/netconf-vrf-table/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Server.NetconfVrfTable.Vrf, ['vrf_name', 'enable', 'ipv4_access_list', 'ipv6_access_list'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                    return meta._meta_table['Ssh.Server.NetconfVrfTable.Vrf']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                return meta._meta_table['Ssh.Server.NetconfVrfTable']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
            return meta._meta_table['Ssh.Server']['meta_info']


    class BackupServer(_Entity_):
        """
        Provide SSH server service
        
        .. attribute:: backup_port_vrf
        
        	backup server config
        	**type**\:  :py:class:`BackupPortVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.BackupServer.BackupPortVrf>`
        
        	**presence node**\: True
        
        

        """

        _prefix = 'crypto-ssh-cfg'
        _revision = '2019-03-28'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ssh.BackupServer, self).__init__()

            self.yang_name = "backup-server"
            self.yang_parent_name = "ssh"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("backup-port-vrf", ("backup_port_vrf", Ssh.BackupServer.BackupPortVrf))])
            self._leafs = OrderedDict()

            self.backup_port_vrf = None
            self._children_name_map["backup_port_vrf"] = "backup-port-vrf"
            self._segment_path = lambda: "backup-server"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ssh.BackupServer, [], name, value)


        class BackupPortVrf(_Entity_):
            """
            backup server config
            
            .. attribute:: port
            
            	Port number
            	**type**\: int
            
            	**range:** 11000..15000
            
            	**mandatory**\: True
            
            .. attribute:: vrf_name
            
            	VRF name (max\:32 chars)
            	**type**\: str
            
            	**length:** 1..32
            
            	**mandatory**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2019-03-28'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh.BackupServer.BackupPortVrf, self).__init__()

                self.yang_name = "backup-port-vrf"
                self.yang_parent_name = "backup-server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.port = None
                self.vrf_name = None
                self._segment_path = lambda: "backup-port-vrf"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/backup-server/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.BackupServer.BackupPortVrf, ['port', 'vrf_name'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
                return meta._meta_table['Ssh.BackupServer.BackupPortVrf']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
            return meta._meta_table['Ssh.BackupServer']['meta_info']

    def clone_ptr(self):
        self._top_entity = Ssh()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_cfg as meta
        return meta._meta_table['Ssh']['meta_info']



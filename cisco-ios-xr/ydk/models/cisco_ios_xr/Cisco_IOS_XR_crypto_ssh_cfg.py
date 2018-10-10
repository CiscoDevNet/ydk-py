""" Cisco_IOS_XR_crypto_ssh_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-ssh package configuration.

This module contains definitions
for the following management objects\:
  ssh\: Secure Shell configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Ssh(Entity):
    """
    Secure Shell configuration
    
    .. attribute:: client
    
    	Provide SSH client service
    	**type**\:  :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Client>`
    
    .. attribute:: server
    
    	Provide SSH server service
    	**type**\:  :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server>`
    
    

    """

    _prefix = 'crypto-ssh-cfg'
    _revision = '2018-05-24'

    def __init__(self):
        super(Ssh, self).__init__()
        self._top_entity = None

        self.yang_name = "ssh"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-ssh-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("client", ("client", Ssh.Client)), ("server", ("server", Ssh.Server))])
        self._leafs = OrderedDict()

        self.client = Ssh.Client()
        self.client.parent = self
        self._children_name_map["client"] = "client"

        self.server = Ssh.Server()
        self.server.parent = self
        self._children_name_map["server"] = "server"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ssh, [], name, value)


    class Client(Entity):
        """
        Provide SSH client service
        
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
        _revision = '2018-05-24'

        def __init__(self):
            super(Ssh.Client, self).__init__()

            self.yang_name = "client"
            self.yang_parent_name = "ssh"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("client-algo", ("client_algo", Ssh.Client.ClientAlgo)), ("client-enable", ("client_enable", Ssh.Client.ClientEnable))])
            self._leafs = OrderedDict([
                ('rekey_volume', (YLeaf(YType.uint32, 'rekey-volume'), ['int'])),
                ('host_public_key', (YLeaf(YType.str, 'host-public-key'), ['str'])),
                ('client_vrf', (YLeaf(YType.str, 'client-vrf'), ['str'])),
                ('rekey_time', (YLeaf(YType.uint32, 'rekey-time'), ['int'])),
                ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                ('dscp', (YLeaf(YType.uint32, 'dscp'), ['int'])),
            ])
            self.rekey_volume = None
            self.host_public_key = None
            self.client_vrf = None
            self.rekey_time = None
            self.source_interface = None
            self.dscp = None

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
            self._perform_setattr(Ssh.Client, ['rekey_volume', 'host_public_key', 'client_vrf', 'rekey_time', 'source_interface', 'dscp'], name, value)


        class ClientAlgo(Entity):
            """
            Cisco ssh algorithms
            
            .. attribute:: key_exchanges
            
            	Key exchange algorithm
            	**type**\:  :py:class:`KeyExchanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Client.ClientAlgo.KeyExchanges>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2018-05-24'

            def __init__(self):
                super(Ssh.Client.ClientAlgo, self).__init__()

                self.yang_name = "client-algo"
                self.yang_parent_name = "client"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("key-exchanges", ("key_exchanges", Ssh.Client.ClientAlgo.KeyExchanges))])
                self._leafs = OrderedDict()

                self.key_exchanges = Ssh.Client.ClientAlgo.KeyExchanges()
                self.key_exchanges.parent = self
                self._children_name_map["key_exchanges"] = "key-exchanges"
                self._segment_path = lambda: "client-algo"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/client/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Client.ClientAlgo, [], name, value)


            class KeyExchanges(Entity):
                """
                Key exchange algorithm
                
                .. attribute:: key_exchange
                
                	key exchange algorithm
                	**type**\: list of str
                
                	**length:** 1..32
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2018-05-24'

                def __init__(self):
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


        class ClientEnable(Entity):
            """
            clientenable
            
            .. attribute:: client_cipher
            
            	Enable AES\-CBC and 3DES\_CBC for ssh client
            	**type**\:  :py:class:`ClientCipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Client.ClientEnable.ClientCipher>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2018-05-24'

            def __init__(self):
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


            class ClientCipher(Entity):
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
                _revision = '2018-05-24'

                def __init__(self):
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


    class Server(Entity):
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
        _revision = '2018-05-24'

        def __init__(self):
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
            self._perform_setattr(Ssh.Server, ['rekey_volume', 'session_limit', 'netconf', 'v2', 'rekey_time', 'logging', 'rate_limit', 'timeout', 'dscp'], name, value)


        class Disable(Entity):
            """
            disable
            
            .. attribute:: hmac
            
            	hmac
            	**type**\:  :py:class:`Hmac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.Disable.Hmac>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2018-05-24'

            def __init__(self):
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


            class Hmac(Entity):
                """
                hmac
                
                .. attribute:: hmac_sha512
                
                	Disable Hmac\-sha2\-512 negotiation
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2018-05-24'

                def __init__(self):
                    super(Ssh.Server.Disable.Hmac, self).__init__()

                    self.yang_name = "hmac"
                    self.yang_parent_name = "disable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('hmac_sha512', (YLeaf(YType.boolean, 'hmac-sha512'), ['bool'])),
                    ])
                    self.hmac_sha512 = None
                    self._segment_path = lambda: "hmac"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/disable/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Server.Disable.Hmac, ['hmac_sha512'], name, value)


        class Enable(Entity):
            """
            enable
            
            .. attribute:: cipher
            
            	Enable AES\-CBC and 3DES\-CBC ciphers
            	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.Enable.Cipher>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2018-05-24'

            def __init__(self):
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


            class Cipher(Entity):
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
                _revision = '2018-05-24'

                def __init__(self):
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


        class VrfTable(Entity):
            """
            Cisco sshd VRF name
            
            .. attribute:: vrf
            
            	Enter VRF name
            	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.VrfTable.Vrf>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2018-05-24'

            def __init__(self):
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


            class Vrf(Entity):
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
                _revision = '2018-05-24'

                def __init__(self):
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


        class ServerAlgo(Entity):
            """
            Cisco ssh algorithms
            
            .. attribute:: key_exchanges
            
            	Key exchange algorithm
            	**type**\:  :py:class:`KeyExchanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.ServerAlgo.KeyExchanges>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2018-05-24'

            def __init__(self):
                super(Ssh.Server.ServerAlgo, self).__init__()

                self.yang_name = "server-algo"
                self.yang_parent_name = "server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("key-exchanges", ("key_exchanges", Ssh.Server.ServerAlgo.KeyExchanges))])
                self._leafs = OrderedDict()

                self.key_exchanges = Ssh.Server.ServerAlgo.KeyExchanges()
                self.key_exchanges.parent = self
                self._children_name_map["key_exchanges"] = "key-exchanges"
                self._segment_path = lambda: "server-algo"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Server.ServerAlgo, [], name, value)


            class KeyExchanges(Entity):
                """
                Key exchange algorithm
                
                .. attribute:: key_exchange
                
                	key exchange algorithm
                	**type**\: list of str
                
                	**length:** 1..32
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2018-05-24'

                def __init__(self):
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


        class Capability(Entity):
            """
            Capability
            
            .. attribute:: netconf_xml
            
            	Enable Netconf\-XML stack on port 22
            	**type**\: bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2018-05-24'

            def __init__(self):
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


        class NetconfVrfTable(Entity):
            """
            Cisco sshd Netconf VRF name
            
            .. attribute:: vrf
            
            	Enter VRF name
            	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.NetconfVrfTable.Vrf>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2018-05-24'

            def __init__(self):
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


            class Vrf(Entity):
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
                _revision = '2018-05-24'

                def __init__(self):
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

    def clone_ptr(self):
        self._top_entity = Ssh()
        return self._top_entity


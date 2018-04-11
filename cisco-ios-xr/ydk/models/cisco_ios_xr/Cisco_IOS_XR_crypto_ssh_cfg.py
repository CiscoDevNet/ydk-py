""" Cisco_IOS_XR_crypto_ssh_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-ssh package configuration.

This module contains definitions
for the following management objects\:
  ssh\: Secure Shell configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
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
    _revision = '2017-11-21'

    def __init__(self):
        super(Ssh, self).__init__()
        self._top_entity = None

        self.yang_name = "ssh"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-ssh-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("client", ("client", Ssh.Client)), ("server", ("server", Ssh.Server))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.client = Ssh.Client()
        self.client.parent = self
        self._children_name_map["client"] = "client"
        self._children_yang_names.add("client")

        self.server = Ssh.Server()
        self.server.parent = self
        self._children_name_map["server"] = "server"
        self._children_yang_names.add("server")
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh"


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
        
        	**pattern:** [a\-zA\-Z0\-9./\-]+
        
        .. attribute:: dscp
        
        	Cisco sshd DSCP value
        	**type**\: int
        
        	**range:** 0..63
        
        

        """

        _prefix = 'crypto-ssh-cfg'
        _revision = '2017-11-21'

        def __init__(self):
            super(Ssh.Client, self).__init__()

            self.yang_name = "client"
            self.yang_parent_name = "ssh"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("client-algo", ("client_algo", Ssh.Client.ClientAlgo)), ("client-enable", ("client_enable", Ssh.Client.ClientEnable))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('rekey_volume', YLeaf(YType.uint32, 'rekey-volume')),
                ('host_public_key', YLeaf(YType.str, 'host-public-key')),
                ('client_vrf', YLeaf(YType.str, 'client-vrf')),
                ('rekey_time', YLeaf(YType.uint32, 'rekey-time')),
                ('source_interface', YLeaf(YType.str, 'source-interface')),
                ('dscp', YLeaf(YType.uint32, 'dscp')),
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
            self._children_yang_names.add("client-algo")

            self.client_enable = Ssh.Client.ClientEnable()
            self.client_enable.parent = self
            self._children_name_map["client_enable"] = "client-enable"
            self._children_yang_names.add("client-enable")
            self._segment_path = lambda: "client"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ssh.Client, ['rekey_volume', 'host_public_key', 'client_vrf', 'rekey_time', 'source_interface', 'dscp'], name, value)


        class ClientAlgo(Entity):
            """
            Cisco ssh algorithms
            
            .. attribute:: key_exchange
            
            	Key exchange algorithm
            	**type**\:  :py:class:`KeyExchange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Client.ClientAlgo.KeyExchange>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2017-11-21'

            def __init__(self):
                super(Ssh.Client.ClientAlgo, self).__init__()

                self.yang_name = "client-algo"
                self.yang_parent_name = "client"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("key-exchange", ("key_exchange", Ssh.Client.ClientAlgo.KeyExchange))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.key_exchange = None
                self._children_name_map["key_exchange"] = "key-exchange"
                self._children_yang_names.add("key-exchange")
                self._segment_path = lambda: "client-algo"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/client/%s" % self._segment_path()


            class KeyExchange(Entity):
                """
                Key exchange algorithm
                
                .. attribute:: kex_algo1st
                
                	key exchange algorithm
                	**type**\: str
                
                	**length:** 1..32
                
                	**mandatory**\: True
                
                .. attribute:: kex_algo2nd
                
                	key exchange algorithm
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: kex_algo3rd
                
                	key exchange algorithm
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: kex_algo4th
                
                	key exchange algorithm
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: kex_algo5th
                
                	key exchange algorithm
                	**type**\: str
                
                	**length:** 1..32
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2017-11-21'

                def __init__(self):
                    super(Ssh.Client.ClientAlgo.KeyExchange, self).__init__()

                    self.yang_name = "key-exchange"
                    self.yang_parent_name = "client-algo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('kex_algo1st', YLeaf(YType.str, 'kex-algo1st')),
                        ('kex_algo2nd', YLeaf(YType.str, 'kex-algo2nd')),
                        ('kex_algo3rd', YLeaf(YType.str, 'kex-algo3rd')),
                        ('kex_algo4th', YLeaf(YType.str, 'kex-algo4th')),
                        ('kex_algo5th', YLeaf(YType.str, 'kex-algo5th')),
                    ])
                    self.kex_algo1st = None
                    self.kex_algo2nd = None
                    self.kex_algo3rd = None
                    self.kex_algo4th = None
                    self.kex_algo5th = None
                    self._segment_path = lambda: "key-exchange"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/client/client-algo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Client.ClientAlgo.KeyExchange, ['kex_algo1st', 'kex_algo2nd', 'kex_algo3rd', 'kex_algo4th', 'kex_algo5th'], name, value)


        class ClientEnable(Entity):
            """
            clientenable
            
            .. attribute:: client_cipher
            
            	clientcipher
            	**type**\:  :py:class:`ClientCipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Client.ClientEnable.ClientCipher>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2017-11-21'

            def __init__(self):
                super(Ssh.Client.ClientEnable, self).__init__()

                self.yang_name = "client-enable"
                self.yang_parent_name = "client"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("client-cipher", ("client_cipher", Ssh.Client.ClientEnable.ClientCipher))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.client_cipher = Ssh.Client.ClientEnable.ClientCipher()
                self.client_cipher.parent = self
                self._children_name_map["client_cipher"] = "client-cipher"
                self._children_yang_names.add("client-cipher")
                self._segment_path = lambda: "client-enable"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/client/%s" % self._segment_path()


            class ClientCipher(Entity):
                """
                clientcipher
                
                .. attribute:: aescbc
                
                	Enable AES\-CBC ciphers for client
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2017-11-21'

                def __init__(self):
                    super(Ssh.Client.ClientEnable.ClientCipher, self).__init__()

                    self.yang_name = "client-cipher"
                    self.yang_parent_name = "client-enable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('aescbc', YLeaf(YType.boolean, 'aescbc')),
                    ])
                    self.aescbc = None
                    self._segment_path = lambda: "client-cipher"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/client/client-enable/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Client.ClientEnable.ClientCipher, ['aescbc'], name, value)


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
        _revision = '2017-11-21'

        def __init__(self):
            super(Ssh.Server, self).__init__()

            self.yang_name = "server"
            self.yang_parent_name = "ssh"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("disable", ("disable", Ssh.Server.Disable)), ("enable", ("enable", Ssh.Server.Enable)), ("vrf-table", ("vrf_table", Ssh.Server.VrfTable)), ("server-algo", ("server_algo", Ssh.Server.ServerAlgo)), ("capability", ("capability", Ssh.Server.Capability)), ("netconf-vrf-table", ("netconf_vrf_table", Ssh.Server.NetconfVrfTable))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('rekey_volume', YLeaf(YType.uint32, 'rekey-volume')),
                ('session_limit', YLeaf(YType.uint32, 'session-limit')),
                ('netconf', YLeaf(YType.uint32, 'netconf')),
                ('v2', YLeaf(YType.empty, 'v2')),
                ('rekey_time', YLeaf(YType.uint32, 'rekey-time')),
                ('logging', YLeaf(YType.empty, 'logging')),
                ('rate_limit', YLeaf(YType.uint32, 'rate-limit')),
                ('timeout', YLeaf(YType.uint32, 'timeout')),
                ('dscp', YLeaf(YType.uint32, 'dscp')),
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
            self._children_yang_names.add("disable")

            self.enable = Ssh.Server.Enable()
            self.enable.parent = self
            self._children_name_map["enable"] = "enable"
            self._children_yang_names.add("enable")

            self.vrf_table = Ssh.Server.VrfTable()
            self.vrf_table.parent = self
            self._children_name_map["vrf_table"] = "vrf-table"
            self._children_yang_names.add("vrf-table")

            self.server_algo = Ssh.Server.ServerAlgo()
            self.server_algo.parent = self
            self._children_name_map["server_algo"] = "server-algo"
            self._children_yang_names.add("server-algo")

            self.capability = Ssh.Server.Capability()
            self.capability.parent = self
            self._children_name_map["capability"] = "capability"
            self._children_yang_names.add("capability")

            self.netconf_vrf_table = Ssh.Server.NetconfVrfTable()
            self.netconf_vrf_table.parent = self
            self._children_name_map["netconf_vrf_table"] = "netconf-vrf-table"
            self._children_yang_names.add("netconf-vrf-table")
            self._segment_path = lambda: "server"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/%s" % self._segment_path()

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
            _revision = '2017-11-21'

            def __init__(self):
                super(Ssh.Server.Disable, self).__init__()

                self.yang_name = "disable"
                self.yang_parent_name = "server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("hmac", ("hmac", Ssh.Server.Disable.Hmac))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.hmac = Ssh.Server.Disable.Hmac()
                self.hmac.parent = self
                self._children_name_map["hmac"] = "hmac"
                self._children_yang_names.add("hmac")
                self._segment_path = lambda: "disable"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()


            class Hmac(Entity):
                """
                hmac
                
                .. attribute:: hmac_sha512
                
                	Disable Hmac\-sha2\-512 negotiation
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2017-11-21'

                def __init__(self):
                    super(Ssh.Server.Disable.Hmac, self).__init__()

                    self.yang_name = "hmac"
                    self.yang_parent_name = "disable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('hmac_sha512', YLeaf(YType.boolean, 'hmac-sha512')),
                    ])
                    self.hmac_sha512 = None
                    self._segment_path = lambda: "hmac"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/disable/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Server.Disable.Hmac, ['hmac_sha512'], name, value)


        class Enable(Entity):
            """
            enable
            
            .. attribute:: cipher
            
            	cipher
            	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.Enable.Cipher>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2017-11-21'

            def __init__(self):
                super(Ssh.Server.Enable, self).__init__()

                self.yang_name = "enable"
                self.yang_parent_name = "server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("cipher", ("cipher", Ssh.Server.Enable.Cipher))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.cipher = Ssh.Server.Enable.Cipher()
                self.cipher.parent = self
                self._children_name_map["cipher"] = "cipher"
                self._children_yang_names.add("cipher")
                self._segment_path = lambda: "enable"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()


            class Cipher(Entity):
                """
                cipher
                
                .. attribute:: aescbc
                
                	Enable AES\-CBC ciphers
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2017-11-21'

                def __init__(self):
                    super(Ssh.Server.Enable.Cipher, self).__init__()

                    self.yang_name = "cipher"
                    self.yang_parent_name = "enable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('aescbc', YLeaf(YType.boolean, 'aescbc')),
                    ])
                    self.aescbc = None
                    self._segment_path = lambda: "cipher"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/enable/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Server.Enable.Cipher, ['aescbc'], name, value)


        class VrfTable(Entity):
            """
            Cisco sshd VRF name
            
            .. attribute:: vrf
            
            	Enter VRF name
            	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.VrfTable.Vrf>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2017-11-21'

            def __init__(self):
                super(Ssh.Server.VrfTable, self).__init__()

                self.yang_name = "vrf-table"
                self.yang_parent_name = "server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("vrf", ("vrf", Ssh.Server.VrfTable.Vrf))])
                self._leafs = OrderedDict()

                self.vrf = YList(self)
                self._segment_path = lambda: "vrf-table"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()

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
                _revision = '2017-11-21'

                def __init__(self):
                    super(Ssh.Server.VrfTable.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrf-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                        ('enable', YLeaf(YType.empty, 'enable')),
                        ('ipv4_access_list', YLeaf(YType.str, 'ipv4-access-list')),
                        ('ipv6_access_list', YLeaf(YType.str, 'ipv6-access-list')),
                    ])
                    self.vrf_name = None
                    self.enable = None
                    self.ipv4_access_list = None
                    self.ipv6_access_list = None
                    self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/vrf-table/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Server.VrfTable.Vrf, ['vrf_name', 'enable', 'ipv4_access_list', 'ipv6_access_list'], name, value)


        class ServerAlgo(Entity):
            """
            Cisco ssh algorithms
            
            .. attribute:: key_exchange
            
            	Key exchange algorithm
            	**type**\:  :py:class:`KeyExchange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_cfg.Ssh.Server.ServerAlgo.KeyExchange>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2017-11-21'

            def __init__(self):
                super(Ssh.Server.ServerAlgo, self).__init__()

                self.yang_name = "server-algo"
                self.yang_parent_name = "server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("key-exchange", ("key_exchange", Ssh.Server.ServerAlgo.KeyExchange))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.key_exchange = None
                self._children_name_map["key_exchange"] = "key-exchange"
                self._children_yang_names.add("key-exchange")
                self._segment_path = lambda: "server-algo"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()


            class KeyExchange(Entity):
                """
                Key exchange algorithm
                
                .. attribute:: kex_algo1st
                
                	key exchange algorithm
                	**type**\: str
                
                	**length:** 1..32
                
                	**mandatory**\: True
                
                .. attribute:: kex_algo2nd
                
                	key exchange algorithm
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: kex_algo3rd
                
                	key exchange algorithm
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: kex_algo4th
                
                	key exchange algorithm
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: kex_algo5th
                
                	key exchange algorithm
                	**type**\: str
                
                	**length:** 1..32
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2017-11-21'

                def __init__(self):
                    super(Ssh.Server.ServerAlgo.KeyExchange, self).__init__()

                    self.yang_name = "key-exchange"
                    self.yang_parent_name = "server-algo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('kex_algo1st', YLeaf(YType.str, 'kex-algo1st')),
                        ('kex_algo2nd', YLeaf(YType.str, 'kex-algo2nd')),
                        ('kex_algo3rd', YLeaf(YType.str, 'kex-algo3rd')),
                        ('kex_algo4th', YLeaf(YType.str, 'kex-algo4th')),
                        ('kex_algo5th', YLeaf(YType.str, 'kex-algo5th')),
                    ])
                    self.kex_algo1st = None
                    self.kex_algo2nd = None
                    self.kex_algo3rd = None
                    self.kex_algo4th = None
                    self.kex_algo5th = None
                    self._segment_path = lambda: "key-exchange"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/server-algo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Server.ServerAlgo.KeyExchange, ['kex_algo1st', 'kex_algo2nd', 'kex_algo3rd', 'kex_algo4th', 'kex_algo5th'], name, value)


        class Capability(Entity):
            """
            Capability
            
            .. attribute:: netconf_xml
            
            	Enable Netconf\-XML stack on port 22
            	**type**\: bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2017-11-21'

            def __init__(self):
                super(Ssh.Server.Capability, self).__init__()

                self.yang_name = "capability"
                self.yang_parent_name = "server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('netconf_xml', YLeaf(YType.boolean, 'netconf-xml')),
                ])
                self.netconf_xml = None
                self._segment_path = lambda: "capability"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()

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
            _revision = '2017-11-21'

            def __init__(self):
                super(Ssh.Server.NetconfVrfTable, self).__init__()

                self.yang_name = "netconf-vrf-table"
                self.yang_parent_name = "server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("vrf", ("vrf", Ssh.Server.NetconfVrfTable.Vrf))])
                self._leafs = OrderedDict()

                self.vrf = YList(self)
                self._segment_path = lambda: "netconf-vrf-table"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()

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
                _revision = '2017-11-21'

                def __init__(self):
                    super(Ssh.Server.NetconfVrfTable.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "netconf-vrf-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                        ('enable', YLeaf(YType.empty, 'enable')),
                        ('ipv4_access_list', YLeaf(YType.str, 'ipv4-access-list')),
                        ('ipv6_access_list', YLeaf(YType.str, 'ipv6-access-list')),
                    ])
                    self.vrf_name = None
                    self.enable = None
                    self.ipv4_access_list = None
                    self.ipv6_access_list = None
                    self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/netconf-vrf-table/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Server.NetconfVrfTable.Vrf, ['vrf_name', 'enable', 'ipv4_access_list', 'ipv6_access_list'], name, value)

    def clone_ptr(self):
        self._top_entity = Ssh()
        return self._top_entity


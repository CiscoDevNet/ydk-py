""" Cisco_IOS_XR_crypto_sam_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-sam package configuration.

This module contains definitions
for the following management objects\:
  crypto\: Crypto configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CryptoSamAction(Enum):
    """
    CryptoSamAction

    Crypto sam action

    .. data:: proceed = 1

    	To respond YES to the SAM prompt

    .. data:: terminate = 2

    	To respond NO to the SAM prompt

    """

    proceed = Enum.YLeaf(1, "proceed")

    terminate = Enum.YLeaf(2, "terminate")



class Crypto(Entity):
    """
    Crypto configuration
    
    .. attribute:: sam
    
    	Software Authentication Manager (SAM) Config
    	**type**\:   :py:class:`Sam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Sam>`
    
    .. attribute:: ssh
    
    	Secure Shell configuration
    	**type**\:   :py:class:`Ssh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh>`
    
    

    """

    _prefix = 'crypto-sam-cfg'
    _revision = '2015-01-07'

    def __init__(self):
        super(Crypto, self).__init__()
        self._top_entity = None

        self.yang_name = "crypto"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-sam-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"sam" : ("sam", Crypto.Sam), "ssh" : ("ssh", Crypto.Ssh)}
        self._child_list_classes = {}

        self.sam = Crypto.Sam()
        self.sam.parent = self
        self._children_name_map["sam"] = "sam"
        self._children_yang_names.add("sam")

        self.ssh = Crypto.Ssh()
        self.ssh.parent = self
        self._children_name_map["ssh"] = "ssh"
        self._children_yang_names.add("ssh")
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto"


    class Sam(Entity):
        """
        Software Authentication Manager (SAM) Config
        
        .. attribute:: prompt_interval
        
        	Set prompt interval at reboot time
        	**type**\:   :py:class:`PromptInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Sam.PromptInterval>`
        
        	**presence node**\: True
        
        

        """

        _prefix = 'crypto-sam-cfg'
        _revision = '2015-01-07'

        def __init__(self):
            super(Crypto.Sam, self).__init__()

            self.yang_name = "sam"
            self.yang_parent_name = "crypto"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"prompt-interval" : ("prompt_interval", Crypto.Sam.PromptInterval)}
            self._child_list_classes = {}

            self.prompt_interval = None
            self._children_name_map["prompt_interval"] = "prompt-interval"
            self._children_yang_names.add("prompt-interval")
            self._segment_path = lambda: "sam"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/%s" % self._segment_path()


        class PromptInterval(Entity):
            """
            Set prompt interval at reboot time
            
            .. attribute:: action
            
            	Respond to SAM prompt either Proceed/Terminate
            	**type**\:   :py:class:`CryptoSamAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.CryptoSamAction>`
            
            	**mandatory**\: True
            
            .. attribute:: prompt_time
            
            	Prompt time from 0 \- 300 seconds
            	**type**\:  int
            
            	**range:** 0..300
            
            	**mandatory**\: True
            
            	**units**\: second
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'crypto-sam-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                super(Crypto.Sam.PromptInterval, self).__init__()

                self.yang_name = "prompt-interval"
                self.yang_parent_name = "sam"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}
                self.is_presence_container = True

                self.action = YLeaf(YType.enumeration, "action")

                self.prompt_time = YLeaf(YType.uint32, "prompt-time")
                self._segment_path = lambda: "prompt-interval"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/sam/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Crypto.Sam.PromptInterval, ['action', 'prompt_time'], name, value)


    class Ssh(Entity):
        """
        Secure Shell configuration
        
        .. attribute:: client
        
        	Provide SSH client service
        	**type**\:   :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Client>`
        
        .. attribute:: server
        
        	Provide SSH server service
        	**type**\:   :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server>`
        
        

        """

        _prefix = 'crypto-ssh-cfg'
        _revision = '2017-07-15'

        def __init__(self):
            super(Crypto.Ssh, self).__init__()

            self.yang_name = "ssh"
            self.yang_parent_name = "crypto"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"client" : ("client", Crypto.Ssh.Client), "server" : ("server", Crypto.Ssh.Server)}
            self._child_list_classes = {}

            self.client = Crypto.Ssh.Client()
            self.client.parent = self
            self._children_name_map["client"] = "client"
            self._children_yang_names.add("client")

            self.server = Crypto.Ssh.Server()
            self.server.parent = self
            self._children_name_map["server"] = "server"
            self._children_yang_names.add("server")
            self._segment_path = lambda: "Cisco-IOS-XR-crypto-ssh-cfg:ssh"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/%s" % self._segment_path()


        class Client(Entity):
            """
            Provide SSH client service
            
            .. attribute:: client_enable
            
            	clientenable
            	**type**\:   :py:class:`ClientEnable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Client.ClientEnable>`
            
            .. attribute:: client_vrf
            
            	Source interface VRF for ssh client sessions
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: dscp
            
            	Cisco sshd DSCP value
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: host_public_key
            
            	Filename \- where to store known host file
            	**type**\:  str
            
            .. attribute:: rekey_time
            
            	Configure client time\-based rekey for SSH
            	**type**\:  int
            
            	**range:** 30..1440
            
            	**default value**\: 60
            
            .. attribute:: rekey_volume
            
            	Configure client volume\-based rekey for SSH
            	**type**\:  int
            
            	**range:** 1024..4095
            
            	**default value**\: 1024
            
            .. attribute:: source_interface
            
            	Source interface for ssh client sessions
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2017-07-15'

            def __init__(self):
                super(Crypto.Ssh.Client, self).__init__()

                self.yang_name = "client"
                self.yang_parent_name = "ssh"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"client-enable" : ("client_enable", Crypto.Ssh.Client.ClientEnable)}
                self._child_list_classes = {}

                self.client_vrf = YLeaf(YType.str, "client-vrf")

                self.dscp = YLeaf(YType.uint32, "dscp")

                self.host_public_key = YLeaf(YType.str, "host-public-key")

                self.rekey_time = YLeaf(YType.uint32, "rekey-time")

                self.rekey_volume = YLeaf(YType.uint32, "rekey-volume")

                self.source_interface = YLeaf(YType.str, "source-interface")

                self.client_enable = Crypto.Ssh.Client.ClientEnable()
                self.client_enable.parent = self
                self._children_name_map["client_enable"] = "client-enable"
                self._children_yang_names.add("client-enable")
                self._segment_path = lambda: "client"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Crypto.Ssh.Client, ['client_vrf', 'dscp', 'host_public_key', 'rekey_time', 'rekey_volume', 'source_interface'], name, value)


            class ClientEnable(Entity):
                """
                clientenable
                
                .. attribute:: client_cipher
                
                	clientcipher
                	**type**\:   :py:class:`ClientCipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Client.ClientEnable.ClientCipher>`
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2017-07-15'

                def __init__(self):
                    super(Crypto.Ssh.Client.ClientEnable, self).__init__()

                    self.yang_name = "client-enable"
                    self.yang_parent_name = "client"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"client-cipher" : ("client_cipher", Crypto.Ssh.Client.ClientEnable.ClientCipher)}
                    self._child_list_classes = {}

                    self.client_cipher = Crypto.Ssh.Client.ClientEnable.ClientCipher()
                    self.client_cipher.parent = self
                    self._children_name_map["client_cipher"] = "client-cipher"
                    self._children_yang_names.add("client-cipher")
                    self._segment_path = lambda: "client-enable"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/client/%s" % self._segment_path()


                class ClientCipher(Entity):
                    """
                    clientcipher
                    
                    .. attribute:: aescbc
                    
                    	Enable AES\-CBC ciphers for client
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'crypto-ssh-cfg'
                    _revision = '2017-07-15'

                    def __init__(self):
                        super(Crypto.Ssh.Client.ClientEnable.ClientCipher, self).__init__()

                        self.yang_name = "client-cipher"
                        self.yang_parent_name = "client-enable"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.aescbc = YLeaf(YType.boolean, "aescbc")
                        self._segment_path = lambda: "client-cipher"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/client/client-enable/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Crypto.Ssh.Client.ClientEnable.ClientCipher, ['aescbc'], name, value)


        class Server(Entity):
            """
            Provide SSH server service
            
            .. attribute:: capability
            
            	Capability
            	**type**\:   :py:class:`Capability <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.Capability>`
            
            .. attribute:: disable
            
            	disable
            	**type**\:   :py:class:`Disable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.Disable>`
            
            .. attribute:: dscp
            
            	Cisco sshd DSCP value
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: enable
            
            	enable
            	**type**\:   :py:class:`Enable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.Enable>`
            
            .. attribute:: logging
            
            	Enable ssh server logging
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: netconf
            
            	port number on which ssh service to be started for netconf
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**default value**\: 830
            
            .. attribute:: netconf_vrf_table
            
            	Cisco sshd Netconf VRF name
            	**type**\:   :py:class:`NetconfVrfTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.NetconfVrfTable>`
            
            .. attribute:: rate_limit
            
            	Cisco sshd rate\-limit of service requests
            	**type**\:  int
            
            	**range:** 1..600
            
            	**default value**\: 60
            
            .. attribute:: rekey_time
            
            	Time Period in minutes, defalut 60
            	**type**\:  int
            
            	**range:** 30..1440
            
            	**default value**\: 60
            
            .. attribute:: rekey_volume
            
            	Configure volume\-based rekey for SSH
            	**type**\:  int
            
            	**range:** 1024..4095
            
            	**default value**\: 1024
            
            .. attribute:: session_limit
            
            	Cisco sshd session\-limit of service requests
            	**type**\:  int
            
            	**range:** 1..1024
            
            .. attribute:: timeout
            
            	Timeout value between 5\-120 seconds defalut 30
            	**type**\:  int
            
            	**range:** 5..120
            
            	**default value**\: 30
            
            .. attribute:: v2
            
            	Cisco sshd force protocol version 2 only
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: vrf_table
            
            	Cisco sshd VRF name
            	**type**\:   :py:class:`VrfTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.VrfTable>`
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2017-07-15'

            def __init__(self):
                super(Crypto.Ssh.Server, self).__init__()

                self.yang_name = "server"
                self.yang_parent_name = "ssh"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"capability" : ("capability", Crypto.Ssh.Server.Capability), "disable" : ("disable", Crypto.Ssh.Server.Disable), "enable" : ("enable", Crypto.Ssh.Server.Enable), "netconf-vrf-table" : ("netconf_vrf_table", Crypto.Ssh.Server.NetconfVrfTable), "vrf-table" : ("vrf_table", Crypto.Ssh.Server.VrfTable)}
                self._child_list_classes = {}

                self.dscp = YLeaf(YType.uint32, "dscp")

                self.logging = YLeaf(YType.empty, "logging")

                self.netconf = YLeaf(YType.uint32, "netconf")

                self.rate_limit = YLeaf(YType.uint32, "rate-limit")

                self.rekey_time = YLeaf(YType.uint32, "rekey-time")

                self.rekey_volume = YLeaf(YType.uint32, "rekey-volume")

                self.session_limit = YLeaf(YType.uint32, "session-limit")

                self.timeout = YLeaf(YType.uint32, "timeout")

                self.v2 = YLeaf(YType.empty, "v2")

                self.capability = Crypto.Ssh.Server.Capability()
                self.capability.parent = self
                self._children_name_map["capability"] = "capability"
                self._children_yang_names.add("capability")

                self.disable = Crypto.Ssh.Server.Disable()
                self.disable.parent = self
                self._children_name_map["disable"] = "disable"
                self._children_yang_names.add("disable")

                self.enable = Crypto.Ssh.Server.Enable()
                self.enable.parent = self
                self._children_name_map["enable"] = "enable"
                self._children_yang_names.add("enable")

                self.netconf_vrf_table = Crypto.Ssh.Server.NetconfVrfTable()
                self.netconf_vrf_table.parent = self
                self._children_name_map["netconf_vrf_table"] = "netconf-vrf-table"
                self._children_yang_names.add("netconf-vrf-table")

                self.vrf_table = Crypto.Ssh.Server.VrfTable()
                self.vrf_table.parent = self
                self._children_name_map["vrf_table"] = "vrf-table"
                self._children_yang_names.add("vrf-table")
                self._segment_path = lambda: "server"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Crypto.Ssh.Server, ['dscp', 'logging', 'netconf', 'rate_limit', 'rekey_time', 'rekey_volume', 'session_limit', 'timeout', 'v2'], name, value)


            class Capability(Entity):
                """
                Capability
                
                .. attribute:: netconf_xml
                
                	Enable Netconf\-XML stack on port 22
                	**type**\:  bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2017-07-15'

                def __init__(self):
                    super(Crypto.Ssh.Server.Capability, self).__init__()

                    self.yang_name = "capability"
                    self.yang_parent_name = "server"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.netconf_xml = YLeaf(YType.boolean, "netconf-xml")
                    self._segment_path = lambda: "capability"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Crypto.Ssh.Server.Capability, ['netconf_xml'], name, value)


            class Disable(Entity):
                """
                disable
                
                .. attribute:: hmac
                
                	hmac
                	**type**\:   :py:class:`Hmac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.Disable.Hmac>`
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2017-07-15'

                def __init__(self):
                    super(Crypto.Ssh.Server.Disable, self).__init__()

                    self.yang_name = "disable"
                    self.yang_parent_name = "server"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"hmac" : ("hmac", Crypto.Ssh.Server.Disable.Hmac)}
                    self._child_list_classes = {}

                    self.hmac = Crypto.Ssh.Server.Disable.Hmac()
                    self.hmac.parent = self
                    self._children_name_map["hmac"] = "hmac"
                    self._children_yang_names.add("hmac")
                    self._segment_path = lambda: "disable"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()


                class Hmac(Entity):
                    """
                    hmac
                    
                    .. attribute:: hmac_sha512
                    
                    	Disable Hmac\-sha2\-512 negotiation
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'crypto-ssh-cfg'
                    _revision = '2017-07-15'

                    def __init__(self):
                        super(Crypto.Ssh.Server.Disable.Hmac, self).__init__()

                        self.yang_name = "hmac"
                        self.yang_parent_name = "disable"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.hmac_sha512 = YLeaf(YType.boolean, "hmac-sha512")
                        self._segment_path = lambda: "hmac"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/disable/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Crypto.Ssh.Server.Disable.Hmac, ['hmac_sha512'], name, value)


            class Enable(Entity):
                """
                enable
                
                .. attribute:: cipher
                
                	cipher
                	**type**\:   :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.Enable.Cipher>`
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2017-07-15'

                def __init__(self):
                    super(Crypto.Ssh.Server.Enable, self).__init__()

                    self.yang_name = "enable"
                    self.yang_parent_name = "server"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"cipher" : ("cipher", Crypto.Ssh.Server.Enable.Cipher)}
                    self._child_list_classes = {}

                    self.cipher = Crypto.Ssh.Server.Enable.Cipher()
                    self.cipher.parent = self
                    self._children_name_map["cipher"] = "cipher"
                    self._children_yang_names.add("cipher")
                    self._segment_path = lambda: "enable"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()


                class Cipher(Entity):
                    """
                    cipher
                    
                    .. attribute:: aescbc
                    
                    	Enable AES\-CBC ciphers
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'crypto-ssh-cfg'
                    _revision = '2017-07-15'

                    def __init__(self):
                        super(Crypto.Ssh.Server.Enable.Cipher, self).__init__()

                        self.yang_name = "cipher"
                        self.yang_parent_name = "enable"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.aescbc = YLeaf(YType.boolean, "aescbc")
                        self._segment_path = lambda: "cipher"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/enable/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Crypto.Ssh.Server.Enable.Cipher, ['aescbc'], name, value)


            class NetconfVrfTable(Entity):
                """
                Cisco sshd Netconf VRF name
                
                .. attribute:: vrf
                
                	Enter VRF name
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.NetconfVrfTable.Vrf>`
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2017-07-15'

                def __init__(self):
                    super(Crypto.Ssh.Server.NetconfVrfTable, self).__init__()

                    self.yang_name = "netconf-vrf-table"
                    self.yang_parent_name = "server"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"vrf" : ("vrf", Crypto.Ssh.Server.NetconfVrfTable.Vrf)}

                    self.vrf = YList(self)
                    self._segment_path = lambda: "netconf-vrf-table"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Crypto.Ssh.Server.NetconfVrfTable, [], name, value)


                class Vrf(Entity):
                    """
                    Enter VRF name
                    
                    .. attribute:: vrf_name  <key>
                    
                    	Enter VRF name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: enable
                    
                    	Enable to use VRF
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: ipv4_access_list
                    
                    	SSH v4 access\-list name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: ipv6_access_list
                    
                    	SSH v6 access\-list name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'crypto-ssh-cfg'
                    _revision = '2017-07-15'

                    def __init__(self):
                        super(Crypto.Ssh.Server.NetconfVrfTable.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "netconf-vrf-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.ipv4_access_list = YLeaf(YType.str, "ipv4-access-list")

                        self.ipv6_access_list = YLeaf(YType.str, "ipv6-access-list")
                        self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/netconf-vrf-table/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Crypto.Ssh.Server.NetconfVrfTable.Vrf, ['vrf_name', 'enable', 'ipv4_access_list', 'ipv6_access_list'], name, value)


            class VrfTable(Entity):
                """
                Cisco sshd VRF name
                
                .. attribute:: vrf
                
                	Enter VRF name
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.VrfTable.Vrf>`
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2017-07-15'

                def __init__(self):
                    super(Crypto.Ssh.Server.VrfTable, self).__init__()

                    self.yang_name = "vrf-table"
                    self.yang_parent_name = "server"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"vrf" : ("vrf", Crypto.Ssh.Server.VrfTable.Vrf)}

                    self.vrf = YList(self)
                    self._segment_path = lambda: "vrf-table"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Crypto.Ssh.Server.VrfTable, [], name, value)


                class Vrf(Entity):
                    """
                    Enter VRF name
                    
                    .. attribute:: vrf_name  <key>
                    
                    	Enter VRF name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: enable
                    
                    	Enable to use VRF
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: ipv4_access_list
                    
                    	SSH v4 access\-list name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: ipv6_access_list
                    
                    	SSH v6 access\-list name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'crypto-ssh-cfg'
                    _revision = '2017-07-15'

                    def __init__(self):
                        super(Crypto.Ssh.Server.VrfTable.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrf-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.ipv4_access_list = YLeaf(YType.str, "ipv4-access-list")

                        self.ipv6_access_list = YLeaf(YType.str, "ipv6-access-list")
                        self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/vrf-table/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Crypto.Ssh.Server.VrfTable.Vrf, ['vrf_name', 'enable', 'ipv4_access_list', 'ipv6_access_list'], name, value)

    def clone_ptr(self):
        self._top_entity = Crypto()
        return self._top_entity


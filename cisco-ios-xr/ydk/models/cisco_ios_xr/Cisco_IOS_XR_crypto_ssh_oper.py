""" Cisco_IOS_XR_crypto_ssh_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-ssh package operational data.

This module contains definitions
for the following management objects\:
  ssh1\: Crypto Secure Shell(SSH) data
  ssh\: ssh

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Authen(Enum):
    """
    Authen (Enum Class)

    SSH session authentication types

    .. data:: password = 0

    	Password

    .. data:: rsa_public_key = 1

    	RSA public key encryption type

    .. data:: keyboard_interactive = 2

    	Keyboard interactive

    """

    password = Enum.YLeaf(0, "password")

    rsa_public_key = Enum.YLeaf(1, "rsa-public-key")

    keyboard_interactive = Enum.YLeaf(2, "keyboard-interactive")


class Cipher(Enum):
    """
    Cipher (Enum Class)

    SSH session in and out cipher standards

    .. data:: aes128_cbc = 0

    	Advanced Encryption Standard(AES) 128 bits

    	cipher block chaining(CBC)

    .. data:: aes192_cbc = 1

    	Advanced Encryption Standard(AES) 192 bits

    	cipher block chaining(CBC)

    .. data:: aes256_cbc = 2

    	Advanced Encryption Standard(AES) 256 bits

    	cipher block chaining(CBC)

    .. data:: triple_des_cbc = 3

    	Triple Data Encryption Standard(DES) cipher

    	block chaining(CBC)

    .. data:: aes128_ctr = 4

    	Advanced Encryption Standard(AES) 128 bits

    	counter mode (CTR)

    .. data:: aes192_ctr = 5

    	Advanced Encryption Standard(AES) 192 bits

    	counter mode (CTR)

    .. data:: aes256_ctr = 6

    	Advanced Encryption Standard(AES) 256 bits

    	counter mode (CTR)

    .. data:: aes128_gcm = 7

    	Advanced Encryption Standard(AES) 128 bits GCM

    	mode (GCM)

    .. data:: aes256_gcm = 8

    	Advanced Encryption Standard(AES) 256 bits GCM

    	mode (GCM)

    """

    aes128_cbc = Enum.YLeaf(0, "aes128-cbc")

    aes192_cbc = Enum.YLeaf(1, "aes192-cbc")

    aes256_cbc = Enum.YLeaf(2, "aes256-cbc")

    triple_des_cbc = Enum.YLeaf(3, "triple-des-cbc")

    aes128_ctr = Enum.YLeaf(4, "aes128-ctr")

    aes192_ctr = Enum.YLeaf(5, "aes192-ctr")

    aes256_ctr = Enum.YLeaf(6, "aes256-ctr")

    aes128_gcm = Enum.YLeaf(7, "aes128-gcm")

    aes256_gcm = Enum.YLeaf(8, "aes256-gcm")


class Connection(Enum):
    """
    Connection (Enum Class)

    SSH channel connection types

    .. data:: undefined = 0

    	connection type not yet known

    .. data:: shell = 1

    	Interactive Shell

    .. data:: exec_ = 2

    	Remote Command Execution

    .. data:: scp = 3

    	Secure Copy

    .. data:: sftp_subsystem = 4

    	Secure File Transfer

    .. data:: netconf_subsystem = 5

    	Netconf Subsystem

    .. data:: tl1_subsystem = 6

    	TL1 Subsystem

    .. data:: netconf_xml_subsystem = 7

    	Netconf XML Subsystem

    """

    undefined = Enum.YLeaf(0, "undefined")

    shell = Enum.YLeaf(1, "shell")

    exec_ = Enum.YLeaf(2, "exec")

    scp = Enum.YLeaf(3, "scp")

    sftp_subsystem = Enum.YLeaf(4, "sftp-subsystem")

    netconf_subsystem = Enum.YLeaf(5, "netconf-subsystem")

    tl1_subsystem = Enum.YLeaf(6, "tl1-subsystem")

    netconf_xml_subsystem = Enum.YLeaf(7, "netconf-xml-subsystem")


class Hostkey(Enum):
    """
    Hostkey (Enum Class)

    SSH session authentication types

    .. data:: ssh_dss = 0

    	Algorithm type DSS

    .. data:: ssh_rsa = 1

    	Algorithm type RSA

    """

    ssh_dss = Enum.YLeaf(0, "ssh-dss")

    ssh_rsa = Enum.YLeaf(1, "ssh-rsa")


class KexName(Enum):
    """
    KexName (Enum Class)

    Different key\-exchange(kex) algorithms

    .. data:: diffie_hellman_group1 = 0

    	Diffie-Hellman group 1 key exchange algorithm

    .. data:: diffie_hellman_group14 = 1

    	Diffie-Hellman group 14 key exchange algorithm

    .. data:: diffie_hellman_group15 = 2

    	Diffie-Hellman group 14 key exchange algorithm

    .. data:: diffie_hellman_group16 = 3

    	Diffie-Hellman group 16 key exchange algorithm

    .. data:: diffie_hellman_group17 = 4

    	Diffie-Hellman group 17 key exchange algorithm

    .. data:: diffie_hellman_group18 = 5

    	Diffie-Hellman key group 18 exchange algorithm

    .. data:: ecdh_nistp256 = 6

    	Elliptical curve Diffie-Hellman prime 256 key

    	exchange algorithm

    .. data:: ecdh_nistp384 = 7

    	Elliptical curve Diffie-Hellman prime 384 key

    	exchange algorithm

    .. data:: ecdh_nistp521 = 8

    	Elliptical curve Diffie-Hellman prime 521

    	exchange algorithm

    .. data:: password_authenticated = 9

    	Password authenticated key agreement algorithm

    """

    diffie_hellman_group1 = Enum.YLeaf(0, "diffie-hellman-group1")

    diffie_hellman_group14 = Enum.YLeaf(1, "diffie-hellman-group14")

    diffie_hellman_group15 = Enum.YLeaf(2, "diffie-hellman-group15")

    diffie_hellman_group16 = Enum.YLeaf(3, "diffie-hellman-group16")

    diffie_hellman_group17 = Enum.YLeaf(4, "diffie-hellman-group17")

    diffie_hellman_group18 = Enum.YLeaf(5, "diffie-hellman-group18")

    ecdh_nistp256 = Enum.YLeaf(6, "ecdh-nistp256")

    ecdh_nistp384 = Enum.YLeaf(7, "ecdh-nistp384")

    ecdh_nistp521 = Enum.YLeaf(8, "ecdh-nistp521")

    password_authenticated = Enum.YLeaf(9, "password-authenticated")


class Mac(Enum):
    """
    Mac (Enum Class)

    Different Message Authentication Code(MAC)

    functions

    .. data:: hmac_md5 = 0

    	Hash-based Message Authentication Code(HMAC)

    	MD5 algorithm

    .. data:: hmac_sha1 = 1

    	Hash-based Message Authentication Code(HMAC)

    	SHA1 algorithm

    .. data:: hmac_sha2_256 = 2

    	Hash-based Message Authentication Code(HMAC)

    	SHA2-256 algorithm

    .. data:: hmac_sha2_512 = 3

    	Hash-based Message Authentication Code(HMAC)

    	SHA2-512 algorithm

    .. data:: aes_gcm = 4

    	AES GCM based Authentication Tag as MAC

    	algorithm

    """

    hmac_md5 = Enum.YLeaf(0, "hmac-md5")

    hmac_sha1 = Enum.YLeaf(1, "hmac-sha1")

    hmac_sha2_256 = Enum.YLeaf(2, "hmac-sha2-256")

    hmac_sha2_512 = Enum.YLeaf(3, "hmac-sha2-512")

    aes_gcm = Enum.YLeaf(4, "aes-gcm")


class States(Enum):
    """
    States (Enum Class)

    SSH session states

    .. data:: open = 1

    	SSH Open

    .. data:: version_ok = 2

    	SSH version OK

    .. data:: key_exchange_initialize = 3

    	Key exchange(KEX) init message exchanged

    .. data:: key_exchange_dh = 4

    	Diffie-Hellman(DH) secret is generated

    .. data:: new_keys = 5

    	New keys are received

    .. data:: authenticate_information = 6

    	Need more information to authenticate

    .. data:: authenticated = 7

    	The client successfully authenticated

    .. data:: channel_open = 8

    	Channel has been successfully opened

    .. data:: pty_open = 9

    	Allocated PTY

    .. data:: session_open = 10

    	Opened an exec shell

    .. data:: rekey = 11

    	Received rekey request

    .. data:: suspended = 12

    	Session is suspended

    .. data:: session_closed = 13

    	Session has been closed

    """

    open = Enum.YLeaf(1, "open")

    version_ok = Enum.YLeaf(2, "version-ok")

    key_exchange_initialize = Enum.YLeaf(3, "key-exchange-initialize")

    key_exchange_dh = Enum.YLeaf(4, "key-exchange-dh")

    new_keys = Enum.YLeaf(5, "new-keys")

    authenticate_information = Enum.YLeaf(6, "authenticate-information")

    authenticated = Enum.YLeaf(7, "authenticated")

    channel_open = Enum.YLeaf(8, "channel-open")

    pty_open = Enum.YLeaf(9, "pty-open")

    session_open = Enum.YLeaf(10, "session-open")

    rekey = Enum.YLeaf(11, "rekey")

    suspended = Enum.YLeaf(12, "suspended")

    session_closed = Enum.YLeaf(13, "session-closed")


class Version(Enum):
    """
    Version (Enum Class)

    SSH state versions

    .. data:: v2 = 0

    	Version V2

    .. data:: v1 = 1

    	Version V1

    """

    v2 = Enum.YLeaf(0, "v2")

    v1 = Enum.YLeaf(1, "v1")



class Ssh1(Entity):
    """
    Crypto Secure Shell(SSH) data
    
    .. attribute:: kex
    
    	key exchange method data
    	**type**\:  :py:class:`Kex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex>`
    
    

    """

    _prefix = 'crypto-ssh-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Ssh1, self).__init__()
        self._top_entity = None

        self.yang_name = "ssh1"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-ssh-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("kex", ("kex", Ssh1.Kex))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.kex = Ssh1.Kex()
        self.kex.parent = self
        self._children_name_map["kex"] = "kex"
        self._children_yang_names.add("kex")
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh1"


    class Kex(Entity):
        """
        key exchange method data
        
        .. attribute:: nodes
        
        	Node\-specific ssh session details
        	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes>`
        
        

        """

        _prefix = 'crypto-ssh-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ssh1.Kex, self).__init__()

            self.yang_name = "kex"
            self.yang_parent_name = "ssh1"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("nodes", ("nodes", Ssh1.Kex.Nodes))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.nodes = Ssh1.Kex.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._children_yang_names.add("nodes")
            self._segment_path = lambda: "kex"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh1/%s" % self._segment_path()


        class Nodes(Entity):
            """
            Node\-specific ssh session details
            
            .. attribute:: node
            
            	SSH session details for a particular node
            	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node>`
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ssh1.Kex.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "kex"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("node", ("node", Ssh1.Kex.Nodes.Node))])
                self._leafs = OrderedDict()

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh1/kex/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh1.Kex.Nodes, [], name, value)


            class Node(Entity):
                """
                SSH session details for a particular node
                
                .. attribute:: node_name  (key)
                
                	Node name
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: incoming_sessions
                
                	List of incoming sessions
                	**type**\:  :py:class:`IncomingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.IncomingSessions>`
                
                .. attribute:: outgoing_connections
                
                	List of outgoing connections
                	**type**\:  :py:class:`OutgoingConnections <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.OutgoingConnections>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ssh1.Kex.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['node_name']
                    self._child_container_classes = OrderedDict([("incoming-sessions", ("incoming_sessions", Ssh1.Kex.Nodes.Node.IncomingSessions)), ("outgoing-connections", ("outgoing_connections", Ssh1.Kex.Nodes.Node.OutgoingConnections))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('node_name', YLeaf(YType.str, 'node-name')),
                    ])
                    self.node_name = None

                    self.incoming_sessions = Ssh1.Kex.Nodes.Node.IncomingSessions()
                    self.incoming_sessions.parent = self
                    self._children_name_map["incoming_sessions"] = "incoming-sessions"
                    self._children_yang_names.add("incoming-sessions")

                    self.outgoing_connections = Ssh1.Kex.Nodes.Node.OutgoingConnections()
                    self.outgoing_connections.parent = self
                    self._children_name_map["outgoing_connections"] = "outgoing-connections"
                    self._children_yang_names.add("outgoing-connections")
                    self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh1/kex/nodes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh1.Kex.Nodes.Node, ['node_name'], name, value)


                class IncomingSessions(Entity):
                    """
                    List of incoming sessions
                    
                    .. attribute:: session_detail_info
                    
                    	session detail info
                    	**type**\: list of  		 :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo>`
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ssh1.Kex.Nodes.Node.IncomingSessions, self).__init__()

                        self.yang_name = "incoming-sessions"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("session-detail-info", ("session_detail_info", Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo))])
                        self._leafs = OrderedDict()

                        self.session_detail_info = YList(self)
                        self._segment_path = lambda: "incoming-sessions"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh1.Kex.Nodes.Node.IncomingSessions, [], name, value)


                    class SessionDetailInfo(Entity):
                        """
                        session detail info
                        
                        .. attribute:: session_id
                        
                        	Session ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: key_exchange
                        
                        	Key exchange name
                        	**type**\:  :py:class:`KexName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexName>`
                        
                        .. attribute:: public_key
                        
                        	Host key algorithm
                        	**type**\:  :py:class:`Hostkey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Hostkey>`
                        
                        .. attribute:: in_cipher
                        
                        	In cipher algorithm
                        	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                        
                        .. attribute:: out_cipher
                        
                        	Out cipher algorithm
                        	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                        
                        .. attribute:: in_mac
                        
                        	In MAC
                        	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                        
                        .. attribute:: out_mac
                        
                        	Out MAC
                        	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo, self).__init__()

                            self.yang_name = "session-detail-info"
                            self.yang_parent_name = "incoming-sessions"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('session_id', YLeaf(YType.uint32, 'session-id')),
                                ('key_exchange', YLeaf(YType.enumeration, 'key-exchange')),
                                ('public_key', YLeaf(YType.enumeration, 'public-key')),
                                ('in_cipher', YLeaf(YType.enumeration, 'in-cipher')),
                                ('out_cipher', YLeaf(YType.enumeration, 'out-cipher')),
                                ('in_mac', YLeaf(YType.enumeration, 'in-mac')),
                                ('out_mac', YLeaf(YType.enumeration, 'out-mac')),
                            ])
                            self.session_id = None
                            self.key_exchange = None
                            self.public_key = None
                            self.in_cipher = None
                            self.out_cipher = None
                            self.in_mac = None
                            self.out_mac = None
                            self._segment_path = lambda: "session-detail-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo, ['session_id', 'key_exchange', 'public_key', 'in_cipher', 'out_cipher', 'in_mac', 'out_mac'], name, value)


                class OutgoingConnections(Entity):
                    """
                    List of outgoing connections
                    
                    .. attribute:: session_detail_info
                    
                    	session detail info
                    	**type**\: list of  		 :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo>`
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ssh1.Kex.Nodes.Node.OutgoingConnections, self).__init__()

                        self.yang_name = "outgoing-connections"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("session-detail-info", ("session_detail_info", Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo))])
                        self._leafs = OrderedDict()

                        self.session_detail_info = YList(self)
                        self._segment_path = lambda: "outgoing-connections"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh1.Kex.Nodes.Node.OutgoingConnections, [], name, value)


                    class SessionDetailInfo(Entity):
                        """
                        session detail info
                        
                        .. attribute:: session_id
                        
                        	Session ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: key_exchange
                        
                        	Key exchange name
                        	**type**\:  :py:class:`KexName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexName>`
                        
                        .. attribute:: public_key
                        
                        	Host key algorithm
                        	**type**\:  :py:class:`Hostkey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Hostkey>`
                        
                        .. attribute:: in_cipher
                        
                        	In cipher algorithm
                        	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                        
                        .. attribute:: out_cipher
                        
                        	Out cipher algorithm
                        	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                        
                        .. attribute:: in_mac
                        
                        	In MAC
                        	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                        
                        .. attribute:: out_mac
                        
                        	Out MAC
                        	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo, self).__init__()

                            self.yang_name = "session-detail-info"
                            self.yang_parent_name = "outgoing-connections"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('session_id', YLeaf(YType.uint32, 'session-id')),
                                ('key_exchange', YLeaf(YType.enumeration, 'key-exchange')),
                                ('public_key', YLeaf(YType.enumeration, 'public-key')),
                                ('in_cipher', YLeaf(YType.enumeration, 'in-cipher')),
                                ('out_cipher', YLeaf(YType.enumeration, 'out-cipher')),
                                ('in_mac', YLeaf(YType.enumeration, 'in-mac')),
                                ('out_mac', YLeaf(YType.enumeration, 'out-mac')),
                            ])
                            self.session_id = None
                            self.key_exchange = None
                            self.public_key = None
                            self.in_cipher = None
                            self.out_cipher = None
                            self.in_mac = None
                            self.out_mac = None
                            self._segment_path = lambda: "session-detail-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo, ['session_id', 'key_exchange', 'public_key', 'in_cipher', 'out_cipher', 'in_mac', 'out_mac'], name, value)

    def clone_ptr(self):
        self._top_entity = Ssh1()
        return self._top_entity

class Ssh(Entity):
    """
    ssh
    
    .. attribute:: session
    
    	Crypto SSH session
    	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session>`
    
    

    """

    _prefix = 'crypto-ssh-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Ssh, self).__init__()
        self._top_entity = None

        self.yang_name = "ssh"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-ssh-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("session", ("session", Ssh.Session))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.session = Ssh.Session()
        self.session.parent = self
        self._children_name_map["session"] = "session"
        self._children_yang_names.add("session")
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh"


    class Session(Entity):
        """
        Crypto SSH session
        
        .. attribute:: rekey
        
        	SSH session rekey information
        	**type**\:  :py:class:`Rekey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey>`
        
        .. attribute:: brief
        
        	SSH session brief information
        	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief>`
        
        .. attribute:: detail
        
        	SSH session detail information
        	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail>`
        
        

        """

        _prefix = 'crypto-ssh-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ssh.Session, self).__init__()

            self.yang_name = "session"
            self.yang_parent_name = "ssh"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("rekey", ("rekey", Ssh.Session.Rekey)), ("brief", ("brief", Ssh.Session.Brief)), ("detail", ("detail", Ssh.Session.Detail))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.rekey = Ssh.Session.Rekey()
            self.rekey.parent = self
            self._children_name_map["rekey"] = "rekey"
            self._children_yang_names.add("rekey")

            self.brief = Ssh.Session.Brief()
            self.brief.parent = self
            self._children_name_map["brief"] = "brief"
            self._children_yang_names.add("brief")

            self.detail = Ssh.Session.Detail()
            self.detail.parent = self
            self._children_name_map["detail"] = "detail"
            self._children_yang_names.add("detail")
            self._segment_path = lambda: "session"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/%s" % self._segment_path()


        class Rekey(Entity):
            """
            SSH session rekey information
            
            .. attribute:: incoming_sessions
            
            	List of incoming sessions
            	**type**\:  :py:class:`IncomingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.IncomingSessions>`
            
            .. attribute:: outgoing_connections
            
            	List of outgoing connections
            	**type**\:  :py:class:`OutgoingConnections <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.OutgoingConnections>`
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ssh.Session.Rekey, self).__init__()

                self.yang_name = "rekey"
                self.yang_parent_name = "session"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("incoming-sessions", ("incoming_sessions", Ssh.Session.Rekey.IncomingSessions)), ("outgoing-connections", ("outgoing_connections", Ssh.Session.Rekey.OutgoingConnections))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.incoming_sessions = Ssh.Session.Rekey.IncomingSessions()
                self.incoming_sessions.parent = self
                self._children_name_map["incoming_sessions"] = "incoming-sessions"
                self._children_yang_names.add("incoming-sessions")

                self.outgoing_connections = Ssh.Session.Rekey.OutgoingConnections()
                self.outgoing_connections.parent = self
                self._children_name_map["outgoing_connections"] = "outgoing-connections"
                self._children_yang_names.add("outgoing-connections")
                self._segment_path = lambda: "rekey"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/%s" % self._segment_path()


            class IncomingSessions(Entity):
                """
                List of incoming sessions
                
                .. attribute:: session_rekey_info
                
                	session rekey info
                	**type**\: list of  		 :py:class:`SessionRekeyInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ssh.Session.Rekey.IncomingSessions, self).__init__()

                    self.yang_name = "incoming-sessions"
                    self.yang_parent_name = "rekey"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("session-rekey-info", ("session_rekey_info", Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo))])
                    self._leafs = OrderedDict()

                    self.session_rekey_info = YList(self)
                    self._segment_path = lambda: "incoming-sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/rekey/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Session.Rekey.IncomingSessions, [], name, value)


                class SessionRekeyInfo(Entity):
                    """
                    session rekey info
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_rekey_count
                    
                    	Session Rekey Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: time_to_rekey
                    
                    	Time To Rekey
                    	**type**\: str
                    
                    .. attribute:: volume_to_rekey
                    
                    	Volume To Rekey
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo, self).__init__()

                        self.yang_name = "session-rekey-info"
                        self.yang_parent_name = "incoming-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('session_id', YLeaf(YType.uint32, 'session-id')),
                            ('session_rekey_count', YLeaf(YType.uint32, 'session-rekey-count')),
                            ('time_to_rekey', YLeaf(YType.str, 'time-to-rekey')),
                            ('volume_to_rekey', YLeaf(YType.str, 'volume-to-rekey')),
                        ])
                        self.session_id = None
                        self.session_rekey_count = None
                        self.time_to_rekey = None
                        self.volume_to_rekey = None
                        self._segment_path = lambda: "session-rekey-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/rekey/incoming-sessions/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo, ['session_id', 'session_rekey_count', 'time_to_rekey', 'volume_to_rekey'], name, value)


            class OutgoingConnections(Entity):
                """
                List of outgoing connections
                
                .. attribute:: session_rekey_info
                
                	session rekey info
                	**type**\: list of  		 :py:class:`SessionRekeyInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ssh.Session.Rekey.OutgoingConnections, self).__init__()

                    self.yang_name = "outgoing-connections"
                    self.yang_parent_name = "rekey"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("session-rekey-info", ("session_rekey_info", Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo))])
                    self._leafs = OrderedDict()

                    self.session_rekey_info = YList(self)
                    self._segment_path = lambda: "outgoing-connections"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/rekey/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Session.Rekey.OutgoingConnections, [], name, value)


                class SessionRekeyInfo(Entity):
                    """
                    session rekey info
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_rekey_count
                    
                    	Session Rekey Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: time_to_rekey
                    
                    	Time To Rekey
                    	**type**\: str
                    
                    .. attribute:: volume_to_rekey
                    
                    	Volume To Rekey
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo, self).__init__()

                        self.yang_name = "session-rekey-info"
                        self.yang_parent_name = "outgoing-connections"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('session_id', YLeaf(YType.uint32, 'session-id')),
                            ('session_rekey_count', YLeaf(YType.uint32, 'session-rekey-count')),
                            ('time_to_rekey', YLeaf(YType.str, 'time-to-rekey')),
                            ('volume_to_rekey', YLeaf(YType.str, 'volume-to-rekey')),
                        ])
                        self.session_id = None
                        self.session_rekey_count = None
                        self.time_to_rekey = None
                        self.volume_to_rekey = None
                        self._segment_path = lambda: "session-rekey-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/rekey/outgoing-connections/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo, ['session_id', 'session_rekey_count', 'time_to_rekey', 'volume_to_rekey'], name, value)


        class Brief(Entity):
            """
            SSH session brief information
            
            .. attribute:: incoming_sessions
            
            	List of incoming sessions
            	**type**\:  :py:class:`IncomingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.IncomingSessions>`
            
            .. attribute:: outgoing_sessions
            
            	List of outgoing sessions
            	**type**\:  :py:class:`OutgoingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.OutgoingSessions>`
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ssh.Session.Brief, self).__init__()

                self.yang_name = "brief"
                self.yang_parent_name = "session"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("incoming-sessions", ("incoming_sessions", Ssh.Session.Brief.IncomingSessions)), ("outgoing-sessions", ("outgoing_sessions", Ssh.Session.Brief.OutgoingSessions))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.incoming_sessions = Ssh.Session.Brief.IncomingSessions()
                self.incoming_sessions.parent = self
                self._children_name_map["incoming_sessions"] = "incoming-sessions"
                self._children_yang_names.add("incoming-sessions")

                self.outgoing_sessions = Ssh.Session.Brief.OutgoingSessions()
                self.outgoing_sessions.parent = self
                self._children_name_map["outgoing_sessions"] = "outgoing-sessions"
                self._children_yang_names.add("outgoing-sessions")
                self._segment_path = lambda: "brief"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/%s" % self._segment_path()


            class IncomingSessions(Entity):
                """
                List of incoming sessions
                
                .. attribute:: session_brief_info
                
                	session brief info
                	**type**\: list of  		 :py:class:`SessionBriefInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.IncomingSessions.SessionBriefInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ssh.Session.Brief.IncomingSessions, self).__init__()

                    self.yang_name = "incoming-sessions"
                    self.yang_parent_name = "brief"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("session-brief-info", ("session_brief_info", Ssh.Session.Brief.IncomingSessions.SessionBriefInfo))])
                    self._leafs = OrderedDict()

                    self.session_brief_info = YList(self)
                    self._segment_path = lambda: "incoming-sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Session.Brief.IncomingSessions, [], name, value)


                class SessionBriefInfo(Entity):
                    """
                    session brief info
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: channel_id
                    
                    	Channel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vty_assigned
                    
                    	Boolean indicating whether line VTY line number is valid
                    	**type**\: bool
                    
                    .. attribute:: vty_line_number
                    
                    	VTY line number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: node_name
                    
                    	Node name
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: session_state
                    
                    	SSH session state
                    	**type**\:  :py:class:`States <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.States>`
                    
                    .. attribute:: user_id
                    
                    	User ID
                    	**type**\: str
                    
                    .. attribute:: host_address
                    
                    	Host address
                    	**type**\: str
                    
                    .. attribute:: version
                    
                    	SSH state version
                    	**type**\:  :py:class:`Version <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Version>`
                    
                    .. attribute:: authentication_type
                    
                    	Authentication method
                    	**type**\:  :py:class:`Authen <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Authen>`
                    
                    .. attribute:: connection_type
                    
                    	Channel Connection Type
                    	**type**\:  :py:class:`Connection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Connection>`
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ssh.Session.Brief.IncomingSessions.SessionBriefInfo, self).__init__()

                        self.yang_name = "session-brief-info"
                        self.yang_parent_name = "incoming-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('session_id', YLeaf(YType.uint32, 'session-id')),
                            ('channel_id', YLeaf(YType.uint32, 'channel-id')),
                            ('vty_assigned', YLeaf(YType.boolean, 'vty-assigned')),
                            ('vty_line_number', YLeaf(YType.uint32, 'vty-line-number')),
                            ('node_name', YLeaf(YType.str, 'node-name')),
                            ('session_state', YLeaf(YType.enumeration, 'session-state')),
                            ('user_id', YLeaf(YType.str, 'user-id')),
                            ('host_address', YLeaf(YType.str, 'host-address')),
                            ('version', YLeaf(YType.enumeration, 'version')),
                            ('authentication_type', YLeaf(YType.enumeration, 'authentication-type')),
                            ('connection_type', YLeaf(YType.enumeration, 'connection-type')),
                        ])
                        self.session_id = None
                        self.channel_id = None
                        self.vty_assigned = None
                        self.vty_line_number = None
                        self.node_name = None
                        self.session_state = None
                        self.user_id = None
                        self.host_address = None
                        self.version = None
                        self.authentication_type = None
                        self.connection_type = None
                        self._segment_path = lambda: "session-brief-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/incoming-sessions/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh.Session.Brief.IncomingSessions.SessionBriefInfo, ['session_id', 'channel_id', 'vty_assigned', 'vty_line_number', 'node_name', 'session_state', 'user_id', 'host_address', 'version', 'authentication_type', 'connection_type'], name, value)


            class OutgoingSessions(Entity):
                """
                List of outgoing sessions
                
                .. attribute:: session_brief_info
                
                	session brief info
                	**type**\: list of  		 :py:class:`SessionBriefInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ssh.Session.Brief.OutgoingSessions, self).__init__()

                    self.yang_name = "outgoing-sessions"
                    self.yang_parent_name = "brief"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("session-brief-info", ("session_brief_info", Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo))])
                    self._leafs = OrderedDict()

                    self.session_brief_info = YList(self)
                    self._segment_path = lambda: "outgoing-sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Session.Brief.OutgoingSessions, [], name, value)


                class SessionBriefInfo(Entity):
                    """
                    session brief info
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: channel_id
                    
                    	Channel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vty_assigned
                    
                    	Boolean indicating whether line VTY line number is valid
                    	**type**\: bool
                    
                    .. attribute:: vty_line_number
                    
                    	VTY line number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: node_name
                    
                    	Node name
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: session_state
                    
                    	SSH session state
                    	**type**\:  :py:class:`States <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.States>`
                    
                    .. attribute:: user_id
                    
                    	User ID
                    	**type**\: str
                    
                    .. attribute:: host_address
                    
                    	Host address
                    	**type**\: str
                    
                    .. attribute:: version
                    
                    	SSH state version
                    	**type**\:  :py:class:`Version <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Version>`
                    
                    .. attribute:: authentication_type
                    
                    	Authentication method
                    	**type**\:  :py:class:`Authen <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Authen>`
                    
                    .. attribute:: connection_type
                    
                    	Channel Connection Type
                    	**type**\:  :py:class:`Connection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Connection>`
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo, self).__init__()

                        self.yang_name = "session-brief-info"
                        self.yang_parent_name = "outgoing-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('session_id', YLeaf(YType.uint32, 'session-id')),
                            ('channel_id', YLeaf(YType.uint32, 'channel-id')),
                            ('vty_assigned', YLeaf(YType.boolean, 'vty-assigned')),
                            ('vty_line_number', YLeaf(YType.uint32, 'vty-line-number')),
                            ('node_name', YLeaf(YType.str, 'node-name')),
                            ('session_state', YLeaf(YType.enumeration, 'session-state')),
                            ('user_id', YLeaf(YType.str, 'user-id')),
                            ('host_address', YLeaf(YType.str, 'host-address')),
                            ('version', YLeaf(YType.enumeration, 'version')),
                            ('authentication_type', YLeaf(YType.enumeration, 'authentication-type')),
                            ('connection_type', YLeaf(YType.enumeration, 'connection-type')),
                        ])
                        self.session_id = None
                        self.channel_id = None
                        self.vty_assigned = None
                        self.vty_line_number = None
                        self.node_name = None
                        self.session_state = None
                        self.user_id = None
                        self.host_address = None
                        self.version = None
                        self.authentication_type = None
                        self.connection_type = None
                        self._segment_path = lambda: "session-brief-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/outgoing-sessions/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo, ['session_id', 'channel_id', 'vty_assigned', 'vty_line_number', 'node_name', 'session_state', 'user_id', 'host_address', 'version', 'authentication_type', 'connection_type'], name, value)


        class Detail(Entity):
            """
            SSH session detail information
            
            .. attribute:: incoming_sessions
            
            	List of incoming sessions
            	**type**\:  :py:class:`IncomingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.IncomingSessions>`
            
            .. attribute:: outgoing_connections
            
            	List of outgoing connections
            	**type**\:  :py:class:`OutgoingConnections <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.OutgoingConnections>`
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ssh.Session.Detail, self).__init__()

                self.yang_name = "detail"
                self.yang_parent_name = "session"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("incoming-sessions", ("incoming_sessions", Ssh.Session.Detail.IncomingSessions)), ("outgoing-connections", ("outgoing_connections", Ssh.Session.Detail.OutgoingConnections))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.incoming_sessions = Ssh.Session.Detail.IncomingSessions()
                self.incoming_sessions.parent = self
                self._children_name_map["incoming_sessions"] = "incoming-sessions"
                self._children_yang_names.add("incoming-sessions")

                self.outgoing_connections = Ssh.Session.Detail.OutgoingConnections()
                self.outgoing_connections.parent = self
                self._children_name_map["outgoing_connections"] = "outgoing-connections"
                self._children_yang_names.add("outgoing-connections")
                self._segment_path = lambda: "detail"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/%s" % self._segment_path()


            class IncomingSessions(Entity):
                """
                List of incoming sessions
                
                .. attribute:: session_detail_info
                
                	session detail info
                	**type**\: list of  		 :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.IncomingSessions.SessionDetailInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ssh.Session.Detail.IncomingSessions, self).__init__()

                    self.yang_name = "incoming-sessions"
                    self.yang_parent_name = "detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("session-detail-info", ("session_detail_info", Ssh.Session.Detail.IncomingSessions.SessionDetailInfo))])
                    self._leafs = OrderedDict()

                    self.session_detail_info = YList(self)
                    self._segment_path = lambda: "incoming-sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/detail/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Session.Detail.IncomingSessions, [], name, value)


                class SessionDetailInfo(Entity):
                    """
                    session detail info
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: key_exchange
                    
                    	Key exchange name
                    	**type**\:  :py:class:`KexName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexName>`
                    
                    .. attribute:: public_key
                    
                    	Host key algorithm
                    	**type**\:  :py:class:`Hostkey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Hostkey>`
                    
                    .. attribute:: in_cipher
                    
                    	In cipher algorithm
                    	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    .. attribute:: out_cipher
                    
                    	Out cipher algorithm
                    	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    .. attribute:: in_mac
                    
                    	In MAC
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    .. attribute:: out_mac
                    
                    	Out MAC
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ssh.Session.Detail.IncomingSessions.SessionDetailInfo, self).__init__()

                        self.yang_name = "session-detail-info"
                        self.yang_parent_name = "incoming-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('session_id', YLeaf(YType.uint32, 'session-id')),
                            ('key_exchange', YLeaf(YType.enumeration, 'key-exchange')),
                            ('public_key', YLeaf(YType.enumeration, 'public-key')),
                            ('in_cipher', YLeaf(YType.enumeration, 'in-cipher')),
                            ('out_cipher', YLeaf(YType.enumeration, 'out-cipher')),
                            ('in_mac', YLeaf(YType.enumeration, 'in-mac')),
                            ('out_mac', YLeaf(YType.enumeration, 'out-mac')),
                        ])
                        self.session_id = None
                        self.key_exchange = None
                        self.public_key = None
                        self.in_cipher = None
                        self.out_cipher = None
                        self.in_mac = None
                        self.out_mac = None
                        self._segment_path = lambda: "session-detail-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/detail/incoming-sessions/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh.Session.Detail.IncomingSessions.SessionDetailInfo, ['session_id', 'key_exchange', 'public_key', 'in_cipher', 'out_cipher', 'in_mac', 'out_mac'], name, value)


            class OutgoingConnections(Entity):
                """
                List of outgoing connections
                
                .. attribute:: session_detail_info
                
                	session detail info
                	**type**\: list of  		 :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ssh.Session.Detail.OutgoingConnections, self).__init__()

                    self.yang_name = "outgoing-connections"
                    self.yang_parent_name = "detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("session-detail-info", ("session_detail_info", Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo))])
                    self._leafs = OrderedDict()

                    self.session_detail_info = YList(self)
                    self._segment_path = lambda: "outgoing-connections"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/detail/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Session.Detail.OutgoingConnections, [], name, value)


                class SessionDetailInfo(Entity):
                    """
                    session detail info
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: key_exchange
                    
                    	Key exchange name
                    	**type**\:  :py:class:`KexName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexName>`
                    
                    .. attribute:: public_key
                    
                    	Host key algorithm
                    	**type**\:  :py:class:`Hostkey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Hostkey>`
                    
                    .. attribute:: in_cipher
                    
                    	In cipher algorithm
                    	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    .. attribute:: out_cipher
                    
                    	Out cipher algorithm
                    	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    .. attribute:: in_mac
                    
                    	In MAC
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    .. attribute:: out_mac
                    
                    	Out MAC
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo, self).__init__()

                        self.yang_name = "session-detail-info"
                        self.yang_parent_name = "outgoing-connections"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('session_id', YLeaf(YType.uint32, 'session-id')),
                            ('key_exchange', YLeaf(YType.enumeration, 'key-exchange')),
                            ('public_key', YLeaf(YType.enumeration, 'public-key')),
                            ('in_cipher', YLeaf(YType.enumeration, 'in-cipher')),
                            ('out_cipher', YLeaf(YType.enumeration, 'out-cipher')),
                            ('in_mac', YLeaf(YType.enumeration, 'in-mac')),
                            ('out_mac', YLeaf(YType.enumeration, 'out-mac')),
                        ])
                        self.session_id = None
                        self.key_exchange = None
                        self.public_key = None
                        self.in_cipher = None
                        self.out_cipher = None
                        self.in_mac = None
                        self.out_mac = None
                        self._segment_path = lambda: "session-detail-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/detail/outgoing-connections/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo, ['session_id', 'key_exchange', 'public_key', 'in_cipher', 'out_cipher', 'in_mac', 'out_mac'], name, value)

    def clone_ptr(self):
        self._top_entity = Ssh()
        return self._top_entity


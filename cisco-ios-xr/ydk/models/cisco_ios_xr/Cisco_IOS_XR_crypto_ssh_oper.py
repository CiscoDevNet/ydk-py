""" Cisco_IOS_XR_crypto_ssh_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-ssh package operational data.

This module contains definitions
for the following management objects\:
  ssh1\: Crypto Secure Shell(SSH) data
  ssh\: ssh

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Authen']


class Cipher(Enum):
    """
    Cipher (Enum Class)

    SSH session in and out cipher standards

    .. data:: cipher_not_applicable = -1

    	unknown

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

    cipher_not_applicable = Enum.YLeaf(-1, "cipher-not-applicable")

    aes128_cbc = Enum.YLeaf(0, "aes128-cbc")

    aes192_cbc = Enum.YLeaf(1, "aes192-cbc")

    aes256_cbc = Enum.YLeaf(2, "aes256-cbc")

    triple_des_cbc = Enum.YLeaf(3, "triple-des-cbc")

    aes128_ctr = Enum.YLeaf(4, "aes128-ctr")

    aes192_ctr = Enum.YLeaf(5, "aes192-ctr")

    aes256_ctr = Enum.YLeaf(6, "aes256-ctr")

    aes128_gcm = Enum.YLeaf(7, "aes128-gcm")

    aes256_gcm = Enum.YLeaf(8, "aes256-gcm")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Cipher']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Connection']


class Hostkey(Enum):
    """
    Hostkey (Enum Class)

    SSH session authentication types

    .. data:: host_key_not_applicable = -1

    	unknown

    .. data:: ssh_dss = 0

    	Algorithm type DSS

    .. data:: ssh_rsa = 1

    	Algorithm type RSA

    .. data:: ecdsa_sha2_nistp521 = 2

    	Algorithm type ECDSA NISTP521

    .. data:: ecdsa_sha2_nistp384 = 3

    	Algorithm type ECDSA NISTP384

    .. data:: ecdsa_sha2_nistp256 = 4

    	Algorithm type ECDSA NISTP256

    """

    host_key_not_applicable = Enum.YLeaf(-1, "host-key-not-applicable")

    ssh_dss = Enum.YLeaf(0, "ssh-dss")

    ssh_rsa = Enum.YLeaf(1, "ssh-rsa")

    ecdsa_sha2_nistp521 = Enum.YLeaf(2, "ecdsa-sha2-nistp521")

    ecdsa_sha2_nistp384 = Enum.YLeaf(3, "ecdsa-sha2-nistp384")

    ecdsa_sha2_nistp256 = Enum.YLeaf(4, "ecdsa-sha2-nistp256")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Hostkey']


class KexName(Enum):
    """
    KexName (Enum Class)

    Different key\-exchange(kex) algorithms

    .. data:: kex_not_applicable = -1

    	unknown

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

    kex_not_applicable = Enum.YLeaf(-1, "kex-not-applicable")

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['KexName']


class Mac(Enum):
    """
    Mac (Enum Class)

    Different Message Authentication Code(MAC)

    functions

    .. data:: mac_not_applicable = -1

    	unknown

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

    mac_not_applicable = Enum.YLeaf(-1, "mac-not-applicable")

    hmac_md5 = Enum.YLeaf(0, "hmac-md5")

    hmac_sha1 = Enum.YLeaf(1, "hmac-sha1")

    hmac_sha2_256 = Enum.YLeaf(2, "hmac-sha2-256")

    hmac_sha2_512 = Enum.YLeaf(3, "hmac-sha2-512")

    aes_gcm = Enum.YLeaf(4, "aes-gcm")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Mac']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['States']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Version']



class Ssh1(_Entity_):
    """
    Crypto Secure Shell(SSH) data
    
    .. attribute:: kex
    
    	key exchange method data
    	**type**\:  :py:class:`Kex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex>`
    
    	**config**\: False
    
    

    """

    _prefix = 'crypto-ssh-oper'
    _revision = '2017-08-25'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Ssh1, self).__init__()
        self._top_entity = None

        self.yang_name = "ssh1"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-ssh-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("kex", ("kex", Ssh1.Kex))])
        self._leafs = OrderedDict()

        self.kex = Ssh1.Kex()
        self.kex.parent = self
        self._children_name_map["kex"] = "kex"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh1"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ssh1, [], name, value)


    class Kex(_Entity_):
        """
        key exchange method data
        
        .. attribute:: nodes
        
        	Node\-specific ssh session details
        	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes>`
        
        	**config**\: False
        
        

        """

        _prefix = 'crypto-ssh-oper'
        _revision = '2017-08-25'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ssh1.Kex, self).__init__()

            self.yang_name = "kex"
            self.yang_parent_name = "ssh1"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nodes", ("nodes", Ssh1.Kex.Nodes))])
            self._leafs = OrderedDict()

            self.nodes = Ssh1.Kex.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._segment_path = lambda: "kex"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh1/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ssh1.Kex, [], name, value)


        class Nodes(_Entity_):
            """
            Node\-specific ssh session details
            
            .. attribute:: node
            
            	SSH session details for a particular node
            	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node>`
            
            	**config**\: False
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2017-08-25'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh1.Kex.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "kex"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("node", ("node", Ssh1.Kex.Nodes.Node))])
                self._leafs = OrderedDict()

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh1/kex/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh1.Kex.Nodes, [], name, value)


            class Node(_Entity_):
                """
                SSH session details for a particular node
                
                .. attribute:: node_name  (key)
                
                	Node name
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                .. attribute:: incoming_sessions
                
                	List of incoming sessions
                	**type**\:  :py:class:`IncomingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.IncomingSessions>`
                
                	**config**\: False
                
                .. attribute:: outgoing_connections
                
                	List of outgoing connections
                	**type**\:  :py:class:`OutgoingConnections <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.OutgoingConnections>`
                
                	**config**\: False
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-08-25'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh1.Kex.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['node_name']
                    self._child_classes = OrderedDict([("incoming-sessions", ("incoming_sessions", Ssh1.Kex.Nodes.Node.IncomingSessions)), ("outgoing-connections", ("outgoing_connections", Ssh1.Kex.Nodes.Node.OutgoingConnections))])
                    self._leafs = OrderedDict([
                        ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                    ])
                    self.node_name = None

                    self.incoming_sessions = Ssh1.Kex.Nodes.Node.IncomingSessions()
                    self.incoming_sessions.parent = self
                    self._children_name_map["incoming_sessions"] = "incoming-sessions"

                    self.outgoing_connections = Ssh1.Kex.Nodes.Node.OutgoingConnections()
                    self.outgoing_connections.parent = self
                    self._children_name_map["outgoing_connections"] = "outgoing-connections"
                    self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh1/kex/nodes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh1.Kex.Nodes.Node, ['node_name'], name, value)


                class IncomingSessions(_Entity_):
                    """
                    List of incoming sessions
                    
                    .. attribute:: session_detail_info
                    
                    	session detail info
                    	**type**\: list of  		 :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-08-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ssh1.Kex.Nodes.Node.IncomingSessions, self).__init__()

                        self.yang_name = "incoming-sessions"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("session-detail-info", ("session_detail_info", Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo))])
                        self._leafs = OrderedDict()

                        self.session_detail_info = YList(self)
                        self._segment_path = lambda: "incoming-sessions"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh1.Kex.Nodes.Node.IncomingSessions, [], name, value)


                    class SessionDetailInfo(_Entity_):
                        """
                        session detail info
                        
                        .. attribute:: next_session
                        
                        	next session
                        	**type**\:  :py:class:`NextSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo.NextSession>`
                        
                        	**config**\: False
                        
                        .. attribute:: session_id
                        
                        	Session ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: key_exchange
                        
                        	Key exchange name
                        	**type**\:  :py:class:`KexName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexName>`
                        
                        	**config**\: False
                        
                        .. attribute:: public_key
                        
                        	Host key algorithm
                        	**type**\:  :py:class:`Hostkey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Hostkey>`
                        
                        	**config**\: False
                        
                        .. attribute:: in_cipher
                        
                        	In cipher algorithm
                        	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                        
                        	**config**\: False
                        
                        .. attribute:: out_cipher
                        
                        	Out cipher algorithm
                        	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                        
                        	**config**\: False
                        
                        .. attribute:: in_mac
                        
                        	In MAC
                        	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                        
                        	**config**\: False
                        
                        .. attribute:: out_mac
                        
                        	Out MAC
                        	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                        
                        	**config**\: False
                        
                        .. attribute:: start_time
                        
                        	session start time
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: end_time
                        
                        	session end time
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-08-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo, self).__init__()

                            self.yang_name = "session-detail-info"
                            self.yang_parent_name = "incoming-sessions"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("next-session", ("next_session", Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo.NextSession))])
                            self._leafs = OrderedDict([
                                ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                                ('key_exchange', (YLeaf(YType.enumeration, 'key-exchange'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'KexName', '')])),
                                ('public_key', (YLeaf(YType.enumeration, 'public-key'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Hostkey', '')])),
                                ('in_cipher', (YLeaf(YType.enumeration, 'in-cipher'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Cipher', '')])),
                                ('out_cipher', (YLeaf(YType.enumeration, 'out-cipher'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Cipher', '')])),
                                ('in_mac', (YLeaf(YType.enumeration, 'in-mac'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Mac', '')])),
                                ('out_mac', (YLeaf(YType.enumeration, 'out-mac'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Mac', '')])),
                                ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                                ('end_time', (YLeaf(YType.str, 'end-time'), ['str'])),
                            ])
                            self.session_id = None
                            self.key_exchange = None
                            self.public_key = None
                            self.in_cipher = None
                            self.out_cipher = None
                            self.in_mac = None
                            self.out_mac = None
                            self.start_time = None
                            self.end_time = None

                            self.next_session = Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo.NextSession()
                            self.next_session.parent = self
                            self._children_name_map["next_session"] = "next-session"
                            self._segment_path = lambda: "session-detail-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo, ['session_id', 'key_exchange', 'public_key', 'in_cipher', 'out_cipher', 'in_mac', 'out_mac', 'start_time', 'end_time'], name, value)


                        class NextSession(_Entity_):
                            """
                            next session
                            
                            

                            """

                            _prefix = 'crypto-ssh-oper'
                            _revision = '2017-08-25'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo.NextSession, self).__init__()

                                self.yang_name = "next-session"
                                self.yang_parent_name = "session-detail-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict()
                                self._segment_path = lambda: "next-session"
                                self._is_frozen = True

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                                return meta._meta_table['Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo.NextSession']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh1.Kex.Nodes.Node.IncomingSessions']['meta_info']


                class OutgoingConnections(_Entity_):
                    """
                    List of outgoing connections
                    
                    .. attribute:: session_detail_info
                    
                    	session detail info
                    	**type**\: list of  		 :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-08-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ssh1.Kex.Nodes.Node.OutgoingConnections, self).__init__()

                        self.yang_name = "outgoing-connections"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("session-detail-info", ("session_detail_info", Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo))])
                        self._leafs = OrderedDict()

                        self.session_detail_info = YList(self)
                        self._segment_path = lambda: "outgoing-connections"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh1.Kex.Nodes.Node.OutgoingConnections, [], name, value)


                    class SessionDetailInfo(_Entity_):
                        """
                        session detail info
                        
                        .. attribute:: next_session
                        
                        	next session
                        	**type**\:  :py:class:`NextSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo.NextSession>`
                        
                        	**config**\: False
                        
                        .. attribute:: session_id
                        
                        	Session ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: key_exchange
                        
                        	Key exchange name
                        	**type**\:  :py:class:`KexName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexName>`
                        
                        	**config**\: False
                        
                        .. attribute:: public_key
                        
                        	Host key algorithm
                        	**type**\:  :py:class:`Hostkey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Hostkey>`
                        
                        	**config**\: False
                        
                        .. attribute:: in_cipher
                        
                        	In cipher algorithm
                        	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                        
                        	**config**\: False
                        
                        .. attribute:: out_cipher
                        
                        	Out cipher algorithm
                        	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                        
                        	**config**\: False
                        
                        .. attribute:: in_mac
                        
                        	In MAC
                        	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                        
                        	**config**\: False
                        
                        .. attribute:: out_mac
                        
                        	Out MAC
                        	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                        
                        	**config**\: False
                        
                        .. attribute:: start_time
                        
                        	session start time
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: end_time
                        
                        	session end time
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-08-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo, self).__init__()

                            self.yang_name = "session-detail-info"
                            self.yang_parent_name = "outgoing-connections"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("next-session", ("next_session", Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo.NextSession))])
                            self._leafs = OrderedDict([
                                ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                                ('key_exchange', (YLeaf(YType.enumeration, 'key-exchange'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'KexName', '')])),
                                ('public_key', (YLeaf(YType.enumeration, 'public-key'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Hostkey', '')])),
                                ('in_cipher', (YLeaf(YType.enumeration, 'in-cipher'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Cipher', '')])),
                                ('out_cipher', (YLeaf(YType.enumeration, 'out-cipher'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Cipher', '')])),
                                ('in_mac', (YLeaf(YType.enumeration, 'in-mac'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Mac', '')])),
                                ('out_mac', (YLeaf(YType.enumeration, 'out-mac'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Mac', '')])),
                                ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                                ('end_time', (YLeaf(YType.str, 'end-time'), ['str'])),
                            ])
                            self.session_id = None
                            self.key_exchange = None
                            self.public_key = None
                            self.in_cipher = None
                            self.out_cipher = None
                            self.in_mac = None
                            self.out_mac = None
                            self.start_time = None
                            self.end_time = None

                            self.next_session = Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo.NextSession()
                            self.next_session.parent = self
                            self._children_name_map["next_session"] = "next-session"
                            self._segment_path = lambda: "session-detail-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo, ['session_id', 'key_exchange', 'public_key', 'in_cipher', 'out_cipher', 'in_mac', 'out_mac', 'start_time', 'end_time'], name, value)


                        class NextSession(_Entity_):
                            """
                            next session
                            
                            

                            """

                            _prefix = 'crypto-ssh-oper'
                            _revision = '2017-08-25'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo.NextSession, self).__init__()

                                self.yang_name = "next-session"
                                self.yang_parent_name = "session-detail-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict()
                                self._segment_path = lambda: "next-session"
                                self._is_frozen = True

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                                return meta._meta_table['Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo.NextSession']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh1.Kex.Nodes.Node.OutgoingConnections']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh1.Kex.Nodes.Node']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                return meta._meta_table['Ssh1.Kex.Nodes']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
            return meta._meta_table['Ssh1.Kex']['meta_info']

    def clone_ptr(self):
        self._top_entity = Ssh1()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Ssh1']['meta_info']


class Ssh(_Entity_):
    """
    ssh
    
    .. attribute:: session
    
    	Crypto SSH session
    	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session>`
    
    	**config**\: False
    
    .. attribute:: server
    
    	SSH server parameters
    	**type**\:  :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Server>`
    
    	**config**\: False
    
    

    """

    _prefix = 'crypto-ssh-oper'
    _revision = '2017-08-25'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Ssh, self).__init__()
        self._top_entity = None

        self.yang_name = "ssh"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-ssh-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("session", ("session", Ssh.Session)), ("server", ("server", Ssh.Server))])
        self._leafs = OrderedDict()

        self.session = Ssh.Session()
        self.session.parent = self
        self._children_name_map["session"] = "session"

        self.server = Ssh.Server()
        self.server.parent = self
        self._children_name_map["server"] = "server"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ssh, [], name, value)


    class Session(_Entity_):
        """
        Crypto SSH session
        
        .. attribute:: rekey
        
        	SSH session rekey information
        	**type**\:  :py:class:`Rekey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey>`
        
        	**config**\: False
        
        .. attribute:: history_detail
        
        	SSH session history detail information
        	**type**\:  :py:class:`HistoryDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.HistoryDetail>`
        
        	**config**\: False
        
        .. attribute:: brief
        
        	SSH session brief information
        	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief>`
        
        	**config**\: False
        
        .. attribute:: history
        
        	SSH session history information
        	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.History>`
        
        	**config**\: False
        
        .. attribute:: detail
        
        	SSH session detail information
        	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail>`
        
        	**config**\: False
        
        

        """

        _prefix = 'crypto-ssh-oper'
        _revision = '2017-08-25'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ssh.Session, self).__init__()

            self.yang_name = "session"
            self.yang_parent_name = "ssh"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rekey", ("rekey", Ssh.Session.Rekey)), ("history-detail", ("history_detail", Ssh.Session.HistoryDetail)), ("brief", ("brief", Ssh.Session.Brief)), ("history", ("history", Ssh.Session.History)), ("detail", ("detail", Ssh.Session.Detail))])
            self._leafs = OrderedDict()

            self.rekey = Ssh.Session.Rekey()
            self.rekey.parent = self
            self._children_name_map["rekey"] = "rekey"

            self.history_detail = Ssh.Session.HistoryDetail()
            self.history_detail.parent = self
            self._children_name_map["history_detail"] = "history-detail"

            self.brief = Ssh.Session.Brief()
            self.brief.parent = self
            self._children_name_map["brief"] = "brief"

            self.history = Ssh.Session.History()
            self.history.parent = self
            self._children_name_map["history"] = "history"

            self.detail = Ssh.Session.Detail()
            self.detail.parent = self
            self._children_name_map["detail"] = "detail"
            self._segment_path = lambda: "session"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ssh.Session, [], name, value)


        class Rekey(_Entity_):
            """
            SSH session rekey information
            
            .. attribute:: incoming_sessions
            
            	List of incoming sessions
            	**type**\:  :py:class:`IncomingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.IncomingSessions>`
            
            	**config**\: False
            
            .. attribute:: outgoing_connections
            
            	List of outgoing connections
            	**type**\:  :py:class:`OutgoingConnections <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.OutgoingConnections>`
            
            	**config**\: False
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2017-08-25'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh.Session.Rekey, self).__init__()

                self.yang_name = "rekey"
                self.yang_parent_name = "session"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("incoming-sessions", ("incoming_sessions", Ssh.Session.Rekey.IncomingSessions)), ("outgoing-connections", ("outgoing_connections", Ssh.Session.Rekey.OutgoingConnections))])
                self._leafs = OrderedDict()

                self.incoming_sessions = Ssh.Session.Rekey.IncomingSessions()
                self.incoming_sessions.parent = self
                self._children_name_map["incoming_sessions"] = "incoming-sessions"

                self.outgoing_connections = Ssh.Session.Rekey.OutgoingConnections()
                self.outgoing_connections.parent = self
                self._children_name_map["outgoing_connections"] = "outgoing-connections"
                self._segment_path = lambda: "rekey"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Session.Rekey, [], name, value)


            class IncomingSessions(_Entity_):
                """
                List of incoming sessions
                
                .. attribute:: session_rekey_info
                
                	session rekey info
                	**type**\: list of  		 :py:class:`SessionRekeyInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-08-25'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Session.Rekey.IncomingSessions, self).__init__()

                    self.yang_name = "incoming-sessions"
                    self.yang_parent_name = "rekey"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session-rekey-info", ("session_rekey_info", Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo))])
                    self._leafs = OrderedDict()

                    self.session_rekey_info = YList(self)
                    self._segment_path = lambda: "incoming-sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/rekey/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Session.Rekey.IncomingSessions, [], name, value)


                class SessionRekeyInfo(_Entity_):
                    """
                    session rekey info
                    
                    .. attribute:: next_session
                    
                    	next session
                    	**type**\:  :py:class:`NextSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo.NextSession>`
                    
                    	**config**\: False
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: session_rekey_count
                    
                    	Session Rekey Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: time_to_rekey
                    
                    	Time To Rekey
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: volume_to_rekey
                    
                    	Volume To Rekey
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-08-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo, self).__init__()

                        self.yang_name = "session-rekey-info"
                        self.yang_parent_name = "incoming-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("next-session", ("next_session", Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo.NextSession))])
                        self._leafs = OrderedDict([
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('session_rekey_count', (YLeaf(YType.uint32, 'session-rekey-count'), ['int'])),
                            ('time_to_rekey', (YLeaf(YType.str, 'time-to-rekey'), ['str'])),
                            ('volume_to_rekey', (YLeaf(YType.str, 'volume-to-rekey'), ['str'])),
                        ])
                        self.session_id = None
                        self.session_rekey_count = None
                        self.time_to_rekey = None
                        self.volume_to_rekey = None

                        self.next_session = Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo.NextSession()
                        self.next_session.parent = self
                        self._children_name_map["next_session"] = "next-session"
                        self._segment_path = lambda: "session-rekey-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/rekey/incoming-sessions/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo, ['session_id', 'session_rekey_count', 'time_to_rekey', 'volume_to_rekey'], name, value)


                    class NextSession(_Entity_):
                        """
                        next session
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-08-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo.NextSession, self).__init__()

                            self.yang_name = "next-session"
                            self.yang_parent_name = "session-rekey-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict()
                            self._segment_path = lambda: "next-session"
                            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/rekey/incoming-sessions/session-rekey-info/%s" % self._segment_path()
                            self._is_frozen = True

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo.NextSession']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Rekey.IncomingSessions']['meta_info']


            class OutgoingConnections(_Entity_):
                """
                List of outgoing connections
                
                .. attribute:: session_rekey_info
                
                	session rekey info
                	**type**\: list of  		 :py:class:`SessionRekeyInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-08-25'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Session.Rekey.OutgoingConnections, self).__init__()

                    self.yang_name = "outgoing-connections"
                    self.yang_parent_name = "rekey"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session-rekey-info", ("session_rekey_info", Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo))])
                    self._leafs = OrderedDict()

                    self.session_rekey_info = YList(self)
                    self._segment_path = lambda: "outgoing-connections"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/rekey/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Session.Rekey.OutgoingConnections, [], name, value)


                class SessionRekeyInfo(_Entity_):
                    """
                    session rekey info
                    
                    .. attribute:: next_session
                    
                    	next session
                    	**type**\:  :py:class:`NextSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo.NextSession>`
                    
                    	**config**\: False
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: session_rekey_count
                    
                    	Session Rekey Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: time_to_rekey
                    
                    	Time To Rekey
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: volume_to_rekey
                    
                    	Volume To Rekey
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-08-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo, self).__init__()

                        self.yang_name = "session-rekey-info"
                        self.yang_parent_name = "outgoing-connections"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("next-session", ("next_session", Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo.NextSession))])
                        self._leafs = OrderedDict([
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('session_rekey_count', (YLeaf(YType.uint32, 'session-rekey-count'), ['int'])),
                            ('time_to_rekey', (YLeaf(YType.str, 'time-to-rekey'), ['str'])),
                            ('volume_to_rekey', (YLeaf(YType.str, 'volume-to-rekey'), ['str'])),
                        ])
                        self.session_id = None
                        self.session_rekey_count = None
                        self.time_to_rekey = None
                        self.volume_to_rekey = None

                        self.next_session = Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo.NextSession()
                        self.next_session.parent = self
                        self._children_name_map["next_session"] = "next-session"
                        self._segment_path = lambda: "session-rekey-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/rekey/outgoing-connections/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo, ['session_id', 'session_rekey_count', 'time_to_rekey', 'volume_to_rekey'], name, value)


                    class NextSession(_Entity_):
                        """
                        next session
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-08-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo.NextSession, self).__init__()

                            self.yang_name = "next-session"
                            self.yang_parent_name = "session-rekey-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict()
                            self._segment_path = lambda: "next-session"
                            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/rekey/outgoing-connections/session-rekey-info/%s" % self._segment_path()
                            self._is_frozen = True

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo.NextSession']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Rekey.OutgoingConnections']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                return meta._meta_table['Ssh.Session.Rekey']['meta_info']


        class HistoryDetail(_Entity_):
            """
            SSH session history detail information
            
            .. attribute:: incoming_sessions
            
            	List of incoming sessions
            	**type**\:  :py:class:`IncomingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.HistoryDetail.IncomingSessions>`
            
            	**config**\: False
            
            .. attribute:: outgoing_connections
            
            	List of outgoing connections
            	**type**\:  :py:class:`OutgoingConnections <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.HistoryDetail.OutgoingConnections>`
            
            	**config**\: False
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2017-08-25'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh.Session.HistoryDetail, self).__init__()

                self.yang_name = "history-detail"
                self.yang_parent_name = "session"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("incoming-sessions", ("incoming_sessions", Ssh.Session.HistoryDetail.IncomingSessions)), ("outgoing-connections", ("outgoing_connections", Ssh.Session.HistoryDetail.OutgoingConnections))])
                self._leafs = OrderedDict()

                self.incoming_sessions = Ssh.Session.HistoryDetail.IncomingSessions()
                self.incoming_sessions.parent = self
                self._children_name_map["incoming_sessions"] = "incoming-sessions"

                self.outgoing_connections = Ssh.Session.HistoryDetail.OutgoingConnections()
                self.outgoing_connections.parent = self
                self._children_name_map["outgoing_connections"] = "outgoing-connections"
                self._segment_path = lambda: "history-detail"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Session.HistoryDetail, [], name, value)


            class IncomingSessions(_Entity_):
                """
                List of incoming sessions
                
                .. attribute:: session_detail_info
                
                	session detail info
                	**type**\: list of  		 :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.HistoryDetail.IncomingSessions.SessionDetailInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-08-25'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Session.HistoryDetail.IncomingSessions, self).__init__()

                    self.yang_name = "incoming-sessions"
                    self.yang_parent_name = "history-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session-detail-info", ("session_detail_info", Ssh.Session.HistoryDetail.IncomingSessions.SessionDetailInfo))])
                    self._leafs = OrderedDict()

                    self.session_detail_info = YList(self)
                    self._segment_path = lambda: "incoming-sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/history-detail/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Session.HistoryDetail.IncomingSessions, [], name, value)


                class SessionDetailInfo(_Entity_):
                    """
                    session detail info
                    
                    .. attribute:: next_session
                    
                    	next session
                    	**type**\:  :py:class:`NextSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.HistoryDetail.IncomingSessions.SessionDetailInfo.NextSession>`
                    
                    	**config**\: False
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: key_exchange
                    
                    	Key exchange name
                    	**type**\:  :py:class:`KexName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexName>`
                    
                    	**config**\: False
                    
                    .. attribute:: public_key
                    
                    	Host key algorithm
                    	**type**\:  :py:class:`Hostkey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Hostkey>`
                    
                    	**config**\: False
                    
                    .. attribute:: in_cipher
                    
                    	In cipher algorithm
                    	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    	**config**\: False
                    
                    .. attribute:: out_cipher
                    
                    	Out cipher algorithm
                    	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    	**config**\: False
                    
                    .. attribute:: in_mac
                    
                    	In MAC
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    	**config**\: False
                    
                    .. attribute:: out_mac
                    
                    	Out MAC
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    	**config**\: False
                    
                    .. attribute:: start_time
                    
                    	session start time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: end_time
                    
                    	session end time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-08-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ssh.Session.HistoryDetail.IncomingSessions.SessionDetailInfo, self).__init__()

                        self.yang_name = "session-detail-info"
                        self.yang_parent_name = "incoming-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("next-session", ("next_session", Ssh.Session.HistoryDetail.IncomingSessions.SessionDetailInfo.NextSession))])
                        self._leafs = OrderedDict([
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('key_exchange', (YLeaf(YType.enumeration, 'key-exchange'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'KexName', '')])),
                            ('public_key', (YLeaf(YType.enumeration, 'public-key'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Hostkey', '')])),
                            ('in_cipher', (YLeaf(YType.enumeration, 'in-cipher'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Cipher', '')])),
                            ('out_cipher', (YLeaf(YType.enumeration, 'out-cipher'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Cipher', '')])),
                            ('in_mac', (YLeaf(YType.enumeration, 'in-mac'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Mac', '')])),
                            ('out_mac', (YLeaf(YType.enumeration, 'out-mac'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Mac', '')])),
                            ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                            ('end_time', (YLeaf(YType.str, 'end-time'), ['str'])),
                        ])
                        self.session_id = None
                        self.key_exchange = None
                        self.public_key = None
                        self.in_cipher = None
                        self.out_cipher = None
                        self.in_mac = None
                        self.out_mac = None
                        self.start_time = None
                        self.end_time = None

                        self.next_session = Ssh.Session.HistoryDetail.IncomingSessions.SessionDetailInfo.NextSession()
                        self.next_session.parent = self
                        self._children_name_map["next_session"] = "next-session"
                        self._segment_path = lambda: "session-detail-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/history-detail/incoming-sessions/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh.Session.HistoryDetail.IncomingSessions.SessionDetailInfo, ['session_id', 'key_exchange', 'public_key', 'in_cipher', 'out_cipher', 'in_mac', 'out_mac', 'start_time', 'end_time'], name, value)


                    class NextSession(_Entity_):
                        """
                        next session
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-08-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ssh.Session.HistoryDetail.IncomingSessions.SessionDetailInfo.NextSession, self).__init__()

                            self.yang_name = "next-session"
                            self.yang_parent_name = "session-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict()
                            self._segment_path = lambda: "next-session"
                            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/history-detail/incoming-sessions/session-detail-info/%s" % self._segment_path()
                            self._is_frozen = True

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh.Session.HistoryDetail.IncomingSessions.SessionDetailInfo.NextSession']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.HistoryDetail.IncomingSessions.SessionDetailInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.HistoryDetail.IncomingSessions']['meta_info']


            class OutgoingConnections(_Entity_):
                """
                List of outgoing connections
                
                .. attribute:: session_detail_info
                
                	session detail info
                	**type**\: list of  		 :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.HistoryDetail.OutgoingConnections.SessionDetailInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-08-25'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Session.HistoryDetail.OutgoingConnections, self).__init__()

                    self.yang_name = "outgoing-connections"
                    self.yang_parent_name = "history-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session-detail-info", ("session_detail_info", Ssh.Session.HistoryDetail.OutgoingConnections.SessionDetailInfo))])
                    self._leafs = OrderedDict()

                    self.session_detail_info = YList(self)
                    self._segment_path = lambda: "outgoing-connections"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/history-detail/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Session.HistoryDetail.OutgoingConnections, [], name, value)


                class SessionDetailInfo(_Entity_):
                    """
                    session detail info
                    
                    .. attribute:: next_session
                    
                    	next session
                    	**type**\:  :py:class:`NextSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.HistoryDetail.OutgoingConnections.SessionDetailInfo.NextSession>`
                    
                    	**config**\: False
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: key_exchange
                    
                    	Key exchange name
                    	**type**\:  :py:class:`KexName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexName>`
                    
                    	**config**\: False
                    
                    .. attribute:: public_key
                    
                    	Host key algorithm
                    	**type**\:  :py:class:`Hostkey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Hostkey>`
                    
                    	**config**\: False
                    
                    .. attribute:: in_cipher
                    
                    	In cipher algorithm
                    	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    	**config**\: False
                    
                    .. attribute:: out_cipher
                    
                    	Out cipher algorithm
                    	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    	**config**\: False
                    
                    .. attribute:: in_mac
                    
                    	In MAC
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    	**config**\: False
                    
                    .. attribute:: out_mac
                    
                    	Out MAC
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    	**config**\: False
                    
                    .. attribute:: start_time
                    
                    	session start time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: end_time
                    
                    	session end time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-08-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ssh.Session.HistoryDetail.OutgoingConnections.SessionDetailInfo, self).__init__()

                        self.yang_name = "session-detail-info"
                        self.yang_parent_name = "outgoing-connections"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("next-session", ("next_session", Ssh.Session.HistoryDetail.OutgoingConnections.SessionDetailInfo.NextSession))])
                        self._leafs = OrderedDict([
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('key_exchange', (YLeaf(YType.enumeration, 'key-exchange'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'KexName', '')])),
                            ('public_key', (YLeaf(YType.enumeration, 'public-key'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Hostkey', '')])),
                            ('in_cipher', (YLeaf(YType.enumeration, 'in-cipher'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Cipher', '')])),
                            ('out_cipher', (YLeaf(YType.enumeration, 'out-cipher'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Cipher', '')])),
                            ('in_mac', (YLeaf(YType.enumeration, 'in-mac'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Mac', '')])),
                            ('out_mac', (YLeaf(YType.enumeration, 'out-mac'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Mac', '')])),
                            ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                            ('end_time', (YLeaf(YType.str, 'end-time'), ['str'])),
                        ])
                        self.session_id = None
                        self.key_exchange = None
                        self.public_key = None
                        self.in_cipher = None
                        self.out_cipher = None
                        self.in_mac = None
                        self.out_mac = None
                        self.start_time = None
                        self.end_time = None

                        self.next_session = Ssh.Session.HistoryDetail.OutgoingConnections.SessionDetailInfo.NextSession()
                        self.next_session.parent = self
                        self._children_name_map["next_session"] = "next-session"
                        self._segment_path = lambda: "session-detail-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/history-detail/outgoing-connections/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh.Session.HistoryDetail.OutgoingConnections.SessionDetailInfo, ['session_id', 'key_exchange', 'public_key', 'in_cipher', 'out_cipher', 'in_mac', 'out_mac', 'start_time', 'end_time'], name, value)


                    class NextSession(_Entity_):
                        """
                        next session
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-08-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ssh.Session.HistoryDetail.OutgoingConnections.SessionDetailInfo.NextSession, self).__init__()

                            self.yang_name = "next-session"
                            self.yang_parent_name = "session-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict()
                            self._segment_path = lambda: "next-session"
                            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/history-detail/outgoing-connections/session-detail-info/%s" % self._segment_path()
                            self._is_frozen = True

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh.Session.HistoryDetail.OutgoingConnections.SessionDetailInfo.NextSession']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.HistoryDetail.OutgoingConnections.SessionDetailInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.HistoryDetail.OutgoingConnections']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                return meta._meta_table['Ssh.Session.HistoryDetail']['meta_info']


        class Brief(_Entity_):
            """
            SSH session brief information
            
            .. attribute:: incoming_sessions
            
            	List of incoming sessions
            	**type**\:  :py:class:`IncomingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.IncomingSessions>`
            
            	**config**\: False
            
            .. attribute:: outgoing_sessions
            
            	List of outgoing sessions
            	**type**\:  :py:class:`OutgoingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.OutgoingSessions>`
            
            	**config**\: False
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2017-08-25'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh.Session.Brief, self).__init__()

                self.yang_name = "brief"
                self.yang_parent_name = "session"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("incoming-sessions", ("incoming_sessions", Ssh.Session.Brief.IncomingSessions)), ("outgoing-sessions", ("outgoing_sessions", Ssh.Session.Brief.OutgoingSessions))])
                self._leafs = OrderedDict()

                self.incoming_sessions = Ssh.Session.Brief.IncomingSessions()
                self.incoming_sessions.parent = self
                self._children_name_map["incoming_sessions"] = "incoming-sessions"

                self.outgoing_sessions = Ssh.Session.Brief.OutgoingSessions()
                self.outgoing_sessions.parent = self
                self._children_name_map["outgoing_sessions"] = "outgoing-sessions"
                self._segment_path = lambda: "brief"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Session.Brief, [], name, value)


            class IncomingSessions(_Entity_):
                """
                List of incoming sessions
                
                .. attribute:: session_brief_info
                
                	session brief info
                	**type**\: list of  		 :py:class:`SessionBriefInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.IncomingSessions.SessionBriefInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-08-25'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Session.Brief.IncomingSessions, self).__init__()

                    self.yang_name = "incoming-sessions"
                    self.yang_parent_name = "brief"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session-brief-info", ("session_brief_info", Ssh.Session.Brief.IncomingSessions.SessionBriefInfo))])
                    self._leafs = OrderedDict()

                    self.session_brief_info = YList(self)
                    self._segment_path = lambda: "incoming-sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Session.Brief.IncomingSessions, [], name, value)


                class SessionBriefInfo(_Entity_):
                    """
                    session brief info
                    
                    .. attribute:: next_session
                    
                    	next session
                    	**type**\:  :py:class:`NextSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.IncomingSessions.SessionBriefInfo.NextSession>`
                    
                    	**config**\: False
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: node_name
                    
                    	Node name
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: session_state
                    
                    	SSH session state
                    	**type**\:  :py:class:`States <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.States>`
                    
                    	**config**\: False
                    
                    .. attribute:: user_id
                    
                    	User ID
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: host_address
                    
                    	Host address
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: version
                    
                    	SSH state version
                    	**type**\:  :py:class:`Version <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Version>`
                    
                    	**config**\: False
                    
                    .. attribute:: authentication_type
                    
                    	Authentication method
                    	**type**\:  :py:class:`Authen <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Authen>`
                    
                    	**config**\: False
                    
                    .. attribute:: mc_info
                    
                    	List of channel info
                    	**type**\: list of  		 :py:class:`McInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.IncomingSessions.SessionBriefInfo.McInfo>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-08-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ssh.Session.Brief.IncomingSessions.SessionBriefInfo, self).__init__()

                        self.yang_name = "session-brief-info"
                        self.yang_parent_name = "incoming-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("next-session", ("next_session", Ssh.Session.Brief.IncomingSessions.SessionBriefInfo.NextSession)), ("mc-info", ("mc_info", Ssh.Session.Brief.IncomingSessions.SessionBriefInfo.McInfo))])
                        self._leafs = OrderedDict([
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('session_state', (YLeaf(YType.enumeration, 'session-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'States', '')])),
                            ('user_id', (YLeaf(YType.str, 'user-id'), ['str'])),
                            ('host_address', (YLeaf(YType.str, 'host-address'), ['str'])),
                            ('version', (YLeaf(YType.enumeration, 'version'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Version', '')])),
                            ('authentication_type', (YLeaf(YType.enumeration, 'authentication-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Authen', '')])),
                        ])
                        self.session_id = None
                        self.node_name = None
                        self.session_state = None
                        self.user_id = None
                        self.host_address = None
                        self.version = None
                        self.authentication_type = None

                        self.next_session = Ssh.Session.Brief.IncomingSessions.SessionBriefInfo.NextSession()
                        self.next_session.parent = self
                        self._children_name_map["next_session"] = "next-session"

                        self.mc_info = YList(self)
                        self._segment_path = lambda: "session-brief-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/incoming-sessions/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh.Session.Brief.IncomingSessions.SessionBriefInfo, ['session_id', 'node_name', 'session_state', 'user_id', 'host_address', 'version', 'authentication_type'], name, value)


                    class NextSession(_Entity_):
                        """
                        next session
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-08-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ssh.Session.Brief.IncomingSessions.SessionBriefInfo.NextSession, self).__init__()

                            self.yang_name = "next-session"
                            self.yang_parent_name = "session-brief-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict()
                            self._segment_path = lambda: "next-session"
                            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/incoming-sessions/session-brief-info/%s" % self._segment_path()
                            self._is_frozen = True

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh.Session.Brief.IncomingSessions.SessionBriefInfo.NextSession']['meta_info']


                    class McInfo(_Entity_):
                        """
                        List of channel info
                        
                        .. attribute:: channel_id
                        
                        	Channel ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: connection_type
                        
                        	Channel Connection Type
                        	**type**\:  :py:class:`Connection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Connection>`
                        
                        	**config**\: False
                        
                        .. attribute:: vty_line_number
                        
                        	VTY line number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: vty_assigned
                        
                        	Boolean indicating whether line VTY line number is valid
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-08-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ssh.Session.Brief.IncomingSessions.SessionBriefInfo.McInfo, self).__init__()

                            self.yang_name = "mc-info"
                            self.yang_parent_name = "session-brief-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('channel_id', (YLeaf(YType.uint32, 'channel-id'), ['int'])),
                                ('connection_type', (YLeaf(YType.enumeration, 'connection-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Connection', '')])),
                                ('vty_line_number', (YLeaf(YType.uint32, 'vty-line-number'), ['int'])),
                                ('vty_assigned', (YLeaf(YType.boolean, 'vty-assigned'), ['bool'])),
                            ])
                            self.channel_id = None
                            self.connection_type = None
                            self.vty_line_number = None
                            self.vty_assigned = None
                            self._segment_path = lambda: "mc-info"
                            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/incoming-sessions/session-brief-info/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ssh.Session.Brief.IncomingSessions.SessionBriefInfo.McInfo, ['channel_id', 'connection_type', 'vty_line_number', 'vty_assigned'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh.Session.Brief.IncomingSessions.SessionBriefInfo.McInfo']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Brief.IncomingSessions.SessionBriefInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Brief.IncomingSessions']['meta_info']


            class OutgoingSessions(_Entity_):
                """
                List of outgoing sessions
                
                .. attribute:: session_brief_info
                
                	session brief info
                	**type**\: list of  		 :py:class:`SessionBriefInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-08-25'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Session.Brief.OutgoingSessions, self).__init__()

                    self.yang_name = "outgoing-sessions"
                    self.yang_parent_name = "brief"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session-brief-info", ("session_brief_info", Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo))])
                    self._leafs = OrderedDict()

                    self.session_brief_info = YList(self)
                    self._segment_path = lambda: "outgoing-sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Session.Brief.OutgoingSessions, [], name, value)


                class SessionBriefInfo(_Entity_):
                    """
                    session brief info
                    
                    .. attribute:: next_session
                    
                    	next session
                    	**type**\:  :py:class:`NextSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo.NextSession>`
                    
                    	**config**\: False
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: node_name
                    
                    	Node name
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: session_state
                    
                    	SSH session state
                    	**type**\:  :py:class:`States <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.States>`
                    
                    	**config**\: False
                    
                    .. attribute:: user_id
                    
                    	User ID
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: host_address
                    
                    	Host address
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: version
                    
                    	SSH state version
                    	**type**\:  :py:class:`Version <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Version>`
                    
                    	**config**\: False
                    
                    .. attribute:: authentication_type
                    
                    	Authentication method
                    	**type**\:  :py:class:`Authen <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Authen>`
                    
                    	**config**\: False
                    
                    .. attribute:: mc_info
                    
                    	List of channel info
                    	**type**\: list of  		 :py:class:`McInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo.McInfo>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-08-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo, self).__init__()

                        self.yang_name = "session-brief-info"
                        self.yang_parent_name = "outgoing-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("next-session", ("next_session", Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo.NextSession)), ("mc-info", ("mc_info", Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo.McInfo))])
                        self._leafs = OrderedDict([
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('session_state', (YLeaf(YType.enumeration, 'session-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'States', '')])),
                            ('user_id', (YLeaf(YType.str, 'user-id'), ['str'])),
                            ('host_address', (YLeaf(YType.str, 'host-address'), ['str'])),
                            ('version', (YLeaf(YType.enumeration, 'version'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Version', '')])),
                            ('authentication_type', (YLeaf(YType.enumeration, 'authentication-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Authen', '')])),
                        ])
                        self.session_id = None
                        self.node_name = None
                        self.session_state = None
                        self.user_id = None
                        self.host_address = None
                        self.version = None
                        self.authentication_type = None

                        self.next_session = Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo.NextSession()
                        self.next_session.parent = self
                        self._children_name_map["next_session"] = "next-session"

                        self.mc_info = YList(self)
                        self._segment_path = lambda: "session-brief-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/outgoing-sessions/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo, ['session_id', 'node_name', 'session_state', 'user_id', 'host_address', 'version', 'authentication_type'], name, value)


                    class NextSession(_Entity_):
                        """
                        next session
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-08-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo.NextSession, self).__init__()

                            self.yang_name = "next-session"
                            self.yang_parent_name = "session-brief-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict()
                            self._segment_path = lambda: "next-session"
                            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/outgoing-sessions/session-brief-info/%s" % self._segment_path()
                            self._is_frozen = True

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo.NextSession']['meta_info']


                    class McInfo(_Entity_):
                        """
                        List of channel info
                        
                        .. attribute:: channel_id
                        
                        	Channel ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: connection_type
                        
                        	Channel Connection Type
                        	**type**\:  :py:class:`Connection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Connection>`
                        
                        	**config**\: False
                        
                        .. attribute:: vty_line_number
                        
                        	VTY line number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: vty_assigned
                        
                        	Boolean indicating whether line VTY line number is valid
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-08-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo.McInfo, self).__init__()

                            self.yang_name = "mc-info"
                            self.yang_parent_name = "session-brief-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('channel_id', (YLeaf(YType.uint32, 'channel-id'), ['int'])),
                                ('connection_type', (YLeaf(YType.enumeration, 'connection-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Connection', '')])),
                                ('vty_line_number', (YLeaf(YType.uint32, 'vty-line-number'), ['int'])),
                                ('vty_assigned', (YLeaf(YType.boolean, 'vty-assigned'), ['bool'])),
                            ])
                            self.channel_id = None
                            self.connection_type = None
                            self.vty_line_number = None
                            self.vty_assigned = None
                            self._segment_path = lambda: "mc-info"
                            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/outgoing-sessions/session-brief-info/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo.McInfo, ['channel_id', 'connection_type', 'vty_line_number', 'vty_assigned'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo.McInfo']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Brief.OutgoingSessions']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                return meta._meta_table['Ssh.Session.Brief']['meta_info']


        class History(_Entity_):
            """
            SSH session history information
            
            .. attribute:: incoming_sessions
            
            	List of incoming sessions
            	**type**\:  :py:class:`IncomingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.History.IncomingSessions>`
            
            	**config**\: False
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2017-08-25'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh.Session.History, self).__init__()

                self.yang_name = "history"
                self.yang_parent_name = "session"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("incoming-sessions", ("incoming_sessions", Ssh.Session.History.IncomingSessions))])
                self._leafs = OrderedDict()

                self.incoming_sessions = Ssh.Session.History.IncomingSessions()
                self.incoming_sessions.parent = self
                self._children_name_map["incoming_sessions"] = "incoming-sessions"
                self._segment_path = lambda: "history"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Session.History, [], name, value)


            class IncomingSessions(_Entity_):
                """
                List of incoming sessions
                
                .. attribute:: session_history_info
                
                	session history info
                	**type**\: list of  		 :py:class:`SessionHistoryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.History.IncomingSessions.SessionHistoryInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-08-25'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Session.History.IncomingSessions, self).__init__()

                    self.yang_name = "incoming-sessions"
                    self.yang_parent_name = "history"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session-history-info", ("session_history_info", Ssh.Session.History.IncomingSessions.SessionHistoryInfo))])
                    self._leafs = OrderedDict()

                    self.session_history_info = YList(self)
                    self._segment_path = lambda: "incoming-sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/history/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Session.History.IncomingSessions, [], name, value)


                class SessionHistoryInfo(_Entity_):
                    """
                    session history info
                    
                    .. attribute:: next_session
                    
                    	next session
                    	**type**\:  :py:class:`NextSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.History.IncomingSessions.SessionHistoryInfo.NextSession>`
                    
                    	**config**\: False
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: node_name
                    
                    	Node name
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: user_id
                    
                    	User ID
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: host_address
                    
                    	Host address
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: version
                    
                    	SSH state version
                    	**type**\:  :py:class:`Version <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Version>`
                    
                    	**config**\: False
                    
                    .. attribute:: authentication_type
                    
                    	Authentication method
                    	**type**\:  :py:class:`Authen <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Authen>`
                    
                    	**config**\: False
                    
                    .. attribute:: mc_info
                    
                    	List of channel info
                    	**type**\: list of  		 :py:class:`McInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.History.IncomingSessions.SessionHistoryInfo.McInfo>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-08-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ssh.Session.History.IncomingSessions.SessionHistoryInfo, self).__init__()

                        self.yang_name = "session-history-info"
                        self.yang_parent_name = "incoming-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("next-session", ("next_session", Ssh.Session.History.IncomingSessions.SessionHistoryInfo.NextSession)), ("mc-info", ("mc_info", Ssh.Session.History.IncomingSessions.SessionHistoryInfo.McInfo))])
                        self._leafs = OrderedDict([
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('user_id', (YLeaf(YType.str, 'user-id'), ['str'])),
                            ('host_address', (YLeaf(YType.str, 'host-address'), ['str'])),
                            ('version', (YLeaf(YType.enumeration, 'version'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Version', '')])),
                            ('authentication_type', (YLeaf(YType.enumeration, 'authentication-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Authen', '')])),
                        ])
                        self.session_id = None
                        self.node_name = None
                        self.user_id = None
                        self.host_address = None
                        self.version = None
                        self.authentication_type = None

                        self.next_session = Ssh.Session.History.IncomingSessions.SessionHistoryInfo.NextSession()
                        self.next_session.parent = self
                        self._children_name_map["next_session"] = "next-session"

                        self.mc_info = YList(self)
                        self._segment_path = lambda: "session-history-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/history/incoming-sessions/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh.Session.History.IncomingSessions.SessionHistoryInfo, ['session_id', 'node_name', 'user_id', 'host_address', 'version', 'authentication_type'], name, value)


                    class NextSession(_Entity_):
                        """
                        next session
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-08-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ssh.Session.History.IncomingSessions.SessionHistoryInfo.NextSession, self).__init__()

                            self.yang_name = "next-session"
                            self.yang_parent_name = "session-history-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict()
                            self._segment_path = lambda: "next-session"
                            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/history/incoming-sessions/session-history-info/%s" % self._segment_path()
                            self._is_frozen = True

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh.Session.History.IncomingSessions.SessionHistoryInfo.NextSession']['meta_info']


                    class McInfo(_Entity_):
                        """
                        List of channel info
                        
                        .. attribute:: channel_id
                        
                        	Channel ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: connection_type
                        
                        	Channel Connection Type
                        	**type**\:  :py:class:`Connection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Connection>`
                        
                        	**config**\: False
                        
                        .. attribute:: vty_line_number
                        
                        	VTY line number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: vty_assigned
                        
                        	Boolean indicating whether line VTY line number is valid
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-08-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ssh.Session.History.IncomingSessions.SessionHistoryInfo.McInfo, self).__init__()

                            self.yang_name = "mc-info"
                            self.yang_parent_name = "session-history-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('channel_id', (YLeaf(YType.uint32, 'channel-id'), ['int'])),
                                ('connection_type', (YLeaf(YType.enumeration, 'connection-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Connection', '')])),
                                ('vty_line_number', (YLeaf(YType.uint32, 'vty-line-number'), ['int'])),
                                ('vty_assigned', (YLeaf(YType.boolean, 'vty-assigned'), ['bool'])),
                            ])
                            self.channel_id = None
                            self.connection_type = None
                            self.vty_line_number = None
                            self.vty_assigned = None
                            self._segment_path = lambda: "mc-info"
                            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/history/incoming-sessions/session-history-info/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ssh.Session.History.IncomingSessions.SessionHistoryInfo.McInfo, ['channel_id', 'connection_type', 'vty_line_number', 'vty_assigned'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh.Session.History.IncomingSessions.SessionHistoryInfo.McInfo']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.History.IncomingSessions.SessionHistoryInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.History.IncomingSessions']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                return meta._meta_table['Ssh.Session.History']['meta_info']


        class Detail(_Entity_):
            """
            SSH session detail information
            
            .. attribute:: incoming_sessions
            
            	List of incoming sessions
            	**type**\:  :py:class:`IncomingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.IncomingSessions>`
            
            	**config**\: False
            
            .. attribute:: outgoing_connections
            
            	List of outgoing connections
            	**type**\:  :py:class:`OutgoingConnections <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.OutgoingConnections>`
            
            	**config**\: False
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2017-08-25'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssh.Session.Detail, self).__init__()

                self.yang_name = "detail"
                self.yang_parent_name = "session"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("incoming-sessions", ("incoming_sessions", Ssh.Session.Detail.IncomingSessions)), ("outgoing-connections", ("outgoing_connections", Ssh.Session.Detail.OutgoingConnections))])
                self._leafs = OrderedDict()

                self.incoming_sessions = Ssh.Session.Detail.IncomingSessions()
                self.incoming_sessions.parent = self
                self._children_name_map["incoming_sessions"] = "incoming-sessions"

                self.outgoing_connections = Ssh.Session.Detail.OutgoingConnections()
                self.outgoing_connections.parent = self
                self._children_name_map["outgoing_connections"] = "outgoing-connections"
                self._segment_path = lambda: "detail"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssh.Session.Detail, [], name, value)


            class IncomingSessions(_Entity_):
                """
                List of incoming sessions
                
                .. attribute:: session_detail_info
                
                	session detail info
                	**type**\: list of  		 :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.IncomingSessions.SessionDetailInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-08-25'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Session.Detail.IncomingSessions, self).__init__()

                    self.yang_name = "incoming-sessions"
                    self.yang_parent_name = "detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session-detail-info", ("session_detail_info", Ssh.Session.Detail.IncomingSessions.SessionDetailInfo))])
                    self._leafs = OrderedDict()

                    self.session_detail_info = YList(self)
                    self._segment_path = lambda: "incoming-sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/detail/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Session.Detail.IncomingSessions, [], name, value)


                class SessionDetailInfo(_Entity_):
                    """
                    session detail info
                    
                    .. attribute:: next_session
                    
                    	next session
                    	**type**\:  :py:class:`NextSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.IncomingSessions.SessionDetailInfo.NextSession>`
                    
                    	**config**\: False
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: key_exchange
                    
                    	Key exchange name
                    	**type**\:  :py:class:`KexName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexName>`
                    
                    	**config**\: False
                    
                    .. attribute:: public_key
                    
                    	Host key algorithm
                    	**type**\:  :py:class:`Hostkey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Hostkey>`
                    
                    	**config**\: False
                    
                    .. attribute:: in_cipher
                    
                    	In cipher algorithm
                    	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    	**config**\: False
                    
                    .. attribute:: out_cipher
                    
                    	Out cipher algorithm
                    	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    	**config**\: False
                    
                    .. attribute:: in_mac
                    
                    	In MAC
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    	**config**\: False
                    
                    .. attribute:: out_mac
                    
                    	Out MAC
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    	**config**\: False
                    
                    .. attribute:: start_time
                    
                    	session start time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: end_time
                    
                    	session end time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-08-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ssh.Session.Detail.IncomingSessions.SessionDetailInfo, self).__init__()

                        self.yang_name = "session-detail-info"
                        self.yang_parent_name = "incoming-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("next-session", ("next_session", Ssh.Session.Detail.IncomingSessions.SessionDetailInfo.NextSession))])
                        self._leafs = OrderedDict([
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('key_exchange', (YLeaf(YType.enumeration, 'key-exchange'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'KexName', '')])),
                            ('public_key', (YLeaf(YType.enumeration, 'public-key'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Hostkey', '')])),
                            ('in_cipher', (YLeaf(YType.enumeration, 'in-cipher'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Cipher', '')])),
                            ('out_cipher', (YLeaf(YType.enumeration, 'out-cipher'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Cipher', '')])),
                            ('in_mac', (YLeaf(YType.enumeration, 'in-mac'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Mac', '')])),
                            ('out_mac', (YLeaf(YType.enumeration, 'out-mac'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Mac', '')])),
                            ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                            ('end_time', (YLeaf(YType.str, 'end-time'), ['str'])),
                        ])
                        self.session_id = None
                        self.key_exchange = None
                        self.public_key = None
                        self.in_cipher = None
                        self.out_cipher = None
                        self.in_mac = None
                        self.out_mac = None
                        self.start_time = None
                        self.end_time = None

                        self.next_session = Ssh.Session.Detail.IncomingSessions.SessionDetailInfo.NextSession()
                        self.next_session.parent = self
                        self._children_name_map["next_session"] = "next-session"
                        self._segment_path = lambda: "session-detail-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/detail/incoming-sessions/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh.Session.Detail.IncomingSessions.SessionDetailInfo, ['session_id', 'key_exchange', 'public_key', 'in_cipher', 'out_cipher', 'in_mac', 'out_mac', 'start_time', 'end_time'], name, value)


                    class NextSession(_Entity_):
                        """
                        next session
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-08-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ssh.Session.Detail.IncomingSessions.SessionDetailInfo.NextSession, self).__init__()

                            self.yang_name = "next-session"
                            self.yang_parent_name = "session-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict()
                            self._segment_path = lambda: "next-session"
                            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/detail/incoming-sessions/session-detail-info/%s" % self._segment_path()
                            self._is_frozen = True

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh.Session.Detail.IncomingSessions.SessionDetailInfo.NextSession']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Detail.IncomingSessions.SessionDetailInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Detail.IncomingSessions']['meta_info']


            class OutgoingConnections(_Entity_):
                """
                List of outgoing connections
                
                .. attribute:: session_detail_info
                
                	session detail info
                	**type**\: list of  		 :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2017-08-25'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssh.Session.Detail.OutgoingConnections, self).__init__()

                    self.yang_name = "outgoing-connections"
                    self.yang_parent_name = "detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session-detail-info", ("session_detail_info", Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo))])
                    self._leafs = OrderedDict()

                    self.session_detail_info = YList(self)
                    self._segment_path = lambda: "outgoing-connections"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/detail/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssh.Session.Detail.OutgoingConnections, [], name, value)


                class SessionDetailInfo(_Entity_):
                    """
                    session detail info
                    
                    .. attribute:: next_session
                    
                    	next session
                    	**type**\:  :py:class:`NextSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo.NextSession>`
                    
                    	**config**\: False
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: key_exchange
                    
                    	Key exchange name
                    	**type**\:  :py:class:`KexName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexName>`
                    
                    	**config**\: False
                    
                    .. attribute:: public_key
                    
                    	Host key algorithm
                    	**type**\:  :py:class:`Hostkey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Hostkey>`
                    
                    	**config**\: False
                    
                    .. attribute:: in_cipher
                    
                    	In cipher algorithm
                    	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    	**config**\: False
                    
                    .. attribute:: out_cipher
                    
                    	Out cipher algorithm
                    	**type**\:  :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    	**config**\: False
                    
                    .. attribute:: in_mac
                    
                    	In MAC
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    	**config**\: False
                    
                    .. attribute:: out_mac
                    
                    	Out MAC
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    	**config**\: False
                    
                    .. attribute:: start_time
                    
                    	session start time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: end_time
                    
                    	session end time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2017-08-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo, self).__init__()

                        self.yang_name = "session-detail-info"
                        self.yang_parent_name = "outgoing-connections"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("next-session", ("next_session", Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo.NextSession))])
                        self._leafs = OrderedDict([
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('key_exchange', (YLeaf(YType.enumeration, 'key-exchange'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'KexName', '')])),
                            ('public_key', (YLeaf(YType.enumeration, 'public-key'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Hostkey', '')])),
                            ('in_cipher', (YLeaf(YType.enumeration, 'in-cipher'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Cipher', '')])),
                            ('out_cipher', (YLeaf(YType.enumeration, 'out-cipher'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Cipher', '')])),
                            ('in_mac', (YLeaf(YType.enumeration, 'in-mac'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Mac', '')])),
                            ('out_mac', (YLeaf(YType.enumeration, 'out-mac'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Mac', '')])),
                            ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                            ('end_time', (YLeaf(YType.str, 'end-time'), ['str'])),
                        ])
                        self.session_id = None
                        self.key_exchange = None
                        self.public_key = None
                        self.in_cipher = None
                        self.out_cipher = None
                        self.in_mac = None
                        self.out_mac = None
                        self.start_time = None
                        self.end_time = None

                        self.next_session = Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo.NextSession()
                        self.next_session.parent = self
                        self._children_name_map["next_session"] = "next-session"
                        self._segment_path = lambda: "session-detail-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/detail/outgoing-connections/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo, ['session_id', 'key_exchange', 'public_key', 'in_cipher', 'out_cipher', 'in_mac', 'out_mac', 'start_time', 'end_time'], name, value)


                    class NextSession(_Entity_):
                        """
                        next session
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2017-08-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo.NextSession, self).__init__()

                            self.yang_name = "next-session"
                            self.yang_parent_name = "session-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict()
                            self._segment_path = lambda: "next-session"
                            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/detail/outgoing-connections/session-detail-info/%s" % self._segment_path()
                            self._is_frozen = True

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo.NextSession']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Detail.OutgoingConnections']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                return meta._meta_table['Ssh.Session.Detail']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
            return meta._meta_table['Ssh.Session']['meta_info']


    class Server(_Entity_):
        """
        SSH server parameters
        
        .. attribute:: version
        
        	Version
        	**type**\: str
        
        	**length:** 0..10
        
        	**config**\: False
        
        .. attribute:: port
        
        	SSH Port
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: vrf
        
        	Vrfs and acls
        	**type**\: str
        
        	**length:** 0..500
        
        	**config**\: False
        
        .. attribute:: netconfport
        
        	Netconf Port
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: netconfvrf
        
        	Netconf vrfs and acls
        	**type**\: str
        
        	**length:** 0..500
        
        	**config**\: False
        
        .. attribute:: netconfver
        
        	Netconf Version
        	**type**\: str
        
        	**length:** 0..10
        
        	**config**\: False
        
        .. attribute:: hostkeyalgo
        
        	Hostkey algorithms
        	**type**\: str
        
        	**length:** 0..200
        
        	**config**\: False
        
        .. attribute:: kexalgo
        
        	Key exchange algorithms
        	**type**\: str
        
        	**length:** 0..200
        
        	**config**\: False
        
        .. attribute:: cipheralgo
        
        	Encryption algorithms
        	**type**\: str
        
        	**length:** 0..200
        
        	**config**\: False
        
        .. attribute:: macalgo
        
        	Mac algorithms
        	**type**\: str
        
        	**length:** 0..200
        
        	**config**\: False
        
        .. attribute:: backupserver
        
        	Backup SSH server
        	**type**\: str
        
        	**length:** 0..100
        
        	**config**\: False
        
        .. attribute:: dscp
        
        	Dscp
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: ratelimit
        
        	ratelimit
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: sessionlimit
        
        	session limit
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: rekeytime
        
        	Rekey Time
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: rekeyvolume
        
        	Rekey Volume
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: windowscalefactor
        
        	Window scale factor
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: passwordauthen
        
        	Password Authentication support
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: keyboardinteractiveauthen
        
        	Pubkey Authentication support
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: pubkeyauthen
        
        	Pubkey Authentication support
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: certificateauthen
        
        	Certificate based Authentication support
        	**type**\: bool
        
        	**config**\: False
        
        

        """

        _prefix = 'crypto-ssh-oper'
        _revision = '2017-08-25'

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
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                ('netconfport', (YLeaf(YType.uint32, 'netconfport'), ['int'])),
                ('netconfvrf', (YLeaf(YType.str, 'netconfvrf'), ['str'])),
                ('netconfver', (YLeaf(YType.str, 'netconfver'), ['str'])),
                ('hostkeyalgo', (YLeaf(YType.str, 'hostkeyalgo'), ['str'])),
                ('kexalgo', (YLeaf(YType.str, 'kexalgo'), ['str'])),
                ('cipheralgo', (YLeaf(YType.str, 'cipheralgo'), ['str'])),
                ('macalgo', (YLeaf(YType.str, 'macalgo'), ['str'])),
                ('backupserver', (YLeaf(YType.str, 'backupserver'), ['str'])),
                ('dscp', (YLeaf(YType.uint32, 'dscp'), ['int'])),
                ('ratelimit', (YLeaf(YType.uint32, 'ratelimit'), ['int'])),
                ('sessionlimit', (YLeaf(YType.uint32, 'sessionlimit'), ['int'])),
                ('rekeytime', (YLeaf(YType.uint32, 'rekeytime'), ['int'])),
                ('rekeyvolume', (YLeaf(YType.uint32, 'rekeyvolume'), ['int'])),
                ('windowscalefactor', (YLeaf(YType.uint32, 'windowscalefactor'), ['int'])),
                ('passwordauthen', (YLeaf(YType.boolean, 'passwordauthen'), ['bool'])),
                ('keyboardinteractiveauthen', (YLeaf(YType.boolean, 'keyboardinteractiveauthen'), ['bool'])),
                ('pubkeyauthen', (YLeaf(YType.boolean, 'pubkeyauthen'), ['bool'])),
                ('certificateauthen', (YLeaf(YType.boolean, 'certificateauthen'), ['bool'])),
            ])
            self.version = None
            self.port = None
            self.vrf = None
            self.netconfport = None
            self.netconfvrf = None
            self.netconfver = None
            self.hostkeyalgo = None
            self.kexalgo = None
            self.cipheralgo = None
            self.macalgo = None
            self.backupserver = None
            self.dscp = None
            self.ratelimit = None
            self.sessionlimit = None
            self.rekeytime = None
            self.rekeyvolume = None
            self.windowscalefactor = None
            self.passwordauthen = None
            self.keyboardinteractiveauthen = None
            self.pubkeyauthen = None
            self.certificateauthen = None
            self._segment_path = lambda: "server"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-ssh-oper:ssh/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ssh.Server, ['version', 'port', 'vrf', 'netconfport', 'netconfvrf', 'netconfver', 'hostkeyalgo', 'kexalgo', 'cipheralgo', 'macalgo', 'backupserver', 'dscp', 'ratelimit', 'sessionlimit', 'rekeytime', 'rekeyvolume', 'windowscalefactor', 'passwordauthen', 'keyboardinteractiveauthen', 'pubkeyauthen', 'certificateauthen'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
            return meta._meta_table['Ssh.Server']['meta_info']

    def clone_ptr(self):
        self._top_entity = Ssh()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Ssh']['meta_info']



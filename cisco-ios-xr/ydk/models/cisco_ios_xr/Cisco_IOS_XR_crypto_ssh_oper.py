""" Cisco_IOS_XR_crypto_ssh_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-ssh package operational data.

This module contains definitions
for the following management objects\:
  ssh1\: Crypto Secure Shell(SSH) data
  ssh\: ssh

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AuthenEnum(Enum):
    """
    AuthenEnum

    SSH session authentication types

    .. data:: password = 0

    	Password

    .. data:: rsa_public_key = 1

    	RSA public key encryption type

    .. data:: keyboard_interactive = 2

    	Keyboard interactive

    """

    password = 0

    rsa_public_key = 1

    keyboard_interactive = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['AuthenEnum']


class CipherEnum(Enum):
    """
    CipherEnum

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

    """

    aes128_cbc = 0

    aes192_cbc = 1

    aes256_cbc = 2

    triple_des_cbc = 3

    aes128_ctr = 4

    aes192_ctr = 5

    aes256_ctr = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['CipherEnum']


class ConnectionEnum(Enum):
    """
    ConnectionEnum

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

    """

    undefined = 0

    shell = 1

    exec_ = 2

    scp = 3

    sftp_subsystem = 4

    netconf_subsystem = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['ConnectionEnum']


class HostkeyEnum(Enum):
    """
    HostkeyEnum

    SSH session authentication types

    .. data:: ssh_dss = 0

    	Algorithm type DSS

    .. data:: ssh_rsa = 1

    	Algorithm type RSA

    """

    ssh_dss = 0

    ssh_rsa = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['HostkeyEnum']


class KexNameEnum(Enum):
    """
    KexNameEnum

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

    diffie_hellman_group1 = 0

    diffie_hellman_group14 = 1

    diffie_hellman_group15 = 2

    diffie_hellman_group16 = 3

    diffie_hellman_group17 = 4

    diffie_hellman_group18 = 5

    ecdh_nistp256 = 6

    ecdh_nistp384 = 7

    ecdh_nistp521 = 8

    password_authenticated = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['KexNameEnum']


class MacEnum(Enum):
    """
    MacEnum

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

    """

    hmac_md5 = 0

    hmac_sha1 = 1

    hmac_sha2_256 = 2

    hmac_sha2_512 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['MacEnum']


class StatesEnum(Enum):
    """
    StatesEnum

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

    open = 1

    version_ok = 2

    key_exchange_initialize = 3

    key_exchange_dh = 4

    new_keys = 5

    authenticate_information = 6

    authenticated = 7

    channel_open = 8

    pty_open = 9

    session_open = 10

    rekey = 11

    suspended = 12

    session_closed = 13


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['StatesEnum']


class VersionEnum(Enum):
    """
    VersionEnum

    SSH state versions

    .. data:: v2 = 0

    	Version V2

    .. data:: v1 = 1

    	Version V1

    """

    v2 = 0

    v1 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['VersionEnum']



class Ssh1(object):
    """
    Crypto Secure Shell(SSH) data
    
    .. attribute:: kex
    
    	key exchange method data
    	**type**\:   :py:class:`Kex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex>`
    
    

    """

    _prefix = 'crypto-ssh-oper'
    _revision = '2015-06-02'

    def __init__(self):
        self.kex = Ssh1.Kex()
        self.kex.parent = self


    class Kex(object):
        """
        key exchange method data
        
        .. attribute:: nodes
        
        	Node\-specific ssh session details
        	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes>`
        
        

        """

        _prefix = 'crypto-ssh-oper'
        _revision = '2015-06-02'

        def __init__(self):
            self.parent = None
            self.nodes = Ssh1.Kex.Nodes()
            self.nodes.parent = self


        class Nodes(object):
            """
            Node\-specific ssh session details
            
            .. attribute:: node
            
            	SSH session details for a particular node
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node>`
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2015-06-02'

            def __init__(self):
                self.parent = None
                self.node = YList()
                self.node.parent = self
                self.node.name = 'node'


            class Node(object):
                """
                SSH session details for a particular node
                
                .. attribute:: node_name  <key>
                
                	Node name
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: incoming_sessions
                
                	List of incoming sessions
                	**type**\:   :py:class:`IncomingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.IncomingSessions>`
                
                .. attribute:: outgoing_connections
                
                	List of outgoing connections
                	**type**\:   :py:class:`OutgoingConnections <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.OutgoingConnections>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.node_name = None
                    self.incoming_sessions = Ssh1.Kex.Nodes.Node.IncomingSessions()
                    self.incoming_sessions.parent = self
                    self.outgoing_connections = Ssh1.Kex.Nodes.Node.OutgoingConnections()
                    self.outgoing_connections.parent = self


                class IncomingSessions(object):
                    """
                    List of incoming sessions
                    
                    .. attribute:: session_detail_info
                    
                    	session detail info
                    	**type**\: list of    :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo>`
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        self.parent = None
                        self.session_detail_info = YList()
                        self.session_detail_info.parent = self
                        self.session_detail_info.name = 'session_detail_info'


                    class SessionDetailInfo(object):
                        """
                        session detail info
                        
                        .. attribute:: in_cipher
                        
                        	In cipher algorithm
                        	**type**\:   :py:class:`CipherEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.CipherEnum>`
                        
                        .. attribute:: in_mac
                        
                        	In MAC
                        	**type**\:   :py:class:`MacEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.MacEnum>`
                        
                        .. attribute:: key_exchange
                        
                        	Key exchange name
                        	**type**\:   :py:class:`KexNameEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexNameEnum>`
                        
                        .. attribute:: out_cipher
                        
                        	Out cipher algorithm
                        	**type**\:   :py:class:`CipherEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.CipherEnum>`
                        
                        .. attribute:: out_mac
                        
                        	Out MAC
                        	**type**\:   :py:class:`MacEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.MacEnum>`
                        
                        .. attribute:: public_key
                        
                        	Host key algorithm
                        	**type**\:   :py:class:`HostkeyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.HostkeyEnum>`
                        
                        .. attribute:: session_id
                        
                        	Session ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2015-06-02'

                        def __init__(self):
                            self.parent = None
                            self.in_cipher = None
                            self.in_mac = None
                            self.key_exchange = None
                            self.out_cipher = None
                            self.out_mac = None
                            self.public_key = None
                            self.session_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-ssh-oper:session-detail-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.in_cipher is not None:
                                return True

                            if self.in_mac is not None:
                                return True

                            if self.key_exchange is not None:
                                return True

                            if self.out_cipher is not None:
                                return True

                            if self.out_mac is not None:
                                return True

                            if self.public_key is not None:
                                return True

                            if self.session_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-ssh-oper:incoming-sessions'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.session_detail_info is not None:
                            for child_ref in self.session_detail_info:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh1.Kex.Nodes.Node.IncomingSessions']['meta_info']


                class OutgoingConnections(object):
                    """
                    List of outgoing connections
                    
                    .. attribute:: session_detail_info
                    
                    	session detail info
                    	**type**\: list of    :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo>`
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        self.parent = None
                        self.session_detail_info = YList()
                        self.session_detail_info.parent = self
                        self.session_detail_info.name = 'session_detail_info'


                    class SessionDetailInfo(object):
                        """
                        session detail info
                        
                        .. attribute:: in_cipher
                        
                        	In cipher algorithm
                        	**type**\:   :py:class:`CipherEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.CipherEnum>`
                        
                        .. attribute:: in_mac
                        
                        	In MAC
                        	**type**\:   :py:class:`MacEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.MacEnum>`
                        
                        .. attribute:: key_exchange
                        
                        	Key exchange name
                        	**type**\:   :py:class:`KexNameEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexNameEnum>`
                        
                        .. attribute:: out_cipher
                        
                        	Out cipher algorithm
                        	**type**\:   :py:class:`CipherEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.CipherEnum>`
                        
                        .. attribute:: out_mac
                        
                        	Out MAC
                        	**type**\:   :py:class:`MacEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.MacEnum>`
                        
                        .. attribute:: public_key
                        
                        	Host key algorithm
                        	**type**\:   :py:class:`HostkeyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.HostkeyEnum>`
                        
                        .. attribute:: session_id
                        
                        	Session ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2015-06-02'

                        def __init__(self):
                            self.parent = None
                            self.in_cipher = None
                            self.in_mac = None
                            self.key_exchange = None
                            self.out_cipher = None
                            self.out_mac = None
                            self.public_key = None
                            self.session_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-ssh-oper:session-detail-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.in_cipher is not None:
                                return True

                            if self.in_mac is not None:
                                return True

                            if self.key_exchange is not None:
                                return True

                            if self.out_cipher is not None:
                                return True

                            if self.out_mac is not None:
                                return True

                            if self.public_key is not None:
                                return True

                            if self.session_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                            return meta._meta_table['Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-ssh-oper:outgoing-connections'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.session_detail_info is not None:
                            for child_ref in self.session_detail_info:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh1.Kex.Nodes.Node.OutgoingConnections']['meta_info']

                @property
                def _common_path(self):
                    if self.node_name is None:
                        raise YPYModelError('Key property node_name is None')

                    return '/Cisco-IOS-XR-crypto-ssh-oper:ssh1/Cisco-IOS-XR-crypto-ssh-oper:kex/Cisco-IOS-XR-crypto-ssh-oper:nodes/Cisco-IOS-XR-crypto-ssh-oper:node[Cisco-IOS-XR-crypto-ssh-oper:node-name = ' + str(self.node_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.node_name is not None:
                        return True

                    if self.incoming_sessions is not None and self.incoming_sessions._has_data():
                        return True

                    if self.outgoing_connections is not None and self.outgoing_connections._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh1.Kex.Nodes.Node']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-crypto-ssh-oper:ssh1/Cisco-IOS-XR-crypto-ssh-oper:kex/Cisco-IOS-XR-crypto-ssh-oper:nodes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node is not None:
                    for child_ref in self.node:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                return meta._meta_table['Ssh1.Kex.Nodes']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-ssh-oper:ssh1/Cisco-IOS-XR-crypto-ssh-oper:kex'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.nodes is not None and self.nodes._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
            return meta._meta_table['Ssh1.Kex']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-ssh-oper:ssh1'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.kex is not None and self.kex._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Ssh1']['meta_info']


class Ssh(object):
    """
    ssh
    
    .. attribute:: session
    
    	Crypto SSH session
    	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session>`
    
    

    """

    _prefix = 'crypto-ssh-oper'
    _revision = '2015-06-02'

    def __init__(self):
        self.session = Ssh.Session()
        self.session.parent = self


    class Session(object):
        """
        Crypto SSH session
        
        .. attribute:: brief
        
        	SSH session brief information
        	**type**\:   :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief>`
        
        .. attribute:: detail
        
        	SSH session detail information
        	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail>`
        
        .. attribute:: rekey
        
        	SSH session rekey information
        	**type**\:   :py:class:`Rekey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey>`
        
        

        """

        _prefix = 'crypto-ssh-oper'
        _revision = '2015-06-02'

        def __init__(self):
            self.parent = None
            self.brief = Ssh.Session.Brief()
            self.brief.parent = self
            self.detail = Ssh.Session.Detail()
            self.detail.parent = self
            self.rekey = Ssh.Session.Rekey()
            self.rekey.parent = self


        class Rekey(object):
            """
            SSH session rekey information
            
            .. attribute:: incoming_sessions
            
            	List of incoming sessions
            	**type**\:   :py:class:`IncomingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.IncomingSessions>`
            
            .. attribute:: outgoing_connections
            
            	List of outgoing connections
            	**type**\:   :py:class:`OutgoingConnections <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.OutgoingConnections>`
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2015-06-02'

            def __init__(self):
                self.parent = None
                self.incoming_sessions = Ssh.Session.Rekey.IncomingSessions()
                self.incoming_sessions.parent = self
                self.outgoing_connections = Ssh.Session.Rekey.OutgoingConnections()
                self.outgoing_connections.parent = self


            class IncomingSessions(object):
                """
                List of incoming sessions
                
                .. attribute:: session_rekey_info
                
                	session rekey info
                	**type**\: list of    :py:class:`SessionRekeyInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.session_rekey_info = YList()
                    self.session_rekey_info.parent = self
                    self.session_rekey_info.name = 'session_rekey_info'


                class SessionRekeyInfo(object):
                    """
                    session rekey info
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_rekey_count
                    
                    	Session Rekey Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: time_to_rekey
                    
                    	Time To Rekey
                    	**type**\:  str
                    
                    .. attribute:: volume_to_rekey
                    
                    	Volume To Rekey
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        self.parent = None
                        self.session_id = None
                        self.session_rekey_count = None
                        self.time_to_rekey = None
                        self.volume_to_rekey = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:rekey/Cisco-IOS-XR-crypto-ssh-oper:incoming-sessions/Cisco-IOS-XR-crypto-ssh-oper:session-rekey-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.session_id is not None:
                            return True

                        if self.session_rekey_count is not None:
                            return True

                        if self.time_to_rekey is not None:
                            return True

                        if self.volume_to_rekey is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:rekey/Cisco-IOS-XR-crypto-ssh-oper:incoming-sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.session_rekey_info is not None:
                        for child_ref in self.session_rekey_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Rekey.IncomingSessions']['meta_info']


            class OutgoingConnections(object):
                """
                List of outgoing connections
                
                .. attribute:: session_rekey_info
                
                	session rekey info
                	**type**\: list of    :py:class:`SessionRekeyInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.session_rekey_info = YList()
                    self.session_rekey_info.parent = self
                    self.session_rekey_info.name = 'session_rekey_info'


                class SessionRekeyInfo(object):
                    """
                    session rekey info
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_rekey_count
                    
                    	Session Rekey Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: time_to_rekey
                    
                    	Time To Rekey
                    	**type**\:  str
                    
                    .. attribute:: volume_to_rekey
                    
                    	Volume To Rekey
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        self.parent = None
                        self.session_id = None
                        self.session_rekey_count = None
                        self.time_to_rekey = None
                        self.volume_to_rekey = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:rekey/Cisco-IOS-XR-crypto-ssh-oper:outgoing-connections/Cisco-IOS-XR-crypto-ssh-oper:session-rekey-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.session_id is not None:
                            return True

                        if self.session_rekey_count is not None:
                            return True

                        if self.time_to_rekey is not None:
                            return True

                        if self.volume_to_rekey is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:rekey/Cisco-IOS-XR-crypto-ssh-oper:outgoing-connections'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.session_rekey_info is not None:
                        for child_ref in self.session_rekey_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Rekey.OutgoingConnections']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:rekey'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.incoming_sessions is not None and self.incoming_sessions._has_data():
                    return True

                if self.outgoing_connections is not None and self.outgoing_connections._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                return meta._meta_table['Ssh.Session.Rekey']['meta_info']


        class Brief(object):
            """
            SSH session brief information
            
            .. attribute:: incoming_sessions
            
            	List of incoming sessions
            	**type**\:   :py:class:`IncomingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.IncomingSessions>`
            
            .. attribute:: outgoing_sessions
            
            	List of outgoing sessions
            	**type**\:   :py:class:`OutgoingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.OutgoingSessions>`
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2015-06-02'

            def __init__(self):
                self.parent = None
                self.incoming_sessions = Ssh.Session.Brief.IncomingSessions()
                self.incoming_sessions.parent = self
                self.outgoing_sessions = Ssh.Session.Brief.OutgoingSessions()
                self.outgoing_sessions.parent = self


            class IncomingSessions(object):
                """
                List of incoming sessions
                
                .. attribute:: session_brief_info
                
                	session brief info
                	**type**\: list of    :py:class:`SessionBriefInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.IncomingSessions.SessionBriefInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.session_brief_info = YList()
                    self.session_brief_info.parent = self
                    self.session_brief_info.name = 'session_brief_info'


                class SessionBriefInfo(object):
                    """
                    session brief info
                    
                    .. attribute:: authentication_type
                    
                    	Authentication method
                    	**type**\:   :py:class:`AuthenEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.AuthenEnum>`
                    
                    .. attribute:: channel_id
                    
                    	Channel ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connection_type
                    
                    	Channel Connection Type
                    	**type**\:   :py:class:`ConnectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.ConnectionEnum>`
                    
                    .. attribute:: host_address
                    
                    	Host address
                    	**type**\:  str
                    
                    .. attribute:: node_name
                    
                    	Node name
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_state
                    
                    	SSH session state
                    	**type**\:   :py:class:`StatesEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.StatesEnum>`
                    
                    .. attribute:: user_id
                    
                    	User ID
                    	**type**\:  str
                    
                    .. attribute:: version
                    
                    	SSH state version
                    	**type**\:   :py:class:`VersionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.VersionEnum>`
                    
                    .. attribute:: vty_assigned
                    
                    	Boolean indicating whether line VTY line number is valid
                    	**type**\:  bool
                    
                    .. attribute:: vty_line_number
                    
                    	VTY line number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        self.parent = None
                        self.authentication_type = None
                        self.channel_id = None
                        self.connection_type = None
                        self.host_address = None
                        self.node_name = None
                        self.session_id = None
                        self.session_state = None
                        self.user_id = None
                        self.version = None
                        self.vty_assigned = None
                        self.vty_line_number = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:brief/Cisco-IOS-XR-crypto-ssh-oper:incoming-sessions/Cisco-IOS-XR-crypto-ssh-oper:session-brief-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.authentication_type is not None:
                            return True

                        if self.channel_id is not None:
                            return True

                        if self.connection_type is not None:
                            return True

                        if self.host_address is not None:
                            return True

                        if self.node_name is not None:
                            return True

                        if self.session_id is not None:
                            return True

                        if self.session_state is not None:
                            return True

                        if self.user_id is not None:
                            return True

                        if self.version is not None:
                            return True

                        if self.vty_assigned is not None:
                            return True

                        if self.vty_line_number is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Brief.IncomingSessions.SessionBriefInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:brief/Cisco-IOS-XR-crypto-ssh-oper:incoming-sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.session_brief_info is not None:
                        for child_ref in self.session_brief_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Brief.IncomingSessions']['meta_info']


            class OutgoingSessions(object):
                """
                List of outgoing sessions
                
                .. attribute:: session_brief_info
                
                	session brief info
                	**type**\: list of    :py:class:`SessionBriefInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.session_brief_info = YList()
                    self.session_brief_info.parent = self
                    self.session_brief_info.name = 'session_brief_info'


                class SessionBriefInfo(object):
                    """
                    session brief info
                    
                    .. attribute:: authentication_type
                    
                    	Authentication method
                    	**type**\:   :py:class:`AuthenEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.AuthenEnum>`
                    
                    .. attribute:: channel_id
                    
                    	Channel ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connection_type
                    
                    	Channel Connection Type
                    	**type**\:   :py:class:`ConnectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.ConnectionEnum>`
                    
                    .. attribute:: host_address
                    
                    	Host address
                    	**type**\:  str
                    
                    .. attribute:: node_name
                    
                    	Node name
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_state
                    
                    	SSH session state
                    	**type**\:   :py:class:`StatesEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.StatesEnum>`
                    
                    .. attribute:: user_id
                    
                    	User ID
                    	**type**\:  str
                    
                    .. attribute:: version
                    
                    	SSH state version
                    	**type**\:   :py:class:`VersionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.VersionEnum>`
                    
                    .. attribute:: vty_assigned
                    
                    	Boolean indicating whether line VTY line number is valid
                    	**type**\:  bool
                    
                    .. attribute:: vty_line_number
                    
                    	VTY line number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        self.parent = None
                        self.authentication_type = None
                        self.channel_id = None
                        self.connection_type = None
                        self.host_address = None
                        self.node_name = None
                        self.session_id = None
                        self.session_state = None
                        self.user_id = None
                        self.version = None
                        self.vty_assigned = None
                        self.vty_line_number = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:brief/Cisco-IOS-XR-crypto-ssh-oper:outgoing-sessions/Cisco-IOS-XR-crypto-ssh-oper:session-brief-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.authentication_type is not None:
                            return True

                        if self.channel_id is not None:
                            return True

                        if self.connection_type is not None:
                            return True

                        if self.host_address is not None:
                            return True

                        if self.node_name is not None:
                            return True

                        if self.session_id is not None:
                            return True

                        if self.session_state is not None:
                            return True

                        if self.user_id is not None:
                            return True

                        if self.version is not None:
                            return True

                        if self.vty_assigned is not None:
                            return True

                        if self.vty_line_number is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:brief/Cisco-IOS-XR-crypto-ssh-oper:outgoing-sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.session_brief_info is not None:
                        for child_ref in self.session_brief_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Brief.OutgoingSessions']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:brief'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.incoming_sessions is not None and self.incoming_sessions._has_data():
                    return True

                if self.outgoing_sessions is not None and self.outgoing_sessions._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                return meta._meta_table['Ssh.Session.Brief']['meta_info']


        class Detail(object):
            """
            SSH session detail information
            
            .. attribute:: incoming_sessions
            
            	List of incoming sessions
            	**type**\:   :py:class:`IncomingSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.IncomingSessions>`
            
            .. attribute:: outgoing_connections
            
            	List of outgoing connections
            	**type**\:   :py:class:`OutgoingConnections <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.OutgoingConnections>`
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2015-06-02'

            def __init__(self):
                self.parent = None
                self.incoming_sessions = Ssh.Session.Detail.IncomingSessions()
                self.incoming_sessions.parent = self
                self.outgoing_connections = Ssh.Session.Detail.OutgoingConnections()
                self.outgoing_connections.parent = self


            class IncomingSessions(object):
                """
                List of incoming sessions
                
                .. attribute:: session_detail_info
                
                	session detail info
                	**type**\: list of    :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.IncomingSessions.SessionDetailInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.session_detail_info = YList()
                    self.session_detail_info.parent = self
                    self.session_detail_info.name = 'session_detail_info'


                class SessionDetailInfo(object):
                    """
                    session detail info
                    
                    .. attribute:: in_cipher
                    
                    	In cipher algorithm
                    	**type**\:   :py:class:`CipherEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.CipherEnum>`
                    
                    .. attribute:: in_mac
                    
                    	In MAC
                    	**type**\:   :py:class:`MacEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.MacEnum>`
                    
                    .. attribute:: key_exchange
                    
                    	Key exchange name
                    	**type**\:   :py:class:`KexNameEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexNameEnum>`
                    
                    .. attribute:: out_cipher
                    
                    	Out cipher algorithm
                    	**type**\:   :py:class:`CipherEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.CipherEnum>`
                    
                    .. attribute:: out_mac
                    
                    	Out MAC
                    	**type**\:   :py:class:`MacEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.MacEnum>`
                    
                    .. attribute:: public_key
                    
                    	Host key algorithm
                    	**type**\:   :py:class:`HostkeyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.HostkeyEnum>`
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        self.parent = None
                        self.in_cipher = None
                        self.in_mac = None
                        self.key_exchange = None
                        self.out_cipher = None
                        self.out_mac = None
                        self.public_key = None
                        self.session_id = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:detail/Cisco-IOS-XR-crypto-ssh-oper:incoming-sessions/Cisco-IOS-XR-crypto-ssh-oper:session-detail-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.in_cipher is not None:
                            return True

                        if self.in_mac is not None:
                            return True

                        if self.key_exchange is not None:
                            return True

                        if self.out_cipher is not None:
                            return True

                        if self.out_mac is not None:
                            return True

                        if self.public_key is not None:
                            return True

                        if self.session_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Detail.IncomingSessions.SessionDetailInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:detail/Cisco-IOS-XR-crypto-ssh-oper:incoming-sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.session_detail_info is not None:
                        for child_ref in self.session_detail_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Detail.IncomingSessions']['meta_info']


            class OutgoingConnections(object):
                """
                List of outgoing connections
                
                .. attribute:: session_detail_info
                
                	session detail info
                	**type**\: list of    :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.session_detail_info = YList()
                    self.session_detail_info.parent = self
                    self.session_detail_info.name = 'session_detail_info'


                class SessionDetailInfo(object):
                    """
                    session detail info
                    
                    .. attribute:: in_cipher
                    
                    	In cipher algorithm
                    	**type**\:   :py:class:`CipherEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.CipherEnum>`
                    
                    .. attribute:: in_mac
                    
                    	In MAC
                    	**type**\:   :py:class:`MacEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.MacEnum>`
                    
                    .. attribute:: key_exchange
                    
                    	Key exchange name
                    	**type**\:   :py:class:`KexNameEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexNameEnum>`
                    
                    .. attribute:: out_cipher
                    
                    	Out cipher algorithm
                    	**type**\:   :py:class:`CipherEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.CipherEnum>`
                    
                    .. attribute:: out_mac
                    
                    	Out MAC
                    	**type**\:   :py:class:`MacEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.MacEnum>`
                    
                    .. attribute:: public_key
                    
                    	Host key algorithm
                    	**type**\:   :py:class:`HostkeyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.HostkeyEnum>`
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        self.parent = None
                        self.in_cipher = None
                        self.in_mac = None
                        self.key_exchange = None
                        self.out_cipher = None
                        self.out_mac = None
                        self.public_key = None
                        self.session_id = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:detail/Cisco-IOS-XR-crypto-ssh-oper:outgoing-connections/Cisco-IOS-XR-crypto-ssh-oper:session-detail-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.in_cipher is not None:
                            return True

                        if self.in_mac is not None:
                            return True

                        if self.key_exchange is not None:
                            return True

                        if self.out_cipher is not None:
                            return True

                        if self.out_mac is not None:
                            return True

                        if self.public_key is not None:
                            return True

                        if self.session_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:detail/Cisco-IOS-XR-crypto-ssh-oper:outgoing-connections'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.session_detail_info is not None:
                        for child_ref in self.session_detail_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Detail.OutgoingConnections']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:detail'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.incoming_sessions is not None and self.incoming_sessions._has_data():
                    return True

                if self.outgoing_connections is not None and self.outgoing_connections._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                return meta._meta_table['Ssh.Session.Detail']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.brief is not None and self.brief._has_data():
                return True

            if self.detail is not None and self.detail._has_data():
                return True

            if self.rekey is not None and self.rekey._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
            return meta._meta_table['Ssh.Session']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-ssh-oper:ssh'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.session is not None and self.session._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Ssh']['meta_info']



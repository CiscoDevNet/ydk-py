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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Authen(Enum):
    """
    Authen

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
    Cipher

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

    aes128_cbc = Enum.YLeaf(0, "aes128-cbc")

    aes192_cbc = Enum.YLeaf(1, "aes192-cbc")

    aes256_cbc = Enum.YLeaf(2, "aes256-cbc")

    triple_des_cbc = Enum.YLeaf(3, "triple-des-cbc")

    aes128_ctr = Enum.YLeaf(4, "aes128-ctr")

    aes192_ctr = Enum.YLeaf(5, "aes192-ctr")

    aes256_ctr = Enum.YLeaf(6, "aes256-ctr")


class Connection(Enum):
    """
    Connection

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
    Hostkey

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
    KexName

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
    Mac

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

    hmac_md5 = Enum.YLeaf(0, "hmac-md5")

    hmac_sha1 = Enum.YLeaf(1, "hmac-sha1")

    hmac_sha2_256 = Enum.YLeaf(2, "hmac-sha2-256")

    hmac_sha2_512 = Enum.YLeaf(3, "hmac-sha2-512")


class States(Enum):
    """
    States

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
    Version

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
    	**type**\:   :py:class:`Kex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex>`
    
    

    """

    _prefix = 'crypto-ssh-oper'
    _revision = '2015-06-02'

    def __init__(self):
        super(Ssh1, self).__init__()
        self._top_entity = None

        self.yang_name = "ssh1"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-ssh-oper"

        self.kex = Ssh1.Kex()
        self.kex.parent = self
        self._children_name_map["kex"] = "kex"
        self._children_yang_names.add("kex")


    class Kex(Entity):
        """
        key exchange method data
        
        .. attribute:: nodes
        
        	Node\-specific ssh session details
        	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes>`
        
        

        """

        _prefix = 'crypto-ssh-oper'
        _revision = '2015-06-02'

        def __init__(self):
            super(Ssh1.Kex, self).__init__()

            self.yang_name = "kex"
            self.yang_parent_name = "ssh1"

            self.nodes = Ssh1.Kex.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._children_yang_names.add("nodes")


        class Nodes(Entity):
            """
            Node\-specific ssh session details
            
            .. attribute:: node
            
            	SSH session details for a particular node
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node>`
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2015-06-02'

            def __init__(self):
                super(Ssh1.Kex.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "kex"

                self.node = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ssh1.Kex.Nodes, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ssh1.Kex.Nodes, self).__setattr__(name, value)


            class Node(Entity):
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
                    super(Ssh1.Kex.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"

                    self.node_name = YLeaf(YType.str, "node-name")

                    self.incoming_sessions = Ssh1.Kex.Nodes.Node.IncomingSessions()
                    self.incoming_sessions.parent = self
                    self._children_name_map["incoming_sessions"] = "incoming-sessions"
                    self._children_yang_names.add("incoming-sessions")

                    self.outgoing_connections = Ssh1.Kex.Nodes.Node.OutgoingConnections()
                    self.outgoing_connections.parent = self
                    self._children_name_map["outgoing_connections"] = "outgoing-connections"
                    self._children_yang_names.add("outgoing-connections")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("node_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ssh1.Kex.Nodes.Node, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ssh1.Kex.Nodes.Node, self).__setattr__(name, value)


                class IncomingSessions(Entity):
                    """
                    List of incoming sessions
                    
                    .. attribute:: session_detail_info
                    
                    	session detail info
                    	**type**\: list of    :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo>`
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        super(Ssh1.Kex.Nodes.Node.IncomingSessions, self).__init__()

                        self.yang_name = "incoming-sessions"
                        self.yang_parent_name = "node"

                        self.session_detail_info = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ssh1.Kex.Nodes.Node.IncomingSessions, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ssh1.Kex.Nodes.Node.IncomingSessions, self).__setattr__(name, value)


                    class SessionDetailInfo(Entity):
                        """
                        session detail info
                        
                        .. attribute:: in_cipher
                        
                        	In cipher algorithm
                        	**type**\:   :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                        
                        .. attribute:: in_mac
                        
                        	In MAC
                        	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                        
                        .. attribute:: key_exchange
                        
                        	Key exchange name
                        	**type**\:   :py:class:`KexName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexName>`
                        
                        .. attribute:: out_cipher
                        
                        	Out cipher algorithm
                        	**type**\:   :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                        
                        .. attribute:: out_mac
                        
                        	Out MAC
                        	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                        
                        .. attribute:: public_key
                        
                        	Host key algorithm
                        	**type**\:   :py:class:`Hostkey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Hostkey>`
                        
                        .. attribute:: session_id
                        
                        	Session ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2015-06-02'

                        def __init__(self):
                            super(Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo, self).__init__()

                            self.yang_name = "session-detail-info"
                            self.yang_parent_name = "incoming-sessions"

                            self.in_cipher = YLeaf(YType.enumeration, "in-cipher")

                            self.in_mac = YLeaf(YType.enumeration, "in-mac")

                            self.key_exchange = YLeaf(YType.enumeration, "key-exchange")

                            self.out_cipher = YLeaf(YType.enumeration, "out-cipher")

                            self.out_mac = YLeaf(YType.enumeration, "out-mac")

                            self.public_key = YLeaf(YType.enumeration, "public-key")

                            self.session_id = YLeaf(YType.uint32, "session-id")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("in_cipher",
                                            "in_mac",
                                            "key_exchange",
                                            "out_cipher",
                                            "out_mac",
                                            "public_key",
                                            "session_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.in_cipher.is_set or
                                self.in_mac.is_set or
                                self.key_exchange.is_set or
                                self.out_cipher.is_set or
                                self.out_mac.is_set or
                                self.public_key.is_set or
                                self.session_id.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.in_cipher.yfilter != YFilter.not_set or
                                self.in_mac.yfilter != YFilter.not_set or
                                self.key_exchange.yfilter != YFilter.not_set or
                                self.out_cipher.yfilter != YFilter.not_set or
                                self.out_mac.yfilter != YFilter.not_set or
                                self.public_key.yfilter != YFilter.not_set or
                                self.session_id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "session-detail-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.in_cipher.is_set or self.in_cipher.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_cipher.get_name_leafdata())
                            if (self.in_mac.is_set or self.in_mac.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_mac.get_name_leafdata())
                            if (self.key_exchange.is_set or self.key_exchange.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.key_exchange.get_name_leafdata())
                            if (self.out_cipher.is_set or self.out_cipher.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.out_cipher.get_name_leafdata())
                            if (self.out_mac.is_set or self.out_mac.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.out_mac.get_name_leafdata())
                            if (self.public_key.is_set or self.public_key.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.public_key.get_name_leafdata())
                            if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "in-cipher" or name == "in-mac" or name == "key-exchange" or name == "out-cipher" or name == "out-mac" or name == "public-key" or name == "session-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "in-cipher"):
                                self.in_cipher = value
                                self.in_cipher.value_namespace = name_space
                                self.in_cipher.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-mac"):
                                self.in_mac = value
                                self.in_mac.value_namespace = name_space
                                self.in_mac.value_namespace_prefix = name_space_prefix
                            if(value_path == "key-exchange"):
                                self.key_exchange = value
                                self.key_exchange.value_namespace = name_space
                                self.key_exchange.value_namespace_prefix = name_space_prefix
                            if(value_path == "out-cipher"):
                                self.out_cipher = value
                                self.out_cipher.value_namespace = name_space
                                self.out_cipher.value_namespace_prefix = name_space_prefix
                            if(value_path == "out-mac"):
                                self.out_mac = value
                                self.out_mac.value_namespace = name_space
                                self.out_mac.value_namespace_prefix = name_space_prefix
                            if(value_path == "public-key"):
                                self.public_key = value
                                self.public_key.value_namespace = name_space
                                self.public_key.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-id"):
                                self.session_id = value
                                self.session_id.value_namespace = name_space
                                self.session_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.session_detail_info:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.session_detail_info:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "incoming-sessions" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "session-detail-info"):
                            for c in self.session_detail_info:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.session_detail_info.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "session-detail-info"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class OutgoingConnections(Entity):
                    """
                    List of outgoing connections
                    
                    .. attribute:: session_detail_info
                    
                    	session detail info
                    	**type**\: list of    :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo>`
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        super(Ssh1.Kex.Nodes.Node.OutgoingConnections, self).__init__()

                        self.yang_name = "outgoing-connections"
                        self.yang_parent_name = "node"

                        self.session_detail_info = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ssh1.Kex.Nodes.Node.OutgoingConnections, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ssh1.Kex.Nodes.Node.OutgoingConnections, self).__setattr__(name, value)


                    class SessionDetailInfo(Entity):
                        """
                        session detail info
                        
                        .. attribute:: in_cipher
                        
                        	In cipher algorithm
                        	**type**\:   :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                        
                        .. attribute:: in_mac
                        
                        	In MAC
                        	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                        
                        .. attribute:: key_exchange
                        
                        	Key exchange name
                        	**type**\:   :py:class:`KexName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexName>`
                        
                        .. attribute:: out_cipher
                        
                        	Out cipher algorithm
                        	**type**\:   :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                        
                        .. attribute:: out_mac
                        
                        	Out MAC
                        	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                        
                        .. attribute:: public_key
                        
                        	Host key algorithm
                        	**type**\:   :py:class:`Hostkey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Hostkey>`
                        
                        .. attribute:: session_id
                        
                        	Session ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'crypto-ssh-oper'
                        _revision = '2015-06-02'

                        def __init__(self):
                            super(Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo, self).__init__()

                            self.yang_name = "session-detail-info"
                            self.yang_parent_name = "outgoing-connections"

                            self.in_cipher = YLeaf(YType.enumeration, "in-cipher")

                            self.in_mac = YLeaf(YType.enumeration, "in-mac")

                            self.key_exchange = YLeaf(YType.enumeration, "key-exchange")

                            self.out_cipher = YLeaf(YType.enumeration, "out-cipher")

                            self.out_mac = YLeaf(YType.enumeration, "out-mac")

                            self.public_key = YLeaf(YType.enumeration, "public-key")

                            self.session_id = YLeaf(YType.uint32, "session-id")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("in_cipher",
                                            "in_mac",
                                            "key_exchange",
                                            "out_cipher",
                                            "out_mac",
                                            "public_key",
                                            "session_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.in_cipher.is_set or
                                self.in_mac.is_set or
                                self.key_exchange.is_set or
                                self.out_cipher.is_set or
                                self.out_mac.is_set or
                                self.public_key.is_set or
                                self.session_id.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.in_cipher.yfilter != YFilter.not_set or
                                self.in_mac.yfilter != YFilter.not_set or
                                self.key_exchange.yfilter != YFilter.not_set or
                                self.out_cipher.yfilter != YFilter.not_set or
                                self.out_mac.yfilter != YFilter.not_set or
                                self.public_key.yfilter != YFilter.not_set or
                                self.session_id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "session-detail-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.in_cipher.is_set or self.in_cipher.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_cipher.get_name_leafdata())
                            if (self.in_mac.is_set or self.in_mac.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_mac.get_name_leafdata())
                            if (self.key_exchange.is_set or self.key_exchange.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.key_exchange.get_name_leafdata())
                            if (self.out_cipher.is_set or self.out_cipher.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.out_cipher.get_name_leafdata())
                            if (self.out_mac.is_set or self.out_mac.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.out_mac.get_name_leafdata())
                            if (self.public_key.is_set or self.public_key.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.public_key.get_name_leafdata())
                            if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "in-cipher" or name == "in-mac" or name == "key-exchange" or name == "out-cipher" or name == "out-mac" or name == "public-key" or name == "session-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "in-cipher"):
                                self.in_cipher = value
                                self.in_cipher.value_namespace = name_space
                                self.in_cipher.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-mac"):
                                self.in_mac = value
                                self.in_mac.value_namespace = name_space
                                self.in_mac.value_namespace_prefix = name_space_prefix
                            if(value_path == "key-exchange"):
                                self.key_exchange = value
                                self.key_exchange.value_namespace = name_space
                                self.key_exchange.value_namespace_prefix = name_space_prefix
                            if(value_path == "out-cipher"):
                                self.out_cipher = value
                                self.out_cipher.value_namespace = name_space
                                self.out_cipher.value_namespace_prefix = name_space_prefix
                            if(value_path == "out-mac"):
                                self.out_mac = value
                                self.out_mac.value_namespace = name_space
                                self.out_mac.value_namespace_prefix = name_space_prefix
                            if(value_path == "public-key"):
                                self.public_key = value
                                self.public_key.value_namespace = name_space
                                self.public_key.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-id"):
                                self.session_id = value
                                self.session_id.value_namespace = name_space
                                self.session_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.session_detail_info:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.session_detail_info:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "outgoing-connections" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "session-detail-info"):
                            for c in self.session_detail_info:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.session_detail_info.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "session-detail-info"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.node_name.is_set or
                        (self.incoming_sessions is not None and self.incoming_sessions.has_data()) or
                        (self.outgoing_connections is not None and self.outgoing_connections.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.node_name.yfilter != YFilter.not_set or
                        (self.incoming_sessions is not None and self.incoming_sessions.has_operation()) or
                        (self.outgoing_connections is not None and self.outgoing_connections.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh1/kex/nodes/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.node_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "incoming-sessions"):
                        if (self.incoming_sessions is None):
                            self.incoming_sessions = Ssh1.Kex.Nodes.Node.IncomingSessions()
                            self.incoming_sessions.parent = self
                            self._children_name_map["incoming_sessions"] = "incoming-sessions"
                        return self.incoming_sessions

                    if (child_yang_name == "outgoing-connections"):
                        if (self.outgoing_connections is None):
                            self.outgoing_connections = Ssh1.Kex.Nodes.Node.OutgoingConnections()
                            self.outgoing_connections.parent = self
                            self._children_name_map["outgoing_connections"] = "outgoing-connections"
                        return self.outgoing_connections

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "incoming-sessions" or name == "outgoing-connections" or name == "node-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "node-name"):
                        self.node_name = value
                        self.node_name.value_namespace = name_space
                        self.node_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.node:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.node:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nodes" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh1/kex/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "node"):
                    for c in self.node:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Ssh1.Kex.Nodes.Node()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.node.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "node"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.nodes is not None and self.nodes.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.nodes is not None and self.nodes.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "kex" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh1/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nodes"):
                if (self.nodes is None):
                    self.nodes = Ssh1.Kex.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"
                return self.nodes

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nodes"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.kex is not None and self.kex.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.kex is not None and self.kex.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh1" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "kex"):
            if (self.kex is None):
                self.kex = Ssh1.Kex()
                self.kex.parent = self
                self._children_name_map["kex"] = "kex"
            return self.kex

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "kex"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Ssh1()
        return self._top_entity

class Ssh(Entity):
    """
    ssh
    
    .. attribute:: session
    
    	Crypto SSH session
    	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session>`
    
    

    """

    _prefix = 'crypto-ssh-oper'
    _revision = '2015-06-02'

    def __init__(self):
        super(Ssh, self).__init__()
        self._top_entity = None

        self.yang_name = "ssh"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-ssh-oper"

        self.session = Ssh.Session()
        self.session.parent = self
        self._children_name_map["session"] = "session"
        self._children_yang_names.add("session")


    class Session(Entity):
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
            super(Ssh.Session, self).__init__()

            self.yang_name = "session"
            self.yang_parent_name = "ssh"

            self.brief = Ssh.Session.Brief()
            self.brief.parent = self
            self._children_name_map["brief"] = "brief"
            self._children_yang_names.add("brief")

            self.detail = Ssh.Session.Detail()
            self.detail.parent = self
            self._children_name_map["detail"] = "detail"
            self._children_yang_names.add("detail")

            self.rekey = Ssh.Session.Rekey()
            self.rekey.parent = self
            self._children_name_map["rekey"] = "rekey"
            self._children_yang_names.add("rekey")


        class Rekey(Entity):
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
                super(Ssh.Session.Rekey, self).__init__()

                self.yang_name = "rekey"
                self.yang_parent_name = "session"

                self.incoming_sessions = Ssh.Session.Rekey.IncomingSessions()
                self.incoming_sessions.parent = self
                self._children_name_map["incoming_sessions"] = "incoming-sessions"
                self._children_yang_names.add("incoming-sessions")

                self.outgoing_connections = Ssh.Session.Rekey.OutgoingConnections()
                self.outgoing_connections.parent = self
                self._children_name_map["outgoing_connections"] = "outgoing-connections"
                self._children_yang_names.add("outgoing-connections")


            class IncomingSessions(Entity):
                """
                List of incoming sessions
                
                .. attribute:: session_rekey_info
                
                	session rekey info
                	**type**\: list of    :py:class:`SessionRekeyInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    super(Ssh.Session.Rekey.IncomingSessions, self).__init__()

                    self.yang_name = "incoming-sessions"
                    self.yang_parent_name = "rekey"

                    self.session_rekey_info = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ssh.Session.Rekey.IncomingSessions, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ssh.Session.Rekey.IncomingSessions, self).__setattr__(name, value)


                class SessionRekeyInfo(Entity):
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
                        super(Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo, self).__init__()

                        self.yang_name = "session-rekey-info"
                        self.yang_parent_name = "incoming-sessions"

                        self.session_id = YLeaf(YType.uint32, "session-id")

                        self.session_rekey_count = YLeaf(YType.uint32, "session-rekey-count")

                        self.time_to_rekey = YLeaf(YType.str, "time-to-rekey")

                        self.volume_to_rekey = YLeaf(YType.str, "volume-to-rekey")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("session_id",
                                        "session_rekey_count",
                                        "time_to_rekey",
                                        "volume_to_rekey") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.session_id.is_set or
                            self.session_rekey_count.is_set or
                            self.time_to_rekey.is_set or
                            self.volume_to_rekey.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.session_id.yfilter != YFilter.not_set or
                            self.session_rekey_count.yfilter != YFilter.not_set or
                            self.time_to_rekey.yfilter != YFilter.not_set or
                            self.volume_to_rekey.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session-rekey-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/rekey/incoming-sessions/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_id.get_name_leafdata())
                        if (self.session_rekey_count.is_set or self.session_rekey_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_rekey_count.get_name_leafdata())
                        if (self.time_to_rekey.is_set or self.time_to_rekey.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time_to_rekey.get_name_leafdata())
                        if (self.volume_to_rekey.is_set or self.volume_to_rekey.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.volume_to_rekey.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "session-id" or name == "session-rekey-count" or name == "time-to-rekey" or name == "volume-to-rekey"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "session-id"):
                            self.session_id = value
                            self.session_id.value_namespace = name_space
                            self.session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-rekey-count"):
                            self.session_rekey_count = value
                            self.session_rekey_count.value_namespace = name_space
                            self.session_rekey_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "time-to-rekey"):
                            self.time_to_rekey = value
                            self.time_to_rekey.value_namespace = name_space
                            self.time_to_rekey.value_namespace_prefix = name_space_prefix
                        if(value_path == "volume-to-rekey"):
                            self.volume_to_rekey = value
                            self.volume_to_rekey.value_namespace = name_space
                            self.volume_to_rekey.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.session_rekey_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.session_rekey_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "incoming-sessions" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/rekey/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "session-rekey-info"):
                        for c in self.session_rekey_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.session_rekey_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "session-rekey-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class OutgoingConnections(Entity):
                """
                List of outgoing connections
                
                .. attribute:: session_rekey_info
                
                	session rekey info
                	**type**\: list of    :py:class:`SessionRekeyInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    super(Ssh.Session.Rekey.OutgoingConnections, self).__init__()

                    self.yang_name = "outgoing-connections"
                    self.yang_parent_name = "rekey"

                    self.session_rekey_info = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ssh.Session.Rekey.OutgoingConnections, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ssh.Session.Rekey.OutgoingConnections, self).__setattr__(name, value)


                class SessionRekeyInfo(Entity):
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
                        super(Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo, self).__init__()

                        self.yang_name = "session-rekey-info"
                        self.yang_parent_name = "outgoing-connections"

                        self.session_id = YLeaf(YType.uint32, "session-id")

                        self.session_rekey_count = YLeaf(YType.uint32, "session-rekey-count")

                        self.time_to_rekey = YLeaf(YType.str, "time-to-rekey")

                        self.volume_to_rekey = YLeaf(YType.str, "volume-to-rekey")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("session_id",
                                        "session_rekey_count",
                                        "time_to_rekey",
                                        "volume_to_rekey") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.session_id.is_set or
                            self.session_rekey_count.is_set or
                            self.time_to_rekey.is_set or
                            self.volume_to_rekey.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.session_id.yfilter != YFilter.not_set or
                            self.session_rekey_count.yfilter != YFilter.not_set or
                            self.time_to_rekey.yfilter != YFilter.not_set or
                            self.volume_to_rekey.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session-rekey-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/rekey/outgoing-connections/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_id.get_name_leafdata())
                        if (self.session_rekey_count.is_set or self.session_rekey_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_rekey_count.get_name_leafdata())
                        if (self.time_to_rekey.is_set or self.time_to_rekey.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time_to_rekey.get_name_leafdata())
                        if (self.volume_to_rekey.is_set or self.volume_to_rekey.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.volume_to_rekey.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "session-id" or name == "session-rekey-count" or name == "time-to-rekey" or name == "volume-to-rekey"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "session-id"):
                            self.session_id = value
                            self.session_id.value_namespace = name_space
                            self.session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-rekey-count"):
                            self.session_rekey_count = value
                            self.session_rekey_count.value_namespace = name_space
                            self.session_rekey_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "time-to-rekey"):
                            self.time_to_rekey = value
                            self.time_to_rekey.value_namespace = name_space
                            self.time_to_rekey.value_namespace_prefix = name_space_prefix
                        if(value_path == "volume-to-rekey"):
                            self.volume_to_rekey = value
                            self.volume_to_rekey.value_namespace = name_space
                            self.volume_to_rekey.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.session_rekey_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.session_rekey_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "outgoing-connections" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/rekey/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "session-rekey-info"):
                        for c in self.session_rekey_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.session_rekey_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "session-rekey-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.incoming_sessions is not None and self.incoming_sessions.has_data()) or
                    (self.outgoing_connections is not None and self.outgoing_connections.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.incoming_sessions is not None and self.incoming_sessions.has_operation()) or
                    (self.outgoing_connections is not None and self.outgoing_connections.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rekey" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "incoming-sessions"):
                    if (self.incoming_sessions is None):
                        self.incoming_sessions = Ssh.Session.Rekey.IncomingSessions()
                        self.incoming_sessions.parent = self
                        self._children_name_map["incoming_sessions"] = "incoming-sessions"
                    return self.incoming_sessions

                if (child_yang_name == "outgoing-connections"):
                    if (self.outgoing_connections is None):
                        self.outgoing_connections = Ssh.Session.Rekey.OutgoingConnections()
                        self.outgoing_connections.parent = self
                        self._children_name_map["outgoing_connections"] = "outgoing-connections"
                    return self.outgoing_connections

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "incoming-sessions" or name == "outgoing-connections"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Brief(Entity):
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
                super(Ssh.Session.Brief, self).__init__()

                self.yang_name = "brief"
                self.yang_parent_name = "session"

                self.incoming_sessions = Ssh.Session.Brief.IncomingSessions()
                self.incoming_sessions.parent = self
                self._children_name_map["incoming_sessions"] = "incoming-sessions"
                self._children_yang_names.add("incoming-sessions")

                self.outgoing_sessions = Ssh.Session.Brief.OutgoingSessions()
                self.outgoing_sessions.parent = self
                self._children_name_map["outgoing_sessions"] = "outgoing-sessions"
                self._children_yang_names.add("outgoing-sessions")


            class IncomingSessions(Entity):
                """
                List of incoming sessions
                
                .. attribute:: session_brief_info
                
                	session brief info
                	**type**\: list of    :py:class:`SessionBriefInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.IncomingSessions.SessionBriefInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    super(Ssh.Session.Brief.IncomingSessions, self).__init__()

                    self.yang_name = "incoming-sessions"
                    self.yang_parent_name = "brief"

                    self.session_brief_info = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ssh.Session.Brief.IncomingSessions, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ssh.Session.Brief.IncomingSessions, self).__setattr__(name, value)


                class SessionBriefInfo(Entity):
                    """
                    session brief info
                    
                    .. attribute:: authentication_type
                    
                    	Authentication method
                    	**type**\:   :py:class:`Authen <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Authen>`
                    
                    .. attribute:: channel_id
                    
                    	Channel ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connection_type
                    
                    	Channel Connection Type
                    	**type**\:   :py:class:`Connection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Connection>`
                    
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
                    	**type**\:   :py:class:`States <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.States>`
                    
                    .. attribute:: user_id
                    
                    	User ID
                    	**type**\:  str
                    
                    .. attribute:: version
                    
                    	SSH state version
                    	**type**\:   :py:class:`Version <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Version>`
                    
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
                        super(Ssh.Session.Brief.IncomingSessions.SessionBriefInfo, self).__init__()

                        self.yang_name = "session-brief-info"
                        self.yang_parent_name = "incoming-sessions"

                        self.authentication_type = YLeaf(YType.enumeration, "authentication-type")

                        self.channel_id = YLeaf(YType.uint32, "channel-id")

                        self.connection_type = YLeaf(YType.enumeration, "connection-type")

                        self.host_address = YLeaf(YType.str, "host-address")

                        self.node_name = YLeaf(YType.str, "node-name")

                        self.session_id = YLeaf(YType.uint32, "session-id")

                        self.session_state = YLeaf(YType.enumeration, "session-state")

                        self.user_id = YLeaf(YType.str, "user-id")

                        self.version = YLeaf(YType.enumeration, "version")

                        self.vty_assigned = YLeaf(YType.boolean, "vty-assigned")

                        self.vty_line_number = YLeaf(YType.uint32, "vty-line-number")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("authentication_type",
                                        "channel_id",
                                        "connection_type",
                                        "host_address",
                                        "node_name",
                                        "session_id",
                                        "session_state",
                                        "user_id",
                                        "version",
                                        "vty_assigned",
                                        "vty_line_number") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ssh.Session.Brief.IncomingSessions.SessionBriefInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ssh.Session.Brief.IncomingSessions.SessionBriefInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.authentication_type.is_set or
                            self.channel_id.is_set or
                            self.connection_type.is_set or
                            self.host_address.is_set or
                            self.node_name.is_set or
                            self.session_id.is_set or
                            self.session_state.is_set or
                            self.user_id.is_set or
                            self.version.is_set or
                            self.vty_assigned.is_set or
                            self.vty_line_number.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.authentication_type.yfilter != YFilter.not_set or
                            self.channel_id.yfilter != YFilter.not_set or
                            self.connection_type.yfilter != YFilter.not_set or
                            self.host_address.yfilter != YFilter.not_set or
                            self.node_name.yfilter != YFilter.not_set or
                            self.session_id.yfilter != YFilter.not_set or
                            self.session_state.yfilter != YFilter.not_set or
                            self.user_id.yfilter != YFilter.not_set or
                            self.version.yfilter != YFilter.not_set or
                            self.vty_assigned.yfilter != YFilter.not_set or
                            self.vty_line_number.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session-brief-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/incoming-sessions/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.authentication_type.is_set or self.authentication_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.authentication_type.get_name_leafdata())
                        if (self.channel_id.is_set or self.channel_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.channel_id.get_name_leafdata())
                        if (self.connection_type.is_set or self.connection_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.connection_type.get_name_leafdata())
                        if (self.host_address.is_set or self.host_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.host_address.get_name_leafdata())
                        if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.node_name.get_name_leafdata())
                        if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_id.get_name_leafdata())
                        if (self.session_state.is_set or self.session_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_state.get_name_leafdata())
                        if (self.user_id.is_set or self.user_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.user_id.get_name_leafdata())
                        if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version.get_name_leafdata())
                        if (self.vty_assigned.is_set or self.vty_assigned.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vty_assigned.get_name_leafdata())
                        if (self.vty_line_number.is_set or self.vty_line_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vty_line_number.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "authentication-type" or name == "channel-id" or name == "connection-type" or name == "host-address" or name == "node-name" or name == "session-id" or name == "session-state" or name == "user-id" or name == "version" or name == "vty-assigned" or name == "vty-line-number"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "authentication-type"):
                            self.authentication_type = value
                            self.authentication_type.value_namespace = name_space
                            self.authentication_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "channel-id"):
                            self.channel_id = value
                            self.channel_id.value_namespace = name_space
                            self.channel_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "connection-type"):
                            self.connection_type = value
                            self.connection_type.value_namespace = name_space
                            self.connection_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "host-address"):
                            self.host_address = value
                            self.host_address.value_namespace = name_space
                            self.host_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "node-name"):
                            self.node_name = value
                            self.node_name.value_namespace = name_space
                            self.node_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-id"):
                            self.session_id = value
                            self.session_id.value_namespace = name_space
                            self.session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-state"):
                            self.session_state = value
                            self.session_state.value_namespace = name_space
                            self.session_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "user-id"):
                            self.user_id = value
                            self.user_id.value_namespace = name_space
                            self.user_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "version"):
                            self.version = value
                            self.version.value_namespace = name_space
                            self.version.value_namespace_prefix = name_space_prefix
                        if(value_path == "vty-assigned"):
                            self.vty_assigned = value
                            self.vty_assigned.value_namespace = name_space
                            self.vty_assigned.value_namespace_prefix = name_space_prefix
                        if(value_path == "vty-line-number"):
                            self.vty_line_number = value
                            self.vty_line_number.value_namespace = name_space
                            self.vty_line_number.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.session_brief_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.session_brief_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "incoming-sessions" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "session-brief-info"):
                        for c in self.session_brief_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ssh.Session.Brief.IncomingSessions.SessionBriefInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.session_brief_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "session-brief-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class OutgoingSessions(Entity):
                """
                List of outgoing sessions
                
                .. attribute:: session_brief_info
                
                	session brief info
                	**type**\: list of    :py:class:`SessionBriefInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    super(Ssh.Session.Brief.OutgoingSessions, self).__init__()

                    self.yang_name = "outgoing-sessions"
                    self.yang_parent_name = "brief"

                    self.session_brief_info = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ssh.Session.Brief.OutgoingSessions, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ssh.Session.Brief.OutgoingSessions, self).__setattr__(name, value)


                class SessionBriefInfo(Entity):
                    """
                    session brief info
                    
                    .. attribute:: authentication_type
                    
                    	Authentication method
                    	**type**\:   :py:class:`Authen <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Authen>`
                    
                    .. attribute:: channel_id
                    
                    	Channel ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connection_type
                    
                    	Channel Connection Type
                    	**type**\:   :py:class:`Connection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Connection>`
                    
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
                    	**type**\:   :py:class:`States <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.States>`
                    
                    .. attribute:: user_id
                    
                    	User ID
                    	**type**\:  str
                    
                    .. attribute:: version
                    
                    	SSH state version
                    	**type**\:   :py:class:`Version <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Version>`
                    
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
                        super(Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo, self).__init__()

                        self.yang_name = "session-brief-info"
                        self.yang_parent_name = "outgoing-sessions"

                        self.authentication_type = YLeaf(YType.enumeration, "authentication-type")

                        self.channel_id = YLeaf(YType.uint32, "channel-id")

                        self.connection_type = YLeaf(YType.enumeration, "connection-type")

                        self.host_address = YLeaf(YType.str, "host-address")

                        self.node_name = YLeaf(YType.str, "node-name")

                        self.session_id = YLeaf(YType.uint32, "session-id")

                        self.session_state = YLeaf(YType.enumeration, "session-state")

                        self.user_id = YLeaf(YType.str, "user-id")

                        self.version = YLeaf(YType.enumeration, "version")

                        self.vty_assigned = YLeaf(YType.boolean, "vty-assigned")

                        self.vty_line_number = YLeaf(YType.uint32, "vty-line-number")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("authentication_type",
                                        "channel_id",
                                        "connection_type",
                                        "host_address",
                                        "node_name",
                                        "session_id",
                                        "session_state",
                                        "user_id",
                                        "version",
                                        "vty_assigned",
                                        "vty_line_number") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.authentication_type.is_set or
                            self.channel_id.is_set or
                            self.connection_type.is_set or
                            self.host_address.is_set or
                            self.node_name.is_set or
                            self.session_id.is_set or
                            self.session_state.is_set or
                            self.user_id.is_set or
                            self.version.is_set or
                            self.vty_assigned.is_set or
                            self.vty_line_number.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.authentication_type.yfilter != YFilter.not_set or
                            self.channel_id.yfilter != YFilter.not_set or
                            self.connection_type.yfilter != YFilter.not_set or
                            self.host_address.yfilter != YFilter.not_set or
                            self.node_name.yfilter != YFilter.not_set or
                            self.session_id.yfilter != YFilter.not_set or
                            self.session_state.yfilter != YFilter.not_set or
                            self.user_id.yfilter != YFilter.not_set or
                            self.version.yfilter != YFilter.not_set or
                            self.vty_assigned.yfilter != YFilter.not_set or
                            self.vty_line_number.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session-brief-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/outgoing-sessions/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.authentication_type.is_set or self.authentication_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.authentication_type.get_name_leafdata())
                        if (self.channel_id.is_set or self.channel_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.channel_id.get_name_leafdata())
                        if (self.connection_type.is_set or self.connection_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.connection_type.get_name_leafdata())
                        if (self.host_address.is_set or self.host_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.host_address.get_name_leafdata())
                        if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.node_name.get_name_leafdata())
                        if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_id.get_name_leafdata())
                        if (self.session_state.is_set or self.session_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_state.get_name_leafdata())
                        if (self.user_id.is_set or self.user_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.user_id.get_name_leafdata())
                        if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version.get_name_leafdata())
                        if (self.vty_assigned.is_set or self.vty_assigned.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vty_assigned.get_name_leafdata())
                        if (self.vty_line_number.is_set or self.vty_line_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vty_line_number.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "authentication-type" or name == "channel-id" or name == "connection-type" or name == "host-address" or name == "node-name" or name == "session-id" or name == "session-state" or name == "user-id" or name == "version" or name == "vty-assigned" or name == "vty-line-number"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "authentication-type"):
                            self.authentication_type = value
                            self.authentication_type.value_namespace = name_space
                            self.authentication_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "channel-id"):
                            self.channel_id = value
                            self.channel_id.value_namespace = name_space
                            self.channel_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "connection-type"):
                            self.connection_type = value
                            self.connection_type.value_namespace = name_space
                            self.connection_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "host-address"):
                            self.host_address = value
                            self.host_address.value_namespace = name_space
                            self.host_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "node-name"):
                            self.node_name = value
                            self.node_name.value_namespace = name_space
                            self.node_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-id"):
                            self.session_id = value
                            self.session_id.value_namespace = name_space
                            self.session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-state"):
                            self.session_state = value
                            self.session_state.value_namespace = name_space
                            self.session_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "user-id"):
                            self.user_id = value
                            self.user_id.value_namespace = name_space
                            self.user_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "version"):
                            self.version = value
                            self.version.value_namespace = name_space
                            self.version.value_namespace_prefix = name_space_prefix
                        if(value_path == "vty-assigned"):
                            self.vty_assigned = value
                            self.vty_assigned.value_namespace = name_space
                            self.vty_assigned.value_namespace_prefix = name_space_prefix
                        if(value_path == "vty-line-number"):
                            self.vty_line_number = value
                            self.vty_line_number.value_namespace = name_space
                            self.vty_line_number.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.session_brief_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.session_brief_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "outgoing-sessions" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/brief/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "session-brief-info"):
                        for c in self.session_brief_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.session_brief_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "session-brief-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.incoming_sessions is not None and self.incoming_sessions.has_data()) or
                    (self.outgoing_sessions is not None and self.outgoing_sessions.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.incoming_sessions is not None and self.incoming_sessions.has_operation()) or
                    (self.outgoing_sessions is not None and self.outgoing_sessions.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "brief" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "incoming-sessions"):
                    if (self.incoming_sessions is None):
                        self.incoming_sessions = Ssh.Session.Brief.IncomingSessions()
                        self.incoming_sessions.parent = self
                        self._children_name_map["incoming_sessions"] = "incoming-sessions"
                    return self.incoming_sessions

                if (child_yang_name == "outgoing-sessions"):
                    if (self.outgoing_sessions is None):
                        self.outgoing_sessions = Ssh.Session.Brief.OutgoingSessions()
                        self.outgoing_sessions.parent = self
                        self._children_name_map["outgoing_sessions"] = "outgoing-sessions"
                    return self.outgoing_sessions

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "incoming-sessions" or name == "outgoing-sessions"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Detail(Entity):
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
                super(Ssh.Session.Detail, self).__init__()

                self.yang_name = "detail"
                self.yang_parent_name = "session"

                self.incoming_sessions = Ssh.Session.Detail.IncomingSessions()
                self.incoming_sessions.parent = self
                self._children_name_map["incoming_sessions"] = "incoming-sessions"
                self._children_yang_names.add("incoming-sessions")

                self.outgoing_connections = Ssh.Session.Detail.OutgoingConnections()
                self.outgoing_connections.parent = self
                self._children_name_map["outgoing_connections"] = "outgoing-connections"
                self._children_yang_names.add("outgoing-connections")


            class IncomingSessions(Entity):
                """
                List of incoming sessions
                
                .. attribute:: session_detail_info
                
                	session detail info
                	**type**\: list of    :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.IncomingSessions.SessionDetailInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    super(Ssh.Session.Detail.IncomingSessions, self).__init__()

                    self.yang_name = "incoming-sessions"
                    self.yang_parent_name = "detail"

                    self.session_detail_info = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ssh.Session.Detail.IncomingSessions, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ssh.Session.Detail.IncomingSessions, self).__setattr__(name, value)


                class SessionDetailInfo(Entity):
                    """
                    session detail info
                    
                    .. attribute:: in_cipher
                    
                    	In cipher algorithm
                    	**type**\:   :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    .. attribute:: in_mac
                    
                    	In MAC
                    	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    .. attribute:: key_exchange
                    
                    	Key exchange name
                    	**type**\:   :py:class:`KexName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexName>`
                    
                    .. attribute:: out_cipher
                    
                    	Out cipher algorithm
                    	**type**\:   :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    .. attribute:: out_mac
                    
                    	Out MAC
                    	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    .. attribute:: public_key
                    
                    	Host key algorithm
                    	**type**\:   :py:class:`Hostkey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Hostkey>`
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        super(Ssh.Session.Detail.IncomingSessions.SessionDetailInfo, self).__init__()

                        self.yang_name = "session-detail-info"
                        self.yang_parent_name = "incoming-sessions"

                        self.in_cipher = YLeaf(YType.enumeration, "in-cipher")

                        self.in_mac = YLeaf(YType.enumeration, "in-mac")

                        self.key_exchange = YLeaf(YType.enumeration, "key-exchange")

                        self.out_cipher = YLeaf(YType.enumeration, "out-cipher")

                        self.out_mac = YLeaf(YType.enumeration, "out-mac")

                        self.public_key = YLeaf(YType.enumeration, "public-key")

                        self.session_id = YLeaf(YType.uint32, "session-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("in_cipher",
                                        "in_mac",
                                        "key_exchange",
                                        "out_cipher",
                                        "out_mac",
                                        "public_key",
                                        "session_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ssh.Session.Detail.IncomingSessions.SessionDetailInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ssh.Session.Detail.IncomingSessions.SessionDetailInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.in_cipher.is_set or
                            self.in_mac.is_set or
                            self.key_exchange.is_set or
                            self.out_cipher.is_set or
                            self.out_mac.is_set or
                            self.public_key.is_set or
                            self.session_id.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.in_cipher.yfilter != YFilter.not_set or
                            self.in_mac.yfilter != YFilter.not_set or
                            self.key_exchange.yfilter != YFilter.not_set or
                            self.out_cipher.yfilter != YFilter.not_set or
                            self.out_mac.yfilter != YFilter.not_set or
                            self.public_key.yfilter != YFilter.not_set or
                            self.session_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session-detail-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/detail/incoming-sessions/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.in_cipher.is_set or self.in_cipher.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.in_cipher.get_name_leafdata())
                        if (self.in_mac.is_set or self.in_mac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.in_mac.get_name_leafdata())
                        if (self.key_exchange.is_set or self.key_exchange.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.key_exchange.get_name_leafdata())
                        if (self.out_cipher.is_set or self.out_cipher.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.out_cipher.get_name_leafdata())
                        if (self.out_mac.is_set or self.out_mac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.out_mac.get_name_leafdata())
                        if (self.public_key.is_set or self.public_key.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.public_key.get_name_leafdata())
                        if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "in-cipher" or name == "in-mac" or name == "key-exchange" or name == "out-cipher" or name == "out-mac" or name == "public-key" or name == "session-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "in-cipher"):
                            self.in_cipher = value
                            self.in_cipher.value_namespace = name_space
                            self.in_cipher.value_namespace_prefix = name_space_prefix
                        if(value_path == "in-mac"):
                            self.in_mac = value
                            self.in_mac.value_namespace = name_space
                            self.in_mac.value_namespace_prefix = name_space_prefix
                        if(value_path == "key-exchange"):
                            self.key_exchange = value
                            self.key_exchange.value_namespace = name_space
                            self.key_exchange.value_namespace_prefix = name_space_prefix
                        if(value_path == "out-cipher"):
                            self.out_cipher = value
                            self.out_cipher.value_namespace = name_space
                            self.out_cipher.value_namespace_prefix = name_space_prefix
                        if(value_path == "out-mac"):
                            self.out_mac = value
                            self.out_mac.value_namespace = name_space
                            self.out_mac.value_namespace_prefix = name_space_prefix
                        if(value_path == "public-key"):
                            self.public_key = value
                            self.public_key.value_namespace = name_space
                            self.public_key.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-id"):
                            self.session_id = value
                            self.session_id.value_namespace = name_space
                            self.session_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.session_detail_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.session_detail_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "incoming-sessions" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/detail/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "session-detail-info"):
                        for c in self.session_detail_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ssh.Session.Detail.IncomingSessions.SessionDetailInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.session_detail_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "session-detail-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class OutgoingConnections(Entity):
                """
                List of outgoing connections
                
                .. attribute:: session_detail_info
                
                	session detail info
                	**type**\: list of    :py:class:`SessionDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    super(Ssh.Session.Detail.OutgoingConnections, self).__init__()

                    self.yang_name = "outgoing-connections"
                    self.yang_parent_name = "detail"

                    self.session_detail_info = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ssh.Session.Detail.OutgoingConnections, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ssh.Session.Detail.OutgoingConnections, self).__setattr__(name, value)


                class SessionDetailInfo(Entity):
                    """
                    session detail info
                    
                    .. attribute:: in_cipher
                    
                    	In cipher algorithm
                    	**type**\:   :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    .. attribute:: in_mac
                    
                    	In MAC
                    	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    .. attribute:: key_exchange
                    
                    	Key exchange name
                    	**type**\:   :py:class:`KexName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.KexName>`
                    
                    .. attribute:: out_cipher
                    
                    	Out cipher algorithm
                    	**type**\:   :py:class:`Cipher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Cipher>`
                    
                    .. attribute:: out_mac
                    
                    	Out MAC
                    	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Mac>`
                    
                    .. attribute:: public_key
                    
                    	Host key algorithm
                    	**type**\:   :py:class:`Hostkey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper.Hostkey>`
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        super(Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo, self).__init__()

                        self.yang_name = "session-detail-info"
                        self.yang_parent_name = "outgoing-connections"

                        self.in_cipher = YLeaf(YType.enumeration, "in-cipher")

                        self.in_mac = YLeaf(YType.enumeration, "in-mac")

                        self.key_exchange = YLeaf(YType.enumeration, "key-exchange")

                        self.out_cipher = YLeaf(YType.enumeration, "out-cipher")

                        self.out_mac = YLeaf(YType.enumeration, "out-mac")

                        self.public_key = YLeaf(YType.enumeration, "public-key")

                        self.session_id = YLeaf(YType.uint32, "session-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("in_cipher",
                                        "in_mac",
                                        "key_exchange",
                                        "out_cipher",
                                        "out_mac",
                                        "public_key",
                                        "session_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.in_cipher.is_set or
                            self.in_mac.is_set or
                            self.key_exchange.is_set or
                            self.out_cipher.is_set or
                            self.out_mac.is_set or
                            self.public_key.is_set or
                            self.session_id.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.in_cipher.yfilter != YFilter.not_set or
                            self.in_mac.yfilter != YFilter.not_set or
                            self.key_exchange.yfilter != YFilter.not_set or
                            self.out_cipher.yfilter != YFilter.not_set or
                            self.out_mac.yfilter != YFilter.not_set or
                            self.public_key.yfilter != YFilter.not_set or
                            self.session_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session-detail-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/detail/outgoing-connections/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.in_cipher.is_set or self.in_cipher.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.in_cipher.get_name_leafdata())
                        if (self.in_mac.is_set or self.in_mac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.in_mac.get_name_leafdata())
                        if (self.key_exchange.is_set or self.key_exchange.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.key_exchange.get_name_leafdata())
                        if (self.out_cipher.is_set or self.out_cipher.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.out_cipher.get_name_leafdata())
                        if (self.out_mac.is_set or self.out_mac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.out_mac.get_name_leafdata())
                        if (self.public_key.is_set or self.public_key.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.public_key.get_name_leafdata())
                        if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "in-cipher" or name == "in-mac" or name == "key-exchange" or name == "out-cipher" or name == "out-mac" or name == "public-key" or name == "session-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "in-cipher"):
                            self.in_cipher = value
                            self.in_cipher.value_namespace = name_space
                            self.in_cipher.value_namespace_prefix = name_space_prefix
                        if(value_path == "in-mac"):
                            self.in_mac = value
                            self.in_mac.value_namespace = name_space
                            self.in_mac.value_namespace_prefix = name_space_prefix
                        if(value_path == "key-exchange"):
                            self.key_exchange = value
                            self.key_exchange.value_namespace = name_space
                            self.key_exchange.value_namespace_prefix = name_space_prefix
                        if(value_path == "out-cipher"):
                            self.out_cipher = value
                            self.out_cipher.value_namespace = name_space
                            self.out_cipher.value_namespace_prefix = name_space_prefix
                        if(value_path == "out-mac"):
                            self.out_mac = value
                            self.out_mac.value_namespace = name_space
                            self.out_mac.value_namespace_prefix = name_space_prefix
                        if(value_path == "public-key"):
                            self.public_key = value
                            self.public_key.value_namespace = name_space
                            self.public_key.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-id"):
                            self.session_id = value
                            self.session_id.value_namespace = name_space
                            self.session_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.session_detail_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.session_detail_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "outgoing-connections" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/detail/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "session-detail-info"):
                        for c in self.session_detail_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.session_detail_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "session-detail-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.incoming_sessions is not None and self.incoming_sessions.has_data()) or
                    (self.outgoing_connections is not None and self.outgoing_connections.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.incoming_sessions is not None and self.incoming_sessions.has_operation()) or
                    (self.outgoing_connections is not None and self.outgoing_connections.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "detail" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/session/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "incoming-sessions"):
                    if (self.incoming_sessions is None):
                        self.incoming_sessions = Ssh.Session.Detail.IncomingSessions()
                        self.incoming_sessions.parent = self
                        self._children_name_map["incoming_sessions"] = "incoming-sessions"
                    return self.incoming_sessions

                if (child_yang_name == "outgoing-connections"):
                    if (self.outgoing_connections is None):
                        self.outgoing_connections = Ssh.Session.Detail.OutgoingConnections()
                        self.outgoing_connections.parent = self
                        self._children_name_map["outgoing_connections"] = "outgoing-connections"
                    return self.outgoing_connections

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "incoming-sessions" or name == "outgoing-connections"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.brief is not None and self.brief.has_data()) or
                (self.detail is not None and self.detail.has_data()) or
                (self.rekey is not None and self.rekey.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.brief is not None and self.brief.has_operation()) or
                (self.detail is not None and self.detail.has_operation()) or
                (self.rekey is not None and self.rekey.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "session" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "brief"):
                if (self.brief is None):
                    self.brief = Ssh.Session.Brief()
                    self.brief.parent = self
                    self._children_name_map["brief"] = "brief"
                return self.brief

            if (child_yang_name == "detail"):
                if (self.detail is None):
                    self.detail = Ssh.Session.Detail()
                    self.detail.parent = self
                    self._children_name_map["detail"] = "detail"
                return self.detail

            if (child_yang_name == "rekey"):
                if (self.rekey is None):
                    self.rekey = Ssh.Session.Rekey()
                    self.rekey.parent = self
                    self._children_name_map["rekey"] = "rekey"
                return self.rekey

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "brief" or name == "detail" or name == "rekey"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.session is not None and self.session.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.session is not None and self.session.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-ssh-oper:ssh" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "session"):
            if (self.session is None):
                self.session = Ssh.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"
            return self.session

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "session"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Ssh()
        return self._top_entity


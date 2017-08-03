""" Cisco_IOS_XR_crypto_sam_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-sam package configuration.

This module contains definitions
for the following management objects\:
  crypto\: Crypto configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

        self.sam = Crypto.Sam()
        self.sam.parent = self
        self._children_name_map["sam"] = "sam"
        self._children_yang_names.add("sam")

        self.ssh = Crypto.Ssh()
        self.ssh.parent = self
        self._children_name_map["ssh"] = "ssh"
        self._children_yang_names.add("ssh")


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

            self.prompt_interval = None
            self._children_name_map["prompt_interval"] = "prompt-interval"
            self._children_yang_names.add("prompt-interval")


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
                self.is_presence_container = True

                self.action = YLeaf(YType.enumeration, "action")

                self.prompt_time = YLeaf(YType.uint32, "prompt-time")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("action",
                                "prompt_time") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Crypto.Sam.PromptInterval, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Crypto.Sam.PromptInterval, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.action.is_set or
                    self.prompt_time.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.action.yfilter != YFilter.not_set or
                    self.prompt_time.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "prompt-interval" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-crypto-sam-cfg:crypto/sam/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.action.get_name_leafdata())
                if (self.prompt_time.is_set or self.prompt_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prompt_time.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "action" or name == "prompt-time"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "action"):
                    self.action = value
                    self.action.value_namespace = name_space
                    self.action.value_namespace_prefix = name_space_prefix
                if(value_path == "prompt-time"):
                    self.prompt_time = value
                    self.prompt_time.value_namespace = name_space
                    self.prompt_time.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.prompt_interval is not None)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.prompt_interval is not None and self.prompt_interval.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sam" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-sam-cfg:crypto/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "prompt-interval"):
                if (self.prompt_interval is None):
                    self.prompt_interval = Crypto.Sam.PromptInterval()
                    self.prompt_interval.parent = self
                    self._children_name_map["prompt_interval"] = "prompt-interval"
                return self.prompt_interval

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "prompt-interval"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        _revision = '2015-07-30'

        def __init__(self):
            super(Crypto.Ssh, self).__init__()

            self.yang_name = "ssh"
            self.yang_parent_name = "crypto"

            self.client = Crypto.Ssh.Client()
            self.client.parent = self
            self._children_name_map["client"] = "client"
            self._children_yang_names.add("client")

            self.server = Crypto.Ssh.Server()
            self.server.parent = self
            self._children_name_map["server"] = "server"
            self._children_yang_names.add("server")


        class Client(Entity):
            """
            Provide SSH client service
            
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
            
            .. attribute:: source_interface
            
            	Source interface for ssh client sessions
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            

            """

            _prefix = 'crypto-ssh-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                super(Crypto.Ssh.Client, self).__init__()

                self.yang_name = "client"
                self.yang_parent_name = "ssh"

                self.client_vrf = YLeaf(YType.str, "client-vrf")

                self.dscp = YLeaf(YType.uint32, "dscp")

                self.host_public_key = YLeaf(YType.str, "host-public-key")

                self.source_interface = YLeaf(YType.str, "source-interface")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("client_vrf",
                                "dscp",
                                "host_public_key",
                                "source_interface") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Crypto.Ssh.Client, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Crypto.Ssh.Client, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.client_vrf.is_set or
                    self.dscp.is_set or
                    self.host_public_key.is_set or
                    self.source_interface.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.client_vrf.yfilter != YFilter.not_set or
                    self.dscp.yfilter != YFilter.not_set or
                    self.host_public_key.yfilter != YFilter.not_set or
                    self.source_interface.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "client" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.client_vrf.is_set or self.client_vrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.client_vrf.get_name_leafdata())
                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dscp.get_name_leafdata())
                if (self.host_public_key.is_set or self.host_public_key.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.host_public_key.get_name_leafdata())
                if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_interface.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "client-vrf" or name == "dscp" or name == "host-public-key" or name == "source-interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "client-vrf"):
                    self.client_vrf = value
                    self.client_vrf.value_namespace = name_space
                    self.client_vrf.value_namespace_prefix = name_space_prefix
                if(value_path == "dscp"):
                    self.dscp = value
                    self.dscp.value_namespace = name_space
                    self.dscp.value_namespace_prefix = name_space_prefix
                if(value_path == "host-public-key"):
                    self.host_public_key = value
                    self.host_public_key.value_namespace = name_space
                    self.host_public_key.value_namespace_prefix = name_space_prefix
                if(value_path == "source-interface"):
                    self.source_interface = value
                    self.source_interface.value_namespace = name_space
                    self.source_interface.value_namespace_prefix = name_space_prefix


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
            _revision = '2015-07-30'

            def __init__(self):
                super(Crypto.Ssh.Server, self).__init__()

                self.yang_name = "server"
                self.yang_parent_name = "ssh"

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

                self.netconf_vrf_table = Crypto.Ssh.Server.NetconfVrfTable()
                self.netconf_vrf_table.parent = self
                self._children_name_map["netconf_vrf_table"] = "netconf-vrf-table"
                self._children_yang_names.add("netconf-vrf-table")

                self.vrf_table = Crypto.Ssh.Server.VrfTable()
                self.vrf_table.parent = self
                self._children_name_map["vrf_table"] = "vrf-table"
                self._children_yang_names.add("vrf-table")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dscp",
                                "logging",
                                "netconf",
                                "rate_limit",
                                "rekey_time",
                                "rekey_volume",
                                "session_limit",
                                "timeout",
                                "v2") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Crypto.Ssh.Server, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Crypto.Ssh.Server, self).__setattr__(name, value)


            class Disable(Entity):
                """
                disable
                
                .. attribute:: hmac
                
                	hmac
                	**type**\:   :py:class:`Hmac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.Disable.Hmac>`
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Crypto.Ssh.Server.Disable, self).__init__()

                    self.yang_name = "disable"
                    self.yang_parent_name = "server"

                    self.hmac = Crypto.Ssh.Server.Disable.Hmac()
                    self.hmac.parent = self
                    self._children_name_map["hmac"] = "hmac"
                    self._children_yang_names.add("hmac")


                class Hmac(Entity):
                    """
                    hmac
                    
                    .. attribute:: hmac_sha512
                    
                    	Disable Hmac\-sha2\-512 negotiation
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'crypto-ssh-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Crypto.Ssh.Server.Disable.Hmac, self).__init__()

                        self.yang_name = "hmac"
                        self.yang_parent_name = "disable"

                        self.hmac_sha512 = YLeaf(YType.boolean, "hmac-sha512")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("hmac_sha512") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Crypto.Ssh.Server.Disable.Hmac, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Crypto.Ssh.Server.Disable.Hmac, self).__setattr__(name, value)

                    def has_data(self):
                        return self.hmac_sha512.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.hmac_sha512.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "hmac" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/disable/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.hmac_sha512.is_set or self.hmac_sha512.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hmac_sha512.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "hmac-sha512"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "hmac-sha512"):
                            self.hmac_sha512 = value
                            self.hmac_sha512.value_namespace = name_space
                            self.hmac_sha512.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.hmac is not None and self.hmac.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.hmac is not None and self.hmac.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "disable" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "hmac"):
                        if (self.hmac is None):
                            self.hmac = Crypto.Ssh.Server.Disable.Hmac()
                            self.hmac.parent = self
                            self._children_name_map["hmac"] = "hmac"
                        return self.hmac

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "hmac"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class VrfTable(Entity):
                """
                Cisco sshd VRF name
                
                .. attribute:: vrf
                
                	Enter VRF name
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.VrfTable.Vrf>`
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Crypto.Ssh.Server.VrfTable, self).__init__()

                    self.yang_name = "vrf-table"
                    self.yang_parent_name = "server"

                    self.vrf = YList(self)

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
                                super(Crypto.Ssh.Server.VrfTable, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Crypto.Ssh.Server.VrfTable, self).__setattr__(name, value)


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
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Crypto.Ssh.Server.VrfTable.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrf-table"

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.ipv4_access_list = YLeaf(YType.str, "ipv4-access-list")

                        self.ipv6_access_list = YLeaf(YType.str, "ipv6-access-list")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("vrf_name",
                                        "enable",
                                        "ipv4_access_list",
                                        "ipv6_access_list") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Crypto.Ssh.Server.VrfTable.Vrf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Crypto.Ssh.Server.VrfTable.Vrf, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.vrf_name.is_set or
                            self.enable.is_set or
                            self.ipv4_access_list.is_set or
                            self.ipv6_access_list.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set or
                            self.ipv4_access_list.yfilter != YFilter.not_set or
                            self.ipv6_access_list.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/vrf-table/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())
                        if (self.ipv4_access_list.is_set or self.ipv4_access_list.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_access_list.get_name_leafdata())
                        if (self.ipv6_access_list.is_set or self.ipv6_access_list.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_access_list.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "vrf-name" or name == "enable" or name == "ipv4-access-list" or name == "ipv6-access-list"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-access-list"):
                            self.ipv4_access_list = value
                            self.ipv4_access_list.value_namespace = name_space
                            self.ipv4_access_list.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-access-list"):
                            self.ipv6_access_list = value
                            self.ipv6_access_list.value_namespace = name_space
                            self.ipv6_access_list.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.vrf:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.vrf:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vrf-table" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "vrf"):
                        for c in self.vrf:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Crypto.Ssh.Server.VrfTable.Vrf()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.vrf.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vrf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Capability(Entity):
                """
                Capability
                
                .. attribute:: netconf_xml
                
                	Enable Netconf\-XML stack on port 22
                	**type**\:  bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Crypto.Ssh.Server.Capability, self).__init__()

                    self.yang_name = "capability"
                    self.yang_parent_name = "server"

                    self.netconf_xml = YLeaf(YType.boolean, "netconf-xml")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("netconf_xml") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Crypto.Ssh.Server.Capability, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Crypto.Ssh.Server.Capability, self).__setattr__(name, value)

                def has_data(self):
                    return self.netconf_xml.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.netconf_xml.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "capability" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.netconf_xml.is_set or self.netconf_xml.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.netconf_xml.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "netconf-xml"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "netconf-xml"):
                        self.netconf_xml = value
                        self.netconf_xml.value_namespace = name_space
                        self.netconf_xml.value_namespace_prefix = name_space_prefix


            class NetconfVrfTable(Entity):
                """
                Cisco sshd Netconf VRF name
                
                .. attribute:: vrf
                
                	Enter VRF name
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Crypto.Ssh.Server.NetconfVrfTable.Vrf>`
                
                

                """

                _prefix = 'crypto-ssh-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Crypto.Ssh.Server.NetconfVrfTable, self).__init__()

                    self.yang_name = "netconf-vrf-table"
                    self.yang_parent_name = "server"

                    self.vrf = YList(self)

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
                                super(Crypto.Ssh.Server.NetconfVrfTable, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Crypto.Ssh.Server.NetconfVrfTable, self).__setattr__(name, value)


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
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Crypto.Ssh.Server.NetconfVrfTable.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "netconf-vrf-table"

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.ipv4_access_list = YLeaf(YType.str, "ipv4-access-list")

                        self.ipv6_access_list = YLeaf(YType.str, "ipv6-access-list")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("vrf_name",
                                        "enable",
                                        "ipv4_access_list",
                                        "ipv6_access_list") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Crypto.Ssh.Server.NetconfVrfTable.Vrf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Crypto.Ssh.Server.NetconfVrfTable.Vrf, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.vrf_name.is_set or
                            self.enable.is_set or
                            self.ipv4_access_list.is_set or
                            self.ipv6_access_list.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set or
                            self.ipv4_access_list.yfilter != YFilter.not_set or
                            self.ipv6_access_list.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/netconf-vrf-table/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())
                        if (self.ipv4_access_list.is_set or self.ipv4_access_list.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_access_list.get_name_leafdata())
                        if (self.ipv6_access_list.is_set or self.ipv6_access_list.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_access_list.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "vrf-name" or name == "enable" or name == "ipv4-access-list" or name == "ipv6-access-list"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-access-list"):
                            self.ipv4_access_list = value
                            self.ipv4_access_list.value_namespace = name_space
                            self.ipv4_access_list.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-access-list"):
                            self.ipv6_access_list = value
                            self.ipv6_access_list.value_namespace = name_space
                            self.ipv6_access_list.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.vrf:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.vrf:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "netconf-vrf-table" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/server/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "vrf"):
                        for c in self.vrf:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Crypto.Ssh.Server.NetconfVrfTable.Vrf()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.vrf.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vrf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.dscp.is_set or
                    self.logging.is_set or
                    self.netconf.is_set or
                    self.rate_limit.is_set or
                    self.rekey_time.is_set or
                    self.rekey_volume.is_set or
                    self.session_limit.is_set or
                    self.timeout.is_set or
                    self.v2.is_set or
                    (self.capability is not None and self.capability.has_data()) or
                    (self.disable is not None and self.disable.has_data()) or
                    (self.netconf_vrf_table is not None and self.netconf_vrf_table.has_data()) or
                    (self.vrf_table is not None and self.vrf_table.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dscp.yfilter != YFilter.not_set or
                    self.logging.yfilter != YFilter.not_set or
                    self.netconf.yfilter != YFilter.not_set or
                    self.rate_limit.yfilter != YFilter.not_set or
                    self.rekey_time.yfilter != YFilter.not_set or
                    self.rekey_volume.yfilter != YFilter.not_set or
                    self.session_limit.yfilter != YFilter.not_set or
                    self.timeout.yfilter != YFilter.not_set or
                    self.v2.yfilter != YFilter.not_set or
                    (self.capability is not None and self.capability.has_operation()) or
                    (self.disable is not None and self.disable.has_operation()) or
                    (self.netconf_vrf_table is not None and self.netconf_vrf_table.has_operation()) or
                    (self.vrf_table is not None and self.vrf_table.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "server" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-crypto-sam-cfg:crypto/Cisco-IOS-XR-crypto-ssh-cfg:ssh/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dscp.get_name_leafdata())
                if (self.logging.is_set or self.logging.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.logging.get_name_leafdata())
                if (self.netconf.is_set or self.netconf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.netconf.get_name_leafdata())
                if (self.rate_limit.is_set or self.rate_limit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rate_limit.get_name_leafdata())
                if (self.rekey_time.is_set or self.rekey_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rekey_time.get_name_leafdata())
                if (self.rekey_volume.is_set or self.rekey_volume.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rekey_volume.get_name_leafdata())
                if (self.session_limit.is_set or self.session_limit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.session_limit.get_name_leafdata())
                if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeout.get_name_leafdata())
                if (self.v2.is_set or self.v2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.v2.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "capability"):
                    if (self.capability is None):
                        self.capability = Crypto.Ssh.Server.Capability()
                        self.capability.parent = self
                        self._children_name_map["capability"] = "capability"
                    return self.capability

                if (child_yang_name == "disable"):
                    if (self.disable is None):
                        self.disable = Crypto.Ssh.Server.Disable()
                        self.disable.parent = self
                        self._children_name_map["disable"] = "disable"
                    return self.disable

                if (child_yang_name == "netconf-vrf-table"):
                    if (self.netconf_vrf_table is None):
                        self.netconf_vrf_table = Crypto.Ssh.Server.NetconfVrfTable()
                        self.netconf_vrf_table.parent = self
                        self._children_name_map["netconf_vrf_table"] = "netconf-vrf-table"
                    return self.netconf_vrf_table

                if (child_yang_name == "vrf-table"):
                    if (self.vrf_table is None):
                        self.vrf_table = Crypto.Ssh.Server.VrfTable()
                        self.vrf_table.parent = self
                        self._children_name_map["vrf_table"] = "vrf-table"
                    return self.vrf_table

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "capability" or name == "disable" or name == "netconf-vrf-table" or name == "vrf-table" or name == "dscp" or name == "logging" or name == "netconf" or name == "rate-limit" or name == "rekey-time" or name == "rekey-volume" or name == "session-limit" or name == "timeout" or name == "v2"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dscp"):
                    self.dscp = value
                    self.dscp.value_namespace = name_space
                    self.dscp.value_namespace_prefix = name_space_prefix
                if(value_path == "logging"):
                    self.logging = value
                    self.logging.value_namespace = name_space
                    self.logging.value_namespace_prefix = name_space_prefix
                if(value_path == "netconf"):
                    self.netconf = value
                    self.netconf.value_namespace = name_space
                    self.netconf.value_namespace_prefix = name_space_prefix
                if(value_path == "rate-limit"):
                    self.rate_limit = value
                    self.rate_limit.value_namespace = name_space
                    self.rate_limit.value_namespace_prefix = name_space_prefix
                if(value_path == "rekey-time"):
                    self.rekey_time = value
                    self.rekey_time.value_namespace = name_space
                    self.rekey_time.value_namespace_prefix = name_space_prefix
                if(value_path == "rekey-volume"):
                    self.rekey_volume = value
                    self.rekey_volume.value_namespace = name_space
                    self.rekey_volume.value_namespace_prefix = name_space_prefix
                if(value_path == "session-limit"):
                    self.session_limit = value
                    self.session_limit.value_namespace = name_space
                    self.session_limit.value_namespace_prefix = name_space_prefix
                if(value_path == "timeout"):
                    self.timeout = value
                    self.timeout.value_namespace = name_space
                    self.timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "v2"):
                    self.v2 = value
                    self.v2.value_namespace = name_space
                    self.v2.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                (self.client is not None and self.client.has_data()) or
                (self.server is not None and self.server.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.client is not None and self.client.has_operation()) or
                (self.server is not None and self.server.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-crypto-ssh-cfg:ssh" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-sam-cfg:crypto/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "client"):
                if (self.client is None):
                    self.client = Crypto.Ssh.Client()
                    self.client.parent = self
                    self._children_name_map["client"] = "client"
                return self.client

            if (child_yang_name == "server"):
                if (self.server is None):
                    self.server = Crypto.Ssh.Server()
                    self.server.parent = self
                    self._children_name_map["server"] = "server"
                return self.server

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "client" or name == "server"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.sam is not None and self.sam.has_data()) or
            (self.ssh is not None and self.ssh.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.sam is not None and self.sam.has_operation()) or
            (self.ssh is not None and self.ssh.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-sam-cfg:crypto" + path_buffer

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

        if (child_yang_name == "sam"):
            if (self.sam is None):
                self.sam = Crypto.Sam()
                self.sam.parent = self
                self._children_name_map["sam"] = "sam"
            return self.sam

        if (child_yang_name == "ssh"):
            if (self.ssh is None):
                self.ssh = Crypto.Ssh()
                self.ssh.parent = self
                self._children_name_map["ssh"] = "ssh"
            return self.ssh

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "sam" or name == "ssh"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Crypto()
        return self._top_entity


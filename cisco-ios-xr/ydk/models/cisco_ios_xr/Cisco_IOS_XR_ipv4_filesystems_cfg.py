""" Cisco_IOS_XR_ipv4_filesystems_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-filesystems package configuration.

This module contains definitions
for the following management objects\:
  rcp\: RCP configuration
  ftp\: ftp
  tftp\: tftp

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Rcp(Entity):
    """
    RCP configuration
    
    .. attribute:: rcp_client
    
    	RCP client configuration
    	**type**\:   :py:class:`RcpClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg.Rcp.RcpClient>`
    
    

    """

    _prefix = 'ipv4-filesystems-cfg'
    _revision = '2017-03-01'

    def __init__(self):
        super(Rcp, self).__init__()
        self._top_entity = None

        self.yang_name = "rcp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-filesystems-cfg"

        self.rcp_client = Rcp.RcpClient()
        self.rcp_client.parent = self
        self._children_name_map["rcp_client"] = "rcp-client"
        self._children_yang_names.add("rcp-client")


    class RcpClient(Entity):
        """
        RCP client configuration
        
        .. attribute:: source_interface
        
        	Specify interface for source address in connections
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        .. attribute:: username
        
        	Specify username for connections
        	**type**\:  str
        
        

        """

        _prefix = 'ipv4-filesystems-cfg'
        _revision = '2017-03-01'

        def __init__(self):
            super(Rcp.RcpClient, self).__init__()

            self.yang_name = "rcp-client"
            self.yang_parent_name = "rcp"

            self.source_interface = YLeaf(YType.str, "source-interface")

            self.username = YLeaf(YType.str, "username")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("source_interface",
                            "username") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Rcp.RcpClient, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rcp.RcpClient, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.source_interface.is_set or
                self.username.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.source_interface.yfilter != YFilter.not_set or
                self.username.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rcp-client" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-filesystems-cfg:rcp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source_interface.get_name_leafdata())
            if (self.username.is_set or self.username.yfilter != YFilter.not_set):
                leaf_name_data.append(self.username.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "source-interface" or name == "username"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "source-interface"):
                self.source_interface = value
                self.source_interface.value_namespace = name_space
                self.source_interface.value_namespace_prefix = name_space_prefix
            if(value_path == "username"):
                self.username = value
                self.username.value_namespace = name_space
                self.username.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.rcp_client is not None and self.rcp_client.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.rcp_client is not None and self.rcp_client.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-filesystems-cfg:rcp" + path_buffer

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

        if (child_yang_name == "rcp-client"):
            if (self.rcp_client is None):
                self.rcp_client = Rcp.RcpClient()
                self.rcp_client.parent = self
                self._children_name_map["rcp_client"] = "rcp-client"
            return self.rcp_client

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "rcp-client"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Rcp()
        return self._top_entity

class Ftp(Entity):
    """
    ftp
    
    .. attribute:: ftp_client
    
    	FTP client configuration
    	**type**\:   :py:class:`FtpClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg.Ftp.FtpClient>`
    
    

    """

    _prefix = 'ipv4-filesystems-cfg'
    _revision = '2017-03-01'

    def __init__(self):
        super(Ftp, self).__init__()
        self._top_entity = None

        self.yang_name = "ftp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-filesystems-cfg"

        self.ftp_client = Ftp.FtpClient()
        self.ftp_client.parent = self
        self._children_name_map["ftp_client"] = "ftp-client"
        self._children_yang_names.add("ftp-client")


    class FtpClient(Entity):
        """
        FTP client configuration
        
        .. attribute:: anonymous_password
        
        	Password for anonymous user (ftp server dependent)
        	**type**\:  str
        
        .. attribute:: passive
        
        	Enable connect using passive mode
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: password
        
        	Specify password for ftp connnection
        	**type**\:  str
        
        	**pattern:** (!.+)\|([^!].+)
        
        .. attribute:: source_interface
        
        	Specify interface for source address in connections
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        .. attribute:: username
        
        	Specify username for connections
        	**type**\:  str
        
        

        """

        _prefix = 'ipv4-filesystems-cfg'
        _revision = '2017-03-01'

        def __init__(self):
            super(Ftp.FtpClient, self).__init__()

            self.yang_name = "ftp-client"
            self.yang_parent_name = "ftp"

            self.anonymous_password = YLeaf(YType.str, "anonymous-password")

            self.passive = YLeaf(YType.empty, "passive")

            self.password = YLeaf(YType.str, "password")

            self.source_interface = YLeaf(YType.str, "source-interface")

            self.username = YLeaf(YType.str, "username")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("anonymous_password",
                            "passive",
                            "password",
                            "source_interface",
                            "username") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ftp.FtpClient, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ftp.FtpClient, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.anonymous_password.is_set or
                self.passive.is_set or
                self.password.is_set or
                self.source_interface.is_set or
                self.username.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.anonymous_password.yfilter != YFilter.not_set or
                self.passive.yfilter != YFilter.not_set or
                self.password.yfilter != YFilter.not_set or
                self.source_interface.yfilter != YFilter.not_set or
                self.username.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ftp-client" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-filesystems-cfg:ftp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.anonymous_password.is_set or self.anonymous_password.yfilter != YFilter.not_set):
                leaf_name_data.append(self.anonymous_password.get_name_leafdata())
            if (self.passive.is_set or self.passive.yfilter != YFilter.not_set):
                leaf_name_data.append(self.passive.get_name_leafdata())
            if (self.password.is_set or self.password.yfilter != YFilter.not_set):
                leaf_name_data.append(self.password.get_name_leafdata())
            if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source_interface.get_name_leafdata())
            if (self.username.is_set or self.username.yfilter != YFilter.not_set):
                leaf_name_data.append(self.username.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "anonymous-password" or name == "passive" or name == "password" or name == "source-interface" or name == "username"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "anonymous-password"):
                self.anonymous_password = value
                self.anonymous_password.value_namespace = name_space
                self.anonymous_password.value_namespace_prefix = name_space_prefix
            if(value_path == "passive"):
                self.passive = value
                self.passive.value_namespace = name_space
                self.passive.value_namespace_prefix = name_space_prefix
            if(value_path == "password"):
                self.password = value
                self.password.value_namespace = name_space
                self.password.value_namespace_prefix = name_space_prefix
            if(value_path == "source-interface"):
                self.source_interface = value
                self.source_interface.value_namespace = name_space
                self.source_interface.value_namespace_prefix = name_space_prefix
            if(value_path == "username"):
                self.username = value
                self.username.value_namespace = name_space
                self.username.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.ftp_client is not None and self.ftp_client.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ftp_client is not None and self.ftp_client.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-filesystems-cfg:ftp" + path_buffer

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

        if (child_yang_name == "ftp-client"):
            if (self.ftp_client is None):
                self.ftp_client = Ftp.FtpClient()
                self.ftp_client.parent = self
                self._children_name_map["ftp_client"] = "ftp-client"
            return self.ftp_client

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ftp-client"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Ftp()
        return self._top_entity

class Tftp(Entity):
    """
    tftp
    
    .. attribute:: tftp_client
    
    	TFTP client configuration
    	**type**\:   :py:class:`TftpClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg.Tftp.TftpClient>`
    
    

    """

    _prefix = 'ipv4-filesystems-cfg'
    _revision = '2017-03-01'

    def __init__(self):
        super(Tftp, self).__init__()
        self._top_entity = None

        self.yang_name = "tftp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-filesystems-cfg"

        self.tftp_client = Tftp.TftpClient()
        self.tftp_client.parent = self
        self._children_name_map["tftp_client"] = "tftp-client"
        self._children_yang_names.add("tftp-client")


    class TftpClient(Entity):
        """
        TFTP client configuration
        
        .. attribute:: source_interface
        
        	Specify interface for source address in connections
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        

        """

        _prefix = 'ipv4-filesystems-cfg'
        _revision = '2017-03-01'

        def __init__(self):
            super(Tftp.TftpClient, self).__init__()

            self.yang_name = "tftp-client"
            self.yang_parent_name = "tftp"

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
                if name in ("source_interface") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Tftp.TftpClient, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Tftp.TftpClient, self).__setattr__(name, value)

        def has_data(self):
            return self.source_interface.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.source_interface.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tftp-client" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-filesystems-cfg:tftp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
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
            if(name == "source-interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "source-interface"):
                self.source_interface = value
                self.source_interface.value_namespace = name_space
                self.source_interface.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.tftp_client is not None and self.tftp_client.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.tftp_client is not None and self.tftp_client.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-filesystems-cfg:tftp" + path_buffer

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

        if (child_yang_name == "tftp-client"):
            if (self.tftp_client is None):
                self.tftp_client = Tftp.TftpClient()
                self.tftp_client.parent = self
                self._children_name_map["tftp_client"] = "tftp-client"
            return self.tftp_client

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "tftp-client"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Tftp()
        return self._top_entity


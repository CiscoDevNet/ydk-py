""" Cisco_IOS_XR_ipv4_filesystems_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-filesystems package configuration.

This module contains definitions
for the following management objects\:
  rcp\: RCP configuration
  ftp\: ftp
  tftp\: tftp

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ftp(Entity):
    """
    ftp
    
    .. attribute:: ftp_client
    
    	FTP client configuration
    	**type**\:   :py:class:`FtpClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg.Ftp.FtpClient>`
    
    

    """

    _prefix = 'ipv4-filesystems-cfg'
    _revision = '2017-07-17'

    def __init__(self):
        super(Ftp, self).__init__()
        self._top_entity = None

        self.yang_name = "ftp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-filesystems-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"ftp-client" : ("ftp_client", Ftp.FtpClient)}
        self._child_list_classes = {}

        self.ftp_client = Ftp.FtpClient()
        self.ftp_client.parent = self
        self._children_name_map["ftp_client"] = "ftp-client"
        self._children_yang_names.add("ftp-client")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-filesystems-cfg:ftp"


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
        
        	**pattern:** [a\-zA\-Z0\-9./\-]+
        
        .. attribute:: username
        
        	Specify username for connections
        	**type**\:  str
        
        

        """

        _prefix = 'ipv4-filesystems-cfg'
        _revision = '2017-07-17'

        def __init__(self):
            super(Ftp.FtpClient, self).__init__()

            self.yang_name = "ftp-client"
            self.yang_parent_name = "ftp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.anonymous_password = YLeaf(YType.str, "anonymous-password")

            self.passive = YLeaf(YType.empty, "passive")

            self.password = YLeaf(YType.str, "password")

            self.source_interface = YLeaf(YType.str, "source-interface")

            self.username = YLeaf(YType.str, "username")
            self._segment_path = lambda: "ftp-client"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-filesystems-cfg:ftp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ftp.FtpClient, ['anonymous_password', 'passive', 'password', 'source_interface', 'username'], name, value)

    def clone_ptr(self):
        self._top_entity = Ftp()
        return self._top_entity

class Rcp(Entity):
    """
    RCP configuration
    
    .. attribute:: rcp_client
    
    	RCP client configuration
    	**type**\:   :py:class:`RcpClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg.Rcp.RcpClient>`
    
    

    """

    _prefix = 'ipv4-filesystems-cfg'
    _revision = '2017-07-17'

    def __init__(self):
        super(Rcp, self).__init__()
        self._top_entity = None

        self.yang_name = "rcp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-filesystems-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"rcp-client" : ("rcp_client", Rcp.RcpClient)}
        self._child_list_classes = {}

        self.rcp_client = Rcp.RcpClient()
        self.rcp_client.parent = self
        self._children_name_map["rcp_client"] = "rcp-client"
        self._children_yang_names.add("rcp-client")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-filesystems-cfg:rcp"


    class RcpClient(Entity):
        """
        RCP client configuration
        
        .. attribute:: source_interface
        
        	Specify interface for source address in connections
        	**type**\:  str
        
        	**pattern:** [a\-zA\-Z0\-9./\-]+
        
        .. attribute:: username
        
        	Specify username for connections
        	**type**\:  str
        
        

        """

        _prefix = 'ipv4-filesystems-cfg'
        _revision = '2017-07-17'

        def __init__(self):
            super(Rcp.RcpClient, self).__init__()

            self.yang_name = "rcp-client"
            self.yang_parent_name = "rcp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.source_interface = YLeaf(YType.str, "source-interface")

            self.username = YLeaf(YType.str, "username")
            self._segment_path = lambda: "rcp-client"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-filesystems-cfg:rcp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Rcp.RcpClient, ['source_interface', 'username'], name, value)

    def clone_ptr(self):
        self._top_entity = Rcp()
        return self._top_entity

class Tftp(Entity):
    """
    tftp
    
    .. attribute:: tftp_client
    
    	TFTP client configuration
    	**type**\:   :py:class:`TftpClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg.Tftp.TftpClient>`
    
    

    """

    _prefix = 'ipv4-filesystems-cfg'
    _revision = '2017-07-17'

    def __init__(self):
        super(Tftp, self).__init__()
        self._top_entity = None

        self.yang_name = "tftp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-filesystems-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"tftp-client" : ("tftp_client", Tftp.TftpClient)}
        self._child_list_classes = {}

        self.tftp_client = Tftp.TftpClient()
        self.tftp_client.parent = self
        self._children_name_map["tftp_client"] = "tftp-client"
        self._children_yang_names.add("tftp-client")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-filesystems-cfg:tftp"


    class TftpClient(Entity):
        """
        TFTP client configuration
        
        .. attribute:: retry
        
        	Specify the number of retries when client requests TFTP connections
        	**type**\:  int
        
        	**range:** 0..256
        
        .. attribute:: source_interface
        
        	Specify interface for source address in connections
        	**type**\:  str
        
        	**pattern:** [a\-zA\-Z0\-9./\-]+
        
        .. attribute:: timeout
        
        	Specify the timeout for every TFTP connection in seconds
        	**type**\:  int
        
        	**range:** 0..256
        
        	**units**\: second
        
        .. attribute:: vrfs
        
        	VRF table
        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg.Tftp.TftpClient.Vrfs>`
        
        

        """

        _prefix = 'ipv4-filesystems-cfg'
        _revision = '2017-07-17'

        def __init__(self):
            super(Tftp.TftpClient, self).__init__()

            self.yang_name = "tftp-client"
            self.yang_parent_name = "tftp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"vrfs" : ("vrfs", Tftp.TftpClient.Vrfs)}
            self._child_list_classes = {}

            self.retry = YLeaf(YType.uint32, "retry")

            self.source_interface = YLeaf(YType.str, "source-interface")

            self.timeout = YLeaf(YType.uint32, "timeout")

            self.vrfs = Tftp.TftpClient.Vrfs()
            self.vrfs.parent = self
            self._children_name_map["vrfs"] = "vrfs"
            self._children_yang_names.add("vrfs")
            self._segment_path = lambda: "tftp-client"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-filesystems-cfg:tftp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Tftp.TftpClient, ['retry', 'source_interface', 'timeout'], name, value)


        class Vrfs(Entity):
            """
            VRF table
            
            .. attribute:: vrf
            
            	VRF specific data
            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg.Tftp.TftpClient.Vrfs.Vrf>`
            
            

            """

            _prefix = 'ipv4-filesystems-cfg'
            _revision = '2017-07-17'

            def __init__(self):
                super(Tftp.TftpClient.Vrfs, self).__init__()

                self.yang_name = "vrfs"
                self.yang_parent_name = "tftp-client"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"vrf" : ("vrf", Tftp.TftpClient.Vrfs.Vrf)}

                self.vrf = YList(self)
                self._segment_path = lambda: "vrfs"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-filesystems-cfg:tftp/tftp-client/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Tftp.TftpClient.Vrfs, [], name, value)


            class Vrf(Entity):
                """
                VRF specific data
                
                .. attribute:: vrf_name  <key>
                
                	Name of the VRF instance
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: retry
                
                	Specify the number of retries when client requests TFTP connections
                	**type**\:  int
                
                	**range:** 0..256
                
                .. attribute:: source_interface
                
                	Specify interface for source address in connections
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: timeout
                
                	Specify the timeout for every TFTP connection in seconds
                	**type**\:  int
                
                	**range:** 0..256
                
                	**units**\: second
                
                

                """

                _prefix = 'ipv4-filesystems-cfg'
                _revision = '2017-07-17'

                def __init__(self):
                    super(Tftp.TftpClient.Vrfs.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrfs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.retry = YLeaf(YType.uint32, "retry")

                    self.source_interface = YLeaf(YType.str, "source-interface")

                    self.timeout = YLeaf(YType.uint32, "timeout")
                    self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-filesystems-cfg:tftp/tftp-client/vrfs/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Tftp.TftpClient.Vrfs.Vrf, ['vrf_name', 'retry', 'source_interface', 'timeout'], name, value)

    def clone_ptr(self):
        self._top_entity = Tftp()
        return self._top_entity


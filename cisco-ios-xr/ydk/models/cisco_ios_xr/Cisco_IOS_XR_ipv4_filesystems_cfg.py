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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Rcp(object):
    """
    RCP configuration
    
    .. attribute:: rcp_client
    
    	RCP client configuration
    	**type**\:   :py:class:`RcpClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg.Rcp.RcpClient>`
    
    

    """

    _prefix = 'ipv4-filesystems-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.rcp_client = Rcp.RcpClient()
        self.rcp_client.parent = self


    class RcpClient(object):
        """
        RCP client configuration
        
        .. attribute:: source_interface
        
        	Specify interface for source address in connections
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        

        """

        _prefix = 'ipv4-filesystems-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.source_interface = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-filesystems-cfg:rcp/Cisco-IOS-XR-ipv4-filesystems-cfg:rcp-client'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.source_interface is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_filesystems_cfg as meta
            return meta._meta_table['Rcp.RcpClient']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-filesystems-cfg:rcp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.rcp_client is not None and self.rcp_client._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_filesystems_cfg as meta
        return meta._meta_table['Rcp']['meta_info']


class Ftp(object):
    """
    ftp
    
    .. attribute:: ftp_client
    
    	FTP client configuration
    	**type**\:   :py:class:`FtpClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg.Ftp.FtpClient>`
    
    

    """

    _prefix = 'ipv4-filesystems-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.ftp_client = Ftp.FtpClient()
        self.ftp_client.parent = self


    class FtpClient(object):
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
        
        

        """

        _prefix = 'ipv4-filesystems-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.anonymous_password = None
            self.passive = None
            self.password = None
            self.source_interface = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-filesystems-cfg:ftp/Cisco-IOS-XR-ipv4-filesystems-cfg:ftp-client'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.anonymous_password is not None:
                return True

            if self.passive is not None:
                return True

            if self.password is not None:
                return True

            if self.source_interface is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_filesystems_cfg as meta
            return meta._meta_table['Ftp.FtpClient']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-filesystems-cfg:ftp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.ftp_client is not None and self.ftp_client._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_filesystems_cfg as meta
        return meta._meta_table['Ftp']['meta_info']


class Tftp(object):
    """
    tftp
    
    .. attribute:: tftp_client
    
    	TFTP client configuration
    	**type**\:   :py:class:`TftpClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg.Tftp.TftpClient>`
    
    

    """

    _prefix = 'ipv4-filesystems-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.tftp_client = Tftp.TftpClient()
        self.tftp_client.parent = self


    class TftpClient(object):
        """
        TFTP client configuration
        
        .. attribute:: source_interface
        
        	Specify interface for source address in connections
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        

        """

        _prefix = 'ipv4-filesystems-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.source_interface = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-filesystems-cfg:tftp/Cisco-IOS-XR-ipv4-filesystems-cfg:tftp-client'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.source_interface is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_filesystems_cfg as meta
            return meta._meta_table['Tftp.TftpClient']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-filesystems-cfg:tftp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.tftp_client is not None and self.tftp_client._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_filesystems_cfg as meta
        return meta._meta_table['Tftp']['meta_info']



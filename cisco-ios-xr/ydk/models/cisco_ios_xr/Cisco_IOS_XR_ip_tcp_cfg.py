""" Cisco_IOS_XR_ip_tcp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-tcp package configuration.

This module contains definitions
for the following management objects\:
  ip\-tcp\: Global IP TCP configuration
  ip\: ip

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class IpTcp(object):
    """
    Global IP TCP configuration
    
    .. attribute:: accept_rate
    
    	TCP connection accept rate
    	**type**\:  int
    
    	**range:** 1..1000
    
    	**default value**\: 500
    
    .. attribute:: directory
    
    	TCP directory details
    	**type**\:   :py:class:`Directory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.IpTcp.Directory>`
    
    	**presence node**\: True
    
    .. attribute:: maximum_segment_size
    
    	TCP initial maximum segment size
    	**type**\:  int
    
    	**range:** 68..10000
    
    .. attribute:: num_thread
    
    	TCP InQueue and OutQueue threads
    	**type**\:   :py:class:`NumThread <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.IpTcp.NumThread>`
    
    	**presence node**\: True
    
    .. attribute:: path_mtu_discovery
    
    	Aging time; 0 for infinite, and range be (10,30)
    	**type**\:  int
    
    	**range:** \-2147483648..2147483647
    
    	**units**\: minute
    
    	**default value**\: 10
    
    .. attribute:: receive_q
    
    	TCP receive Queue Size
    	**type**\:  int
    
    	**range:** 40..800
    
    .. attribute:: selective_ack
    
    	Enable TCP selective\-ACK
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: syn_wait_time
    
    	Time to wait on new TCP connections in seconds
    	**type**\:  int
    
    	**range:** 5..30
    
    	**units**\: second
    
    .. attribute:: throttle
    
    	Throttle TCP receive buffer (in percentage)
    	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.IpTcp.Throttle>`
    
    	**presence node**\: True
    
    .. attribute:: timestamp
    
    	Enable TCP timestamp option
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: window_size
    
    	TCP receive window size (bytes)
    	**type**\:  int
    
    	**range:** 2048..65535
    
    	**units**\: byte
    
    

    """

    _prefix = 'ip-tcp-cfg'
    _revision = '2016-02-26'

    def __init__(self):
        self.accept_rate = None
        self.directory = None
        self.maximum_segment_size = None
        self.num_thread = None
        self.path_mtu_discovery = None
        self.receive_q = None
        self.selective_ack = None
        self.syn_wait_time = None
        self.throttle = None
        self.timestamp = None
        self.window_size = None


    class Directory(object):
        """
        TCP directory details
        
        .. attribute:: directoryname
        
        	Directory name 
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: max_debug_files
        
        	Set number of Debug files
        	**type**\:  int
        
        	**range:** 1..10000
        
        	**mandatory**\: True
        
        .. attribute:: max_file_size_files
        
        	Set size of debug files in bytes
        	**type**\:  int
        
        	**range:** 1024..4294967295
        
        	**mandatory**\: True
        
        	**units**\: byte
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-tcp-cfg'
        _revision = '2016-02-26'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.directoryname = None
            self.max_debug_files = None
            self.max_file_size_files = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-tcp-cfg:ip-tcp/Cisco-IOS-XR-ip-tcp-cfg:directory'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.directoryname is not None:
                return True

            if self.max_debug_files is not None:
                return True

            if self.max_file_size_files is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
            return meta._meta_table['IpTcp.Directory']['meta_info']


    class Throttle(object):
        """
        Throttle TCP receive buffer (in percentage)
        
        .. attribute:: tcpmaxthrottle
        
        	Max throttle
        	**type**\:  int
        
        	**range:** 0..100
        
        	**mandatory**\: True
        
        .. attribute:: tcpmin_throttle
        
        	Min throttle
        	**type**\:  int
        
        	**range:** 0..100
        
        	**mandatory**\: True
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-tcp-cfg'
        _revision = '2016-02-26'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.tcpmaxthrottle = None
            self.tcpmin_throttle = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-tcp-cfg:ip-tcp/Cisco-IOS-XR-ip-tcp-cfg:throttle'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.tcpmaxthrottle is not None:
                return True

            if self.tcpmin_throttle is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
            return meta._meta_table['IpTcp.Throttle']['meta_info']


    class NumThread(object):
        """
        TCP InQueue and OutQueue threads
        
        .. attribute:: tcp_in_q_threads
        
        	InQ Threads
        	**type**\:  int
        
        	**range:** 1..16
        
        	**mandatory**\: True
        
        .. attribute:: tcp_out_q_threads
        
        	OutQ Threads
        	**type**\:  int
        
        	**range:** 1..16
        
        	**mandatory**\: True
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-tcp-cfg'
        _revision = '2016-02-26'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.tcp_in_q_threads = None
            self.tcp_out_q_threads = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-tcp-cfg:ip-tcp/Cisco-IOS-XR-ip-tcp-cfg:num-thread'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.tcp_in_q_threads is not None:
                return True

            if self.tcp_out_q_threads is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
            return meta._meta_table['IpTcp.NumThread']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-tcp-cfg:ip-tcp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.accept_rate is not None:
            return True

        if self.directory is not None and self.directory._has_data():
            return True

        if self.maximum_segment_size is not None:
            return True

        if self.num_thread is not None and self.num_thread._has_data():
            return True

        if self.path_mtu_discovery is not None:
            return True

        if self.receive_q is not None:
            return True

        if self.selective_ack is not None:
            return True

        if self.syn_wait_time is not None:
            return True

        if self.throttle is not None and self.throttle._has_data():
            return True

        if self.timestamp is not None:
            return True

        if self.window_size is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
        return meta._meta_table['IpTcp']['meta_info']


class Ip(object):
    """
    ip
    
    .. attribute:: cinetd
    
    	Cinetd configuration data
    	**type**\:   :py:class:`Cinetd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd>`
    
    .. attribute:: forward_protocol
    
    	Controls forwarding of physical and directed IP broadcasts
    	**type**\:   :py:class:`ForwardProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.ForwardProtocol>`
    
    

    """

    _prefix = 'ip-tcp-cfg'
    _revision = '2016-02-26'

    def __init__(self):
        self.cinetd = Ip.Cinetd()
        self.cinetd.parent = self
        self.forward_protocol = Ip.ForwardProtocol()
        self.forward_protocol.parent = self


    class Cinetd(object):
        """
        Cinetd configuration data
        
        .. attribute:: services
        
        	Describing services of cinetd
        	**type**\:   :py:class:`Services <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services>`
        
        

        """

        _prefix = 'ip-tcp-cfg'
        _revision = '2016-02-26'

        def __init__(self):
            self.parent = None
            self.services = Ip.Cinetd.Services()
            self.services.parent = self


        class Services(object):
            """
            Describing services of cinetd
            
            .. attribute:: ipv4
            
            	IPV4 related services
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv4>`
            
            .. attribute:: ipv6
            
            	IPV6 related services
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv6>`
            
            .. attribute:: vrfs
            
            	VRF table
            	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs>`
            
            

            """

            _prefix = 'ip-tcp-cfg'
            _revision = '2016-02-26'

            def __init__(self):
                self.parent = None
                self.ipv4 = Ip.Cinetd.Services.Ipv4()
                self.ipv4.parent = self
                self.ipv6 = Ip.Cinetd.Services.Ipv6()
                self.ipv6.parent = self
                self.vrfs = Ip.Cinetd.Services.Vrfs()
                self.vrfs.parent = self


            class Ipv4(object):
                """
                IPV4 related services
                
                .. attribute:: small_servers
                
                	Describing IPV4 and IPV6 small servers
                	**type**\:   :py:class:`SmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv4.SmallServers>`
                
                

                """

                _prefix = 'ip-tcp-cfg'
                _revision = '2016-02-26'

                def __init__(self):
                    self.parent = None
                    self.small_servers = Ip.Cinetd.Services.Ipv4.SmallServers()
                    self.small_servers.parent = self


                class SmallServers(object):
                    """
                    Describing IPV4 and IPV6 small servers
                    
                    .. attribute:: tcp_small_servers
                    
                    	Describing TCP related IPV4 and IPV6 small servers
                    	**type**\:   :py:class:`TcpSmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: udp_small_servers
                    
                    	UDP small servers configuration
                    	**type**\:   :py:class:`UdpSmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ip-tcp-cfg'
                    _revision = '2016-02-26'

                    def __init__(self):
                        self.parent = None
                        self.tcp_small_servers = None
                        self.udp_small_servers = None


                    class TcpSmallServers(object):
                        """
                        Describing TCP related IPV4 and IPV6 small
                        servers
                        
                        .. attribute:: access_control_list_name
                        
                        	Access list
                        	**type**\:  str
                        
                        .. attribute:: small_server
                        
                        	Set number of allowable TCP small servers, specify 0 for no\-limit
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**mandatory**\: True
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ip-tcp-cfg'
                        _revision = '2016-02-26'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.access_control_list_name = None
                            self.small_server = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-tcp-cfg:cinetd/Cisco-IOS-XR-ip-tcp-cfg:services/Cisco-IOS-XR-ip-tcp-cfg:ipv4/Cisco-IOS-XR-ip-tcp-cfg:small-servers/Cisco-IOS-XR-ip-tcp-cfg:tcp-small-servers'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.access_control_list_name is not None:
                                return True

                            if self.small_server is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                            return meta._meta_table['Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers']['meta_info']


                    class UdpSmallServers(object):
                        """
                        UDP small servers configuration
                        
                        .. attribute:: access_control_list_name
                        
                        	Specify the access list
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: small_server
                        
                        	Set number of allowable small servers, specify 0 for no\-limit
                        	**type**\:  int
                        
                        	**range:** 0..2147483647
                        
                        	**mandatory**\: True
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ip-udp-cfg'
                        _revision = '2016-02-26'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.access_control_list_name = None
                            self.small_server = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-tcp-cfg:cinetd/Cisco-IOS-XR-ip-tcp-cfg:services/Cisco-IOS-XR-ip-tcp-cfg:ipv4/Cisco-IOS-XR-ip-tcp-cfg:small-servers/Cisco-IOS-XR-ip-udp-cfg:udp-small-servers'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.access_control_list_name is not None:
                                return True

                            if self.small_server is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                            return meta._meta_table['Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-tcp-cfg:cinetd/Cisco-IOS-XR-ip-tcp-cfg:services/Cisco-IOS-XR-ip-tcp-cfg:ipv4/Cisco-IOS-XR-ip-tcp-cfg:small-servers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.tcp_small_servers is not None and self.tcp_small_servers._has_data():
                            return True

                        if self.udp_small_servers is not None and self.udp_small_servers._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                        return meta._meta_table['Ip.Cinetd.Services.Ipv4.SmallServers']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-tcp-cfg:cinetd/Cisco-IOS-XR-ip-tcp-cfg:services/Cisco-IOS-XR-ip-tcp-cfg:ipv4'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.small_servers is not None and self.small_servers._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                    return meta._meta_table['Ip.Cinetd.Services.Ipv4']['meta_info']


            class Vrfs(object):
                """
                VRF table
                
                .. attribute:: vrf
                
                	VRF specific data
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf>`
                
                

                """

                _prefix = 'ip-tcp-cfg'
                _revision = '2016-02-26'

                def __init__(self):
                    self.parent = None
                    self.vrf = YList()
                    self.vrf.parent = self
                    self.vrf.name = 'vrf'


                class Vrf(object):
                    """
                    VRF specific data
                    
                    .. attribute:: vrf_name  <key>
                    
                    	Name of the VRF instance
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: ipv4
                    
                    	IPV4 related services
                    	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv4>`
                    
                    .. attribute:: ipv6
                    
                    	IPV6 related services
                    	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv6>`
                    
                    

                    """

                    _prefix = 'ip-tcp-cfg'
                    _revision = '2016-02-26'

                    def __init__(self):
                        self.parent = None
                        self.vrf_name = None
                        self.ipv4 = Ip.Cinetd.Services.Vrfs.Vrf.Ipv4()
                        self.ipv4.parent = self
                        self.ipv6 = Ip.Cinetd.Services.Vrfs.Vrf.Ipv6()
                        self.ipv6.parent = self


                    class Ipv6(object):
                        """
                        IPV6 related services
                        
                        .. attribute:: telnet
                        
                        	TELNET server configuration commands
                        	**type**\:   :py:class:`Telnet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet>`
                        
                        .. attribute:: tftp
                        
                        	TFTP server configuration commands
                        	**type**\:   :py:class:`Tftp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp>`
                        
                        

                        """

                        _prefix = 'ip-tcp-cfg'
                        _revision = '2016-02-26'

                        def __init__(self):
                            self.parent = None
                            self.telnet = Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet()
                            self.telnet.parent = self
                            self.tftp = Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp()
                            self.tftp.parent = self


                        class Telnet(object):
                            """
                            TELNET server configuration commands
                            
                            .. attribute:: tcp
                            
                            	TCP details
                            	**type**\:   :py:class:`Tcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp>`
                            
                            	**presence node**\: True
                            
                            

                            """

                            _prefix = 'ip-tcp-cfg'
                            _revision = '2016-02-26'

                            def __init__(self):
                                self.parent = None
                                self.tcp = None


                            class Tcp(object):
                                """
                                TCP details
                                
                                .. attribute:: access_list_name
                                
                                	Access list
                                	**type**\:  str
                                
                                .. attribute:: maximum_server
                                
                                	Set number of allowable servers
                                	**type**\:  int
                                
                                	**range:** 1..100
                                
                                	**mandatory**\: True
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ip-tcp-cfg'
                                _revision = '2016-02-26'

                                def __init__(self):
                                    self.parent = None
                                    self._is_presence = True
                                    self.access_list_name = None
                                    self.maximum_server = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-cfg:tcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self._is_presence:
                                        return True
                                    if self.access_list_name is not None:
                                        return True

                                    if self.maximum_server is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                                    return meta._meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-cfg:telnet'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.tcp is not None and self.tcp._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                                return meta._meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet']['meta_info']


                        class Tftp(object):
                            """
                            TFTP server configuration commands
                            
                            .. attribute:: udp
                            
                            	UDP details
                            	**type**\:   :py:class:`Udp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp>`
                            
                            	**presence node**\: True
                            
                            

                            """

                            _prefix = 'ip-tcp-cfg'
                            _revision = '2016-02-26'

                            def __init__(self):
                                self.parent = None
                                self.udp = None


                            class Udp(object):
                                """
                                UDP details
                                
                                .. attribute:: access_list_name
                                
                                	Access list
                                	**type**\:  str
                                
                                .. attribute:: dscp_value
                                
                                	Set IP DSCP (DiffServ CodePoint) for TFTP Server Packets
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: home_directory
                                
                                	Specify device name where file is read from (e .g. flash\:)
                                	**type**\:  str
                                
                                	**mandatory**\: True
                                
                                .. attribute:: maximum_server
                                
                                	Set number of allowable servers, 0 for no\-limit
                                	**type**\:  int
                                
                                	**range:** 0..2147483647
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ip-tcp-cfg'
                                _revision = '2016-02-26'

                                def __init__(self):
                                    self.parent = None
                                    self._is_presence = True
                                    self.access_list_name = None
                                    self.dscp_value = None
                                    self.home_directory = None
                                    self.maximum_server = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-cfg:udp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self._is_presence:
                                        return True
                                    if self.access_list_name is not None:
                                        return True

                                    if self.dscp_value is not None:
                                        return True

                                    if self.home_directory is not None:
                                        return True

                                    if self.maximum_server is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                                    return meta._meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-cfg:tftp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.udp is not None and self.udp._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                                return meta._meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-cfg:ipv6'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.telnet is not None and self.telnet._has_data():
                                return True

                            if self.tftp is not None and self.tftp._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                            return meta._meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6']['meta_info']


                    class Ipv4(object):
                        """
                        IPV4 related services
                        
                        .. attribute:: telnet
                        
                        	TELNET server configuration commands
                        	**type**\:   :py:class:`Telnet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet>`
                        
                        .. attribute:: tftp
                        
                        	TFTP server configuration commands
                        	**type**\:   :py:class:`Tftp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp>`
                        
                        

                        """

                        _prefix = 'ip-tcp-cfg'
                        _revision = '2016-02-26'

                        def __init__(self):
                            self.parent = None
                            self.telnet = Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet()
                            self.telnet.parent = self
                            self.tftp = Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp()
                            self.tftp.parent = self


                        class Telnet(object):
                            """
                            TELNET server configuration commands
                            
                            .. attribute:: tcp
                            
                            	TCP details
                            	**type**\:   :py:class:`Tcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp>`
                            
                            	**presence node**\: True
                            
                            

                            """

                            _prefix = 'ip-tcp-cfg'
                            _revision = '2016-02-26'

                            def __init__(self):
                                self.parent = None
                                self.tcp = None


                            class Tcp(object):
                                """
                                TCP details
                                
                                .. attribute:: access_list_name
                                
                                	Access list
                                	**type**\:  str
                                
                                .. attribute:: maximum_server
                                
                                	Set number of allowable servers
                                	**type**\:  int
                                
                                	**range:** 1..100
                                
                                	**mandatory**\: True
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ip-tcp-cfg'
                                _revision = '2016-02-26'

                                def __init__(self):
                                    self.parent = None
                                    self._is_presence = True
                                    self.access_list_name = None
                                    self.maximum_server = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-cfg:tcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self._is_presence:
                                        return True
                                    if self.access_list_name is not None:
                                        return True

                                    if self.maximum_server is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                                    return meta._meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-cfg:telnet'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.tcp is not None and self.tcp._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                                return meta._meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet']['meta_info']


                        class Tftp(object):
                            """
                            TFTP server configuration commands
                            
                            .. attribute:: udp
                            
                            	UDP details
                            	**type**\:   :py:class:`Udp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp>`
                            
                            	**presence node**\: True
                            
                            

                            """

                            _prefix = 'ip-tcp-cfg'
                            _revision = '2016-02-26'

                            def __init__(self):
                                self.parent = None
                                self.udp = None


                            class Udp(object):
                                """
                                UDP details
                                
                                .. attribute:: access_list_name
                                
                                	Access list
                                	**type**\:  str
                                
                                .. attribute:: dscp_value
                                
                                	Set IP DSCP (DiffServ CodePoint) for TFTP Server Packets
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: home_directory
                                
                                	Specify device name where file is read from (e .g. flash\:)
                                	**type**\:  str
                                
                                	**mandatory**\: True
                                
                                .. attribute:: maximum_server
                                
                                	Set number of allowable servers, 0 for no\-limit
                                	**type**\:  int
                                
                                	**range:** 0..2147483647
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ip-tcp-cfg'
                                _revision = '2016-02-26'

                                def __init__(self):
                                    self.parent = None
                                    self._is_presence = True
                                    self.access_list_name = None
                                    self.dscp_value = None
                                    self.home_directory = None
                                    self.maximum_server = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-cfg:udp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self._is_presence:
                                        return True
                                    if self.access_list_name is not None:
                                        return True

                                    if self.dscp_value is not None:
                                        return True

                                    if self.home_directory is not None:
                                        return True

                                    if self.maximum_server is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                                    return meta._meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-cfg:tftp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.udp is not None and self.udp._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                                return meta._meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-cfg:ipv4'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.telnet is not None and self.telnet._has_data():
                                return True

                            if self.tftp is not None and self.tftp._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                            return meta._meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4']['meta_info']

                    @property
                    def _common_path(self):
                        if self.vrf_name is None:
                            raise YPYModelError('Key property vrf_name is None')

                        return '/Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-tcp-cfg:cinetd/Cisco-IOS-XR-ip-tcp-cfg:services/Cisco-IOS-XR-ip-tcp-cfg:vrfs/Cisco-IOS-XR-ip-tcp-cfg:vrf[Cisco-IOS-XR-ip-tcp-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.vrf_name is not None:
                            return True

                        if self.ipv4 is not None and self.ipv4._has_data():
                            return True

                        if self.ipv6 is not None and self.ipv6._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                        return meta._meta_table['Ip.Cinetd.Services.Vrfs.Vrf']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-tcp-cfg:cinetd/Cisco-IOS-XR-ip-tcp-cfg:services/Cisco-IOS-XR-ip-tcp-cfg:vrfs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vrf is not None:
                        for child_ref in self.vrf:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                    return meta._meta_table['Ip.Cinetd.Services.Vrfs']['meta_info']


            class Ipv6(object):
                """
                IPV6 related services
                
                .. attribute:: small_servers
                
                	Describing IPV4 and IPV6 small servers
                	**type**\:   :py:class:`SmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv6.SmallServers>`
                
                

                """

                _prefix = 'ip-tcp-cfg'
                _revision = '2016-02-26'

                def __init__(self):
                    self.parent = None
                    self.small_servers = Ip.Cinetd.Services.Ipv6.SmallServers()
                    self.small_servers.parent = self


                class SmallServers(object):
                    """
                    Describing IPV4 and IPV6 small servers
                    
                    .. attribute:: tcp_small_servers
                    
                    	Describing TCP related IPV4 and IPV6 small servers
                    	**type**\:   :py:class:`TcpSmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ip-tcp-cfg'
                    _revision = '2016-02-26'

                    def __init__(self):
                        self.parent = None
                        self.tcp_small_servers = None


                    class TcpSmallServers(object):
                        """
                        Describing TCP related IPV4 and IPV6 small
                        servers
                        
                        .. attribute:: access_control_list_name
                        
                        	Access list
                        	**type**\:  str
                        
                        .. attribute:: small_server
                        
                        	Set number of allowable TCP small servers, specify 0 for no\-limit
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**mandatory**\: True
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ip-tcp-cfg'
                        _revision = '2016-02-26'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.access_control_list_name = None
                            self.small_server = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-tcp-cfg:cinetd/Cisco-IOS-XR-ip-tcp-cfg:services/Cisco-IOS-XR-ip-tcp-cfg:ipv6/Cisco-IOS-XR-ip-tcp-cfg:small-servers/Cisco-IOS-XR-ip-tcp-cfg:tcp-small-servers'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.access_control_list_name is not None:
                                return True

                            if self.small_server is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                            return meta._meta_table['Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-tcp-cfg:cinetd/Cisco-IOS-XR-ip-tcp-cfg:services/Cisco-IOS-XR-ip-tcp-cfg:ipv6/Cisco-IOS-XR-ip-tcp-cfg:small-servers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.tcp_small_servers is not None and self.tcp_small_servers._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                        return meta._meta_table['Ip.Cinetd.Services.Ipv6.SmallServers']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-tcp-cfg:cinetd/Cisco-IOS-XR-ip-tcp-cfg:services/Cisco-IOS-XR-ip-tcp-cfg:ipv6'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.small_servers is not None and self.small_servers._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                    return meta._meta_table['Ip.Cinetd.Services.Ipv6']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-tcp-cfg:cinetd/Cisco-IOS-XR-ip-tcp-cfg:services'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ipv4 is not None and self.ipv4._has_data():
                    return True

                if self.ipv6 is not None and self.ipv6._has_data():
                    return True

                if self.vrfs is not None and self.vrfs._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                return meta._meta_table['Ip.Cinetd.Services']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-tcp-cfg:cinetd'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.services is not None and self.services._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
            return meta._meta_table['Ip.Cinetd']['meta_info']


    class ForwardProtocol(object):
        """
        Controls forwarding of physical and directed IP
        broadcasts
        
        .. attribute:: udp
        
        	Packets to a specific UDP port
        	**type**\:   :py:class:`Udp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.ForwardProtocol.Udp>`
        
        

        """

        _prefix = 'ip-udp-cfg'
        _revision = '2016-02-26'

        def __init__(self):
            self.parent = None
            self.udp = Ip.ForwardProtocol.Udp()
            self.udp.parent = self


        class Udp(object):
            """
            Packets to a specific UDP port
            
            .. attribute:: disable
            
            	Disable IP Forward Protocol UDP
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: ports
            
            	Port configuration
            	**type**\:   :py:class:`Ports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.ForwardProtocol.Udp.Ports>`
            
            

            """

            _prefix = 'ip-udp-cfg'
            _revision = '2016-02-26'

            def __init__(self):
                self.parent = None
                self.disable = None
                self.ports = Ip.ForwardProtocol.Udp.Ports()
                self.ports.parent = self


            class Ports(object):
                """
                Port configuration
                
                .. attribute:: port
                
                	Well\-known ports are enabled by default and non well\-known ports are disabled by default. It is not allowed to configure the default
                	**type**\: list of    :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.ForwardProtocol.Udp.Ports.Port>`
                
                

                """

                _prefix = 'ip-udp-cfg'
                _revision = '2016-02-26'

                def __init__(self):
                    self.parent = None
                    self.port = YList()
                    self.port.parent = self
                    self.port.name = 'port'


                class Port(object):
                    """
                    Well\-known ports are enabled by default and
                    non well\-known ports are disabled by default.
                    It is not allowed to configure the default.
                    
                    .. attribute:: port_id  <key>
                    
                    	Port number
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: enable
                    
                    	Specify 'false' to disable well\-known ports Domain (53), TFTP (69), NameServer (42), TACACS (49), NetBiosNameService (137), or NetBiosDatagramService (138).  Specify 'true' to enable non well\-known ports
                    	**type**\:  bool
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ip-udp-cfg'
                    _revision = '2016-02-26'

                    def __init__(self):
                        self.parent = None
                        self.port_id = None
                        self.enable = None

                    @property
                    def _common_path(self):
                        if self.port_id is None:
                            raise YPYModelError('Key property port_id is None')

                        return '/Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-udp-cfg:forward-protocol/Cisco-IOS-XR-ip-udp-cfg:udp/Cisco-IOS-XR-ip-udp-cfg:ports/Cisco-IOS-XR-ip-udp-cfg:port[Cisco-IOS-XR-ip-udp-cfg:port-id = ' + str(self.port_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.port_id is not None:
                            return True

                        if self.enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                        return meta._meta_table['Ip.ForwardProtocol.Udp.Ports.Port']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-udp-cfg:forward-protocol/Cisco-IOS-XR-ip-udp-cfg:udp/Cisco-IOS-XR-ip-udp-cfg:ports'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.port is not None:
                        for child_ref in self.port:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                    return meta._meta_table['Ip.ForwardProtocol.Udp.Ports']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-udp-cfg:forward-protocol/Cisco-IOS-XR-ip-udp-cfg:udp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.disable is not None:
                    return True

                if self.ports is not None and self.ports._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
                return meta._meta_table['Ip.ForwardProtocol.Udp']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-udp-cfg:forward-protocol'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.udp is not None and self.udp._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
            return meta._meta_table['Ip.ForwardProtocol']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-tcp-cfg:ip'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.cinetd is not None and self.cinetd._has_data():
            return True

        if self.forward_protocol is not None and self.forward_protocol._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_tcp_cfg as meta
        return meta._meta_table['Ip']['meta_info']



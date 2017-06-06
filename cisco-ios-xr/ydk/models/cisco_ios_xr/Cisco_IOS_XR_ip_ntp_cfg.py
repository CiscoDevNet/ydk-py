""" Cisco_IOS_XR_ip_ntp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-ntp package configuration.

This module contains definitions
for the following management objects\:
  ntp\: NTP configuration

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class NtpAccessAfEnum(Enum):
    """
    NtpAccessAfEnum

    Ntp access af

    .. data:: ipv4 = 0

    	IPv4

    .. data:: ipv6 = 1

    	IPv6

    """

    ipv4 = 0

    ipv6 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
        return meta._meta_table['NtpAccessAfEnum']


class NtpAccessEnum(Enum):
    """
    NtpAccessEnum

    Ntp access

    .. data:: peer = 0

    	Peer

    .. data:: serve = 1

    	Serve

    .. data:: serve_only = 2

    	Serve Only

    .. data:: query_only = 3

    	Query Only

    """

    peer = 0

    serve = 1

    serve_only = 2

    query_only = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
        return meta._meta_table['NtpAccessEnum']


class NtpPeerEnum(Enum):
    """
    NtpPeerEnum

    Ntp peer

    .. data:: peer = 0

    	Peer

    .. data:: server = 1

    	Server

    """

    peer = 0

    server = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
        return meta._meta_table['NtpPeerEnum']


class NtpdscpEnum(Enum):
    """
    NtpdscpEnum

    Ntpdscp

    .. data:: ntp_precedence = 0

    	Precedence Value

    .. data:: ntpdscp = 1

    	DSCP Value

    """

    ntp_precedence = 0

    ntpdscp = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
        return meta._meta_table['NtpdscpEnum']



class Ntp(object):
    """
    NTP configuration
    
    .. attribute:: access_group_tables
    
    	Control NTP access
    	**type**\:   :py:class:`AccessGroupTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.AccessGroupTables>`
    
    .. attribute:: authentication
    
    	Configure NTP Authentication keys
    	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication>`
    
    .. attribute:: broadcast_delay
    
    	Estimated round\-trip delay
    	**type**\:  int
    
    	**range:** 1..999999
    
    .. attribute:: dscp_ipv4
    
    	 Set IP DSCP value for outgoing NTP IPV4 packets
    	**type**\:   :py:class:`DscpIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.DscpIpv4>`
    
    	**presence node**\: True
    
    .. attribute:: dscp_ipv6
    
    	 Set IP DSCP value for outgoing NTP IPV6 packets
    	**type**\:   :py:class:`DscpIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.DscpIpv6>`
    
    	**presence node**\: True
    
    .. attribute:: interface_tables
    
    	NTP per interface configuration
    	**type**\:   :py:class:`InterfaceTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables>`
    
    .. attribute:: log_internal_sync
    
    	To enable logging internal sync conflicts
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: master
    
    	Act as NTP master clock
    	**type**\:  int
    
    	**range:** 1..15
    
    	**default value**\: 8
    
    .. attribute:: max_associations
    
    	Set maximum number of associations
    	**type**\:  int
    
    	**range:** \-2147483648..2147483647
    
    .. attribute:: passive
    
    	Configure NTP passive associations
    	**type**\:   :py:class:`Passive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Passive>`
    
    .. attribute:: peer_vrfs
    
    	Configures NTP Peers or Servers
    	**type**\:   :py:class:`PeerVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs>`
    
    .. attribute:: sources
    
    	Configure  NTP source interface
    	**type**\:   :py:class:`Sources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Sources>`
    
    .. attribute:: update_calendar
    
    	To enable calendar update with NTP time
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ip-ntp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self._is_presence = True
        self.access_group_tables = Ntp.AccessGroupTables()
        self.access_group_tables.parent = self
        self.authentication = Ntp.Authentication()
        self.authentication.parent = self
        self.broadcast_delay = None
        self.dscp_ipv4 = None
        self.dscp_ipv6 = None
        self.interface_tables = Ntp.InterfaceTables()
        self.interface_tables.parent = self
        self.log_internal_sync = None
        self.master = None
        self.max_associations = None
        self.passive = Ntp.Passive()
        self.passive.parent = self
        self.peer_vrfs = Ntp.PeerVrfs()
        self.peer_vrfs.parent = self
        self.sources = Ntp.Sources()
        self.sources.parent = self
        self.update_calendar = None


    class PeerVrfs(object):
        """
        Configures NTP Peers or Servers
        
        .. attribute:: peer_vrf
        
        	Configures NTP Peers or Servers for a single VRF. The 'default' must also be specified for default VRF
        	**type**\: list of    :py:class:`PeerVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.peer_vrf = YList()
            self.peer_vrf.parent = self
            self.peer_vrf.name = 'peer_vrf'


        class PeerVrf(object):
            """
            Configures NTP Peers or Servers for a single
            VRF. The 'default' must also be specified for
            default VRF
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: peer_ipv4s
            
            	Configures IPv4 NTP Peers or Servers
            	**type**\:   :py:class:`PeerIpv4S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv4S>`
            
            .. attribute:: peer_ipv6s
            
            	Configuration NTP Peers or Servers of IPV6
            	**type**\:   :py:class:`PeerIpv6S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv6S>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.peer_ipv4s = Ntp.PeerVrfs.PeerVrf.PeerIpv4S()
                self.peer_ipv4s.parent = self
                self.peer_ipv6s = Ntp.PeerVrfs.PeerVrf.PeerIpv6S()
                self.peer_ipv6s.parent = self


            class PeerIpv4S(object):
                """
                Configures IPv4 NTP Peers or Servers
                
                .. attribute:: peer_ipv4
                
                	Configure an IPv4 NTP server or peer
                	**type**\: list of    :py:class:`PeerIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4>`
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.peer_ipv4 = YList()
                    self.peer_ipv4.parent = self
                    self.peer_ipv4.name = 'peer_ipv4'


                class PeerIpv4(object):
                    """
                    Configure an IPv4 NTP server or peer
                    
                    .. attribute:: address_ipv4  <key>
                    
                    	IPv4 Address of a peer
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_type_ipv4
                    
                    	Configure an IPv4 NTP server or peer
                    	**type**\: list of    :py:class:`PeerTypeIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4.PeerTypeIpv4>`
                    
                    

                    """

                    _prefix = 'ip-ntp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.address_ipv4 = None
                        self.peer_type_ipv4 = YList()
                        self.peer_type_ipv4.parent = self
                        self.peer_type_ipv4.name = 'peer_type_ipv4'


                    class PeerTypeIpv4(object):
                        """
                        Configure an IPv4 NTP server or peer
                        
                        .. attribute:: peer_type  <key>
                        
                        	Peer or Server
                        	**type**\:   :py:class:`NtpPeerEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.NtpPeerEnum>`
                        
                        .. attribute:: authentication_key
                        
                        	Authentication Key
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: burst
                        
                        	Use burst mode
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: iburst
                        
                        	Use iburst mode
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: max_poll
                        
                        	Maxinum poll interval
                        	**type**\:  int
                        
                        	**range:** 4..17
                        
                        .. attribute:: min_poll
                        
                        	Minimum poll interval
                        	**type**\:  int
                        
                        	**range:** 4..17
                        
                        .. attribute:: ntp_version
                        
                        	NTP version
                        	**type**\:  int
                        
                        	**range:** 2..4
                        
                        .. attribute:: preferred_peer
                        
                        	Preferred peer
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: source_interface
                        
                        	Source interface of this peer
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.peer_type = None
                            self.authentication_key = None
                            self.burst = None
                            self.iburst = None
                            self.max_poll = None
                            self.min_poll = None
                            self.ntp_version = None
                            self.preferred_peer = None
                            self.source_interface = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.peer_type is None:
                                raise YPYModelError('Key property peer_type is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:peer-type-ipv4[Cisco-IOS-XR-ip-ntp-cfg:peer-type = ' + str(self.peer_type) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.peer_type is not None:
                                return True

                            if self.authentication_key is not None:
                                return True

                            if self.burst is not None:
                                return True

                            if self.iburst is not None:
                                return True

                            if self.max_poll is not None:
                                return True

                            if self.min_poll is not None:
                                return True

                            if self.ntp_version is not None:
                                return True

                            if self.preferred_peer is not None:
                                return True

                            if self.source_interface is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                            return meta._meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4.PeerTypeIpv4']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address_ipv4 is None:
                            raise YPYModelError('Key property address_ipv4 is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:peer-ipv4[Cisco-IOS-XR-ip-ntp-cfg:address-ipv4 = ' + str(self.address_ipv4) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.address_ipv4 is not None:
                            return True

                        if self.peer_type_ipv4 is not None:
                            for child_ref in self.peer_type_ipv4:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                        return meta._meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:peer-ipv4s'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.peer_ipv4 is not None:
                        for child_ref in self.peer_ipv4:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                    return meta._meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv4S']['meta_info']


            class PeerIpv6S(object):
                """
                Configuration NTP Peers or Servers of IPV6
                
                .. attribute:: peer_ipv6
                
                	Configure a NTP server or peer
                	**type**\: list of    :py:class:`PeerIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6>`
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.peer_ipv6 = YList()
                    self.peer_ipv6.parent = self
                    self.peer_ipv6.name = 'peer_ipv6'


                class PeerIpv6(object):
                    """
                    Configure a NTP server or peer
                    
                    .. attribute:: address_ipv6  <key>
                    
                    	Address of a peer
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_type_ipv6
                    
                    	Configure a NTP server or peer
                    	**type**\: list of    :py:class:`PeerTypeIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6.PeerTypeIpv6>`
                    
                    

                    """

                    _prefix = 'ip-ntp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.address_ipv6 = None
                        self.peer_type_ipv6 = YList()
                        self.peer_type_ipv6.parent = self
                        self.peer_type_ipv6.name = 'peer_type_ipv6'


                    class PeerTypeIpv6(object):
                        """
                        Configure a NTP server or peer
                        
                        .. attribute:: peer_type  <key>
                        
                        	Peer or Server
                        	**type**\:   :py:class:`NtpPeerEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.NtpPeerEnum>`
                        
                        .. attribute:: address_ipv6
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: authentication_key
                        
                        	Authentication Key
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: burst
                        
                        	Use burst mode
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: iburst
                        
                        	Use iburst mode
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: max_poll
                        
                        	Maxinum poll interval
                        	**type**\:  int
                        
                        	**range:** 4..17
                        
                        .. attribute:: min_poll
                        
                        	Minimum poll interval
                        	**type**\:  int
                        
                        	**range:** 4..17
                        
                        .. attribute:: ntp_version
                        
                        	NTP version
                        	**type**\:  int
                        
                        	**range:** 2..4
                        
                        .. attribute:: preferred_peer
                        
                        	Preferred peer
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: source_interface
                        
                        	Source interface of this peer
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.peer_type = None
                            self.address_ipv6 = None
                            self.authentication_key = None
                            self.burst = None
                            self.iburst = None
                            self.max_poll = None
                            self.min_poll = None
                            self.ntp_version = None
                            self.preferred_peer = None
                            self.source_interface = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.peer_type is None:
                                raise YPYModelError('Key property peer_type is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:peer-type-ipv6[Cisco-IOS-XR-ip-ntp-cfg:peer-type = ' + str(self.peer_type) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.peer_type is not None:
                                return True

                            if self.address_ipv6 is not None:
                                return True

                            if self.authentication_key is not None:
                                return True

                            if self.burst is not None:
                                return True

                            if self.iburst is not None:
                                return True

                            if self.max_poll is not None:
                                return True

                            if self.min_poll is not None:
                                return True

                            if self.ntp_version is not None:
                                return True

                            if self.preferred_peer is not None:
                                return True

                            if self.source_interface is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                            return meta._meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6.PeerTypeIpv6']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address_ipv6 is None:
                            raise YPYModelError('Key property address_ipv6 is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:peer-ipv6[Cisco-IOS-XR-ip-ntp-cfg:address-ipv6 = ' + str(self.address_ipv6) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.address_ipv6 is not None:
                            return True

                        if self.peer_type_ipv6 is not None:
                            for child_ref in self.peer_type_ipv6:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                        return meta._meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:peer-ipv6s'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.peer_ipv6 is not None:
                        for child_ref in self.peer_ipv6:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                    return meta._meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv6S']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:peer-vrfs/Cisco-IOS-XR-ip-ntp-cfg:peer-vrf[Cisco-IOS-XR-ip-ntp-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.peer_ipv4s is not None and self.peer_ipv4s._has_data():
                    return True

                if self.peer_ipv6s is not None and self.peer_ipv6s._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                return meta._meta_table['Ntp.PeerVrfs.PeerVrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:peer-vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.peer_vrf is not None:
                for child_ref in self.peer_vrf:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
            return meta._meta_table['Ntp.PeerVrfs']['meta_info']


    class DscpIpv4(object):
        """
         Set IP DSCP value for outgoing NTP IPV4 packets
        
        .. attribute:: dscp_or_precedence_value
        
        	If Mode is set to 'NTPPRECEDENCE(0)' specify Precedence value , if Mode is set to 'NTPDSCP(1)' specify DSCP
        	**type**\:  int
        
        	**range:** 0..63
        
        	**mandatory**\: True
        
        .. attribute:: mode
        
        	NTPPRECEDENCE (0) to specify Precedence value  NTPDSCP (1) to specify DSCP value
        	**type**\:   :py:class:`NtpdscpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.NtpdscpEnum>`
        
        	**mandatory**\: True
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.dscp_or_precedence_value = None
            self.mode = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:dscp-ipv4'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.dscp_or_precedence_value is not None:
                return True

            if self.mode is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
            return meta._meta_table['Ntp.DscpIpv4']['meta_info']


    class DscpIpv6(object):
        """
         Set IP DSCP value for outgoing NTP IPV6 packets
        
        .. attribute:: dscp_or_precedence_value
        
        	If Mode is set to 'NTPPRECEDENCE(0)' specify Precedence value , if Mode is set to 'NTPDSCP(1)' specify DSCP
        	**type**\:  int
        
        	**range:** 0..63
        
        	**mandatory**\: True
        
        .. attribute:: mode
        
        	NTPPRECEDENCE(0) to specify Precedence value NTPDSCP(1) to specify DSCP value
        	**type**\:   :py:class:`NtpdscpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.NtpdscpEnum>`
        
        	**mandatory**\: True
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.dscp_or_precedence_value = None
            self.mode = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:dscp-ipv6'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.dscp_or_precedence_value is not None:
                return True

            if self.mode is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
            return meta._meta_table['Ntp.DscpIpv6']['meta_info']


    class Sources(object):
        """
        Configure  NTP source interface
        
        .. attribute:: source
        
        	Configure  NTP source interface
        	**type**\: list of    :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Sources.Source>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.source = YList()
            self.source.parent = self
            self.source.name = 'source'


        class Source(object):
            """
            Configure  NTP source interface
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: source_interface
            
            	Source Interface for NTP
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.source_interface = None

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:sources/Cisco-IOS-XR-ip-ntp-cfg:source[Cisco-IOS-XR-ip-ntp-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.source_interface is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                return meta._meta_table['Ntp.Sources.Source']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:sources'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.source is not None:
                for child_ref in self.source:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
            return meta._meta_table['Ntp.Sources']['meta_info']


    class Authentication(object):
        """
        Configure NTP Authentication keys
        
        .. attribute:: enable
        
        	Enable NTP authentication keys
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: keies
        
        	Authentication Key Table
        	**type**\:   :py:class:`Keies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication.Keies>`
        
        .. attribute:: trusted_keies
        
        	Key numbers for trusted time sources
        	**type**\:   :py:class:`TrustedKeies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication.TrustedKeies>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.enable = None
            self.keies = Ntp.Authentication.Keies()
            self.keies.parent = self
            self.trusted_keies = Ntp.Authentication.TrustedKeies()
            self.trusted_keies.parent = self


        class Keies(object):
            """
            Authentication Key Table
            
            .. attribute:: key
            
            	Authentication key for trusted time sources
            	**type**\: list of    :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication.Keies.Key>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.key = YList()
                self.key.parent = self
                self.key.name = 'key'


            class Key(object):
                """
                Authentication key for trusted time sources
                
                .. attribute:: key_number  <key>
                
                	Authentication Key number
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: authentication_key
                
                	Authentication key \- maximum 32 characters
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.key_number = None
                    self.authentication_key = None

                @property
                def _common_path(self):
                    if self.key_number is None:
                        raise YPYModelError('Key property key_number is None')

                    return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:authentication/Cisco-IOS-XR-ip-ntp-cfg:keies/Cisco-IOS-XR-ip-ntp-cfg:key[Cisco-IOS-XR-ip-ntp-cfg:key-number = ' + str(self.key_number) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.key_number is not None:
                        return True

                    if self.authentication_key is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                    return meta._meta_table['Ntp.Authentication.Keies.Key']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:authentication/Cisco-IOS-XR-ip-ntp-cfg:keies'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.key is not None:
                    for child_ref in self.key:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                return meta._meta_table['Ntp.Authentication.Keies']['meta_info']


        class TrustedKeies(object):
            """
            Key numbers for trusted time sources
            
            .. attribute:: trusted_key
            
            	Configure NTP trusted key
            	**type**\: list of    :py:class:`TrustedKey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication.TrustedKeies.TrustedKey>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.trusted_key = YList()
                self.trusted_key.parent = self
                self.trusted_key.name = 'trusted_key'


            class TrustedKey(object):
                """
                Configure NTP trusted key
                
                .. attribute:: key_number  <key>
                
                	Key number
                	**type**\:  int
                
                	**range:** 1..65535
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.key_number = None

                @property
                def _common_path(self):
                    if self.key_number is None:
                        raise YPYModelError('Key property key_number is None')

                    return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:authentication/Cisco-IOS-XR-ip-ntp-cfg:trusted-keies/Cisco-IOS-XR-ip-ntp-cfg:trusted-key[Cisco-IOS-XR-ip-ntp-cfg:key-number = ' + str(self.key_number) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.key_number is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                    return meta._meta_table['Ntp.Authentication.TrustedKeies.TrustedKey']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:authentication/Cisco-IOS-XR-ip-ntp-cfg:trusted-keies'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.trusted_key is not None:
                    for child_ref in self.trusted_key:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                return meta._meta_table['Ntp.Authentication.TrustedKeies']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:authentication'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.enable is not None:
                return True

            if self.keies is not None and self.keies._has_data():
                return True

            if self.trusted_keies is not None and self.trusted_keies._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
            return meta._meta_table['Ntp.Authentication']['meta_info']


    class Passive(object):
        """
        Configure NTP passive associations
        
        .. attribute:: enable
        
        	Enable NTP Passive associations
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.enable = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:passive'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.enable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
            return meta._meta_table['Ntp.Passive']['meta_info']


    class InterfaceTables(object):
        """
        NTP per interface configuration
        
        .. attribute:: interface_table
        
        	NTP per interface configuration
        	**type**\: list of    :py:class:`InterfaceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface_table = YList()
            self.interface_table.parent = self
            self.interface_table.name = 'interface_table'


        class InterfaceTable(object):
            """
            NTP per interface configuration
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: interface
            
            	Name of the interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                Name of the interface
                
                .. attribute:: interface  <key>
                
                	interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: disable
                
                	Disable NTP
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: interface_broadcast
                
                	Configure NTP broadcast service
                	**type**\:   :py:class:`InterfaceBroadcast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast>`
                
                .. attribute:: interface_multicast
                
                	Configure NTP multicast service
                	**type**\:   :py:class:`InterfaceMulticast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast>`
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = None
                    self.disable = None
                    self.interface_broadcast = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast()
                    self.interface_broadcast.parent = self
                    self.interface_multicast = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast()
                    self.interface_multicast.parent = self


                class InterfaceMulticast(object):
                    """
                    Configure NTP multicast service
                    
                    .. attribute:: multicast_clients
                    
                    	Configures multicast client peers
                    	**type**\:   :py:class:`MulticastClients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients>`
                    
                    .. attribute:: multicast_servers
                    
                    	Configures multicast server peers
                    	**type**\:   :py:class:`MulticastServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers>`
                    
                    

                    """

                    _prefix = 'ip-ntp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.multicast_clients = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients()
                        self.multicast_clients.parent = self
                        self.multicast_servers = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers()
                        self.multicast_servers.parent = self


                    class MulticastClients(object):
                        """
                        Configures multicast client peers
                        
                        .. attribute:: multicast_client
                        
                        	Listen to NTP multicasts
                        	**type**\: list of    :py:class:`MulticastClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient>`
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.multicast_client = YList()
                            self.multicast_client.parent = self
                            self.multicast_client.name = 'multicast_client'


                        class MulticastClient(object):
                            """
                            Listen to NTP multicasts
                            
                            .. attribute:: ip_address  <key>
                            
                            	IP address of a multicast group
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            

                            """

                            _prefix = 'ip-ntp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.ip_address is None:
                                    raise YPYModelError('Key property ip_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:multicast-client[Cisco-IOS-XR-ip-ntp-cfg:ip-address = ' + str(self.ip_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.ip_address is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                                return meta._meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:multicast-clients'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.multicast_client is not None:
                                for child_ref in self.multicast_client:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                            return meta._meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients']['meta_info']


                    class MulticastServers(object):
                        """
                        Configures multicast server peers
                        
                        .. attribute:: multicast_server
                        
                        	Configure NTP multicast group server peer
                        	**type**\: list of    :py:class:`MulticastServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer>`
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.multicast_server = YList()
                            self.multicast_server.parent = self
                            self.multicast_server.name = 'multicast_server'


                        class MulticastServer(object):
                            """
                            Configure NTP multicast group server peer
                            
                            .. attribute:: ip_address  <key>
                            
                            	IP address of a multicast group
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: authentication_key
                            
                            	Authentication key
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: ttl
                            
                            	TTL
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            .. attribute:: version
                            
                            	NTP version
                            	**type**\:  int
                            
                            	**range:** 2..4
                            
                            

                            """

                            _prefix = 'ip-ntp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_address = None
                                self.authentication_key = None
                                self.ttl = None
                                self.version = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.ip_address is None:
                                    raise YPYModelError('Key property ip_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:multicast-server[Cisco-IOS-XR-ip-ntp-cfg:ip-address = ' + str(self.ip_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.ip_address is not None:
                                    return True

                                if self.authentication_key is not None:
                                    return True

                                if self.ttl is not None:
                                    return True

                                if self.version is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                                return meta._meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:multicast-servers'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.multicast_server is not None:
                                for child_ref in self.multicast_server:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                            return meta._meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:interface-multicast'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.multicast_clients is not None and self.multicast_clients._has_data():
                            return True

                        if self.multicast_servers is not None and self.multicast_servers._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                        return meta._meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast']['meta_info']


                class InterfaceBroadcast(object):
                    """
                    Configure NTP broadcast service
                    
                    .. attribute:: broadcast
                    
                    	Configure NTP broadcast
                    	**type**\:   :py:class:`Broadcast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast>`
                    
                    .. attribute:: broadcast_client
                    
                    	Listen to NTP broadcasts
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-ntp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.broadcast = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast()
                        self.broadcast.parent = self
                        self.broadcast_client = None


                    class Broadcast(object):
                        """
                        Configure NTP broadcast
                        
                        .. attribute:: address
                        
                        	Destination broadcast IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: authentication_key
                        
                        	Authentication key
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: ntp_version
                        
                        	NTP version
                        	**type**\:  int
                        
                        	**range:** 2..4
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address = None
                            self.authentication_key = None
                            self.ntp_version = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:broadcast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.address is not None:
                                return True

                            if self.authentication_key is not None:
                                return True

                            if self.ntp_version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                            return meta._meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:interface-broadcast'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.broadcast is not None and self.broadcast._has_data():
                            return True

                        if self.broadcast_client is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                        return meta._meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.interface is None:
                        raise YPYModelError('Key property interface is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:interface[Cisco-IOS-XR-ip-ntp-cfg:interface = ' + str(self.interface) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface is not None:
                        return True

                    if self.disable is not None:
                        return True

                    if self.interface_broadcast is not None and self.interface_broadcast._has_data():
                        return True

                    if self.interface_multicast is not None and self.interface_multicast._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                    return meta._meta_table['Ntp.InterfaceTables.InterfaceTable.Interface']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:interface-tables/Cisco-IOS-XR-ip-ntp-cfg:interface-table[Cisco-IOS-XR-ip-ntp-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                return meta._meta_table['Ntp.InterfaceTables.InterfaceTable']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:interface-tables'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.interface_table is not None:
                for child_ref in self.interface_table:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
            return meta._meta_table['Ntp.InterfaceTables']['meta_info']


    class AccessGroupTables(object):
        """
        Control NTP access
        
        .. attribute:: access_group_table
        
        	Control NTP access
        	**type**\: list of    :py:class:`AccessGroupTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.AccessGroupTables.AccessGroupTable>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.access_group_table = YList()
            self.access_group_table.parent = self
            self.access_group_table.name = 'access_group_table'


        class AccessGroupTable(object):
            """
            Control NTP access
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: access_group_af_table
            
            	Configure NTP access address family
            	**type**\: list of    :py:class:`AccessGroupAfTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.access_group_af_table = YList()
                self.access_group_af_table.parent = self
                self.access_group_af_table.name = 'access_group_af_table'


            class AccessGroupAfTable(object):
                """
                Configure NTP access address family
                
                .. attribute:: af  <key>
                
                	Address family
                	**type**\:   :py:class:`NtpAccessAfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.NtpAccessAfEnum>`
                
                .. attribute:: access_group
                
                	Configure NTP access group
                	**type**\: list of    :py:class:`AccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup>`
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.af = None
                    self.access_group = YList()
                    self.access_group.parent = self
                    self.access_group.name = 'access_group'


                class AccessGroup(object):
                    """
                    Configure NTP access group
                    
                    .. attribute:: access_group_type  <key>
                    
                    	Access group type
                    	**type**\:   :py:class:`NtpAccessEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.NtpAccessEnum>`
                    
                    .. attribute:: access_list_name
                    
                    	Access list name \- maximum 32 characters
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ip-ntp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.access_group_type = None
                        self.access_list_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.access_group_type is None:
                            raise YPYModelError('Key property access_group_type is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:access-group[Cisco-IOS-XR-ip-ntp-cfg:access-group-type = ' + str(self.access_group_type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.access_group_type is not None:
                            return True

                        if self.access_list_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                        return meta._meta_table['Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.af is None:
                        raise YPYModelError('Key property af is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-cfg:access-group-af-table[Cisco-IOS-XR-ip-ntp-cfg:af = ' + str(self.af) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.af is not None:
                        return True

                    if self.access_group is not None:
                        for child_ref in self.access_group:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                    return meta._meta_table['Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:access-group-tables/Cisco-IOS-XR-ip-ntp-cfg:access-group-table[Cisco-IOS-XR-ip-ntp-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.access_group_af_table is not None:
                    for child_ref in self.access_group_af_table:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
                return meta._meta_table['Ntp.AccessGroupTables.AccessGroupTable']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-ntp-cfg:ntp/Cisco-IOS-XR-ip-ntp-cfg:access-group-tables'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.access_group_table is not None:
                for child_ref in self.access_group_table:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
            return meta._meta_table['Ntp.AccessGroupTables']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-ntp-cfg:ntp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self._is_presence:
            return True
        if self.access_group_tables is not None and self.access_group_tables._has_data():
            return True

        if self.authentication is not None and self.authentication._has_data():
            return True

        if self.broadcast_delay is not None:
            return True

        if self.dscp_ipv4 is not None and self.dscp_ipv4._has_data():
            return True

        if self.dscp_ipv6 is not None and self.dscp_ipv6._has_data():
            return True

        if self.interface_tables is not None and self.interface_tables._has_data():
            return True

        if self.log_internal_sync is not None:
            return True

        if self.master is not None:
            return True

        if self.max_associations is not None:
            return True

        if self.passive is not None and self.passive._has_data():
            return True

        if self.peer_vrfs is not None and self.peer_vrfs._has_data():
            return True

        if self.sources is not None and self.sources._has_data():
            return True

        if self.update_calendar is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_cfg as meta
        return meta._meta_table['Ntp']['meta_info']



""" Cisco_IOS_XR_ipv4_msdp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-msdp package configuration.

This module contains definitions
for the following management objects\:
  msdp\: MSDP Configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MsdpFilterTypeVrfEnum(Enum):
    """
    MsdpFilterTypeVrfEnum

    Msdp filter type vrf

    .. data:: incoming = 1

    	Incoming Mode

    .. data:: outgoing = 2

    	Outgoing Mode

    """

    incoming = 1

    outgoing = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
        return meta._meta_table['MsdpFilterTypeVrfEnum']


class MsdpListTypeVrfEnum(Enum):
    """
    MsdpListTypeVrfEnum

    Msdp list type vrf

    .. data:: list = 3

    	List

    .. data:: rp_list = 4

    	RPList

    """

    list = 3

    rp_list = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
        return meta._meta_table['MsdpListTypeVrfEnum']



class Msdp(object):
    """
    MSDP Configuration
    
    .. attribute:: default_context
    
    	Default Context
    	**type**\:   :py:class:`DefaultContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.DefaultContext>`
    
    	**presence node**\: True
    
    .. attribute:: global_max_sa
    
    	Configure the global MAX SA state for the router
    	**type**\:  int
    
    	**range:** 1..75000
    
    .. attribute:: nsr_delay
    
    	NSR\-Ready delay period for MSDP Peer
    	**type**\:  int
    
    	**range:** 5..90
    
    	**units**\: second
    
    .. attribute:: vrfs
    
    	VRF Table
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs>`
    
    

    """

    _prefix = 'ipv4-msdp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.default_context = None
        self.global_max_sa = None
        self.nsr_delay = None
        self.vrfs = Msdp.Vrfs()
        self.vrfs.parent = self


    class Vrfs(object):
        """
        VRF Table
        
        .. attribute:: vrf
        
        	VRF Name
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-msdp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
            """
            VRF Name
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: cache_state
            
            	Configure this systems SA cache access\-lists
            	**type**\:   :py:class:`CacheState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs.Vrf.CacheState>`
            
            .. attribute:: connect_source
            
            	Configure interface name used for MSDP connection
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: default_peer
            
            	Configure default peers for the box
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: keep_alive
            
            	MSDP keep alive period
            	**type**\:   :py:class:`KeepAlive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs.Vrf.KeepAlive>`
            
            	**presence node**\: True
            
            .. attribute:: max_peer_sa
            
            	Configure inheritable MAX SA state for peers
            	**type**\:  int
            
            	**range:** 1..75000
            
            .. attribute:: max_sa
            
            	Configure context's MAX SA state for the router
            	**type**\:  int
            
            	**range:** 1..75000
            
            .. attribute:: originator_id
            
            	Configure interface name used as originator ID
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: peers
            
            	Entering Peer Configuration
            	**type**\:   :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs.Vrf.Peers>`
            
            .. attribute:: sa_filters
            
            	Filter SA messages from peer
            	**type**\:   :py:class:`SaFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs.Vrf.SaFilters>`
            
            .. attribute:: ttl_threshold
            
            	Configure TTL Threshold for MSDP Peer
            	**type**\:  int
            
            	**range:** 1..255
            
            

            """

            _prefix = 'ipv4-msdp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.cache_state = Msdp.Vrfs.Vrf.CacheState()
                self.cache_state.parent = self
                self.connect_source = None
                self.default_peer = None
                self.keep_alive = None
                self.max_peer_sa = None
                self.max_sa = None
                self.originator_id = None
                self.peers = Msdp.Vrfs.Vrf.Peers()
                self.peers.parent = self
                self.sa_filters = Msdp.Vrfs.Vrf.SaFilters()
                self.sa_filters.parent = self
                self.ttl_threshold = None


            class CacheState(object):
                """
                Configure this systems SA cache access\-lists
                
                .. attribute:: list
                
                	Access list name
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: rp_list
                
                	Access\-list for originating RP
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: sa_holdtime
                
                	SA State Holdtime period
                	**type**\:  int
                
                	**range:** 150..3600
                
                	**units**\: second
                
                	**default value**\: 150
                
                

                """

                _prefix = 'ipv4-msdp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.list = None
                    self.rp_list = None
                    self.sa_holdtime = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-msdp-cfg:cache-state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.list is not None:
                        return True

                    if self.rp_list is not None:
                        return True

                    if self.sa_holdtime is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                    return meta._meta_table['Msdp.Vrfs.Vrf.CacheState']['meta_info']


            class KeepAlive(object):
                """
                MSDP keep alive period
                
                .. attribute:: keep_alive_period
                
                	Keep alive period in seconds
                	**type**\:  int
                
                	**range:** 1..60
                
                	**mandatory**\: True
                
                	**units**\: second
                
                .. attribute:: peer_timeout_period
                
                	Peer timeout period in seconds
                	**type**\:  int
                
                	**range:** 1..75
                
                	**mandatory**\: True
                
                	**units**\: second
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-msdp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.keep_alive_period = None
                    self.peer_timeout_period = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-msdp-cfg:keep-alive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.keep_alive_period is not None:
                        return True

                    if self.peer_timeout_period is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                    return meta._meta_table['Msdp.Vrfs.Vrf.KeepAlive']['meta_info']


            class Peers(object):
                """
                Entering Peer Configuration
                
                .. attribute:: peer
                
                	Peer address
                	**type**\: list of    :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs.Vrf.Peers.Peer>`
                
                

                """

                _prefix = 'ipv4-msdp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.peer = YList()
                    self.peer.parent = self
                    self.peer.name = 'peer'


                class Peer(object):
                    """
                    Peer address
                    
                    .. attribute:: peer_address  <key>
                    
                    	Peer address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: connect_source
                    
                    	Configure interface name used for MSDP connection
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: description
                    
                    	Up to 80 characters describing this peer
                    	**type**\:  str
                    
                    	**length:** 1..80
                    
                    .. attribute:: enable
                    
                    	Enabling Peer Configuration
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: keep_alive
                    
                    	MSDP keep alive period
                    	**type**\:   :py:class:`KeepAlive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs.Vrf.Peers.Peer.KeepAlive>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: max_sa
                    
                    	Maximum SA accepted from this peer
                    	**type**\:  int
                    
                    	**range:** 1..75000
                    
                    .. attribute:: mesh_group
                    
                    	Configure an MSDP mesh\-group
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: nsr_down
                    
                    	Disable NSR for the peer
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: peer_password
                    
                    	Configuration of password of peer
                    	**type**\:  str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    .. attribute:: remote_as
                    
                    	Configure the remote AS of this peer
                    	**type**\:   :py:class:`RemoteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs.Vrf.Peers.Peer.RemoteAs>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sa_filters
                    
                    	Filter SA messages from peer
                    	**type**\:   :py:class:`SaFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs.Vrf.Peers.Peer.SaFilters>`
                    
                    .. attribute:: shutdown
                    
                    	MSDP Peer Shutdown
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: ttl_threshold
                    
                    	Configure TTL Threshold for MSDP Peer
                    	**type**\:  int
                    
                    	**range:** 1..255
                    
                    

                    """

                    _prefix = 'ipv4-msdp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.peer_address = None
                        self.connect_source = None
                        self.description = None
                        self.enable = None
                        self.keep_alive = None
                        self.max_sa = None
                        self.mesh_group = None
                        self.nsr_down = None
                        self.peer_password = None
                        self.remote_as = None
                        self.sa_filters = Msdp.Vrfs.Vrf.Peers.Peer.SaFilters()
                        self.sa_filters.parent = self
                        self.shutdown = None
                        self.ttl_threshold = None


                    class RemoteAs(object):
                        """
                        Configure the remote AS of this peer
                        
                        .. attribute:: as_xx
                        
                        	First half of ASN in asdot format or 0 in asplain
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        	**default value**\: 0
                        
                        .. attribute:: as_yy
                        
                        	Second half of ASN in asdot format or complete ASN in asplain
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-msdp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.as_xx = None
                            self.as_yy = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-msdp-cfg:remote-as'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.as_xx is not None:
                                return True

                            if self.as_yy is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                            return meta._meta_table['Msdp.Vrfs.Vrf.Peers.Peer.RemoteAs']['meta_info']


                    class KeepAlive(object):
                        """
                        MSDP keep alive period
                        
                        .. attribute:: keep_alive_period
                        
                        	Keep alive period in seconds
                        	**type**\:  int
                        
                        	**range:** 1..60
                        
                        	**mandatory**\: True
                        
                        	**units**\: second
                        
                        .. attribute:: peer_timeout_period
                        
                        	Peer timeout period in seconds
                        	**type**\:  int
                        
                        	**range:** 1..75
                        
                        	**mandatory**\: True
                        
                        	**units**\: second
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-msdp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.keep_alive_period = None
                            self.peer_timeout_period = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-msdp-cfg:keep-alive'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.keep_alive_period is not None:
                                return True

                            if self.peer_timeout_period is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                            return meta._meta_table['Msdp.Vrfs.Vrf.Peers.Peer.KeepAlive']['meta_info']


                    class SaFilters(object):
                        """
                        Filter SA messages from peer
                        
                        .. attribute:: sa_filter
                        
                        	SA\-Filter incoming/outgoing list or RPlist
                        	**type**\: list of    :py:class:`SaFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs.Vrf.Peers.Peer.SaFilters.SaFilter>`
                        
                        

                        """

                        _prefix = 'ipv4-msdp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sa_filter = YList()
                            self.sa_filter.parent = self
                            self.sa_filter.name = 'sa_filter'


                        class SaFilter(object):
                            """
                            SA\-Filter incoming/outgoing list or RPlist
                            
                            .. attribute:: list  <key>
                            
                            	Src List/RP List
                            	**type**\:   :py:class:`MsdpListTypeVrfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpListTypeVrfEnum>`
                            
                            .. attribute:: filter_type  <key>
                            
                            	Incoming/Outgoing ACL
                            	**type**\:   :py:class:`MsdpFilterTypeVrfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpFilterTypeVrfEnum>`
                            
                            .. attribute:: access_list_name
                            
                            	Access list name
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-msdp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.list = None
                                self.filter_type = None
                                self.access_list_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.list is None:
                                    raise YPYModelError('Key property list is None')
                                if self.filter_type is None:
                                    raise YPYModelError('Key property filter_type is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-msdp-cfg:sa-filter[Cisco-IOS-XR-ipv4-msdp-cfg:list = ' + str(self.list) + '][Cisco-IOS-XR-ipv4-msdp-cfg:filter-type = ' + str(self.filter_type) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.list is not None:
                                    return True

                                if self.filter_type is not None:
                                    return True

                                if self.access_list_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                                return meta._meta_table['Msdp.Vrfs.Vrf.Peers.Peer.SaFilters.SaFilter']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-msdp-cfg:sa-filters'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.sa_filter is not None:
                                for child_ref in self.sa_filter:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                            return meta._meta_table['Msdp.Vrfs.Vrf.Peers.Peer.SaFilters']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.peer_address is None:
                            raise YPYModelError('Key property peer_address is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-msdp-cfg:peer[Cisco-IOS-XR-ipv4-msdp-cfg:peer-address = ' + str(self.peer_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.peer_address is not None:
                            return True

                        if self.connect_source is not None:
                            return True

                        if self.description is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.keep_alive is not None and self.keep_alive._has_data():
                            return True

                        if self.max_sa is not None:
                            return True

                        if self.mesh_group is not None:
                            return True

                        if self.nsr_down is not None:
                            return True

                        if self.peer_password is not None:
                            return True

                        if self.remote_as is not None and self.remote_as._has_data():
                            return True

                        if self.sa_filters is not None and self.sa_filters._has_data():
                            return True

                        if self.shutdown is not None:
                            return True

                        if self.ttl_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                        return meta._meta_table['Msdp.Vrfs.Vrf.Peers.Peer']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-msdp-cfg:peers'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.peer is not None:
                        for child_ref in self.peer:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                    return meta._meta_table['Msdp.Vrfs.Vrf.Peers']['meta_info']


            class SaFilters(object):
                """
                Filter SA messages from peer
                
                .. attribute:: sa_filter
                
                	SA\-Filter incoming/outgoing list or RPlist
                	**type**\: list of    :py:class:`SaFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs.Vrf.SaFilters.SaFilter>`
                
                

                """

                _prefix = 'ipv4-msdp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.sa_filter = YList()
                    self.sa_filter.parent = self
                    self.sa_filter.name = 'sa_filter'


                class SaFilter(object):
                    """
                    SA\-Filter incoming/outgoing list or RPlist
                    
                    .. attribute:: list  <key>
                    
                    	Src List/RP List
                    	**type**\:   :py:class:`MsdpListTypeVrfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpListTypeVrfEnum>`
                    
                    .. attribute:: filter_type  <key>
                    
                    	Incoming/Outgoing ACL
                    	**type**\:   :py:class:`MsdpFilterTypeVrfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpFilterTypeVrfEnum>`
                    
                    .. attribute:: access_list_name
                    
                    	Access list name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ipv4-msdp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.list = None
                        self.filter_type = None
                        self.access_list_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.list is None:
                            raise YPYModelError('Key property list is None')
                        if self.filter_type is None:
                            raise YPYModelError('Key property filter_type is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-msdp-cfg:sa-filter[Cisco-IOS-XR-ipv4-msdp-cfg:list = ' + str(self.list) + '][Cisco-IOS-XR-ipv4-msdp-cfg:filter-type = ' + str(self.filter_type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.list is not None:
                            return True

                        if self.filter_type is not None:
                            return True

                        if self.access_list_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                        return meta._meta_table['Msdp.Vrfs.Vrf.SaFilters.SaFilter']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-msdp-cfg:sa-filters'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.sa_filter is not None:
                        for child_ref in self.sa_filter:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                    return meta._meta_table['Msdp.Vrfs.Vrf.SaFilters']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ipv4-msdp-cfg:msdp/Cisco-IOS-XR-ipv4-msdp-cfg:vrfs/Cisco-IOS-XR-ipv4-msdp-cfg:vrf[Cisco-IOS-XR-ipv4-msdp-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.cache_state is not None and self.cache_state._has_data():
                    return True

                if self.connect_source is not None:
                    return True

                if self.default_peer is not None:
                    return True

                if self.keep_alive is not None and self.keep_alive._has_data():
                    return True

                if self.max_peer_sa is not None:
                    return True

                if self.max_sa is not None:
                    return True

                if self.originator_id is not None:
                    return True

                if self.peers is not None and self.peers._has_data():
                    return True

                if self.sa_filters is not None and self.sa_filters._has_data():
                    return True

                if self.ttl_threshold is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                return meta._meta_table['Msdp.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-msdp-cfg:msdp/Cisco-IOS-XR-ipv4-msdp-cfg:vrfs'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
            return meta._meta_table['Msdp.Vrfs']['meta_info']


    class DefaultContext(object):
        """
        Default Context
        
        .. attribute:: cache_state
        
        	Configure this systems SA cache access\-lists
        	**type**\:   :py:class:`CacheState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.DefaultContext.CacheState>`
        
        .. attribute:: connect_source
        
        	Configure interface name used for MSDP connection
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        .. attribute:: default_peer
        
        	Configure default peers for the box
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: keep_alive
        
        	MSDP keep alive period
        	**type**\:   :py:class:`KeepAlive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.DefaultContext.KeepAlive>`
        
        	**presence node**\: True
        
        .. attribute:: max_peer_sa
        
        	Configure inheritable MAX SA state for peers
        	**type**\:  int
        
        	**range:** 1..75000
        
        .. attribute:: max_sa
        
        	Configure context's MAX SA state for the router
        	**type**\:  int
        
        	**range:** 1..75000
        
        .. attribute:: originator_id
        
        	Configure interface name used as originator ID
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        .. attribute:: peers
        
        	Entering Peer Configuration
        	**type**\:   :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.DefaultContext.Peers>`
        
        .. attribute:: sa_filters
        
        	Filter SA messages from peer
        	**type**\:   :py:class:`SaFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.DefaultContext.SaFilters>`
        
        .. attribute:: ttl_threshold
        
        	Configure TTL Threshold for MSDP Peer
        	**type**\:  int
        
        	**range:** 1..255
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-msdp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.cache_state = Msdp.DefaultContext.CacheState()
            self.cache_state.parent = self
            self.connect_source = None
            self.default_peer = None
            self.keep_alive = None
            self.max_peer_sa = None
            self.max_sa = None
            self.originator_id = None
            self.peers = Msdp.DefaultContext.Peers()
            self.peers.parent = self
            self.sa_filters = Msdp.DefaultContext.SaFilters()
            self.sa_filters.parent = self
            self.ttl_threshold = None


        class CacheState(object):
            """
            Configure this systems SA cache access\-lists
            
            .. attribute:: list
            
            	Access list name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: rp_list
            
            	Access\-list for originating RP
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: sa_holdtime
            
            	SA State Holdtime period
            	**type**\:  int
            
            	**range:** 150..3600
            
            	**units**\: second
            
            	**default value**\: 150
            
            

            """

            _prefix = 'ipv4-msdp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.list = None
                self.rp_list = None
                self.sa_holdtime = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-msdp-cfg:msdp/Cisco-IOS-XR-ipv4-msdp-cfg:default-context/Cisco-IOS-XR-ipv4-msdp-cfg:cache-state'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.list is not None:
                    return True

                if self.rp_list is not None:
                    return True

                if self.sa_holdtime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                return meta._meta_table['Msdp.DefaultContext.CacheState']['meta_info']


        class KeepAlive(object):
            """
            MSDP keep alive period
            
            .. attribute:: keep_alive_period
            
            	Keep alive period in seconds
            	**type**\:  int
            
            	**range:** 1..60
            
            	**mandatory**\: True
            
            	**units**\: second
            
            .. attribute:: peer_timeout_period
            
            	Peer timeout period in seconds
            	**type**\:  int
            
            	**range:** 1..75
            
            	**mandatory**\: True
            
            	**units**\: second
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ipv4-msdp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self._is_presence = True
                self.keep_alive_period = None
                self.peer_timeout_period = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-msdp-cfg:msdp/Cisco-IOS-XR-ipv4-msdp-cfg:default-context/Cisco-IOS-XR-ipv4-msdp-cfg:keep-alive'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self._is_presence:
                    return True
                if self.keep_alive_period is not None:
                    return True

                if self.peer_timeout_period is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                return meta._meta_table['Msdp.DefaultContext.KeepAlive']['meta_info']


        class Peers(object):
            """
            Entering Peer Configuration
            
            .. attribute:: peer
            
            	Peer address
            	**type**\: list of    :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.DefaultContext.Peers.Peer>`
            
            

            """

            _prefix = 'ipv4-msdp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.peer = YList()
                self.peer.parent = self
                self.peer.name = 'peer'


            class Peer(object):
                """
                Peer address
                
                .. attribute:: peer_address  <key>
                
                	Peer address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: connect_source
                
                	Configure interface name used for MSDP connection
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: description
                
                	Up to 80 characters describing this peer
                	**type**\:  str
                
                	**length:** 1..80
                
                .. attribute:: enable
                
                	Enabling Peer Configuration
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: keep_alive
                
                	MSDP keep alive period
                	**type**\:   :py:class:`KeepAlive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.DefaultContext.Peers.Peer.KeepAlive>`
                
                	**presence node**\: True
                
                .. attribute:: max_sa
                
                	Maximum SA accepted from this peer
                	**type**\:  int
                
                	**range:** 1..75000
                
                .. attribute:: mesh_group
                
                	Configure an MSDP mesh\-group
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: nsr_down
                
                	Disable NSR for the peer
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: peer_password
                
                	Configuration of password of peer
                	**type**\:  str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: remote_as
                
                	Configure the remote AS of this peer
                	**type**\:   :py:class:`RemoteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.DefaultContext.Peers.Peer.RemoteAs>`
                
                	**presence node**\: True
                
                .. attribute:: sa_filters
                
                	Filter SA messages from peer
                	**type**\:   :py:class:`SaFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.DefaultContext.Peers.Peer.SaFilters>`
                
                .. attribute:: shutdown
                
                	MSDP Peer Shutdown
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ttl_threshold
                
                	Configure TTL Threshold for MSDP Peer
                	**type**\:  int
                
                	**range:** 1..255
                
                

                """

                _prefix = 'ipv4-msdp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.peer_address = None
                    self.connect_source = None
                    self.description = None
                    self.enable = None
                    self.keep_alive = None
                    self.max_sa = None
                    self.mesh_group = None
                    self.nsr_down = None
                    self.peer_password = None
                    self.remote_as = None
                    self.sa_filters = Msdp.DefaultContext.Peers.Peer.SaFilters()
                    self.sa_filters.parent = self
                    self.shutdown = None
                    self.ttl_threshold = None


                class RemoteAs(object):
                    """
                    Configure the remote AS of this peer
                    
                    .. attribute:: as_xx
                    
                    	First half of ASN in asdot format or 0 in asplain
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**default value**\: 0
                    
                    .. attribute:: as_yy
                    
                    	Second half of ASN in asdot format or complete ASN in asplain
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-msdp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.as_xx = None
                        self.as_yy = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-msdp-cfg:remote-as'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.as_xx is not None:
                            return True

                        if self.as_yy is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                        return meta._meta_table['Msdp.DefaultContext.Peers.Peer.RemoteAs']['meta_info']


                class KeepAlive(object):
                    """
                    MSDP keep alive period
                    
                    .. attribute:: keep_alive_period
                    
                    	Keep alive period in seconds
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    .. attribute:: peer_timeout_period
                    
                    	Peer timeout period in seconds
                    	**type**\:  int
                    
                    	**range:** 1..75
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-msdp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.keep_alive_period = None
                        self.peer_timeout_period = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-msdp-cfg:keep-alive'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.keep_alive_period is not None:
                            return True

                        if self.peer_timeout_period is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                        return meta._meta_table['Msdp.DefaultContext.Peers.Peer.KeepAlive']['meta_info']


                class SaFilters(object):
                    """
                    Filter SA messages from peer
                    
                    .. attribute:: sa_filter
                    
                    	SA\-Filter incoming/outgoing list or RPlist
                    	**type**\: list of    :py:class:`SaFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.DefaultContext.Peers.Peer.SaFilters.SaFilter>`
                    
                    

                    """

                    _prefix = 'ipv4-msdp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.sa_filter = YList()
                        self.sa_filter.parent = self
                        self.sa_filter.name = 'sa_filter'


                    class SaFilter(object):
                        """
                        SA\-Filter incoming/outgoing list or RPlist
                        
                        .. attribute:: list  <key>
                        
                        	Src List/RP List
                        	**type**\:   :py:class:`MsdpListTypeVrfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpListTypeVrfEnum>`
                        
                        .. attribute:: filter_type  <key>
                        
                        	Incoming/Outgoing ACL
                        	**type**\:   :py:class:`MsdpFilterTypeVrfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpFilterTypeVrfEnum>`
                        
                        .. attribute:: access_list_name
                        
                        	Access list name
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-msdp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.list = None
                            self.filter_type = None
                            self.access_list_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.list is None:
                                raise YPYModelError('Key property list is None')
                            if self.filter_type is None:
                                raise YPYModelError('Key property filter_type is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-msdp-cfg:sa-filter[Cisco-IOS-XR-ipv4-msdp-cfg:list = ' + str(self.list) + '][Cisco-IOS-XR-ipv4-msdp-cfg:filter-type = ' + str(self.filter_type) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.list is not None:
                                return True

                            if self.filter_type is not None:
                                return True

                            if self.access_list_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                            return meta._meta_table['Msdp.DefaultContext.Peers.Peer.SaFilters.SaFilter']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-msdp-cfg:sa-filters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.sa_filter is not None:
                            for child_ref in self.sa_filter:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                        return meta._meta_table['Msdp.DefaultContext.Peers.Peer.SaFilters']['meta_info']

                @property
                def _common_path(self):
                    if self.peer_address is None:
                        raise YPYModelError('Key property peer_address is None')

                    return '/Cisco-IOS-XR-ipv4-msdp-cfg:msdp/Cisco-IOS-XR-ipv4-msdp-cfg:default-context/Cisco-IOS-XR-ipv4-msdp-cfg:peers/Cisco-IOS-XR-ipv4-msdp-cfg:peer[Cisco-IOS-XR-ipv4-msdp-cfg:peer-address = ' + str(self.peer_address) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.peer_address is not None:
                        return True

                    if self.connect_source is not None:
                        return True

                    if self.description is not None:
                        return True

                    if self.enable is not None:
                        return True

                    if self.keep_alive is not None and self.keep_alive._has_data():
                        return True

                    if self.max_sa is not None:
                        return True

                    if self.mesh_group is not None:
                        return True

                    if self.nsr_down is not None:
                        return True

                    if self.peer_password is not None:
                        return True

                    if self.remote_as is not None and self.remote_as._has_data():
                        return True

                    if self.sa_filters is not None and self.sa_filters._has_data():
                        return True

                    if self.shutdown is not None:
                        return True

                    if self.ttl_threshold is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                    return meta._meta_table['Msdp.DefaultContext.Peers.Peer']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-msdp-cfg:msdp/Cisco-IOS-XR-ipv4-msdp-cfg:default-context/Cisco-IOS-XR-ipv4-msdp-cfg:peers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.peer is not None:
                    for child_ref in self.peer:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                return meta._meta_table['Msdp.DefaultContext.Peers']['meta_info']


        class SaFilters(object):
            """
            Filter SA messages from peer
            
            .. attribute:: sa_filter
            
            	SA\-Filter incoming/outgoing list or RPlist
            	**type**\: list of    :py:class:`SaFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.DefaultContext.SaFilters.SaFilter>`
            
            

            """

            _prefix = 'ipv4-msdp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.sa_filter = YList()
                self.sa_filter.parent = self
                self.sa_filter.name = 'sa_filter'


            class SaFilter(object):
                """
                SA\-Filter incoming/outgoing list or RPlist
                
                .. attribute:: list  <key>
                
                	Src List/RP List
                	**type**\:   :py:class:`MsdpListTypeVrfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpListTypeVrfEnum>`
                
                .. attribute:: filter_type  <key>
                
                	Incoming/Outgoing ACL
                	**type**\:   :py:class:`MsdpFilterTypeVrfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpFilterTypeVrfEnum>`
                
                .. attribute:: access_list_name
                
                	Access list name
                	**type**\:  str
                
                	**length:** 1..64
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ipv4-msdp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.list = None
                    self.filter_type = None
                    self.access_list_name = None

                @property
                def _common_path(self):
                    if self.list is None:
                        raise YPYModelError('Key property list is None')
                    if self.filter_type is None:
                        raise YPYModelError('Key property filter_type is None')

                    return '/Cisco-IOS-XR-ipv4-msdp-cfg:msdp/Cisco-IOS-XR-ipv4-msdp-cfg:default-context/Cisco-IOS-XR-ipv4-msdp-cfg:sa-filters/Cisco-IOS-XR-ipv4-msdp-cfg:sa-filter[Cisco-IOS-XR-ipv4-msdp-cfg:list = ' + str(self.list) + '][Cisco-IOS-XR-ipv4-msdp-cfg:filter-type = ' + str(self.filter_type) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.list is not None:
                        return True

                    if self.filter_type is not None:
                        return True

                    if self.access_list_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                    return meta._meta_table['Msdp.DefaultContext.SaFilters.SaFilter']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-msdp-cfg:msdp/Cisco-IOS-XR-ipv4-msdp-cfg:default-context/Cisco-IOS-XR-ipv4-msdp-cfg:sa-filters'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.sa_filter is not None:
                    for child_ref in self.sa_filter:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
                return meta._meta_table['Msdp.DefaultContext.SaFilters']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-msdp-cfg:msdp/Cisco-IOS-XR-ipv4-msdp-cfg:default-context'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.cache_state is not None and self.cache_state._has_data():
                return True

            if self.connect_source is not None:
                return True

            if self.default_peer is not None:
                return True

            if self.keep_alive is not None and self.keep_alive._has_data():
                return True

            if self.max_peer_sa is not None:
                return True

            if self.max_sa is not None:
                return True

            if self.originator_id is not None:
                return True

            if self.peers is not None and self.peers._has_data():
                return True

            if self.sa_filters is not None and self.sa_filters._has_data():
                return True

            if self.ttl_threshold is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
            return meta._meta_table['Msdp.DefaultContext']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-msdp-cfg:msdp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.default_context is not None and self.default_context._has_data():
            return True

        if self.global_max_sa is not None:
            return True

        if self.nsr_delay is not None:
            return True

        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_msdp_cfg as meta
        return meta._meta_table['Msdp']['meta_info']



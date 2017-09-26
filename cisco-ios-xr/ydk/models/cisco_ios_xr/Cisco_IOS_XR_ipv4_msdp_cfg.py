""" Cisco_IOS_XR_ipv4_msdp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-msdp package configuration.

This module contains definitions
for the following management objects\:
  msdp\: MSDP Configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MsdpFilterTypeVrf(Enum):
    """
    MsdpFilterTypeVrf

    Msdp filter type vrf

    .. data:: incoming = 1

    	Incoming Mode

    .. data:: outgoing = 2

    	Outgoing Mode

    """

    incoming = Enum.YLeaf(1, "incoming")

    outgoing = Enum.YLeaf(2, "outgoing")


class MsdpListTypeVrf(Enum):
    """
    MsdpListTypeVrf

    Msdp list type vrf

    .. data:: list = 3

    	List

    .. data:: rp_list = 4

    	RPList

    """

    list = Enum.YLeaf(3, "list")

    rp_list = Enum.YLeaf(4, "rp-list")



class Msdp(Entity):
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
        super(Msdp, self).__init__()
        self._top_entity = None

        self.yang_name = "msdp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-msdp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"default-context" : ("default_context", Msdp.DefaultContext), "vrfs" : ("vrfs", Msdp.Vrfs)}
        self._child_list_classes = {}

        self.global_max_sa = YLeaf(YType.uint32, "global-max-sa")

        self.nsr_delay = YLeaf(YType.uint32, "nsr-delay")

        self.default_context = None
        self._children_name_map["default_context"] = "default-context"
        self._children_yang_names.add("default-context")

        self.vrfs = Msdp.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-msdp-cfg:msdp"

    def __setattr__(self, name, value):
        self._perform_setattr(Msdp, ['global_max_sa', 'nsr_delay'], name, value)


    class DefaultContext(Entity):
        """
        Default Context
        
        .. attribute:: cache_state
        
        	Configure this systems SA cache access\-lists
        	**type**\:   :py:class:`CacheState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.DefaultContext.CacheState>`
        
        .. attribute:: connect_source
        
        	Configure interface name used for MSDP connection
        	**type**\:  str
        
        	**pattern:** [a\-zA\-Z0\-9./\-]+
        
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
        
        	**pattern:** [a\-zA\-Z0\-9./\-]+
        
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
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-msdp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Msdp.DefaultContext, self).__init__()

            self.yang_name = "default-context"
            self.yang_parent_name = "msdp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"cache-state" : ("cache_state", Msdp.DefaultContext.CacheState), "keep-alive" : ("keep_alive", Msdp.DefaultContext.KeepAlive), "peers" : ("peers", Msdp.DefaultContext.Peers), "sa-filters" : ("sa_filters", Msdp.DefaultContext.SaFilters)}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.connect_source = YLeaf(YType.str, "connect-source")

            self.default_peer = YLeaf(YType.str, "default-peer")

            self.max_peer_sa = YLeaf(YType.uint32, "max-peer-sa")

            self.max_sa = YLeaf(YType.uint32, "max-sa")

            self.originator_id = YLeaf(YType.str, "originator-id")

            self.ttl_threshold = YLeaf(YType.uint32, "ttl-threshold")

            self.cache_state = Msdp.DefaultContext.CacheState()
            self.cache_state.parent = self
            self._children_name_map["cache_state"] = "cache-state"
            self._children_yang_names.add("cache-state")

            self.keep_alive = None
            self._children_name_map["keep_alive"] = "keep-alive"
            self._children_yang_names.add("keep-alive")

            self.peers = Msdp.DefaultContext.Peers()
            self.peers.parent = self
            self._children_name_map["peers"] = "peers"
            self._children_yang_names.add("peers")

            self.sa_filters = Msdp.DefaultContext.SaFilters()
            self.sa_filters.parent = self
            self._children_name_map["sa_filters"] = "sa-filters"
            self._children_yang_names.add("sa-filters")
            self._segment_path = lambda: "default-context"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Msdp.DefaultContext, ['connect_source', 'default_peer', 'max_peer_sa', 'max_sa', 'originator_id', 'ttl_threshold'], name, value)


        class CacheState(Entity):
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
                super(Msdp.DefaultContext.CacheState, self).__init__()

                self.yang_name = "cache-state"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.list = YLeaf(YType.str, "list")

                self.rp_list = YLeaf(YType.str, "rp-list")

                self.sa_holdtime = YLeaf(YType.uint32, "sa-holdtime")
                self._segment_path = lambda: "cache-state"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Msdp.DefaultContext.CacheState, ['list', 'rp_list', 'sa_holdtime'], name, value)


        class KeepAlive(Entity):
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
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ipv4-msdp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Msdp.DefaultContext.KeepAlive, self).__init__()

                self.yang_name = "keep-alive"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}
                self.is_presence_container = True

                self.keep_alive_period = YLeaf(YType.uint32, "keep-alive-period")

                self.peer_timeout_period = YLeaf(YType.uint32, "peer-timeout-period")
                self._segment_path = lambda: "keep-alive"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Msdp.DefaultContext.KeepAlive, ['keep_alive_period', 'peer_timeout_period'], name, value)


        class Peers(Entity):
            """
            Entering Peer Configuration
            
            .. attribute:: peer
            
            	Peer address
            	**type**\: list of    :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.DefaultContext.Peers.Peer>`
            
            

            """

            _prefix = 'ipv4-msdp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Msdp.DefaultContext.Peers, self).__init__()

                self.yang_name = "peers"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"peer" : ("peer", Msdp.DefaultContext.Peers.Peer)}

                self.peer = YList(self)
                self._segment_path = lambda: "peers"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Msdp.DefaultContext.Peers, [], name, value)


            class Peer(Entity):
                """
                Peer address
                
                .. attribute:: peer_address  <key>
                
                	Peer address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: connect_source
                
                	Configure interface name used for MSDP connection
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
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
                    super(Msdp.DefaultContext.Peers.Peer, self).__init__()

                    self.yang_name = "peer"
                    self.yang_parent_name = "peers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"keep-alive" : ("keep_alive", Msdp.DefaultContext.Peers.Peer.KeepAlive), "remote-as" : ("remote_as", Msdp.DefaultContext.Peers.Peer.RemoteAs), "sa-filters" : ("sa_filters", Msdp.DefaultContext.Peers.Peer.SaFilters)}
                    self._child_list_classes = {}

                    self.peer_address = YLeaf(YType.str, "peer-address")

                    self.connect_source = YLeaf(YType.str, "connect-source")

                    self.description = YLeaf(YType.str, "description")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.max_sa = YLeaf(YType.uint32, "max-sa")

                    self.mesh_group = YLeaf(YType.str, "mesh-group")

                    self.nsr_down = YLeaf(YType.empty, "nsr-down")

                    self.peer_password = YLeaf(YType.str, "peer-password")

                    self.shutdown = YLeaf(YType.empty, "shutdown")

                    self.ttl_threshold = YLeaf(YType.uint32, "ttl-threshold")

                    self.keep_alive = None
                    self._children_name_map["keep_alive"] = "keep-alive"
                    self._children_yang_names.add("keep-alive")

                    self.remote_as = None
                    self._children_name_map["remote_as"] = "remote-as"
                    self._children_yang_names.add("remote-as")

                    self.sa_filters = Msdp.DefaultContext.Peers.Peer.SaFilters()
                    self.sa_filters.parent = self
                    self._children_name_map["sa_filters"] = "sa-filters"
                    self._children_yang_names.add("sa-filters")
                    self._segment_path = lambda: "peer" + "[peer-address='" + self.peer_address.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/default-context/peers/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Msdp.DefaultContext.Peers.Peer, ['peer_address', 'connect_source', 'description', 'enable', 'max_sa', 'mesh_group', 'nsr_down', 'peer_password', 'shutdown', 'ttl_threshold'], name, value)


                class KeepAlive(Entity):
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
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-msdp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Msdp.DefaultContext.Peers.Peer.KeepAlive, self).__init__()

                        self.yang_name = "keep-alive"
                        self.yang_parent_name = "peer"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.keep_alive_period = YLeaf(YType.uint32, "keep-alive-period")

                        self.peer_timeout_period = YLeaf(YType.uint32, "peer-timeout-period")
                        self._segment_path = lambda: "keep-alive"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Msdp.DefaultContext.Peers.Peer.KeepAlive, ['keep_alive_period', 'peer_timeout_period'], name, value)


                class RemoteAs(Entity):
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
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-msdp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Msdp.DefaultContext.Peers.Peer.RemoteAs, self).__init__()

                        self.yang_name = "remote-as"
                        self.yang_parent_name = "peer"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.as_xx = YLeaf(YType.uint32, "as-xx")

                        self.as_yy = YLeaf(YType.uint32, "as-yy")
                        self._segment_path = lambda: "remote-as"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Msdp.DefaultContext.Peers.Peer.RemoteAs, ['as_xx', 'as_yy'], name, value)


                class SaFilters(Entity):
                    """
                    Filter SA messages from peer
                    
                    .. attribute:: sa_filter
                    
                    	SA\-Filter incoming/outgoing list or RPlist
                    	**type**\: list of    :py:class:`SaFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.DefaultContext.Peers.Peer.SaFilters.SaFilter>`
                    
                    

                    """

                    _prefix = 'ipv4-msdp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Msdp.DefaultContext.Peers.Peer.SaFilters, self).__init__()

                        self.yang_name = "sa-filters"
                        self.yang_parent_name = "peer"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"sa-filter" : ("sa_filter", Msdp.DefaultContext.Peers.Peer.SaFilters.SaFilter)}

                        self.sa_filter = YList(self)
                        self._segment_path = lambda: "sa-filters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Msdp.DefaultContext.Peers.Peer.SaFilters, [], name, value)


                    class SaFilter(Entity):
                        """
                        SA\-Filter incoming/outgoing list or RPlist
                        
                        .. attribute:: list  <key>
                        
                        	Src List/RP List
                        	**type**\:   :py:class:`MsdpListTypeVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpListTypeVrf>`
                        
                        .. attribute:: filter_type  <key>
                        
                        	Incoming/Outgoing ACL
                        	**type**\:   :py:class:`MsdpFilterTypeVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpFilterTypeVrf>`
                        
                        .. attribute:: access_list_name
                        
                        	Access list name
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-msdp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Msdp.DefaultContext.Peers.Peer.SaFilters.SaFilter, self).__init__()

                            self.yang_name = "sa-filter"
                            self.yang_parent_name = "sa-filters"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.list = YLeaf(YType.enumeration, "list")

                            self.filter_type = YLeaf(YType.enumeration, "filter-type")

                            self.access_list_name = YLeaf(YType.str, "access-list-name")
                            self._segment_path = lambda: "sa-filter" + "[list='" + self.list.get() + "']" + "[filter-type='" + self.filter_type.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Msdp.DefaultContext.Peers.Peer.SaFilters.SaFilter, ['list', 'filter_type', 'access_list_name'], name, value)


        class SaFilters(Entity):
            """
            Filter SA messages from peer
            
            .. attribute:: sa_filter
            
            	SA\-Filter incoming/outgoing list or RPlist
            	**type**\: list of    :py:class:`SaFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.DefaultContext.SaFilters.SaFilter>`
            
            

            """

            _prefix = 'ipv4-msdp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Msdp.DefaultContext.SaFilters, self).__init__()

                self.yang_name = "sa-filters"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"sa-filter" : ("sa_filter", Msdp.DefaultContext.SaFilters.SaFilter)}

                self.sa_filter = YList(self)
                self._segment_path = lambda: "sa-filters"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Msdp.DefaultContext.SaFilters, [], name, value)


            class SaFilter(Entity):
                """
                SA\-Filter incoming/outgoing list or RPlist
                
                .. attribute:: list  <key>
                
                	Src List/RP List
                	**type**\:   :py:class:`MsdpListTypeVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpListTypeVrf>`
                
                .. attribute:: filter_type  <key>
                
                	Incoming/Outgoing ACL
                	**type**\:   :py:class:`MsdpFilterTypeVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpFilterTypeVrf>`
                
                .. attribute:: access_list_name
                
                	Access list name
                	**type**\:  str
                
                	**length:** 1..64
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ipv4-msdp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Msdp.DefaultContext.SaFilters.SaFilter, self).__init__()

                    self.yang_name = "sa-filter"
                    self.yang_parent_name = "sa-filters"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.list = YLeaf(YType.enumeration, "list")

                    self.filter_type = YLeaf(YType.enumeration, "filter-type")

                    self.access_list_name = YLeaf(YType.str, "access-list-name")
                    self._segment_path = lambda: "sa-filter" + "[list='" + self.list.get() + "']" + "[filter-type='" + self.filter_type.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/default-context/sa-filters/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Msdp.DefaultContext.SaFilters.SaFilter, ['list', 'filter_type', 'access_list_name'], name, value)


    class Vrfs(Entity):
        """
        VRF Table
        
        .. attribute:: vrf
        
        	VRF Name
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-msdp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Msdp.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "msdp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"vrf" : ("vrf", Msdp.Vrfs.Vrf)}

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Msdp.Vrfs, [], name, value)


        class Vrf(Entity):
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
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
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
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
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
                super(Msdp.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"cache-state" : ("cache_state", Msdp.Vrfs.Vrf.CacheState), "keep-alive" : ("keep_alive", Msdp.Vrfs.Vrf.KeepAlive), "peers" : ("peers", Msdp.Vrfs.Vrf.Peers), "sa-filters" : ("sa_filters", Msdp.Vrfs.Vrf.SaFilters)}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.connect_source = YLeaf(YType.str, "connect-source")

                self.default_peer = YLeaf(YType.str, "default-peer")

                self.max_peer_sa = YLeaf(YType.uint32, "max-peer-sa")

                self.max_sa = YLeaf(YType.uint32, "max-sa")

                self.originator_id = YLeaf(YType.str, "originator-id")

                self.ttl_threshold = YLeaf(YType.uint32, "ttl-threshold")

                self.cache_state = Msdp.Vrfs.Vrf.CacheState()
                self.cache_state.parent = self
                self._children_name_map["cache_state"] = "cache-state"
                self._children_yang_names.add("cache-state")

                self.keep_alive = None
                self._children_name_map["keep_alive"] = "keep-alive"
                self._children_yang_names.add("keep-alive")

                self.peers = Msdp.Vrfs.Vrf.Peers()
                self.peers.parent = self
                self._children_name_map["peers"] = "peers"
                self._children_yang_names.add("peers")

                self.sa_filters = Msdp.Vrfs.Vrf.SaFilters()
                self.sa_filters.parent = self
                self._children_name_map["sa_filters"] = "sa-filters"
                self._children_yang_names.add("sa-filters")
                self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Msdp.Vrfs.Vrf, ['vrf_name', 'connect_source', 'default_peer', 'max_peer_sa', 'max_sa', 'originator_id', 'ttl_threshold'], name, value)


            class CacheState(Entity):
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
                    super(Msdp.Vrfs.Vrf.CacheState, self).__init__()

                    self.yang_name = "cache-state"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.list = YLeaf(YType.str, "list")

                    self.rp_list = YLeaf(YType.str, "rp-list")

                    self.sa_holdtime = YLeaf(YType.uint32, "sa-holdtime")
                    self._segment_path = lambda: "cache-state"

                def __setattr__(self, name, value):
                    self._perform_setattr(Msdp.Vrfs.Vrf.CacheState, ['list', 'rp_list', 'sa_holdtime'], name, value)


            class KeepAlive(Entity):
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
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-msdp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Msdp.Vrfs.Vrf.KeepAlive, self).__init__()

                    self.yang_name = "keep-alive"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.keep_alive_period = YLeaf(YType.uint32, "keep-alive-period")

                    self.peer_timeout_period = YLeaf(YType.uint32, "peer-timeout-period")
                    self._segment_path = lambda: "keep-alive"

                def __setattr__(self, name, value):
                    self._perform_setattr(Msdp.Vrfs.Vrf.KeepAlive, ['keep_alive_period', 'peer_timeout_period'], name, value)


            class Peers(Entity):
                """
                Entering Peer Configuration
                
                .. attribute:: peer
                
                	Peer address
                	**type**\: list of    :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs.Vrf.Peers.Peer>`
                
                

                """

                _prefix = 'ipv4-msdp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Msdp.Vrfs.Vrf.Peers, self).__init__()

                    self.yang_name = "peers"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"peer" : ("peer", Msdp.Vrfs.Vrf.Peers.Peer)}

                    self.peer = YList(self)
                    self._segment_path = lambda: "peers"

                def __setattr__(self, name, value):
                    self._perform_setattr(Msdp.Vrfs.Vrf.Peers, [], name, value)


                class Peer(Entity):
                    """
                    Peer address
                    
                    .. attribute:: peer_address  <key>
                    
                    	Peer address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: connect_source
                    
                    	Configure interface name used for MSDP connection
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        super(Msdp.Vrfs.Vrf.Peers.Peer, self).__init__()

                        self.yang_name = "peer"
                        self.yang_parent_name = "peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"keep-alive" : ("keep_alive", Msdp.Vrfs.Vrf.Peers.Peer.KeepAlive), "remote-as" : ("remote_as", Msdp.Vrfs.Vrf.Peers.Peer.RemoteAs), "sa-filters" : ("sa_filters", Msdp.Vrfs.Vrf.Peers.Peer.SaFilters)}
                        self._child_list_classes = {}

                        self.peer_address = YLeaf(YType.str, "peer-address")

                        self.connect_source = YLeaf(YType.str, "connect-source")

                        self.description = YLeaf(YType.str, "description")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.max_sa = YLeaf(YType.uint32, "max-sa")

                        self.mesh_group = YLeaf(YType.str, "mesh-group")

                        self.nsr_down = YLeaf(YType.empty, "nsr-down")

                        self.peer_password = YLeaf(YType.str, "peer-password")

                        self.shutdown = YLeaf(YType.empty, "shutdown")

                        self.ttl_threshold = YLeaf(YType.uint32, "ttl-threshold")

                        self.keep_alive = None
                        self._children_name_map["keep_alive"] = "keep-alive"
                        self._children_yang_names.add("keep-alive")

                        self.remote_as = None
                        self._children_name_map["remote_as"] = "remote-as"
                        self._children_yang_names.add("remote-as")

                        self.sa_filters = Msdp.Vrfs.Vrf.Peers.Peer.SaFilters()
                        self.sa_filters.parent = self
                        self._children_name_map["sa_filters"] = "sa-filters"
                        self._children_yang_names.add("sa-filters")
                        self._segment_path = lambda: "peer" + "[peer-address='" + self.peer_address.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Msdp.Vrfs.Vrf.Peers.Peer, ['peer_address', 'connect_source', 'description', 'enable', 'max_sa', 'mesh_group', 'nsr_down', 'peer_password', 'shutdown', 'ttl_threshold'], name, value)


                    class KeepAlive(Entity):
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
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-msdp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Msdp.Vrfs.Vrf.Peers.Peer.KeepAlive, self).__init__()

                            self.yang_name = "keep-alive"
                            self.yang_parent_name = "peer"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.keep_alive_period = YLeaf(YType.uint32, "keep-alive-period")

                            self.peer_timeout_period = YLeaf(YType.uint32, "peer-timeout-period")
                            self._segment_path = lambda: "keep-alive"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Msdp.Vrfs.Vrf.Peers.Peer.KeepAlive, ['keep_alive_period', 'peer_timeout_period'], name, value)


                    class RemoteAs(Entity):
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
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-msdp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Msdp.Vrfs.Vrf.Peers.Peer.RemoteAs, self).__init__()

                            self.yang_name = "remote-as"
                            self.yang_parent_name = "peer"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.as_xx = YLeaf(YType.uint32, "as-xx")

                            self.as_yy = YLeaf(YType.uint32, "as-yy")
                            self._segment_path = lambda: "remote-as"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Msdp.Vrfs.Vrf.Peers.Peer.RemoteAs, ['as_xx', 'as_yy'], name, value)


                    class SaFilters(Entity):
                        """
                        Filter SA messages from peer
                        
                        .. attribute:: sa_filter
                        
                        	SA\-Filter incoming/outgoing list or RPlist
                        	**type**\: list of    :py:class:`SaFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs.Vrf.Peers.Peer.SaFilters.SaFilter>`
                        
                        

                        """

                        _prefix = 'ipv4-msdp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Msdp.Vrfs.Vrf.Peers.Peer.SaFilters, self).__init__()

                            self.yang_name = "sa-filters"
                            self.yang_parent_name = "peer"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sa-filter" : ("sa_filter", Msdp.Vrfs.Vrf.Peers.Peer.SaFilters.SaFilter)}

                            self.sa_filter = YList(self)
                            self._segment_path = lambda: "sa-filters"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Msdp.Vrfs.Vrf.Peers.Peer.SaFilters, [], name, value)


                        class SaFilter(Entity):
                            """
                            SA\-Filter incoming/outgoing list or RPlist
                            
                            .. attribute:: list  <key>
                            
                            	Src List/RP List
                            	**type**\:   :py:class:`MsdpListTypeVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpListTypeVrf>`
                            
                            .. attribute:: filter_type  <key>
                            
                            	Incoming/Outgoing ACL
                            	**type**\:   :py:class:`MsdpFilterTypeVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpFilterTypeVrf>`
                            
                            .. attribute:: access_list_name
                            
                            	Access list name
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-msdp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Msdp.Vrfs.Vrf.Peers.Peer.SaFilters.SaFilter, self).__init__()

                                self.yang_name = "sa-filter"
                                self.yang_parent_name = "sa-filters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.list = YLeaf(YType.enumeration, "list")

                                self.filter_type = YLeaf(YType.enumeration, "filter-type")

                                self.access_list_name = YLeaf(YType.str, "access-list-name")
                                self._segment_path = lambda: "sa-filter" + "[list='" + self.list.get() + "']" + "[filter-type='" + self.filter_type.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Msdp.Vrfs.Vrf.Peers.Peer.SaFilters.SaFilter, ['list', 'filter_type', 'access_list_name'], name, value)


            class SaFilters(Entity):
                """
                Filter SA messages from peer
                
                .. attribute:: sa_filter
                
                	SA\-Filter incoming/outgoing list or RPlist
                	**type**\: list of    :py:class:`SaFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.Msdp.Vrfs.Vrf.SaFilters.SaFilter>`
                
                

                """

                _prefix = 'ipv4-msdp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Msdp.Vrfs.Vrf.SaFilters, self).__init__()

                    self.yang_name = "sa-filters"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"sa-filter" : ("sa_filter", Msdp.Vrfs.Vrf.SaFilters.SaFilter)}

                    self.sa_filter = YList(self)
                    self._segment_path = lambda: "sa-filters"

                def __setattr__(self, name, value):
                    self._perform_setattr(Msdp.Vrfs.Vrf.SaFilters, [], name, value)


                class SaFilter(Entity):
                    """
                    SA\-Filter incoming/outgoing list or RPlist
                    
                    .. attribute:: list  <key>
                    
                    	Src List/RP List
                    	**type**\:   :py:class:`MsdpListTypeVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpListTypeVrf>`
                    
                    .. attribute:: filter_type  <key>
                    
                    	Incoming/Outgoing ACL
                    	**type**\:   :py:class:`MsdpFilterTypeVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg.MsdpFilterTypeVrf>`
                    
                    .. attribute:: access_list_name
                    
                    	Access list name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ipv4-msdp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Msdp.Vrfs.Vrf.SaFilters.SaFilter, self).__init__()

                        self.yang_name = "sa-filter"
                        self.yang_parent_name = "sa-filters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.list = YLeaf(YType.enumeration, "list")

                        self.filter_type = YLeaf(YType.enumeration, "filter-type")

                        self.access_list_name = YLeaf(YType.str, "access-list-name")
                        self._segment_path = lambda: "sa-filter" + "[list='" + self.list.get() + "']" + "[filter-type='" + self.filter_type.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Msdp.Vrfs.Vrf.SaFilters.SaFilter, ['list', 'filter_type', 'access_list_name'], name, value)

    def clone_ptr(self):
        self._top_entity = Msdp()
        return self._top_entity


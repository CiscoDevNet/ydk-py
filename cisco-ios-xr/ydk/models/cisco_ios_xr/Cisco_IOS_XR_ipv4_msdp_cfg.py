""" Cisco_IOS_XR_ipv4_msdp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-msdp package configuration.

This module contains definitions
for the following management objects\:
  msdp\: MSDP Configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

        self.global_max_sa = YLeaf(YType.uint32, "global-max-sa")

        self.nsr_delay = YLeaf(YType.uint32, "nsr-delay")

        self.default_context = None
        self._children_name_map["default_context"] = "default-context"
        self._children_yang_names.add("default-context")

        self.vrfs = Msdp.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("global_max_sa",
                        "nsr_delay") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Msdp, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Msdp, self).__setattr__(name, value)


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
                        super(Msdp.Vrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Msdp.Vrfs, self).__setattr__(name, value)


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
                super(Msdp.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"

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
                                "connect_source",
                                "default_peer",
                                "max_peer_sa",
                                "max_sa",
                                "originator_id",
                                "ttl_threshold") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Msdp.Vrfs.Vrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Msdp.Vrfs.Vrf, self).__setattr__(name, value)


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

                    self.list = YLeaf(YType.str, "list")

                    self.rp_list = YLeaf(YType.str, "rp-list")

                    self.sa_holdtime = YLeaf(YType.uint32, "sa-holdtime")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("list",
                                    "rp_list",
                                    "sa_holdtime") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Msdp.Vrfs.Vrf.CacheState, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Msdp.Vrfs.Vrf.CacheState, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.list.is_set or
                        self.rp_list.is_set or
                        self.sa_holdtime.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.list.yfilter != YFilter.not_set or
                        self.rp_list.yfilter != YFilter.not_set or
                        self.sa_holdtime.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cache-state" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.list.is_set or self.list.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.list.get_name_leafdata())
                    if (self.rp_list.is_set or self.rp_list.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rp_list.get_name_leafdata())
                    if (self.sa_holdtime.is_set or self.sa_holdtime.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sa_holdtime.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "list" or name == "rp-list" or name == "sa-holdtime"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "list"):
                        self.list = value
                        self.list.value_namespace = name_space
                        self.list.value_namespace_prefix = name_space_prefix
                    if(value_path == "rp-list"):
                        self.rp_list = value
                        self.rp_list.value_namespace = name_space
                        self.rp_list.value_namespace_prefix = name_space_prefix
                    if(value_path == "sa-holdtime"):
                        self.sa_holdtime = value
                        self.sa_holdtime.value_namespace = name_space
                        self.sa_holdtime.value_namespace_prefix = name_space_prefix


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
                    self.is_presence_container = True

                    self.keep_alive_period = YLeaf(YType.uint32, "keep-alive-period")

                    self.peer_timeout_period = YLeaf(YType.uint32, "peer-timeout-period")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("keep_alive_period",
                                    "peer_timeout_period") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Msdp.Vrfs.Vrf.KeepAlive, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Msdp.Vrfs.Vrf.KeepAlive, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.keep_alive_period.is_set or
                        self.peer_timeout_period.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.keep_alive_period.yfilter != YFilter.not_set or
                        self.peer_timeout_period.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "keep-alive" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.keep_alive_period.is_set or self.keep_alive_period.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.keep_alive_period.get_name_leafdata())
                    if (self.peer_timeout_period.is_set or self.peer_timeout_period.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peer_timeout_period.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "keep-alive-period" or name == "peer-timeout-period"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "keep-alive-period"):
                        self.keep_alive_period = value
                        self.keep_alive_period.value_namespace = name_space
                        self.keep_alive_period.value_namespace_prefix = name_space_prefix
                    if(value_path == "peer-timeout-period"):
                        self.peer_timeout_period = value
                        self.peer_timeout_period.value_namespace = name_space
                        self.peer_timeout_period.value_namespace_prefix = name_space_prefix


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

                    self.peer = YList(self)

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
                                super(Msdp.Vrfs.Vrf.Peers, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Msdp.Vrfs.Vrf.Peers, self).__setattr__(name, value)


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
                        super(Msdp.Vrfs.Vrf.Peers.Peer, self).__init__()

                        self.yang_name = "peer"
                        self.yang_parent_name = "peers"

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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("peer_address",
                                        "connect_source",
                                        "description",
                                        "enable",
                                        "max_sa",
                                        "mesh_group",
                                        "nsr_down",
                                        "peer_password",
                                        "shutdown",
                                        "ttl_threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Msdp.Vrfs.Vrf.Peers.Peer, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Msdp.Vrfs.Vrf.Peers.Peer, self).__setattr__(name, value)


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
                            self.is_presence_container = True

                            self.as_xx = YLeaf(YType.uint32, "as-xx")

                            self.as_yy = YLeaf(YType.uint32, "as-yy")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("as_xx",
                                            "as_yy") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Msdp.Vrfs.Vrf.Peers.Peer.RemoteAs, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Msdp.Vrfs.Vrf.Peers.Peer.RemoteAs, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.as_xx.is_set or
                                self.as_yy.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.as_xx.yfilter != YFilter.not_set or
                                self.as_yy.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "remote-as" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.as_xx.is_set or self.as_xx.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.as_xx.get_name_leafdata())
                            if (self.as_yy.is_set or self.as_yy.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.as_yy.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "as-xx" or name == "as-yy"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "as-xx"):
                                self.as_xx = value
                                self.as_xx.value_namespace = name_space
                                self.as_xx.value_namespace_prefix = name_space_prefix
                            if(value_path == "as-yy"):
                                self.as_yy = value
                                self.as_yy.value_namespace = name_space
                                self.as_yy.value_namespace_prefix = name_space_prefix


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
                            self.is_presence_container = True

                            self.keep_alive_period = YLeaf(YType.uint32, "keep-alive-period")

                            self.peer_timeout_period = YLeaf(YType.uint32, "peer-timeout-period")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("keep_alive_period",
                                            "peer_timeout_period") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Msdp.Vrfs.Vrf.Peers.Peer.KeepAlive, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Msdp.Vrfs.Vrf.Peers.Peer.KeepAlive, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.keep_alive_period.is_set or
                                self.peer_timeout_period.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.keep_alive_period.yfilter != YFilter.not_set or
                                self.peer_timeout_period.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "keep-alive" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.keep_alive_period.is_set or self.keep_alive_period.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.keep_alive_period.get_name_leafdata())
                            if (self.peer_timeout_period.is_set or self.peer_timeout_period.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.peer_timeout_period.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "keep-alive-period" or name == "peer-timeout-period"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "keep-alive-period"):
                                self.keep_alive_period = value
                                self.keep_alive_period.value_namespace = name_space
                                self.keep_alive_period.value_namespace_prefix = name_space_prefix
                            if(value_path == "peer-timeout-period"):
                                self.peer_timeout_period = value
                                self.peer_timeout_period.value_namespace = name_space
                                self.peer_timeout_period.value_namespace_prefix = name_space_prefix


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

                            self.sa_filter = YList(self)

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
                                        super(Msdp.Vrfs.Vrf.Peers.Peer.SaFilters, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Msdp.Vrfs.Vrf.Peers.Peer.SaFilters, self).__setattr__(name, value)


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

                                self.list = YLeaf(YType.enumeration, "list")

                                self.filter_type = YLeaf(YType.enumeration, "filter-type")

                                self.access_list_name = YLeaf(YType.str, "access-list-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("list",
                                                "filter_type",
                                                "access_list_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Msdp.Vrfs.Vrf.Peers.Peer.SaFilters.SaFilter, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Msdp.Vrfs.Vrf.Peers.Peer.SaFilters.SaFilter, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.list.is_set or
                                    self.filter_type.is_set or
                                    self.access_list_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.list.yfilter != YFilter.not_set or
                                    self.filter_type.yfilter != YFilter.not_set or
                                    self.access_list_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sa-filter" + "[list='" + self.list.get() + "']" + "[filter-type='" + self.filter_type.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.list.is_set or self.list.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.list.get_name_leafdata())
                                if (self.filter_type.is_set or self.filter_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.filter_type.get_name_leafdata())
                                if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.access_list_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "list" or name == "filter-type" or name == "access-list-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "list"):
                                    self.list = value
                                    self.list.value_namespace = name_space
                                    self.list.value_namespace_prefix = name_space_prefix
                                if(value_path == "filter-type"):
                                    self.filter_type = value
                                    self.filter_type.value_namespace = name_space
                                    self.filter_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "access-list-name"):
                                    self.access_list_name = value
                                    self.access_list_name.value_namespace = name_space
                                    self.access_list_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sa_filter:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sa_filter:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sa-filters" + path_buffer

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

                            if (child_yang_name == "sa-filter"):
                                for c in self.sa_filter:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Msdp.Vrfs.Vrf.Peers.Peer.SaFilters.SaFilter()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sa_filter.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sa-filter"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.peer_address.is_set or
                            self.connect_source.is_set or
                            self.description.is_set or
                            self.enable.is_set or
                            self.max_sa.is_set or
                            self.mesh_group.is_set or
                            self.nsr_down.is_set or
                            self.peer_password.is_set or
                            self.shutdown.is_set or
                            self.ttl_threshold.is_set or
                            (self.sa_filters is not None and self.sa_filters.has_data()) or
                            (self.keep_alive is not None) or
                            (self.remote_as is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.peer_address.yfilter != YFilter.not_set or
                            self.connect_source.yfilter != YFilter.not_set or
                            self.description.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set or
                            self.max_sa.yfilter != YFilter.not_set or
                            self.mesh_group.yfilter != YFilter.not_set or
                            self.nsr_down.yfilter != YFilter.not_set or
                            self.peer_password.yfilter != YFilter.not_set or
                            self.shutdown.yfilter != YFilter.not_set or
                            self.ttl_threshold.yfilter != YFilter.not_set or
                            (self.keep_alive is not None and self.keep_alive.has_operation()) or
                            (self.remote_as is not None and self.remote_as.has_operation()) or
                            (self.sa_filters is not None and self.sa_filters.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "peer" + "[peer-address='" + self.peer_address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.peer_address.is_set or self.peer_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_address.get_name_leafdata())
                        if (self.connect_source.is_set or self.connect_source.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.connect_source.get_name_leafdata())
                        if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.description.get_name_leafdata())
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())
                        if (self.max_sa.is_set or self.max_sa.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_sa.get_name_leafdata())
                        if (self.mesh_group.is_set or self.mesh_group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mesh_group.get_name_leafdata())
                        if (self.nsr_down.is_set or self.nsr_down.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nsr_down.get_name_leafdata())
                        if (self.peer_password.is_set or self.peer_password.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_password.get_name_leafdata())
                        if (self.shutdown.is_set or self.shutdown.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.shutdown.get_name_leafdata())
                        if (self.ttl_threshold.is_set or self.ttl_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ttl_threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "keep-alive"):
                            if (self.keep_alive is None):
                                self.keep_alive = Msdp.Vrfs.Vrf.Peers.Peer.KeepAlive()
                                self.keep_alive.parent = self
                                self._children_name_map["keep_alive"] = "keep-alive"
                            return self.keep_alive

                        if (child_yang_name == "remote-as"):
                            if (self.remote_as is None):
                                self.remote_as = Msdp.Vrfs.Vrf.Peers.Peer.RemoteAs()
                                self.remote_as.parent = self
                                self._children_name_map["remote_as"] = "remote-as"
                            return self.remote_as

                        if (child_yang_name == "sa-filters"):
                            if (self.sa_filters is None):
                                self.sa_filters = Msdp.Vrfs.Vrf.Peers.Peer.SaFilters()
                                self.sa_filters.parent = self
                                self._children_name_map["sa_filters"] = "sa-filters"
                            return self.sa_filters

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "keep-alive" or name == "remote-as" or name == "sa-filters" or name == "peer-address" or name == "connect-source" or name == "description" or name == "enable" or name == "max-sa" or name == "mesh-group" or name == "nsr-down" or name == "peer-password" or name == "shutdown" or name == "ttl-threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "peer-address"):
                            self.peer_address = value
                            self.peer_address.value_namespace = name_space
                            self.peer_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "connect-source"):
                            self.connect_source = value
                            self.connect_source.value_namespace = name_space
                            self.connect_source.value_namespace_prefix = name_space_prefix
                        if(value_path == "description"):
                            self.description = value
                            self.description.value_namespace = name_space
                            self.description.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-sa"):
                            self.max_sa = value
                            self.max_sa.value_namespace = name_space
                            self.max_sa.value_namespace_prefix = name_space_prefix
                        if(value_path == "mesh-group"):
                            self.mesh_group = value
                            self.mesh_group.value_namespace = name_space
                            self.mesh_group.value_namespace_prefix = name_space_prefix
                        if(value_path == "nsr-down"):
                            self.nsr_down = value
                            self.nsr_down.value_namespace = name_space
                            self.nsr_down.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-password"):
                            self.peer_password = value
                            self.peer_password.value_namespace = name_space
                            self.peer_password.value_namespace_prefix = name_space_prefix
                        if(value_path == "shutdown"):
                            self.shutdown = value
                            self.shutdown.value_namespace = name_space
                            self.shutdown.value_namespace_prefix = name_space_prefix
                        if(value_path == "ttl-threshold"):
                            self.ttl_threshold = value
                            self.ttl_threshold.value_namespace = name_space
                            self.ttl_threshold.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.peer:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.peer:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "peers" + path_buffer

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

                    if (child_yang_name == "peer"):
                        for c in self.peer:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Msdp.Vrfs.Vrf.Peers.Peer()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.peer.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "peer"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.sa_filter = YList(self)

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
                                super(Msdp.Vrfs.Vrf.SaFilters, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Msdp.Vrfs.Vrf.SaFilters, self).__setattr__(name, value)


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

                        self.list = YLeaf(YType.enumeration, "list")

                        self.filter_type = YLeaf(YType.enumeration, "filter-type")

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("list",
                                        "filter_type",
                                        "access_list_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Msdp.Vrfs.Vrf.SaFilters.SaFilter, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Msdp.Vrfs.Vrf.SaFilters.SaFilter, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.list.is_set or
                            self.filter_type.is_set or
                            self.access_list_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.list.yfilter != YFilter.not_set or
                            self.filter_type.yfilter != YFilter.not_set or
                            self.access_list_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sa-filter" + "[list='" + self.list.get() + "']" + "[filter-type='" + self.filter_type.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.list.is_set or self.list.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.list.get_name_leafdata())
                        if (self.filter_type.is_set or self.filter_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.filter_type.get_name_leafdata())
                        if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "list" or name == "filter-type" or name == "access-list-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "list"):
                            self.list = value
                            self.list.value_namespace = name_space
                            self.list.value_namespace_prefix = name_space_prefix
                        if(value_path == "filter-type"):
                            self.filter_type = value
                            self.filter_type.value_namespace = name_space
                            self.filter_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "access-list-name"):
                            self.access_list_name = value
                            self.access_list_name.value_namespace = name_space
                            self.access_list_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.sa_filter:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.sa_filter:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "sa-filters" + path_buffer

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

                    if (child_yang_name == "sa-filter"):
                        for c in self.sa_filter:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Msdp.Vrfs.Vrf.SaFilters.SaFilter()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.sa_filter.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "sa-filter"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    self.connect_source.is_set or
                    self.default_peer.is_set or
                    self.max_peer_sa.is_set or
                    self.max_sa.is_set or
                    self.originator_id.is_set or
                    self.ttl_threshold.is_set or
                    (self.cache_state is not None and self.cache_state.has_data()) or
                    (self.peers is not None and self.peers.has_data()) or
                    (self.sa_filters is not None and self.sa_filters.has_data()) or
                    (self.keep_alive is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.connect_source.yfilter != YFilter.not_set or
                    self.default_peer.yfilter != YFilter.not_set or
                    self.max_peer_sa.yfilter != YFilter.not_set or
                    self.max_sa.yfilter != YFilter.not_set or
                    self.originator_id.yfilter != YFilter.not_set or
                    self.ttl_threshold.yfilter != YFilter.not_set or
                    (self.cache_state is not None and self.cache_state.has_operation()) or
                    (self.keep_alive is not None and self.keep_alive.has_operation()) or
                    (self.peers is not None and self.peers.has_operation()) or
                    (self.sa_filters is not None and self.sa_filters.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.connect_source.is_set or self.connect_source.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.connect_source.get_name_leafdata())
                if (self.default_peer.is_set or self.default_peer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.default_peer.get_name_leafdata())
                if (self.max_peer_sa.is_set or self.max_peer_sa.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_peer_sa.get_name_leafdata())
                if (self.max_sa.is_set or self.max_sa.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_sa.get_name_leafdata())
                if (self.originator_id.is_set or self.originator_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.originator_id.get_name_leafdata())
                if (self.ttl_threshold.is_set or self.ttl_threshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ttl_threshold.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "cache-state"):
                    if (self.cache_state is None):
                        self.cache_state = Msdp.Vrfs.Vrf.CacheState()
                        self.cache_state.parent = self
                        self._children_name_map["cache_state"] = "cache-state"
                    return self.cache_state

                if (child_yang_name == "keep-alive"):
                    if (self.keep_alive is None):
                        self.keep_alive = Msdp.Vrfs.Vrf.KeepAlive()
                        self.keep_alive.parent = self
                        self._children_name_map["keep_alive"] = "keep-alive"
                    return self.keep_alive

                if (child_yang_name == "peers"):
                    if (self.peers is None):
                        self.peers = Msdp.Vrfs.Vrf.Peers()
                        self.peers.parent = self
                        self._children_name_map["peers"] = "peers"
                    return self.peers

                if (child_yang_name == "sa-filters"):
                    if (self.sa_filters is None):
                        self.sa_filters = Msdp.Vrfs.Vrf.SaFilters()
                        self.sa_filters.parent = self
                        self._children_name_map["sa_filters"] = "sa-filters"
                    return self.sa_filters

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cache-state" or name == "keep-alive" or name == "peers" or name == "sa-filters" or name == "vrf-name" or name == "connect-source" or name == "default-peer" or name == "max-peer-sa" or name == "max-sa" or name == "originator-id" or name == "ttl-threshold"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "connect-source"):
                    self.connect_source = value
                    self.connect_source.value_namespace = name_space
                    self.connect_source.value_namespace_prefix = name_space_prefix
                if(value_path == "default-peer"):
                    self.default_peer = value
                    self.default_peer.value_namespace = name_space
                    self.default_peer.value_namespace_prefix = name_space_prefix
                if(value_path == "max-peer-sa"):
                    self.max_peer_sa = value
                    self.max_peer_sa.value_namespace = name_space
                    self.max_peer_sa.value_namespace_prefix = name_space_prefix
                if(value_path == "max-sa"):
                    self.max_sa = value
                    self.max_sa.value_namespace = name_space
                    self.max_sa.value_namespace_prefix = name_space_prefix
                if(value_path == "originator-id"):
                    self.originator_id = value
                    self.originator_id.value_namespace = name_space
                    self.originator_id.value_namespace_prefix = name_space_prefix
                if(value_path == "ttl-threshold"):
                    self.ttl_threshold = value
                    self.ttl_threshold.value_namespace = name_space
                    self.ttl_threshold.value_namespace_prefix = name_space_prefix

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
            path_buffer = "vrfs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/%s" % self.get_segment_path()
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
                c = Msdp.Vrfs.Vrf()
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


    class DefaultContext(Entity):
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
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-msdp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Msdp.DefaultContext, self).__init__()

            self.yang_name = "default-context"
            self.yang_parent_name = "msdp"
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

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("connect_source",
                            "default_peer",
                            "max_peer_sa",
                            "max_sa",
                            "originator_id",
                            "ttl_threshold") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Msdp.DefaultContext, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Msdp.DefaultContext, self).__setattr__(name, value)


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

                self.list = YLeaf(YType.str, "list")

                self.rp_list = YLeaf(YType.str, "rp-list")

                self.sa_holdtime = YLeaf(YType.uint32, "sa-holdtime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("list",
                                "rp_list",
                                "sa_holdtime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Msdp.DefaultContext.CacheState, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Msdp.DefaultContext.CacheState, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.list.is_set or
                    self.rp_list.is_set or
                    self.sa_holdtime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.list.yfilter != YFilter.not_set or
                    self.rp_list.yfilter != YFilter.not_set or
                    self.sa_holdtime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cache-state" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.list.is_set or self.list.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.list.get_name_leafdata())
                if (self.rp_list.is_set or self.rp_list.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rp_list.get_name_leafdata())
                if (self.sa_holdtime.is_set or self.sa_holdtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sa_holdtime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "list" or name == "rp-list" or name == "sa-holdtime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "list"):
                    self.list = value
                    self.list.value_namespace = name_space
                    self.list.value_namespace_prefix = name_space_prefix
                if(value_path == "rp-list"):
                    self.rp_list = value
                    self.rp_list.value_namespace = name_space
                    self.rp_list.value_namespace_prefix = name_space_prefix
                if(value_path == "sa-holdtime"):
                    self.sa_holdtime = value
                    self.sa_holdtime.value_namespace = name_space
                    self.sa_holdtime.value_namespace_prefix = name_space_prefix


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
                self.is_presence_container = True

                self.keep_alive_period = YLeaf(YType.uint32, "keep-alive-period")

                self.peer_timeout_period = YLeaf(YType.uint32, "peer-timeout-period")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("keep_alive_period",
                                "peer_timeout_period") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Msdp.DefaultContext.KeepAlive, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Msdp.DefaultContext.KeepAlive, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.keep_alive_period.is_set or
                    self.peer_timeout_period.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.keep_alive_period.yfilter != YFilter.not_set or
                    self.peer_timeout_period.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "keep-alive" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.keep_alive_period.is_set or self.keep_alive_period.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.keep_alive_period.get_name_leafdata())
                if (self.peer_timeout_period.is_set or self.peer_timeout_period.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.peer_timeout_period.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "keep-alive-period" or name == "peer-timeout-period"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "keep-alive-period"):
                    self.keep_alive_period = value
                    self.keep_alive_period.value_namespace = name_space
                    self.keep_alive_period.value_namespace_prefix = name_space_prefix
                if(value_path == "peer-timeout-period"):
                    self.peer_timeout_period = value
                    self.peer_timeout_period.value_namespace = name_space
                    self.peer_timeout_period.value_namespace_prefix = name_space_prefix


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

                self.peer = YList(self)

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
                            super(Msdp.DefaultContext.Peers, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Msdp.DefaultContext.Peers, self).__setattr__(name, value)


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
                    super(Msdp.DefaultContext.Peers.Peer, self).__init__()

                    self.yang_name = "peer"
                    self.yang_parent_name = "peers"

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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("peer_address",
                                    "connect_source",
                                    "description",
                                    "enable",
                                    "max_sa",
                                    "mesh_group",
                                    "nsr_down",
                                    "peer_password",
                                    "shutdown",
                                    "ttl_threshold") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Msdp.DefaultContext.Peers.Peer, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Msdp.DefaultContext.Peers.Peer, self).__setattr__(name, value)


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
                        self.is_presence_container = True

                        self.as_xx = YLeaf(YType.uint32, "as-xx")

                        self.as_yy = YLeaf(YType.uint32, "as-yy")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("as_xx",
                                        "as_yy") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Msdp.DefaultContext.Peers.Peer.RemoteAs, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Msdp.DefaultContext.Peers.Peer.RemoteAs, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.as_xx.is_set or
                            self.as_yy.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.as_xx.yfilter != YFilter.not_set or
                            self.as_yy.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "remote-as" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.as_xx.is_set or self.as_xx.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.as_xx.get_name_leafdata())
                        if (self.as_yy.is_set or self.as_yy.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.as_yy.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "as-xx" or name == "as-yy"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "as-xx"):
                            self.as_xx = value
                            self.as_xx.value_namespace = name_space
                            self.as_xx.value_namespace_prefix = name_space_prefix
                        if(value_path == "as-yy"):
                            self.as_yy = value
                            self.as_yy.value_namespace = name_space
                            self.as_yy.value_namespace_prefix = name_space_prefix


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
                        self.is_presence_container = True

                        self.keep_alive_period = YLeaf(YType.uint32, "keep-alive-period")

                        self.peer_timeout_period = YLeaf(YType.uint32, "peer-timeout-period")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("keep_alive_period",
                                        "peer_timeout_period") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Msdp.DefaultContext.Peers.Peer.KeepAlive, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Msdp.DefaultContext.Peers.Peer.KeepAlive, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.keep_alive_period.is_set or
                            self.peer_timeout_period.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.keep_alive_period.yfilter != YFilter.not_set or
                            self.peer_timeout_period.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "keep-alive" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.keep_alive_period.is_set or self.keep_alive_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.keep_alive_period.get_name_leafdata())
                        if (self.peer_timeout_period.is_set or self.peer_timeout_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_timeout_period.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "keep-alive-period" or name == "peer-timeout-period"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "keep-alive-period"):
                            self.keep_alive_period = value
                            self.keep_alive_period.value_namespace = name_space
                            self.keep_alive_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-timeout-period"):
                            self.peer_timeout_period = value
                            self.peer_timeout_period.value_namespace = name_space
                            self.peer_timeout_period.value_namespace_prefix = name_space_prefix


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

                        self.sa_filter = YList(self)

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
                                    super(Msdp.DefaultContext.Peers.Peer.SaFilters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Msdp.DefaultContext.Peers.Peer.SaFilters, self).__setattr__(name, value)


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

                            self.list = YLeaf(YType.enumeration, "list")

                            self.filter_type = YLeaf(YType.enumeration, "filter-type")

                            self.access_list_name = YLeaf(YType.str, "access-list-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("list",
                                            "filter_type",
                                            "access_list_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Msdp.DefaultContext.Peers.Peer.SaFilters.SaFilter, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Msdp.DefaultContext.Peers.Peer.SaFilters.SaFilter, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.list.is_set or
                                self.filter_type.is_set or
                                self.access_list_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.list.yfilter != YFilter.not_set or
                                self.filter_type.yfilter != YFilter.not_set or
                                self.access_list_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sa-filter" + "[list='" + self.list.get() + "']" + "[filter-type='" + self.filter_type.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.list.is_set or self.list.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.list.get_name_leafdata())
                            if (self.filter_type.is_set or self.filter_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.filter_type.get_name_leafdata())
                            if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_list_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "list" or name == "filter-type" or name == "access-list-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "list"):
                                self.list = value
                                self.list.value_namespace = name_space
                                self.list.value_namespace_prefix = name_space_prefix
                            if(value_path == "filter-type"):
                                self.filter_type = value
                                self.filter_type.value_namespace = name_space
                                self.filter_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "access-list-name"):
                                self.access_list_name = value
                                self.access_list_name.value_namespace = name_space
                                self.access_list_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.sa_filter:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.sa_filter:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sa-filters" + path_buffer

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

                        if (child_yang_name == "sa-filter"):
                            for c in self.sa_filter:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Msdp.DefaultContext.Peers.Peer.SaFilters.SaFilter()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.sa_filter.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sa-filter"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.peer_address.is_set or
                        self.connect_source.is_set or
                        self.description.is_set or
                        self.enable.is_set or
                        self.max_sa.is_set or
                        self.mesh_group.is_set or
                        self.nsr_down.is_set or
                        self.peer_password.is_set or
                        self.shutdown.is_set or
                        self.ttl_threshold.is_set or
                        (self.sa_filters is not None and self.sa_filters.has_data()) or
                        (self.keep_alive is not None) or
                        (self.remote_as is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.peer_address.yfilter != YFilter.not_set or
                        self.connect_source.yfilter != YFilter.not_set or
                        self.description.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        self.max_sa.yfilter != YFilter.not_set or
                        self.mesh_group.yfilter != YFilter.not_set or
                        self.nsr_down.yfilter != YFilter.not_set or
                        self.peer_password.yfilter != YFilter.not_set or
                        self.shutdown.yfilter != YFilter.not_set or
                        self.ttl_threshold.yfilter != YFilter.not_set or
                        (self.keep_alive is not None and self.keep_alive.has_operation()) or
                        (self.remote_as is not None and self.remote_as.has_operation()) or
                        (self.sa_filters is not None and self.sa_filters.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "peer" + "[peer-address='" + self.peer_address.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/default-context/peers/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.peer_address.is_set or self.peer_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peer_address.get_name_leafdata())
                    if (self.connect_source.is_set or self.connect_source.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.connect_source.get_name_leafdata())
                    if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.description.get_name_leafdata())
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())
                    if (self.max_sa.is_set or self.max_sa.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_sa.get_name_leafdata())
                    if (self.mesh_group.is_set or self.mesh_group.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mesh_group.get_name_leafdata())
                    if (self.nsr_down.is_set or self.nsr_down.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nsr_down.get_name_leafdata())
                    if (self.peer_password.is_set or self.peer_password.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peer_password.get_name_leafdata())
                    if (self.shutdown.is_set or self.shutdown.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.shutdown.get_name_leafdata())
                    if (self.ttl_threshold.is_set or self.ttl_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ttl_threshold.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "keep-alive"):
                        if (self.keep_alive is None):
                            self.keep_alive = Msdp.DefaultContext.Peers.Peer.KeepAlive()
                            self.keep_alive.parent = self
                            self._children_name_map["keep_alive"] = "keep-alive"
                        return self.keep_alive

                    if (child_yang_name == "remote-as"):
                        if (self.remote_as is None):
                            self.remote_as = Msdp.DefaultContext.Peers.Peer.RemoteAs()
                            self.remote_as.parent = self
                            self._children_name_map["remote_as"] = "remote-as"
                        return self.remote_as

                    if (child_yang_name == "sa-filters"):
                        if (self.sa_filters is None):
                            self.sa_filters = Msdp.DefaultContext.Peers.Peer.SaFilters()
                            self.sa_filters.parent = self
                            self._children_name_map["sa_filters"] = "sa-filters"
                        return self.sa_filters

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "keep-alive" or name == "remote-as" or name == "sa-filters" or name == "peer-address" or name == "connect-source" or name == "description" or name == "enable" or name == "max-sa" or name == "mesh-group" or name == "nsr-down" or name == "peer-password" or name == "shutdown" or name == "ttl-threshold"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "peer-address"):
                        self.peer_address = value
                        self.peer_address.value_namespace = name_space
                        self.peer_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "connect-source"):
                        self.connect_source = value
                        self.connect_source.value_namespace = name_space
                        self.connect_source.value_namespace_prefix = name_space_prefix
                    if(value_path == "description"):
                        self.description = value
                        self.description.value_namespace = name_space
                        self.description.value_namespace_prefix = name_space_prefix
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-sa"):
                        self.max_sa = value
                        self.max_sa.value_namespace = name_space
                        self.max_sa.value_namespace_prefix = name_space_prefix
                    if(value_path == "mesh-group"):
                        self.mesh_group = value
                        self.mesh_group.value_namespace = name_space
                        self.mesh_group.value_namespace_prefix = name_space_prefix
                    if(value_path == "nsr-down"):
                        self.nsr_down = value
                        self.nsr_down.value_namespace = name_space
                        self.nsr_down.value_namespace_prefix = name_space_prefix
                    if(value_path == "peer-password"):
                        self.peer_password = value
                        self.peer_password.value_namespace = name_space
                        self.peer_password.value_namespace_prefix = name_space_prefix
                    if(value_path == "shutdown"):
                        self.shutdown = value
                        self.shutdown.value_namespace = name_space
                        self.shutdown.value_namespace_prefix = name_space_prefix
                    if(value_path == "ttl-threshold"):
                        self.ttl_threshold = value
                        self.ttl_threshold.value_namespace = name_space
                        self.ttl_threshold.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.peer:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.peer:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "peers" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "peer"):
                    for c in self.peer:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Msdp.DefaultContext.Peers.Peer()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.peer.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "peer"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


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

                self.sa_filter = YList(self)

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
                            super(Msdp.DefaultContext.SaFilters, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Msdp.DefaultContext.SaFilters, self).__setattr__(name, value)


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

                    self.list = YLeaf(YType.enumeration, "list")

                    self.filter_type = YLeaf(YType.enumeration, "filter-type")

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("list",
                                    "filter_type",
                                    "access_list_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Msdp.DefaultContext.SaFilters.SaFilter, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Msdp.DefaultContext.SaFilters.SaFilter, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.list.is_set or
                        self.filter_type.is_set or
                        self.access_list_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.list.yfilter != YFilter.not_set or
                        self.filter_type.yfilter != YFilter.not_set or
                        self.access_list_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "sa-filter" + "[list='" + self.list.get() + "']" + "[filter-type='" + self.filter_type.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/default-context/sa-filters/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.list.is_set or self.list.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.list.get_name_leafdata())
                    if (self.filter_type.is_set or self.filter_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.filter_type.get_name_leafdata())
                    if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_list_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "list" or name == "filter-type" or name == "access-list-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "list"):
                        self.list = value
                        self.list.value_namespace = name_space
                        self.list.value_namespace_prefix = name_space_prefix
                    if(value_path == "filter-type"):
                        self.filter_type = value
                        self.filter_type.value_namespace = name_space
                        self.filter_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "access-list-name"):
                        self.access_list_name = value
                        self.access_list_name.value_namespace = name_space
                        self.access_list_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.sa_filter:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.sa_filter:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sa-filters" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "sa-filter"):
                    for c in self.sa_filter:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Msdp.DefaultContext.SaFilters.SaFilter()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.sa_filter.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "sa-filter"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.connect_source.is_set or
                self.default_peer.is_set or
                self.max_peer_sa.is_set or
                self.max_sa.is_set or
                self.originator_id.is_set or
                self.ttl_threshold.is_set or
                (self.cache_state is not None and self.cache_state.has_data()) or
                (self.peers is not None and self.peers.has_data()) or
                (self.sa_filters is not None and self.sa_filters.has_data()) or
                (self.keep_alive is not None))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.connect_source.yfilter != YFilter.not_set or
                self.default_peer.yfilter != YFilter.not_set or
                self.max_peer_sa.yfilter != YFilter.not_set or
                self.max_sa.yfilter != YFilter.not_set or
                self.originator_id.yfilter != YFilter.not_set or
                self.ttl_threshold.yfilter != YFilter.not_set or
                (self.cache_state is not None and self.cache_state.has_operation()) or
                (self.keep_alive is not None and self.keep_alive.has_operation()) or
                (self.peers is not None and self.peers.has_operation()) or
                (self.sa_filters is not None and self.sa_filters.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "default-context" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-msdp-cfg:msdp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.connect_source.is_set or self.connect_source.yfilter != YFilter.not_set):
                leaf_name_data.append(self.connect_source.get_name_leafdata())
            if (self.default_peer.is_set or self.default_peer.yfilter != YFilter.not_set):
                leaf_name_data.append(self.default_peer.get_name_leafdata())
            if (self.max_peer_sa.is_set or self.max_peer_sa.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_peer_sa.get_name_leafdata())
            if (self.max_sa.is_set or self.max_sa.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_sa.get_name_leafdata())
            if (self.originator_id.is_set or self.originator_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.originator_id.get_name_leafdata())
            if (self.ttl_threshold.is_set or self.ttl_threshold.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ttl_threshold.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cache-state"):
                if (self.cache_state is None):
                    self.cache_state = Msdp.DefaultContext.CacheState()
                    self.cache_state.parent = self
                    self._children_name_map["cache_state"] = "cache-state"
                return self.cache_state

            if (child_yang_name == "keep-alive"):
                if (self.keep_alive is None):
                    self.keep_alive = Msdp.DefaultContext.KeepAlive()
                    self.keep_alive.parent = self
                    self._children_name_map["keep_alive"] = "keep-alive"
                return self.keep_alive

            if (child_yang_name == "peers"):
                if (self.peers is None):
                    self.peers = Msdp.DefaultContext.Peers()
                    self.peers.parent = self
                    self._children_name_map["peers"] = "peers"
                return self.peers

            if (child_yang_name == "sa-filters"):
                if (self.sa_filters is None):
                    self.sa_filters = Msdp.DefaultContext.SaFilters()
                    self.sa_filters.parent = self
                    self._children_name_map["sa_filters"] = "sa-filters"
                return self.sa_filters

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cache-state" or name == "keep-alive" or name == "peers" or name == "sa-filters" or name == "connect-source" or name == "default-peer" or name == "max-peer-sa" or name == "max-sa" or name == "originator-id" or name == "ttl-threshold"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "connect-source"):
                self.connect_source = value
                self.connect_source.value_namespace = name_space
                self.connect_source.value_namespace_prefix = name_space_prefix
            if(value_path == "default-peer"):
                self.default_peer = value
                self.default_peer.value_namespace = name_space
                self.default_peer.value_namespace_prefix = name_space_prefix
            if(value_path == "max-peer-sa"):
                self.max_peer_sa = value
                self.max_peer_sa.value_namespace = name_space
                self.max_peer_sa.value_namespace_prefix = name_space_prefix
            if(value_path == "max-sa"):
                self.max_sa = value
                self.max_sa.value_namespace = name_space
                self.max_sa.value_namespace_prefix = name_space_prefix
            if(value_path == "originator-id"):
                self.originator_id = value
                self.originator_id.value_namespace = name_space
                self.originator_id.value_namespace_prefix = name_space_prefix
            if(value_path == "ttl-threshold"):
                self.ttl_threshold = value
                self.ttl_threshold.value_namespace = name_space
                self.ttl_threshold.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.global_max_sa.is_set or
            self.nsr_delay.is_set or
            (self.vrfs is not None and self.vrfs.has_data()) or
            (self.default_context is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.global_max_sa.yfilter != YFilter.not_set or
            self.nsr_delay.yfilter != YFilter.not_set or
            (self.default_context is not None and self.default_context.has_operation()) or
            (self.vrfs is not None and self.vrfs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-msdp-cfg:msdp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.global_max_sa.is_set or self.global_max_sa.yfilter != YFilter.not_set):
            leaf_name_data.append(self.global_max_sa.get_name_leafdata())
        if (self.nsr_delay.is_set or self.nsr_delay.yfilter != YFilter.not_set):
            leaf_name_data.append(self.nsr_delay.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "default-context"):
            if (self.default_context is None):
                self.default_context = Msdp.DefaultContext()
                self.default_context.parent = self
                self._children_name_map["default_context"] = "default-context"
            return self.default_context

        if (child_yang_name == "vrfs"):
            if (self.vrfs is None):
                self.vrfs = Msdp.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
            return self.vrfs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "default-context" or name == "vrfs" or name == "global-max-sa" or name == "nsr-delay"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "global-max-sa"):
            self.global_max_sa = value
            self.global_max_sa.value_namespace = name_space
            self.global_max_sa.value_namespace_prefix = name_space_prefix
        if(value_path == "nsr-delay"):
            self.nsr_delay = value
            self.nsr_delay.value_namespace = name_space
            self.nsr_delay.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Msdp()
        return self._top_entity


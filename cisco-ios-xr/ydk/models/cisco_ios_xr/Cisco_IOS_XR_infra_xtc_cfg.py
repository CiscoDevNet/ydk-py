""" Cisco_IOS_XR_infra_xtc_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-xtc package configuration.

This module contains definitions
for the following management objects\:
  pce\: PCE configuration data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class PceDisjointPath(Enum):
    """
    PceDisjointPath

    Pce disjoint path

    .. data:: link = 1

    	Link

    .. data:: node = 2

    	Node

    .. data:: srlg = 3

    	SRLG

    """

    link = Enum.YLeaf(1, "link")

    node = Enum.YLeaf(2, "node")

    srlg = Enum.YLeaf(3, "srlg")


class PceExplicitPathHop(Enum):
    """
    PceExplicitPathHop

    Pce explicit path hop

    .. data:: address = 1

    	Address

    .. data:: sid_node = 2

    	SID Node

    .. data:: sid_adjancency = 3

    	SID Adjacency

    .. data:: binding_sid = 4

    	Binding SID

    """

    address = Enum.YLeaf(1, "address")

    sid_node = Enum.YLeaf(2, "sid-node")

    sid_adjancency = Enum.YLeaf(3, "sid-adjancency")

    binding_sid = Enum.YLeaf(4, "binding-sid")



class Pce(Entity):
    """
    PCE configuration data
    
    .. attribute:: backoff
    
    	PCE backoff configuration
    	**type**\:   :py:class:`Backoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Backoff>`
    
    .. attribute:: disjoint_path
    
    	Disjoint path configuration
    	**type**\:   :py:class:`DisjointPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.DisjointPath>`
    
    .. attribute:: enable
    
    	True only
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: explicit_paths
    
    	Explicit paths
    	**type**\:   :py:class:`ExplicitPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.ExplicitPaths>`
    
    .. attribute:: logging
    
    	PCE logging configuration
    	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Logging>`
    
    .. attribute:: netconf
    
    	NETCONF configuration
    	**type**\:   :py:class:`Netconf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Netconf>`
    
    .. attribute:: password
    
    	MD5 password
    	**type**\:  str
    
    	**pattern:** (!.+)\|([^!].+)
    
    .. attribute:: pcc_addresses
    
    	Path computation client configuration
    	**type**\:   :py:class:`PccAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses>`
    
    .. attribute:: segment_routing
    
    	PCE segment\-routing configuration
    	**type**\:   :py:class:`SegmentRouting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting>`
    
    .. attribute:: server_address
    
    	IPv4 address of PCE server
    	**type**\:  str
    
    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
    
    .. attribute:: state_syncs
    
    	Standby PCE configuration
    	**type**\:   :py:class:`StateSyncs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.StateSyncs>`
    
    .. attribute:: timers
    
    	PCE Timers configuration
    	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Timers>`
    
    

    """

    _prefix = 'infra-xtc-cfg'
    _revision = '2016-05-31'

    def __init__(self):
        super(Pce, self).__init__()
        self._top_entity = None

        self.yang_name = "pce"
        self.yang_parent_name = "Cisco-IOS-XR-infra-xtc-cfg"

        self.enable = YLeaf(YType.empty, "enable")

        self.password = YLeaf(YType.str, "password")

        self.server_address = YLeaf(YType.str, "server-address")

        self.backoff = Pce.Backoff()
        self.backoff.parent = self
        self._children_name_map["backoff"] = "backoff"
        self._children_yang_names.add("backoff")

        self.disjoint_path = Pce.DisjointPath()
        self.disjoint_path.parent = self
        self._children_name_map["disjoint_path"] = "disjoint-path"
        self._children_yang_names.add("disjoint-path")

        self.explicit_paths = Pce.ExplicitPaths()
        self.explicit_paths.parent = self
        self._children_name_map["explicit_paths"] = "explicit-paths"
        self._children_yang_names.add("explicit-paths")

        self.logging = Pce.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"
        self._children_yang_names.add("logging")

        self.netconf = Pce.Netconf()
        self.netconf.parent = self
        self._children_name_map["netconf"] = "netconf"
        self._children_yang_names.add("netconf")

        self.pcc_addresses = Pce.PccAddresses()
        self.pcc_addresses.parent = self
        self._children_name_map["pcc_addresses"] = "pcc-addresses"
        self._children_yang_names.add("pcc-addresses")

        self.segment_routing = Pce.SegmentRouting()
        self.segment_routing.parent = self
        self._children_name_map["segment_routing"] = "segment-routing"
        self._children_yang_names.add("segment-routing")

        self.state_syncs = Pce.StateSyncs()
        self.state_syncs.parent = self
        self._children_name_map["state_syncs"] = "state-syncs"
        self._children_yang_names.add("state-syncs")

        self.timers = Pce.Timers()
        self.timers.parent = self
        self._children_name_map["timers"] = "timers"
        self._children_yang_names.add("timers")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("enable",
                        "password",
                        "server_address") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Pce, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Pce, self).__setattr__(name, value)


    class PccAddresses(Entity):
        """
        Path computation client configuration
        
        .. attribute:: pcc_address
        
        	Path computation client address
        	**type**\: list of    :py:class:`PccAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.PccAddresses, self).__init__()

            self.yang_name = "pcc-addresses"
            self.yang_parent_name = "pce"

            self.pcc_address = YList(self)

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
                        super(Pce.PccAddresses, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Pce.PccAddresses, self).__setattr__(name, value)


        class PccAddress(Entity):
            """
            Path computation client address
            
            .. attribute:: address  <key>
            
            	IPv4 address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: enable
            
            	True only
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: lsp_names
            
            	MPLS label switched path
            	**type**\:   :py:class:`LspNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress.LspNames>`
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2016-05-31'

            def __init__(self):
                super(Pce.PccAddresses.PccAddress, self).__init__()

                self.yang_name = "pcc-address"
                self.yang_parent_name = "pcc-addresses"

                self.address = YLeaf(YType.str, "address")

                self.enable = YLeaf(YType.empty, "enable")

                self.lsp_names = Pce.PccAddresses.PccAddress.LspNames()
                self.lsp_names.parent = self
                self._children_name_map["lsp_names"] = "lsp-names"
                self._children_yang_names.add("lsp-names")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("address",
                                "enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Pce.PccAddresses.PccAddress, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Pce.PccAddresses.PccAddress, self).__setattr__(name, value)


            class LspNames(Entity):
                """
                MPLS label switched path
                
                .. attribute:: lsp_name
                
                	MPLS label switched path
                	**type**\: list of    :py:class:`LspName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress.LspNames.LspName>`
                
                

                """

                _prefix = 'infra-xtc-cfg'
                _revision = '2016-05-31'

                def __init__(self):
                    super(Pce.PccAddresses.PccAddress.LspNames, self).__init__()

                    self.yang_name = "lsp-names"
                    self.yang_parent_name = "pcc-address"

                    self.lsp_name = YList(self)

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
                                super(Pce.PccAddresses.PccAddress.LspNames, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Pce.PccAddresses.PccAddress.LspNames, self).__setattr__(name, value)


                class LspName(Entity):
                    """
                    MPLS label switched path
                    
                    .. attribute:: name  <key>
                    
                    	LSP name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: enable
                    
                    	True only
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: explicit_path_name
                    
                    	Explicit\-path name
                    	**type**\:  str
                    
                    .. attribute:: rsvp_te
                    
                    	RSVP\-TE configuration
                    	**type**\:   :py:class:`RsvpTe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe>`
                    
                    .. attribute:: undelegate
                    
                    	Undelegate LSP
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-xtc-cfg'
                    _revision = '2016-05-31'

                    def __init__(self):
                        super(Pce.PccAddresses.PccAddress.LspNames.LspName, self).__init__()

                        self.yang_name = "lsp-name"
                        self.yang_parent_name = "lsp-names"

                        self.name = YLeaf(YType.str, "name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.explicit_path_name = YLeaf(YType.str, "explicit-path-name")

                        self.undelegate = YLeaf(YType.empty, "undelegate")

                        self.rsvp_te = Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe()
                        self.rsvp_te.parent = self
                        self._children_name_map["rsvp_te"] = "rsvp-te"
                        self._children_yang_names.add("rsvp-te")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("name",
                                        "enable",
                                        "explicit_path_name",
                                        "undelegate") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pce.PccAddresses.PccAddress.LspNames.LspName, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pce.PccAddresses.PccAddress.LspNames.LspName, self).__setattr__(name, value)


                    class RsvpTe(Entity):
                        """
                        RSVP\-TE configuration
                        
                        .. attribute:: affinity
                        
                        	LSP Affinity
                        	**type**\:   :py:class:`Affinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity>`
                        
                        .. attribute:: bandwidth
                        
                        	Bandwidth configuration
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**units**\: kbit/s
                        
                        .. attribute:: enable
                        
                        	True only
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: fast_protect
                        
                        	Enable fast protection
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: priority
                        
                        	Tunnel Setup and Hold Priorities
                        	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority>`
                        
                        	**presence node**\: True
                        
                        

                        """

                        _prefix = 'infra-xtc-cfg'
                        _revision = '2016-05-31'

                        def __init__(self):
                            super(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe, self).__init__()

                            self.yang_name = "rsvp-te"
                            self.yang_parent_name = "lsp-name"

                            self.bandwidth = YLeaf(YType.int32, "bandwidth")

                            self.enable = YLeaf(YType.empty, "enable")

                            self.fast_protect = YLeaf(YType.empty, "fast-protect")

                            self.affinity = Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity()
                            self.affinity.parent = self
                            self._children_name_map["affinity"] = "affinity"
                            self._children_yang_names.add("affinity")

                            self.priority = None
                            self._children_name_map["priority"] = "priority"
                            self._children_yang_names.add("priority")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("bandwidth",
                                            "enable",
                                            "fast_protect") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe, self).__setattr__(name, value)


                        class Affinity(Entity):
                            """
                            LSP Affinity
                            
                            .. attribute:: exclude_any
                            
                            	Exclude\-any affinity value
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: include_all
                            
                            	Include\-all affinity value
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: include_any
                            
                            	Include\-any affinity value
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            

                            """

                            _prefix = 'infra-xtc-cfg'
                            _revision = '2016-05-31'

                            def __init__(self):
                                super(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity, self).__init__()

                                self.yang_name = "affinity"
                                self.yang_parent_name = "rsvp-te"

                                self.exclude_any = YLeaf(YType.str, "exclude-any")

                                self.include_all = YLeaf(YType.str, "include-all")

                                self.include_any = YLeaf(YType.str, "include-any")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("exclude_any",
                                                "include_all",
                                                "include_any") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.exclude_any.is_set or
                                    self.include_all.is_set or
                                    self.include_any.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.exclude_any.yfilter != YFilter.not_set or
                                    self.include_all.yfilter != YFilter.not_set or
                                    self.include_any.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "affinity" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.exclude_any.is_set or self.exclude_any.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.exclude_any.get_name_leafdata())
                                if (self.include_all.is_set or self.include_all.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.include_all.get_name_leafdata())
                                if (self.include_any.is_set or self.include_any.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.include_any.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "exclude-any" or name == "include-all" or name == "include-any"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "exclude-any"):
                                    self.exclude_any = value
                                    self.exclude_any.value_namespace = name_space
                                    self.exclude_any.value_namespace_prefix = name_space_prefix
                                if(value_path == "include-all"):
                                    self.include_all = value
                                    self.include_all.value_namespace = name_space
                                    self.include_all.value_namespace_prefix = name_space_prefix
                                if(value_path == "include-any"):
                                    self.include_any = value
                                    self.include_any.value_namespace = name_space
                                    self.include_any.value_namespace_prefix = name_space_prefix


                        class Priority(Entity):
                            """
                            Tunnel Setup and Hold Priorities
                            
                            .. attribute:: hold_priority
                            
                            	Hold Priority
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            	**mandatory**\: True
                            
                            .. attribute:: setup_priority
                            
                            	Setup Priority
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'infra-xtc-cfg'
                            _revision = '2016-05-31'

                            def __init__(self):
                                super(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority, self).__init__()

                                self.yang_name = "priority"
                                self.yang_parent_name = "rsvp-te"
                                self.is_presence_container = True

                                self.hold_priority = YLeaf(YType.uint32, "hold-priority")

                                self.setup_priority = YLeaf(YType.uint32, "setup-priority")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("hold_priority",
                                                "setup_priority") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.hold_priority.is_set or
                                    self.setup_priority.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.hold_priority.yfilter != YFilter.not_set or
                                    self.setup_priority.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "priority" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.hold_priority.is_set or self.hold_priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hold_priority.get_name_leafdata())
                                if (self.setup_priority.is_set or self.setup_priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.setup_priority.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "hold-priority" or name == "setup-priority"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "hold-priority"):
                                    self.hold_priority = value
                                    self.hold_priority.value_namespace = name_space
                                    self.hold_priority.value_namespace_prefix = name_space_prefix
                                if(value_path == "setup-priority"):
                                    self.setup_priority = value
                                    self.setup_priority.value_namespace = name_space
                                    self.setup_priority.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.bandwidth.is_set or
                                self.enable.is_set or
                                self.fast_protect.is_set or
                                (self.affinity is not None and self.affinity.has_data()) or
                                (self.priority is not None))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.bandwidth.yfilter != YFilter.not_set or
                                self.enable.yfilter != YFilter.not_set or
                                self.fast_protect.yfilter != YFilter.not_set or
                                (self.affinity is not None and self.affinity.has_operation()) or
                                (self.priority is not None and self.priority.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rsvp-te" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.bandwidth.is_set or self.bandwidth.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bandwidth.get_name_leafdata())
                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.enable.get_name_leafdata())
                            if (self.fast_protect.is_set or self.fast_protect.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fast_protect.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "affinity"):
                                if (self.affinity is None):
                                    self.affinity = Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity()
                                    self.affinity.parent = self
                                    self._children_name_map["affinity"] = "affinity"
                                return self.affinity

                            if (child_yang_name == "priority"):
                                if (self.priority is None):
                                    self.priority = Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority()
                                    self.priority.parent = self
                                    self._children_name_map["priority"] = "priority"
                                return self.priority

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "affinity" or name == "priority" or name == "bandwidth" or name == "enable" or name == "fast-protect"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "bandwidth"):
                                self.bandwidth = value
                                self.bandwidth.value_namespace = name_space
                                self.bandwidth.value_namespace_prefix = name_space_prefix
                            if(value_path == "enable"):
                                self.enable = value
                                self.enable.value_namespace = name_space
                                self.enable.value_namespace_prefix = name_space_prefix
                            if(value_path == "fast-protect"):
                                self.fast_protect = value
                                self.fast_protect.value_namespace = name_space
                                self.fast_protect.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.name.is_set or
                            self.enable.is_set or
                            self.explicit_path_name.is_set or
                            self.undelegate.is_set or
                            (self.rsvp_te is not None and self.rsvp_te.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set or
                            self.explicit_path_name.yfilter != YFilter.not_set or
                            self.undelegate.yfilter != YFilter.not_set or
                            (self.rsvp_te is not None and self.rsvp_te.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "lsp-name" + "[name='" + self.name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())
                        if (self.explicit_path_name.is_set or self.explicit_path_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.explicit_path_name.get_name_leafdata())
                        if (self.undelegate.is_set or self.undelegate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.undelegate.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "rsvp-te"):
                            if (self.rsvp_te is None):
                                self.rsvp_te = Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe()
                                self.rsvp_te.parent = self
                                self._children_name_map["rsvp_te"] = "rsvp-te"
                            return self.rsvp_te

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "rsvp-te" or name == "name" or name == "enable" or name == "explicit-path-name" or name == "undelegate"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix
                        if(value_path == "explicit-path-name"):
                            self.explicit_path_name = value
                            self.explicit_path_name.value_namespace = name_space
                            self.explicit_path_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "undelegate"):
                            self.undelegate = value
                            self.undelegate.value_namespace = name_space
                            self.undelegate.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.lsp_name:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.lsp_name:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "lsp-names" + path_buffer

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

                    if (child_yang_name == "lsp-name"):
                        for c in self.lsp_name:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Pce.PccAddresses.PccAddress.LspNames.LspName()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.lsp_name.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "lsp-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.address.is_set or
                    self.enable.is_set or
                    (self.lsp_names is not None and self.lsp_names.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.address.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    (self.lsp_names is not None and self.lsp_names.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pcc-address" + "[address='" + self.address.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce/pcc-addresses/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.address.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "lsp-names"):
                    if (self.lsp_names is None):
                        self.lsp_names = Pce.PccAddresses.PccAddress.LspNames()
                        self.lsp_names.parent = self
                        self._children_name_map["lsp_names"] = "lsp-names"
                    return self.lsp_names

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "lsp-names" or name == "address" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "address"):
                    self.address = value
                    self.address.value_namespace = name_space
                    self.address.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.pcc_address:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.pcc_address:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "pcc-addresses" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "pcc-address"):
                for c in self.pcc_address:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Pce.PccAddresses.PccAddress()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.pcc_address.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pcc-address"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Logging(Entity):
        """
        PCE logging configuration
        
        .. attribute:: fallback
        
        	Logging fallback configuration
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: no_path
        
        	Logging NO\-PATH configuration
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "pce"

            self.fallback = YLeaf(YType.empty, "fallback")

            self.no_path = YLeaf(YType.empty, "no-path")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("fallback",
                            "no_path") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Pce.Logging, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Pce.Logging, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.fallback.is_set or
                self.no_path.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.fallback.yfilter != YFilter.not_set or
                self.no_path.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "logging" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.fallback.is_set or self.fallback.yfilter != YFilter.not_set):
                leaf_name_data.append(self.fallback.get_name_leafdata())
            if (self.no_path.is_set or self.no_path.yfilter != YFilter.not_set):
                leaf_name_data.append(self.no_path.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "fallback" or name == "no-path"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "fallback"):
                self.fallback = value
                self.fallback.value_namespace = name_space
                self.fallback.value_namespace_prefix = name_space_prefix
            if(value_path == "no-path"):
                self.no_path = value
                self.no_path.value_namespace = name_space
                self.no_path.value_namespace_prefix = name_space_prefix


    class Backoff(Entity):
        """
        PCE backoff configuration
        
        .. attribute:: difference
        
        	Backoff common difference configuration
        	**type**\:  int
        
        	**range:** 0..255
        
        	**default value**\: 2
        
        .. attribute:: ratio
        
        	Backoff common ratio configuration
        	**type**\:  int
        
        	**range:** 0..255
        
        	**default value**\: 2
        
        .. attribute:: threshold
        
        	Backoff threshold configuration
        	**type**\:  int
        
        	**range:** 0..3600
        
        	**default value**\: 0
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.Backoff, self).__init__()

            self.yang_name = "backoff"
            self.yang_parent_name = "pce"

            self.difference = YLeaf(YType.uint32, "difference")

            self.ratio = YLeaf(YType.uint32, "ratio")

            self.threshold = YLeaf(YType.uint32, "threshold")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("difference",
                            "ratio",
                            "threshold") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Pce.Backoff, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Pce.Backoff, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.difference.is_set or
                self.ratio.is_set or
                self.threshold.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.difference.yfilter != YFilter.not_set or
                self.ratio.yfilter != YFilter.not_set or
                self.threshold.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "backoff" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.difference.is_set or self.difference.yfilter != YFilter.not_set):
                leaf_name_data.append(self.difference.get_name_leafdata())
            if (self.ratio.is_set or self.ratio.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ratio.get_name_leafdata())
            if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                leaf_name_data.append(self.threshold.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "difference" or name == "ratio" or name == "threshold"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "difference"):
                self.difference = value
                self.difference.value_namespace = name_space
                self.difference.value_namespace_prefix = name_space_prefix
            if(value_path == "ratio"):
                self.ratio = value
                self.ratio.value_namespace = name_space
                self.ratio.value_namespace_prefix = name_space_prefix
            if(value_path == "threshold"):
                self.threshold = value
                self.threshold.value_namespace = name_space
                self.threshold.value_namespace_prefix = name_space_prefix


    class StateSyncs(Entity):
        """
        Standby PCE configuration
        
        .. attribute:: state_sync
        
        	Standby PCE ipv4 address
        	**type**\: list of    :py:class:`StateSync <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.StateSyncs.StateSync>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.StateSyncs, self).__init__()

            self.yang_name = "state-syncs"
            self.yang_parent_name = "pce"

            self.state_sync = YList(self)

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
                        super(Pce.StateSyncs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Pce.StateSyncs, self).__setattr__(name, value)


        class StateSync(Entity):
            """
            Standby PCE ipv4 address
            
            .. attribute:: address  <key>
            
            	IPv4 address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2016-05-31'

            def __init__(self):
                super(Pce.StateSyncs.StateSync, self).__init__()

                self.yang_name = "state-sync"
                self.yang_parent_name = "state-syncs"

                self.address = YLeaf(YType.str, "address")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("address") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Pce.StateSyncs.StateSync, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Pce.StateSyncs.StateSync, self).__setattr__(name, value)

            def has_data(self):
                return self.address.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.address.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "state-sync" + "[address='" + self.address.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce/state-syncs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.address.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "address"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "address"):
                    self.address = value
                    self.address.value_namespace = name_space
                    self.address.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.state_sync:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.state_sync:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "state-syncs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "state-sync"):
                for c in self.state_sync:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Pce.StateSyncs.StateSync()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.state_sync.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "state-sync"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class SegmentRouting(Entity):
        """
        PCE segment\-routing configuration
        
        .. attribute:: strict_sid_only
        
        	Use strict\-sid\-only configuration
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: te_latency
        
        	Use te\-latency algorithm configuration
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.SegmentRouting, self).__init__()

            self.yang_name = "segment-routing"
            self.yang_parent_name = "pce"

            self.strict_sid_only = YLeaf(YType.empty, "strict-sid-only")

            self.te_latency = YLeaf(YType.empty, "te-latency")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("strict_sid_only",
                            "te_latency") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Pce.SegmentRouting, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Pce.SegmentRouting, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.strict_sid_only.is_set or
                self.te_latency.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.strict_sid_only.yfilter != YFilter.not_set or
                self.te_latency.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "segment-routing" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.strict_sid_only.is_set or self.strict_sid_only.yfilter != YFilter.not_set):
                leaf_name_data.append(self.strict_sid_only.get_name_leafdata())
            if (self.te_latency.is_set or self.te_latency.yfilter != YFilter.not_set):
                leaf_name_data.append(self.te_latency.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "strict-sid-only" or name == "te-latency"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "strict-sid-only"):
                self.strict_sid_only = value
                self.strict_sid_only.value_namespace = name_space
                self.strict_sid_only.value_namespace_prefix = name_space_prefix
            if(value_path == "te-latency"):
                self.te_latency = value
                self.te_latency.value_namespace = name_space
                self.te_latency.value_namespace_prefix = name_space_prefix


    class Timers(Entity):
        """
        PCE Timers configuration
        
        .. attribute:: keepalive
        
        	Keepalive interval in seconds, zero to disable
        	**type**\:  int
        
        	**range:** 0..255
        
        	**units**\: second
        
        	**default value**\: 30
        
        .. attribute:: minimum_peer_keepalive
        
        	Minimum acceptable peer proposed keepalive interval
        	**type**\:  int
        
        	**range:** 0..255
        
        	**units**\: second
        
        	**default value**\: 20
        
        .. attribute:: reoptimization_timer
        
        	Topology reoptimization timer configuration
        	**type**\:  int
        
        	**range:** 10..3600
        
        	**units**\: second
        
        	**default value**\: 60
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.Timers, self).__init__()

            self.yang_name = "timers"
            self.yang_parent_name = "pce"

            self.keepalive = YLeaf(YType.uint32, "keepalive")

            self.minimum_peer_keepalive = YLeaf(YType.uint32, "minimum-peer-keepalive")

            self.reoptimization_timer = YLeaf(YType.uint32, "reoptimization-timer")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("keepalive",
                            "minimum_peer_keepalive",
                            "reoptimization_timer") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Pce.Timers, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Pce.Timers, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.keepalive.is_set or
                self.minimum_peer_keepalive.is_set or
                self.reoptimization_timer.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.keepalive.yfilter != YFilter.not_set or
                self.minimum_peer_keepalive.yfilter != YFilter.not_set or
                self.reoptimization_timer.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "timers" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.keepalive.is_set or self.keepalive.yfilter != YFilter.not_set):
                leaf_name_data.append(self.keepalive.get_name_leafdata())
            if (self.minimum_peer_keepalive.is_set or self.minimum_peer_keepalive.yfilter != YFilter.not_set):
                leaf_name_data.append(self.minimum_peer_keepalive.get_name_leafdata())
            if (self.reoptimization_timer.is_set or self.reoptimization_timer.yfilter != YFilter.not_set):
                leaf_name_data.append(self.reoptimization_timer.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "keepalive" or name == "minimum-peer-keepalive" or name == "reoptimization-timer"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "keepalive"):
                self.keepalive = value
                self.keepalive.value_namespace = name_space
                self.keepalive.value_namespace_prefix = name_space_prefix
            if(value_path == "minimum-peer-keepalive"):
                self.minimum_peer_keepalive = value
                self.minimum_peer_keepalive.value_namespace = name_space
                self.minimum_peer_keepalive.value_namespace_prefix = name_space_prefix
            if(value_path == "reoptimization-timer"):
                self.reoptimization_timer = value
                self.reoptimization_timer.value_namespace = name_space
                self.reoptimization_timer.value_namespace_prefix = name_space_prefix


    class Netconf(Entity):
        """
        NETCONF configuration
        
        .. attribute:: netconf_ssh
        
        	NETCONF SSH configuration
        	**type**\:   :py:class:`NetconfSsh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Netconf.NetconfSsh>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.Netconf, self).__init__()

            self.yang_name = "netconf"
            self.yang_parent_name = "pce"

            self.netconf_ssh = Pce.Netconf.NetconfSsh()
            self.netconf_ssh.parent = self
            self._children_name_map["netconf_ssh"] = "netconf-ssh"
            self._children_yang_names.add("netconf-ssh")


        class NetconfSsh(Entity):
            """
            NETCONF SSH configuration
            
            .. attribute:: netconf_ssh_password
            
            	Password to use for NETCONF SSH connections
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: netconf_ssh_user
            
            	User name to use for NETCONF SSH connections
            	**type**\:  str
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2016-05-31'

            def __init__(self):
                super(Pce.Netconf.NetconfSsh, self).__init__()

                self.yang_name = "netconf-ssh"
                self.yang_parent_name = "netconf"

                self.netconf_ssh_password = YLeaf(YType.str, "netconf-ssh-password")

                self.netconf_ssh_user = YLeaf(YType.str, "netconf-ssh-user")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("netconf_ssh_password",
                                "netconf_ssh_user") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Pce.Netconf.NetconfSsh, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Pce.Netconf.NetconfSsh, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.netconf_ssh_password.is_set or
                    self.netconf_ssh_user.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.netconf_ssh_password.yfilter != YFilter.not_set or
                    self.netconf_ssh_user.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "netconf-ssh" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce/netconf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.netconf_ssh_password.is_set or self.netconf_ssh_password.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.netconf_ssh_password.get_name_leafdata())
                if (self.netconf_ssh_user.is_set or self.netconf_ssh_user.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.netconf_ssh_user.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "netconf-ssh-password" or name == "netconf-ssh-user"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "netconf-ssh-password"):
                    self.netconf_ssh_password = value
                    self.netconf_ssh_password.value_namespace = name_space
                    self.netconf_ssh_password.value_namespace_prefix = name_space_prefix
                if(value_path == "netconf-ssh-user"):
                    self.netconf_ssh_user = value
                    self.netconf_ssh_user.value_namespace = name_space
                    self.netconf_ssh_user.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.netconf_ssh is not None and self.netconf_ssh.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.netconf_ssh is not None and self.netconf_ssh.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "netconf" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "netconf-ssh"):
                if (self.netconf_ssh is None):
                    self.netconf_ssh = Pce.Netconf.NetconfSsh()
                    self.netconf_ssh.parent = self
                    self._children_name_map["netconf_ssh"] = "netconf-ssh"
                return self.netconf_ssh

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "netconf-ssh"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class DisjointPath(Entity):
        """
        Disjoint path configuration
        
        .. attribute:: groups
        
        	Association configuration
        	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.DisjointPath.Groups>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.DisjointPath, self).__init__()

            self.yang_name = "disjoint-path"
            self.yang_parent_name = "pce"

            self.groups = Pce.DisjointPath.Groups()
            self.groups.parent = self
            self._children_name_map["groups"] = "groups"
            self._children_yang_names.add("groups")


        class Groups(Entity):
            """
            Association configuration
            
            .. attribute:: group
            
            	Association Group Configuration
            	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.DisjointPath.Groups.Group>`
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2016-05-31'

            def __init__(self):
                super(Pce.DisjointPath.Groups, self).__init__()

                self.yang_name = "groups"
                self.yang_parent_name = "disjoint-path"

                self.group = YList(self)

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
                            super(Pce.DisjointPath.Groups, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Pce.DisjointPath.Groups, self).__setattr__(name, value)


            class Group(Entity):
                """
                Association Group Configuration
                
                .. attribute:: group_id  <key>
                
                	Group ID
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: dp_type  <key>
                
                	Disjoiness type
                	**type**\:   :py:class:`PceDisjointPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.PceDisjointPath>`
                
                .. attribute:: sub_id  <key>
                
                	Sub group ID, 0 to unset
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: strict
                
                	Disable Fallback
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-xtc-cfg'
                _revision = '2016-05-31'

                def __init__(self):
                    super(Pce.DisjointPath.Groups.Group, self).__init__()

                    self.yang_name = "group"
                    self.yang_parent_name = "groups"

                    self.group_id = YLeaf(YType.uint32, "group-id")

                    self.dp_type = YLeaf(YType.enumeration, "dp-type")

                    self.sub_id = YLeaf(YType.uint32, "sub-id")

                    self.strict = YLeaf(YType.empty, "strict")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("group_id",
                                    "dp_type",
                                    "sub_id",
                                    "strict") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Pce.DisjointPath.Groups.Group, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Pce.DisjointPath.Groups.Group, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.group_id.is_set or
                        self.dp_type.is_set or
                        self.sub_id.is_set or
                        self.strict.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.group_id.yfilter != YFilter.not_set or
                        self.dp_type.yfilter != YFilter.not_set or
                        self.sub_id.yfilter != YFilter.not_set or
                        self.strict.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "group" + "[group-id='" + self.group_id.get() + "']" + "[dp-type='" + self.dp_type.get() + "']" + "[sub-id='" + self.sub_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce/disjoint-path/groups/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group_id.get_name_leafdata())
                    if (self.dp_type.is_set or self.dp_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dp_type.get_name_leafdata())
                    if (self.sub_id.is_set or self.sub_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sub_id.get_name_leafdata())
                    if (self.strict.is_set or self.strict.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.strict.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "group-id" or name == "dp-type" or name == "sub-id" or name == "strict"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "group-id"):
                        self.group_id = value
                        self.group_id.value_namespace = name_space
                        self.group_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "dp-type"):
                        self.dp_type = value
                        self.dp_type.value_namespace = name_space
                        self.dp_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "sub-id"):
                        self.sub_id = value
                        self.sub_id.value_namespace = name_space
                        self.sub_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "strict"):
                        self.strict = value
                        self.strict.value_namespace = name_space
                        self.strict.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.group:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.group:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "groups" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce/disjoint-path/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "group"):
                    for c in self.group:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Pce.DisjointPath.Groups.Group()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.group.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "group"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.groups is not None and self.groups.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.groups is not None and self.groups.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "disjoint-path" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "groups"):
                if (self.groups is None):
                    self.groups = Pce.DisjointPath.Groups()
                    self.groups.parent = self
                    self._children_name_map["groups"] = "groups"
                return self.groups

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "groups"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class ExplicitPaths(Entity):
        """
        Explicit paths
        
        .. attribute:: explicit_path
        
        	Explicit\-path configuration
        	**type**\: list of    :py:class:`ExplicitPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.ExplicitPaths.ExplicitPath>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.ExplicitPaths, self).__init__()

            self.yang_name = "explicit-paths"
            self.yang_parent_name = "pce"

            self.explicit_path = YList(self)

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
                        super(Pce.ExplicitPaths, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Pce.ExplicitPaths, self).__setattr__(name, value)


        class ExplicitPath(Entity):
            """
            Explicit\-path configuration
            
            .. attribute:: name  <key>
            
            	Explicit\-path name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: enable
            
            	True only
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: path_hops
            
            	Path Hops
            	**type**\:   :py:class:`PathHops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.ExplicitPaths.ExplicitPath.PathHops>`
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2016-05-31'

            def __init__(self):
                super(Pce.ExplicitPaths.ExplicitPath, self).__init__()

                self.yang_name = "explicit-path"
                self.yang_parent_name = "explicit-paths"

                self.name = YLeaf(YType.str, "name")

                self.enable = YLeaf(YType.empty, "enable")

                self.path_hops = Pce.ExplicitPaths.ExplicitPath.PathHops()
                self.path_hops.parent = self
                self._children_name_map["path_hops"] = "path-hops"
                self._children_yang_names.add("path-hops")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Pce.ExplicitPaths.ExplicitPath, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Pce.ExplicitPaths.ExplicitPath, self).__setattr__(name, value)


            class PathHops(Entity):
                """
                Path Hops
                
                .. attribute:: path_hop
                
                	Explicit path hop configuration
                	**type**\: list of    :py:class:`PathHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop>`
                
                

                """

                _prefix = 'infra-xtc-cfg'
                _revision = '2016-05-31'

                def __init__(self):
                    super(Pce.ExplicitPaths.ExplicitPath.PathHops, self).__init__()

                    self.yang_name = "path-hops"
                    self.yang_parent_name = "explicit-path"

                    self.path_hop = YList(self)

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
                                super(Pce.ExplicitPaths.ExplicitPath.PathHops, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Pce.ExplicitPaths.ExplicitPath.PathHops, self).__setattr__(name, value)


                class PathHop(Entity):
                    """
                    Explicit path hop configuration
                    
                    .. attribute:: index  <key>
                    
                    	Hop Index
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: address
                    
                    	IPv4 Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**default value**\: 0.0.0.0
                    
                    .. attribute:: hop_type
                    
                    	Path hop type
                    	**type**\:   :py:class:`PceExplicitPathHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.PceExplicitPathHop>`
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\:  int
                    
                    	**range:** 0..1048575
                    
                    	**default value**\: 0
                    
                    .. attribute:: remote_address
                    
                    	Remote IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**default value**\: 0.0.0.0
                    
                    

                    """

                    _prefix = 'infra-xtc-cfg'
                    _revision = '2016-05-31'

                    def __init__(self):
                        super(Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop, self).__init__()

                        self.yang_name = "path-hop"
                        self.yang_parent_name = "path-hops"

                        self.index = YLeaf(YType.uint32, "index")

                        self.address = YLeaf(YType.str, "address")

                        self.hop_type = YLeaf(YType.enumeration, "hop-type")

                        self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                        self.remote_address = YLeaf(YType.str, "remote-address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("index",
                                        "address",
                                        "hop_type",
                                        "mpls_label",
                                        "remote_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.index.is_set or
                            self.address.is_set or
                            self.hop_type.is_set or
                            self.mpls_label.is_set or
                            self.remote_address.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.index.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.hop_type.yfilter != YFilter.not_set or
                            self.mpls_label.yfilter != YFilter.not_set or
                            self.remote_address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "path-hop" + "[index='" + self.index.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.index.get_name_leafdata())
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.hop_type.is_set or self.hop_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hop_type.get_name_leafdata())
                        if (self.mpls_label.is_set or self.mpls_label.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mpls_label.get_name_leafdata())
                        if (self.remote_address.is_set or self.remote_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "index" or name == "address" or name == "hop-type" or name == "mpls-label" or name == "remote-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "index"):
                            self.index = value
                            self.index.value_namespace = name_space
                            self.index.value_namespace_prefix = name_space_prefix
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "hop-type"):
                            self.hop_type = value
                            self.hop_type.value_namespace = name_space
                            self.hop_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "mpls-label"):
                            self.mpls_label = value
                            self.mpls_label.value_namespace = name_space
                            self.mpls_label.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-address"):
                            self.remote_address = value
                            self.remote_address.value_namespace = name_space
                            self.remote_address.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.path_hop:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.path_hop:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "path-hops" + path_buffer

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

                    if (child_yang_name == "path-hop"):
                        for c in self.path_hop:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.path_hop.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "path-hop"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.name.is_set or
                    self.enable.is_set or
                    (self.path_hops is not None and self.path_hops.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    (self.path_hops is not None and self.path_hops.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "explicit-path" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce/explicit-paths/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "path-hops"):
                    if (self.path_hops is None):
                        self.path_hops = Pce.ExplicitPaths.ExplicitPath.PathHops()
                        self.path_hops.parent = self
                        self._children_name_map["path_hops"] = "path-hops"
                    return self.path_hops

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "path-hops" or name == "name" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.explicit_path:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.explicit_path:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "explicit-paths" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "explicit-path"):
                for c in self.explicit_path:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Pce.ExplicitPaths.ExplicitPath()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.explicit_path.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "explicit-path"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.enable.is_set or
            self.password.is_set or
            self.server_address.is_set or
            (self.backoff is not None and self.backoff.has_data()) or
            (self.disjoint_path is not None and self.disjoint_path.has_data()) or
            (self.explicit_paths is not None and self.explicit_paths.has_data()) or
            (self.logging is not None and self.logging.has_data()) or
            (self.netconf is not None and self.netconf.has_data()) or
            (self.pcc_addresses is not None and self.pcc_addresses.has_data()) or
            (self.segment_routing is not None and self.segment_routing.has_data()) or
            (self.state_syncs is not None and self.state_syncs.has_data()) or
            (self.timers is not None and self.timers.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            self.password.yfilter != YFilter.not_set or
            self.server_address.yfilter != YFilter.not_set or
            (self.backoff is not None and self.backoff.has_operation()) or
            (self.disjoint_path is not None and self.disjoint_path.has_operation()) or
            (self.explicit_paths is not None and self.explicit_paths.has_operation()) or
            (self.logging is not None and self.logging.has_operation()) or
            (self.netconf is not None and self.netconf.has_operation()) or
            (self.pcc_addresses is not None and self.pcc_addresses.has_operation()) or
            (self.segment_routing is not None and self.segment_routing.has_operation()) or
            (self.state_syncs is not None and self.state_syncs.has_operation()) or
            (self.timers is not None and self.timers.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-xtc-cfg:pce" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())
        if (self.password.is_set or self.password.yfilter != YFilter.not_set):
            leaf_name_data.append(self.password.get_name_leafdata())
        if (self.server_address.is_set or self.server_address.yfilter != YFilter.not_set):
            leaf_name_data.append(self.server_address.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "backoff"):
            if (self.backoff is None):
                self.backoff = Pce.Backoff()
                self.backoff.parent = self
                self._children_name_map["backoff"] = "backoff"
            return self.backoff

        if (child_yang_name == "disjoint-path"):
            if (self.disjoint_path is None):
                self.disjoint_path = Pce.DisjointPath()
                self.disjoint_path.parent = self
                self._children_name_map["disjoint_path"] = "disjoint-path"
            return self.disjoint_path

        if (child_yang_name == "explicit-paths"):
            if (self.explicit_paths is None):
                self.explicit_paths = Pce.ExplicitPaths()
                self.explicit_paths.parent = self
                self._children_name_map["explicit_paths"] = "explicit-paths"
            return self.explicit_paths

        if (child_yang_name == "logging"):
            if (self.logging is None):
                self.logging = Pce.Logging()
                self.logging.parent = self
                self._children_name_map["logging"] = "logging"
            return self.logging

        if (child_yang_name == "netconf"):
            if (self.netconf is None):
                self.netconf = Pce.Netconf()
                self.netconf.parent = self
                self._children_name_map["netconf"] = "netconf"
            return self.netconf

        if (child_yang_name == "pcc-addresses"):
            if (self.pcc_addresses is None):
                self.pcc_addresses = Pce.PccAddresses()
                self.pcc_addresses.parent = self
                self._children_name_map["pcc_addresses"] = "pcc-addresses"
            return self.pcc_addresses

        if (child_yang_name == "segment-routing"):
            if (self.segment_routing is None):
                self.segment_routing = Pce.SegmentRouting()
                self.segment_routing.parent = self
                self._children_name_map["segment_routing"] = "segment-routing"
            return self.segment_routing

        if (child_yang_name == "state-syncs"):
            if (self.state_syncs is None):
                self.state_syncs = Pce.StateSyncs()
                self.state_syncs.parent = self
                self._children_name_map["state_syncs"] = "state-syncs"
            return self.state_syncs

        if (child_yang_name == "timers"):
            if (self.timers is None):
                self.timers = Pce.Timers()
                self.timers.parent = self
                self._children_name_map["timers"] = "timers"
            return self.timers

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "backoff" or name == "disjoint-path" or name == "explicit-paths" or name == "logging" or name == "netconf" or name == "pcc-addresses" or name == "segment-routing" or name == "state-syncs" or name == "timers" or name == "enable" or name == "password" or name == "server-address"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix
        if(value_path == "password"):
            self.password = value
            self.password.value_namespace = name_space
            self.password.value_namespace_prefix = name_space_prefix
        if(value_path == "server-address"):
            self.server_address = value
            self.server_address.value_namespace = name_space
            self.server_address.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Pce()
        return self._top_entity


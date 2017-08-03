""" Cisco_IOS_XR_ip_rip_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-rip package configuration.

This module contains definitions
for the following management objects\:
  rip\: RIP configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BgpRedistRoute(Enum):
    """
    BgpRedistRoute

    Bgp redist route

    .. data:: all = 0

    	All routes

    .. data:: internal = 512

    	Internal routes only

    .. data:: external = 1024

    	External routes only

    .. data:: local = 2048

    	Local routes only

    """

    all = Enum.YLeaf(0, "all")

    internal = Enum.YLeaf(512, "internal")

    external = Enum.YLeaf(1024, "external")

    local = Enum.YLeaf(2048, "local")


class DefaultInformationOption(Enum):
    """
    DefaultInformationOption

    Default information option

    .. data:: always = 0

    	Always

    .. data:: policy = 1

    	Use route-policy

    """

    always = Enum.YLeaf(0, "always")

    policy = Enum.YLeaf(1, "policy")


class DefaultRedistRoute(Enum):
    """
    DefaultRedistRoute

    Default redist route

    .. data:: all = 0

    	All routes

    """

    all = Enum.YLeaf(0, "all")


class IsisRedistRoute(Enum):
    """
    IsisRedistRoute

    Isis redist route

    .. data:: level1 = 1

    	Level-1 routes only

    .. data:: level2 = 2

    	Level-1 routes only

    .. data:: level1_and2 = 3

    	Level-1 and level-2 routes

    """

    level1 = Enum.YLeaf(1, "level1")

    level2 = Enum.YLeaf(2, "level2")

    level1_and2 = Enum.YLeaf(3, "level1-and2")


class RipAuthMode(Enum):
    """
    RipAuthMode

    Rip auth mode

    .. data:: text = 2

    	Text mode

    .. data:: md5 = 3

    	MD5 mode

    """

    text = Enum.YLeaf(2, "text")

    md5 = Enum.YLeaf(3, "md5")


class RipExtCommunity(Enum):
    """
    RipExtCommunity

    Rip ext community

    .. data:: as_ = 0

    	AS:nn format

    .. data:: ipv4_address = 1

    	IPV4Address:nn format

    .. data:: four_byte_as = 2

    	4-byte ASN format

    """

    as_ = Enum.YLeaf(0, "as")

    ipv4_address = Enum.YLeaf(1, "ipv4-address")

    four_byte_as = Enum.YLeaf(2, "four-byte-as")



class Rip(Entity):
    """
    RIP configuration
    
    .. attribute:: default_vrf
    
    	RIP configuration for Default VRF
    	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf>`
    
    .. attribute:: vrfs
    
    	VRF related RIP configuration
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs>`
    
    

    """

    _prefix = 'ip-rip-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Rip, self).__init__()
        self._top_entity = None

        self.yang_name = "rip"
        self.yang_parent_name = "Cisco-IOS-XR-ip-rip-cfg"

        self.default_vrf = Rip.DefaultVrf()
        self.default_vrf.parent = self
        self._children_name_map["default_vrf"] = "default-vrf"
        self._children_yang_names.add("default-vrf")

        self.vrfs = Rip.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")


    class DefaultVrf(Entity):
        """
        RIP configuration for Default VRF
        
        .. attribute:: auto_summary
        
        	Enable automatic network number summarization
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: broadcast_for_v2
        
        	Send RIP v2 output packets to broadcast address
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: default_information
        
        	Controls default information origination
        	**type**\:   :py:class:`DefaultInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.DefaultInformation>`
        
        	**presence node**\: True
        
        .. attribute:: default_metric
        
        	Default metric of redistributed routes
        	**type**\:  int
        
        	**range:** 0..16
        
        .. attribute:: distance
        
        	Administrative distance
        	**type**\:  int
        
        	**range:** 0..255
        
        	**default value**\: 120
        
        .. attribute:: enable
        
        	Starts RIP configuration for Default VRF
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: interfaces
        
        	Table of RIP interfaces
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces>`
        
        .. attribute:: ip_distances
        
        	Table of IP specific administrative distances
        	**type**\:   :py:class:`IpDistances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.IpDistances>`
        
        .. attribute:: maximum_paths
        
        	Maximum number of paths allowed per route
        	**type**\:  int
        
        	**range:** 1..128
        
        	**default value**\: 4
        
        .. attribute:: neighbors
        
        	Configure RIP Neighbors
        	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Neighbors>`
        
        .. attribute:: nsf
        
        	Enable Cisco Non Stop Forwarding
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: output_delay
        
        	Inter\-packet delay for RIP updates
        	**type**\:  int
        
        	**range:** 8..50
        
        	**units**\: millisecond
        
        .. attribute:: policy_in
        
        	Route Policy for inbbound routing updates
        	**type**\:  str
        
        .. attribute:: policy_out
        
        	Route Policy for outbound routing updates
        	**type**\:  str
        
        .. attribute:: redistribution
        
        	Redistribute information from another routing protocol
        	**type**\:   :py:class:`Redistribution <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution>`
        
        .. attribute:: timers
        
        	Various routing timers
        	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Timers>`
        
        .. attribute:: validate_source_disable
        
        	Disable validation of source address of routing updates
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ip-rip-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rip.DefaultVrf, self).__init__()

            self.yang_name = "default-vrf"
            self.yang_parent_name = "rip"

            self.auto_summary = YLeaf(YType.empty, "auto-summary")

            self.broadcast_for_v2 = YLeaf(YType.empty, "broadcast-for-v2")

            self.default_metric = YLeaf(YType.uint32, "default-metric")

            self.distance = YLeaf(YType.uint32, "distance")

            self.enable = YLeaf(YType.empty, "enable")

            self.maximum_paths = YLeaf(YType.uint32, "maximum-paths")

            self.nsf = YLeaf(YType.empty, "nsf")

            self.output_delay = YLeaf(YType.uint32, "output-delay")

            self.policy_in = YLeaf(YType.str, "policy-in")

            self.policy_out = YLeaf(YType.str, "policy-out")

            self.validate_source_disable = YLeaf(YType.empty, "validate-source-disable")

            self.default_information = None
            self._children_name_map["default_information"] = "default-information"
            self._children_yang_names.add("default-information")

            self.interfaces = Rip.DefaultVrf.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.ip_distances = Rip.DefaultVrf.IpDistances()
            self.ip_distances.parent = self
            self._children_name_map["ip_distances"] = "ip-distances"
            self._children_yang_names.add("ip-distances")

            self.neighbors = Rip.DefaultVrf.Neighbors()
            self.neighbors.parent = self
            self._children_name_map["neighbors"] = "neighbors"
            self._children_yang_names.add("neighbors")

            self.redistribution = Rip.DefaultVrf.Redistribution()
            self.redistribution.parent = self
            self._children_name_map["redistribution"] = "redistribution"
            self._children_yang_names.add("redistribution")

            self.timers = Rip.DefaultVrf.Timers()
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
                if name in ("auto_summary",
                            "broadcast_for_v2",
                            "default_metric",
                            "distance",
                            "enable",
                            "maximum_paths",
                            "nsf",
                            "output_delay",
                            "policy_in",
                            "policy_out",
                            "validate_source_disable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Rip.DefaultVrf, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rip.DefaultVrf, self).__setattr__(name, value)


        class DefaultInformation(Entity):
            """
            Controls default information origination
            
            .. attribute:: option
            
            	Origination option
            	**type**\:   :py:class:`DefaultInformationOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultInformationOption>`
            
            	**mandatory**\: True
            
            .. attribute:: route_policy_name
            
            	Route policy name
            	**type**\:  str
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.DefaultInformation, self).__init__()

                self.yang_name = "default-information"
                self.yang_parent_name = "default-vrf"
                self.is_presence_container = True

                self.option = YLeaf(YType.enumeration, "option")

                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("option",
                                "route_policy_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rip.DefaultVrf.DefaultInformation, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rip.DefaultVrf.DefaultInformation, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.option.is_set or
                    self.route_policy_name.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.option.yfilter != YFilter.not_set or
                    self.route_policy_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "default-information" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.option.is_set or self.option.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.option.get_name_leafdata())
                if (self.route_policy_name.is_set or self.route_policy_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.route_policy_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "option" or name == "route-policy-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "option"):
                    self.option = value
                    self.option.value_namespace = name_space
                    self.option.value_namespace_prefix = name_space_prefix
                if(value_path == "route-policy-name"):
                    self.route_policy_name = value
                    self.route_policy_name.value_namespace = name_space
                    self.route_policy_name.value_namespace_prefix = name_space_prefix


        class Redistribution(Entity):
            """
            Redistribute information from another routing
            protocol
            
            .. attribute:: bgps
            
            	Redistribute BGP routes
            	**type**\:   :py:class:`Bgps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Bgps>`
            
            .. attribute:: connected
            
            	Redistribute connected routes
            	**type**\:   :py:class:`Connected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Connected>`
            
            	**presence node**\: True
            
            .. attribute:: eigrp_s
            
            	Redistribute EIGRP routes
            	**type**\:   :py:class:`EigrpS <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.EigrpS>`
            
            .. attribute:: isises
            
            	Redistribute IS\-IS routes
            	**type**\:   :py:class:`Isises <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Isises>`
            
            .. attribute:: ospfs
            
            	Redistribute OSPF routes
            	**type**\:   :py:class:`Ospfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Ospfs>`
            
            .. attribute:: static
            
            	Redistribute static routes
            	**type**\:   :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Static>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Redistribution, self).__init__()

                self.yang_name = "redistribution"
                self.yang_parent_name = "default-vrf"

                self.bgps = Rip.DefaultVrf.Redistribution.Bgps()
                self.bgps.parent = self
                self._children_name_map["bgps"] = "bgps"
                self._children_yang_names.add("bgps")

                self.connected = None
                self._children_name_map["connected"] = "connected"
                self._children_yang_names.add("connected")

                self.eigrp_s = Rip.DefaultVrf.Redistribution.EigrpS()
                self.eigrp_s.parent = self
                self._children_name_map["eigrp_s"] = "eigrp-s"
                self._children_yang_names.add("eigrp-s")

                self.isises = Rip.DefaultVrf.Redistribution.Isises()
                self.isises.parent = self
                self._children_name_map["isises"] = "isises"
                self._children_yang_names.add("isises")

                self.ospfs = Rip.DefaultVrf.Redistribution.Ospfs()
                self.ospfs.parent = self
                self._children_name_map["ospfs"] = "ospfs"
                self._children_yang_names.add("ospfs")

                self.static = None
                self._children_name_map["static"] = "static"
                self._children_yang_names.add("static")


            class Connected(Entity):
                """
                Redistribute connected routes
                
                .. attribute:: route_policy_name
                
                	Route Policy name
                	**type**\:  str
                
                .. attribute:: route_type
                
                	Route type
                	**type**\:   :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.Connected, self).__init__()

                    self.yang_name = "connected"
                    self.yang_parent_name = "redistribution"
                    self.is_presence_container = True

                    self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                    self.route_type = YLeaf(YType.enumeration, "route-type")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("route_policy_name",
                                    "route_type") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.DefaultVrf.Redistribution.Connected, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.DefaultVrf.Redistribution.Connected, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.route_policy_name.is_set or
                        self.route_type.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.route_policy_name.yfilter != YFilter.not_set or
                        self.route_type.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "connected" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.route_policy_name.is_set or self.route_policy_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_policy_name.get_name_leafdata())
                    if (self.route_type.is_set or self.route_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_type.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "route-policy-name" or name == "route-type"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "route-policy-name"):
                        self.route_policy_name = value
                        self.route_policy_name.value_namespace = name_space
                        self.route_policy_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "route-type"):
                        self.route_type = value
                        self.route_type.value_namespace = name_space
                        self.route_type.value_namespace_prefix = name_space_prefix


            class Bgps(Entity):
                """
                Redistribute BGP routes
                
                .. attribute:: bgp
                
                	Autonomous system number
                	**type**\: list of    :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Bgps.Bgp>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.Bgps, self).__init__()

                    self.yang_name = "bgps"
                    self.yang_parent_name = "redistribution"

                    self.bgp = YList(self)

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
                                super(Rip.DefaultVrf.Redistribution.Bgps, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.DefaultVrf.Redistribution.Bgps, self).__setattr__(name, value)


                class Bgp(Entity):
                    """
                    Autonomous system number
                    
                    .. attribute:: asnxx  <key>
                    
                    	Higher 16 bits of 4\-byte BGP AS number
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: asnyy  <key>
                    
                    	2\-byte or 4\-byte BGP AS number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: policy
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    .. attribute:: type
                    
                    	Route type
                    	**type**\:   :py:class:`BgpRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.BgpRedistRoute>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Redistribution.Bgps.Bgp, self).__init__()

                        self.yang_name = "bgp"
                        self.yang_parent_name = "bgps"

                        self.asnxx = YLeaf(YType.uint32, "asnxx")

                        self.asnyy = YLeaf(YType.uint32, "asnyy")

                        self.policy = YLeaf(YType.str, "policy")

                        self.type = YLeaf(YType.enumeration, "type")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("asnxx",
                                        "asnyy",
                                        "policy",
                                        "type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.DefaultVrf.Redistribution.Bgps.Bgp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.DefaultVrf.Redistribution.Bgps.Bgp, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.asnxx.is_set or
                            self.asnyy.is_set or
                            self.policy.is_set or
                            self.type.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.asnxx.yfilter != YFilter.not_set or
                            self.asnyy.yfilter != YFilter.not_set or
                            self.policy.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bgp" + "[asnxx='" + self.asnxx.get() + "']" + "[asnyy='" + self.asnyy.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/bgps/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.asnxx.is_set or self.asnxx.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.asnxx.get_name_leafdata())
                        if (self.asnyy.is_set or self.asnyy.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.asnyy.get_name_leafdata())
                        if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.policy.get_name_leafdata())
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "asnxx" or name == "asnyy" or name == "policy" or name == "type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "asnxx"):
                            self.asnxx = value
                            self.asnxx.value_namespace = name_space
                            self.asnxx.value_namespace_prefix = name_space_prefix
                        if(value_path == "asnyy"):
                            self.asnyy = value
                            self.asnyy.value_namespace = name_space
                            self.asnyy.value_namespace_prefix = name_space_prefix
                        if(value_path == "policy"):
                            self.policy = value
                            self.policy.value_namespace = name_space
                            self.policy.value_namespace_prefix = name_space_prefix
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bgp:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bgp:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bgps" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "bgp"):
                        for c in self.bgp:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.DefaultVrf.Redistribution.Bgps.Bgp()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bgp.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bgp"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Isises(Entity):
                """
                Redistribute IS\-IS routes
                
                .. attribute:: isis
                
                	Redistribute IS\-IS routes
                	**type**\: list of    :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Isises.Isis>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.Isises, self).__init__()

                    self.yang_name = "isises"
                    self.yang_parent_name = "redistribution"

                    self.isis = YList(self)

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
                                super(Rip.DefaultVrf.Redistribution.Isises, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.DefaultVrf.Redistribution.Isises, self).__setattr__(name, value)


                class Isis(Entity):
                    """
                    Redistribute IS\-IS routes
                    
                    .. attribute:: isis_name  <key>
                    
                    	IS\-IS instance name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:   :py:class:`IsisRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.IsisRedistRoute>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Redistribution.Isises.Isis, self).__init__()

                        self.yang_name = "isis"
                        self.yang_parent_name = "isises"

                        self.isis_name = YLeaf(YType.str, "isis-name")

                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                        self.route_type = YLeaf(YType.enumeration, "route-type")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("isis_name",
                                        "route_policy_name",
                                        "route_type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.DefaultVrf.Redistribution.Isises.Isis, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.DefaultVrf.Redistribution.Isises.Isis, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.isis_name.is_set or
                            self.route_policy_name.is_set or
                            self.route_type.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.isis_name.yfilter != YFilter.not_set or
                            self.route_policy_name.yfilter != YFilter.not_set or
                            self.route_type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "isis" + "[isis-name='" + self.isis_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/isises/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.isis_name.is_set or self.isis_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.isis_name.get_name_leafdata())
                        if (self.route_policy_name.is_set or self.route_policy_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_policy_name.get_name_leafdata())
                        if (self.route_type.is_set or self.route_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "isis-name" or name == "route-policy-name" or name == "route-type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "isis-name"):
                            self.isis_name = value
                            self.isis_name.value_namespace = name_space
                            self.isis_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-policy-name"):
                            self.route_policy_name = value
                            self.route_policy_name.value_namespace = name_space
                            self.route_policy_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-type"):
                            self.route_type = value
                            self.route_type.value_namespace = name_space
                            self.route_type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.isis:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.isis:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "isises" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "isis"):
                        for c in self.isis:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.DefaultVrf.Redistribution.Isises.Isis()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.isis.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "isis"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class EigrpS(Entity):
                """
                Redistribute EIGRP routes
                
                .. attribute:: eigrp
                
                	Redistribute EIGRP routes
                	**type**\: list of    :py:class:`Eigrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.EigrpS.Eigrp>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.EigrpS, self).__init__()

                    self.yang_name = "eigrp-s"
                    self.yang_parent_name = "redistribution"

                    self.eigrp = YList(self)

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
                                super(Rip.DefaultVrf.Redistribution.EigrpS, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.DefaultVrf.Redistribution.EigrpS, self).__setattr__(name, value)


                class Eigrp(Entity):
                    """
                    Redistribute EIGRP routes
                    
                    .. attribute:: as_  <key>
                    
                    	Autonomous system number
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:   :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Redistribution.EigrpS.Eigrp, self).__init__()

                        self.yang_name = "eigrp"
                        self.yang_parent_name = "eigrp-s"

                        self.as_ = YLeaf(YType.uint32, "as")

                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                        self.route_type = YLeaf(YType.enumeration, "route-type")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("as_",
                                        "route_policy_name",
                                        "route_type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.DefaultVrf.Redistribution.EigrpS.Eigrp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.DefaultVrf.Redistribution.EigrpS.Eigrp, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.as_.is_set or
                            self.route_policy_name.is_set or
                            self.route_type.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.as_.yfilter != YFilter.not_set or
                            self.route_policy_name.yfilter != YFilter.not_set or
                            self.route_type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "eigrp" + "[as='" + self.as_.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/eigrp-s/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.as_.is_set or self.as_.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.as_.get_name_leafdata())
                        if (self.route_policy_name.is_set or self.route_policy_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_policy_name.get_name_leafdata())
                        if (self.route_type.is_set or self.route_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "as" or name == "route-policy-name" or name == "route-type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "as"):
                            self.as_ = value
                            self.as_.value_namespace = name_space
                            self.as_.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-policy-name"):
                            self.route_policy_name = value
                            self.route_policy_name.value_namespace = name_space
                            self.route_policy_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-type"):
                            self.route_type = value
                            self.route_type.value_namespace = name_space
                            self.route_type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.eigrp:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.eigrp:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "eigrp-s" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "eigrp"):
                        for c in self.eigrp:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.DefaultVrf.Redistribution.EigrpS.Eigrp()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.eigrp.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "eigrp"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Static(Entity):
                """
                Redistribute static routes
                
                .. attribute:: route_policy_name
                
                	Route Policy name
                	**type**\:  str
                
                .. attribute:: route_type
                
                	Route type
                	**type**\:   :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.Static, self).__init__()

                    self.yang_name = "static"
                    self.yang_parent_name = "redistribution"
                    self.is_presence_container = True

                    self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                    self.route_type = YLeaf(YType.enumeration, "route-type")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("route_policy_name",
                                    "route_type") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.DefaultVrf.Redistribution.Static, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.DefaultVrf.Redistribution.Static, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.route_policy_name.is_set or
                        self.route_type.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.route_policy_name.yfilter != YFilter.not_set or
                        self.route_type.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "static" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.route_policy_name.is_set or self.route_policy_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_policy_name.get_name_leafdata())
                    if (self.route_type.is_set or self.route_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_type.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "route-policy-name" or name == "route-type"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "route-policy-name"):
                        self.route_policy_name = value
                        self.route_policy_name.value_namespace = name_space
                        self.route_policy_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "route-type"):
                        self.route_type = value
                        self.route_type.value_namespace = name_space
                        self.route_type.value_namespace_prefix = name_space_prefix


            class Ospfs(Entity):
                """
                Redistribute OSPF routes
                
                .. attribute:: ospf
                
                	Redistribute OSPF routes
                	**type**\: list of    :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Ospfs.Ospf>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Redistribution.Ospfs, self).__init__()

                    self.yang_name = "ospfs"
                    self.yang_parent_name = "redistribution"

                    self.ospf = YList(self)

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
                                super(Rip.DefaultVrf.Redistribution.Ospfs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.DefaultVrf.Redistribution.Ospfs, self).__setattr__(name, value)


                class Ospf(Entity):
                    """
                    Redistribute OSPF routes
                    
                    .. attribute:: ospf_name  <key>
                    
                    	Process ID for the OSPF instance
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: external
                    
                    	External routes
                    	**type**\:  bool
                    
                    .. attribute:: external_type
                    
                    	External route type
                    	**type**\:  int
                    
                    	**range:** 0..2
                    
                    .. attribute:: internal
                    
                    	Internal routes
                    	**type**\:  bool
                    
                    .. attribute:: nssa_external
                    
                    	NSSA External routes
                    	**type**\:  bool
                    
                    .. attribute:: nssa_external_type
                    
                    	NSSA External route type
                    	**type**\:  int
                    
                    	**range:** 0..2
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Redistribution.Ospfs.Ospf, self).__init__()

                        self.yang_name = "ospf"
                        self.yang_parent_name = "ospfs"

                        self.ospf_name = YLeaf(YType.str, "ospf-name")

                        self.external = YLeaf(YType.boolean, "external")

                        self.external_type = YLeaf(YType.uint32, "external-type")

                        self.internal = YLeaf(YType.boolean, "internal")

                        self.nssa_external = YLeaf(YType.boolean, "nssa-external")

                        self.nssa_external_type = YLeaf(YType.uint32, "nssa-external-type")

                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ospf_name",
                                        "external",
                                        "external_type",
                                        "internal",
                                        "nssa_external",
                                        "nssa_external_type",
                                        "route_policy_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.DefaultVrf.Redistribution.Ospfs.Ospf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.DefaultVrf.Redistribution.Ospfs.Ospf, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ospf_name.is_set or
                            self.external.is_set or
                            self.external_type.is_set or
                            self.internal.is_set or
                            self.nssa_external.is_set or
                            self.nssa_external_type.is_set or
                            self.route_policy_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ospf_name.yfilter != YFilter.not_set or
                            self.external.yfilter != YFilter.not_set or
                            self.external_type.yfilter != YFilter.not_set or
                            self.internal.yfilter != YFilter.not_set or
                            self.nssa_external.yfilter != YFilter.not_set or
                            self.nssa_external_type.yfilter != YFilter.not_set or
                            self.route_policy_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ospf" + "[ospf-name='" + self.ospf_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/ospfs/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ospf_name.is_set or self.ospf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ospf_name.get_name_leafdata())
                        if (self.external.is_set or self.external.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.external.get_name_leafdata())
                        if (self.external_type.is_set or self.external_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.external_type.get_name_leafdata())
                        if (self.internal.is_set or self.internal.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.internal.get_name_leafdata())
                        if (self.nssa_external.is_set or self.nssa_external.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nssa_external.get_name_leafdata())
                        if (self.nssa_external_type.is_set or self.nssa_external_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nssa_external_type.get_name_leafdata())
                        if (self.route_policy_name.is_set or self.route_policy_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_policy_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ospf-name" or name == "external" or name == "external-type" or name == "internal" or name == "nssa-external" or name == "nssa-external-type" or name == "route-policy-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ospf-name"):
                            self.ospf_name = value
                            self.ospf_name.value_namespace = name_space
                            self.ospf_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "external"):
                            self.external = value
                            self.external.value_namespace = name_space
                            self.external.value_namespace_prefix = name_space_prefix
                        if(value_path == "external-type"):
                            self.external_type = value
                            self.external_type.value_namespace = name_space
                            self.external_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "internal"):
                            self.internal = value
                            self.internal.value_namespace = name_space
                            self.internal.value_namespace_prefix = name_space_prefix
                        if(value_path == "nssa-external"):
                            self.nssa_external = value
                            self.nssa_external.value_namespace = name_space
                            self.nssa_external.value_namespace_prefix = name_space_prefix
                        if(value_path == "nssa-external-type"):
                            self.nssa_external_type = value
                            self.nssa_external_type.value_namespace = name_space
                            self.nssa_external_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-policy-name"):
                            self.route_policy_name = value
                            self.route_policy_name.value_namespace = name_space
                            self.route_policy_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ospf:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ospf:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ospfs" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/redistribution/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ospf"):
                        for c in self.ospf:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.DefaultVrf.Redistribution.Ospfs.Ospf()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ospf.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ospf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.bgps is not None and self.bgps.has_data()) or
                    (self.eigrp_s is not None and self.eigrp_s.has_data()) or
                    (self.isises is not None and self.isises.has_data()) or
                    (self.ospfs is not None and self.ospfs.has_data()) or
                    (self.connected is not None) or
                    (self.static is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.bgps is not None and self.bgps.has_operation()) or
                    (self.connected is not None and self.connected.has_operation()) or
                    (self.eigrp_s is not None and self.eigrp_s.has_operation()) or
                    (self.isises is not None and self.isises.has_operation()) or
                    (self.ospfs is not None and self.ospfs.has_operation()) or
                    (self.static is not None and self.static.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "redistribution" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bgps"):
                    if (self.bgps is None):
                        self.bgps = Rip.DefaultVrf.Redistribution.Bgps()
                        self.bgps.parent = self
                        self._children_name_map["bgps"] = "bgps"
                    return self.bgps

                if (child_yang_name == "connected"):
                    if (self.connected is None):
                        self.connected = Rip.DefaultVrf.Redistribution.Connected()
                        self.connected.parent = self
                        self._children_name_map["connected"] = "connected"
                    return self.connected

                if (child_yang_name == "eigrp-s"):
                    if (self.eigrp_s is None):
                        self.eigrp_s = Rip.DefaultVrf.Redistribution.EigrpS()
                        self.eigrp_s.parent = self
                        self._children_name_map["eigrp_s"] = "eigrp-s"
                    return self.eigrp_s

                if (child_yang_name == "isises"):
                    if (self.isises is None):
                        self.isises = Rip.DefaultVrf.Redistribution.Isises()
                        self.isises.parent = self
                        self._children_name_map["isises"] = "isises"
                    return self.isises

                if (child_yang_name == "ospfs"):
                    if (self.ospfs is None):
                        self.ospfs = Rip.DefaultVrf.Redistribution.Ospfs()
                        self.ospfs.parent = self
                        self._children_name_map["ospfs"] = "ospfs"
                    return self.ospfs

                if (child_yang_name == "static"):
                    if (self.static is None):
                        self.static = Rip.DefaultVrf.Redistribution.Static()
                        self.static.parent = self
                        self._children_name_map["static"] = "static"
                    return self.static

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bgps" or name == "connected" or name == "eigrp-s" or name == "isises" or name == "ospfs" or name == "static"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class IpDistances(Entity):
            """
            Table of IP specific administrative distances
            
            .. attribute:: ip_distance
            
            	IP specific administrative distance
            	**type**\: list of    :py:class:`IpDistance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.IpDistances.IpDistance>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.IpDistances, self).__init__()

                self.yang_name = "ip-distances"
                self.yang_parent_name = "default-vrf"

                self.ip_distance = YList(self)

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
                            super(Rip.DefaultVrf.IpDistances, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rip.DefaultVrf.IpDistances, self).__setattr__(name, value)


            class IpDistance(Entity):
                """
                IP specific administrative distance
                
                .. attribute:: address  <key>
                
                	IP Source address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: netmask  <key>
                
                	IP address mask
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: distance
                
                	Administrative distance
                	**type**\:  int
                
                	**range:** 0..255
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.IpDistances.IpDistance, self).__init__()

                    self.yang_name = "ip-distance"
                    self.yang_parent_name = "ip-distances"

                    self.address = YLeaf(YType.str, "address")

                    self.netmask = YLeaf(YType.str, "netmask")

                    self.distance = YLeaf(YType.uint32, "distance")

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
                                    "netmask",
                                    "distance") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.DefaultVrf.IpDistances.IpDistance, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.DefaultVrf.IpDistances.IpDistance, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.address.is_set or
                        self.netmask.is_set or
                        self.distance.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address.yfilter != YFilter.not_set or
                        self.netmask.yfilter != YFilter.not_set or
                        self.distance.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ip-distance" + "[address='" + self.address.get() + "']" + "[netmask='" + self.netmask.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/ip-distances/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address.get_name_leafdata())
                    if (self.netmask.is_set or self.netmask.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.netmask.get_name_leafdata())
                    if (self.distance.is_set or self.distance.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.distance.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "address" or name == "netmask" or name == "distance"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address"):
                        self.address = value
                        self.address.value_namespace = name_space
                        self.address.value_namespace_prefix = name_space_prefix
                    if(value_path == "netmask"):
                        self.netmask = value
                        self.netmask.value_namespace = name_space
                        self.netmask.value_namespace_prefix = name_space_prefix
                    if(value_path == "distance"):
                        self.distance = value
                        self.distance.value_namespace = name_space
                        self.distance.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ip_distance:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.ip_distance:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ip-distances" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ip-distance"):
                    for c in self.ip_distance:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Rip.DefaultVrf.IpDistances.IpDistance()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ip_distance.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ip-distance"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Interfaces(Entity):
            """
            Table of RIP interfaces
            
            .. attribute:: interface
            
            	RIP interface name
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "default-vrf"

                self.interface = YList(self)

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
                            super(Rip.DefaultVrf.Interfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rip.DefaultVrf.Interfaces, self).__setattr__(name, value)


            class Interface(Entity):
                """
                RIP interface name
                
                .. attribute:: interface_name  <key>
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: accept_metric_zero
                
                	Accept RIP updates with metric 0
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: authentication
                
                	Authentication keychain and mode
                	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.Authentication>`
                
                	**presence node**\: True
                
                .. attribute:: broadcast_for_v2
                
                	Send RIP v2 output packets to broadcast address
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: enable
                
                	Starts RIP interface configuration
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: passive
                
                	Suppress routing updates on this interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: poison_reverse
                
                	Enable poison reverse
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: policy_in
                
                	Route Policy for inbound routing updates
                	**type**\:  str
                
                .. attribute:: policy_out
                
                	Route Policy for outbound routing updates
                	**type**\:  str
                
                .. attribute:: receive_version
                
                	RIP versions supported for receiving advertisements
                	**type**\:   :py:class:`ReceiveVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion>`
                
                .. attribute:: send_version
                
                	RIP versions supported for sending advertisements
                	**type**\:   :py:class:`SendVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.SendVersion>`
                
                .. attribute:: site_of_origin
                
                	SOO community for prefixes learned over this interface
                	**type**\:   :py:class:`SiteOfOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin>`
                
                .. attribute:: split_horizon_disable
                
                	Disable split horizon
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.accept_metric_zero = YLeaf(YType.empty, "accept-metric-zero")

                    self.broadcast_for_v2 = YLeaf(YType.empty, "broadcast-for-v2")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.passive = YLeaf(YType.empty, "passive")

                    self.poison_reverse = YLeaf(YType.empty, "poison-reverse")

                    self.policy_in = YLeaf(YType.str, "policy-in")

                    self.policy_out = YLeaf(YType.str, "policy-out")

                    self.split_horizon_disable = YLeaf(YType.empty, "split-horizon-disable")

                    self.authentication = None
                    self._children_name_map["authentication"] = "authentication"
                    self._children_yang_names.add("authentication")

                    self.receive_version = Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion()
                    self.receive_version.parent = self
                    self._children_name_map["receive_version"] = "receive-version"
                    self._children_yang_names.add("receive-version")

                    self.send_version = Rip.DefaultVrf.Interfaces.Interface.SendVersion()
                    self.send_version.parent = self
                    self._children_name_map["send_version"] = "send-version"
                    self._children_yang_names.add("send-version")

                    self.site_of_origin = Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin()
                    self.site_of_origin.parent = self
                    self._children_name_map["site_of_origin"] = "site-of-origin"
                    self._children_yang_names.add("site-of-origin")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "accept_metric_zero",
                                    "broadcast_for_v2",
                                    "enable",
                                    "passive",
                                    "poison_reverse",
                                    "policy_in",
                                    "policy_out",
                                    "split_horizon_disable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.DefaultVrf.Interfaces.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.DefaultVrf.Interfaces.Interface, self).__setattr__(name, value)


                class Authentication(Entity):
                    """
                    Authentication keychain and mode
                    
                    .. attribute:: keychain
                    
                    	Name of keychain
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: mode
                    
                    	Authentication mode
                    	**type**\:   :py:class:`RipAuthMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipAuthMode>`
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Interfaces.Interface.Authentication, self).__init__()

                        self.yang_name = "authentication"
                        self.yang_parent_name = "interface"
                        self.is_presence_container = True

                        self.keychain = YLeaf(YType.str, "keychain")

                        self.mode = YLeaf(YType.enumeration, "mode")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("keychain",
                                        "mode") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.DefaultVrf.Interfaces.Interface.Authentication, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.DefaultVrf.Interfaces.Interface.Authentication, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.keychain.is_set or
                            self.mode.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.keychain.yfilter != YFilter.not_set or
                            self.mode.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "authentication" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.keychain.is_set or self.keychain.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.keychain.get_name_leafdata())
                        if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mode.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "keychain" or name == "mode"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "keychain"):
                            self.keychain = value
                            self.keychain.value_namespace = name_space
                            self.keychain.value_namespace_prefix = name_space_prefix
                        if(value_path == "mode"):
                            self.mode = value
                            self.mode.value_namespace = name_space
                            self.mode.value_namespace_prefix = name_space_prefix


                class SiteOfOrigin(Entity):
                    """
                    SOO community for prefixes learned over this
                    interface
                    
                    .. attribute:: address
                    
                    	IPV4 address for IPV4Address\:nn format
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: address_index
                    
                    	16bit value for IPV4Address\:nn format
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: as_index
                    
                    	AS Number Index
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: as_xx
                    
                    	AS Number for AS\:nn format
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: as_yy
                    
                    	32 bit value for AS\:nn format
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: type
                    
                    	Extended community type
                    	**type**\:   :py:class:`RipExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipExtCommunity>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin, self).__init__()

                        self.yang_name = "site-of-origin"
                        self.yang_parent_name = "interface"

                        self.address = YLeaf(YType.str, "address")

                        self.address_index = YLeaf(YType.uint32, "address-index")

                        self.as_index = YLeaf(YType.uint32, "as-index")

                        self.as_xx = YLeaf(YType.uint32, "as-xx")

                        self.as_yy = YLeaf(YType.uint32, "as-yy")

                        self.type = YLeaf(YType.enumeration, "type")

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
                                        "address_index",
                                        "as_index",
                                        "as_xx",
                                        "as_yy",
                                        "type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.address_index.is_set or
                            self.as_index.is_set or
                            self.as_xx.is_set or
                            self.as_yy.is_set or
                            self.type.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.address_index.yfilter != YFilter.not_set or
                            self.as_index.yfilter != YFilter.not_set or
                            self.as_xx.yfilter != YFilter.not_set or
                            self.as_yy.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "site-of-origin" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.address_index.is_set or self.address_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address_index.get_name_leafdata())
                        if (self.as_index.is_set or self.as_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.as_index.get_name_leafdata())
                        if (self.as_xx.is_set or self.as_xx.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.as_xx.get_name_leafdata())
                        if (self.as_yy.is_set or self.as_yy.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.as_yy.get_name_leafdata())
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "address-index" or name == "as-index" or name == "as-xx" or name == "as-yy" or name == "type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "address-index"):
                            self.address_index = value
                            self.address_index.value_namespace = name_space
                            self.address_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "as-index"):
                            self.as_index = value
                            self.as_index.value_namespace = name_space
                            self.as_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "as-xx"):
                            self.as_xx = value
                            self.as_xx.value_namespace = name_space
                            self.as_xx.value_namespace_prefix = name_space_prefix
                        if(value_path == "as-yy"):
                            self.as_yy = value
                            self.as_yy.value_namespace = name_space
                            self.as_yy.value_namespace_prefix = name_space_prefix
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix


                class ReceiveVersion(Entity):
                    """
                    RIP versions supported for receiving
                    advertisements
                    
                    .. attribute:: version1
                    
                    	Support RIP version 1
                    	**type**\:  bool
                    
                    .. attribute:: version2
                    
                    	Support RIP version 2
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion, self).__init__()

                        self.yang_name = "receive-version"
                        self.yang_parent_name = "interface"

                        self.version1 = YLeaf(YType.boolean, "version1")

                        self.version2 = YLeaf(YType.boolean, "version2")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("version1",
                                        "version2") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.version1.is_set or
                            self.version2.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.version1.yfilter != YFilter.not_set or
                            self.version2.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "receive-version" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.version1.is_set or self.version1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version1.get_name_leafdata())
                        if (self.version2.is_set or self.version2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version2.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "version1" or name == "version2"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "version1"):
                            self.version1 = value
                            self.version1.value_namespace = name_space
                            self.version1.value_namespace_prefix = name_space_prefix
                        if(value_path == "version2"):
                            self.version2 = value
                            self.version2.value_namespace = name_space
                            self.version2.value_namespace_prefix = name_space_prefix


                class SendVersion(Entity):
                    """
                    RIP versions supported for sending
                    advertisements
                    
                    .. attribute:: version1
                    
                    	Support RIP version 1
                    	**type**\:  bool
                    
                    .. attribute:: version2
                    
                    	Support RIP version 2
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Interfaces.Interface.SendVersion, self).__init__()

                        self.yang_name = "send-version"
                        self.yang_parent_name = "interface"

                        self.version1 = YLeaf(YType.boolean, "version1")

                        self.version2 = YLeaf(YType.boolean, "version2")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("version1",
                                        "version2") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.DefaultVrf.Interfaces.Interface.SendVersion, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.DefaultVrf.Interfaces.Interface.SendVersion, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.version1.is_set or
                            self.version2.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.version1.yfilter != YFilter.not_set or
                            self.version2.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "send-version" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.version1.is_set or self.version1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version1.get_name_leafdata())
                        if (self.version2.is_set or self.version2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version2.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "version1" or name == "version2"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "version1"):
                            self.version1 = value
                            self.version1.value_namespace = name_space
                            self.version1.value_namespace_prefix = name_space_prefix
                        if(value_path == "version2"):
                            self.version2 = value
                            self.version2.value_namespace = name_space
                            self.version2.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.accept_metric_zero.is_set or
                        self.broadcast_for_v2.is_set or
                        self.enable.is_set or
                        self.passive.is_set or
                        self.poison_reverse.is_set or
                        self.policy_in.is_set or
                        self.policy_out.is_set or
                        self.split_horizon_disable.is_set or
                        (self.receive_version is not None and self.receive_version.has_data()) or
                        (self.send_version is not None and self.send_version.has_data()) or
                        (self.site_of_origin is not None and self.site_of_origin.has_data()) or
                        (self.authentication is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.accept_metric_zero.yfilter != YFilter.not_set or
                        self.broadcast_for_v2.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        self.passive.yfilter != YFilter.not_set or
                        self.poison_reverse.yfilter != YFilter.not_set or
                        self.policy_in.yfilter != YFilter.not_set or
                        self.policy_out.yfilter != YFilter.not_set or
                        self.split_horizon_disable.yfilter != YFilter.not_set or
                        (self.authentication is not None and self.authentication.has_operation()) or
                        (self.receive_version is not None and self.receive_version.has_operation()) or
                        (self.send_version is not None and self.send_version.has_operation()) or
                        (self.site_of_origin is not None and self.site_of_origin.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.accept_metric_zero.is_set or self.accept_metric_zero.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accept_metric_zero.get_name_leafdata())
                    if (self.broadcast_for_v2.is_set or self.broadcast_for_v2.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.broadcast_for_v2.get_name_leafdata())
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())
                    if (self.passive.is_set or self.passive.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.passive.get_name_leafdata())
                    if (self.poison_reverse.is_set or self.poison_reverse.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.poison_reverse.get_name_leafdata())
                    if (self.policy_in.is_set or self.policy_in.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.policy_in.get_name_leafdata())
                    if (self.policy_out.is_set or self.policy_out.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.policy_out.get_name_leafdata())
                    if (self.split_horizon_disable.is_set or self.split_horizon_disable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.split_horizon_disable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "authentication"):
                        if (self.authentication is None):
                            self.authentication = Rip.DefaultVrf.Interfaces.Interface.Authentication()
                            self.authentication.parent = self
                            self._children_name_map["authentication"] = "authentication"
                        return self.authentication

                    if (child_yang_name == "receive-version"):
                        if (self.receive_version is None):
                            self.receive_version = Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion()
                            self.receive_version.parent = self
                            self._children_name_map["receive_version"] = "receive-version"
                        return self.receive_version

                    if (child_yang_name == "send-version"):
                        if (self.send_version is None):
                            self.send_version = Rip.DefaultVrf.Interfaces.Interface.SendVersion()
                            self.send_version.parent = self
                            self._children_name_map["send_version"] = "send-version"
                        return self.send_version

                    if (child_yang_name == "site-of-origin"):
                        if (self.site_of_origin is None):
                            self.site_of_origin = Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin()
                            self.site_of_origin.parent = self
                            self._children_name_map["site_of_origin"] = "site-of-origin"
                        return self.site_of_origin

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "authentication" or name == "receive-version" or name == "send-version" or name == "site-of-origin" or name == "interface-name" or name == "accept-metric-zero" or name == "broadcast-for-v2" or name == "enable" or name == "passive" or name == "poison-reverse" or name == "policy-in" or name == "policy-out" or name == "split-horizon-disable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "accept-metric-zero"):
                        self.accept_metric_zero = value
                        self.accept_metric_zero.value_namespace = name_space
                        self.accept_metric_zero.value_namespace_prefix = name_space_prefix
                    if(value_path == "broadcast-for-v2"):
                        self.broadcast_for_v2 = value
                        self.broadcast_for_v2.value_namespace = name_space
                        self.broadcast_for_v2.value_namespace_prefix = name_space_prefix
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "passive"):
                        self.passive = value
                        self.passive.value_namespace = name_space
                        self.passive.value_namespace_prefix = name_space_prefix
                    if(value_path == "poison-reverse"):
                        self.poison_reverse = value
                        self.poison_reverse.value_namespace = name_space
                        self.poison_reverse.value_namespace_prefix = name_space_prefix
                    if(value_path == "policy-in"):
                        self.policy_in = value
                        self.policy_in.value_namespace = name_space
                        self.policy_in.value_namespace_prefix = name_space_prefix
                    if(value_path == "policy-out"):
                        self.policy_out = value
                        self.policy_out.value_namespace = name_space
                        self.policy_out.value_namespace_prefix = name_space_prefix
                    if(value_path == "split-horizon-disable"):
                        self.split_horizon_disable = value
                        self.split_horizon_disable.value_namespace = name_space
                        self.split_horizon_disable.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.interface:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interfaces" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface"):
                    for c in self.interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Rip.DefaultVrf.Interfaces.Interface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Neighbors(Entity):
            """
            Configure RIP Neighbors
            
            .. attribute:: neighbor
            
            	Neighbor address
            	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Neighbors.Neighbor>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Neighbors, self).__init__()

                self.yang_name = "neighbors"
                self.yang_parent_name = "default-vrf"

                self.neighbor = YList(self)

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
                            super(Rip.DefaultVrf.Neighbors, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rip.DefaultVrf.Neighbors, self).__setattr__(name, value)


            class Neighbor(Entity):
                """
                Neighbor address
                
                .. attribute:: neighbor_address  <key>
                
                	IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Neighbors.Neighbor, self).__init__()

                    self.yang_name = "neighbor"
                    self.yang_parent_name = "neighbors"

                    self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("neighbor_address") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.DefaultVrf.Neighbors.Neighbor, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.DefaultVrf.Neighbors.Neighbor, self).__setattr__(name, value)

                def has_data(self):
                    return self.neighbor_address.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.neighbor_address.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "neighbor" + "[neighbor-address='" + self.neighbor_address.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/neighbors/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.neighbor_address.is_set or self.neighbor_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.neighbor_address.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "neighbor-address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "neighbor-address"):
                        self.neighbor_address = value
                        self.neighbor_address.value_namespace = name_space
                        self.neighbor_address.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.neighbor:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.neighbor:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "neighbors" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "neighbor"):
                    for c in self.neighbor:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Rip.DefaultVrf.Neighbors.Neighbor()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.neighbor.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "neighbor"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Timers(Entity):
            """
            Various routing timers
            
            .. attribute:: flush_timer
            
            	Flush
            	**type**\:  int
            
            	**range:** 16..250000
            
            	**default value**\: 240
            
            .. attribute:: holddown_timer
            
            	Holddown
            	**type**\:  int
            
            	**range:** 15..200000
            
            	**default value**\: 180
            
            .. attribute:: invalid_timer
            
            	Invalid
            	**type**\:  int
            
            	**range:** 15..200000
            
            	**default value**\: 180
            
            .. attribute:: update_timer
            
            	Interval between updates
            	**type**\:  int
            
            	**range:** 5..50000
            
            	**default value**\: 30
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Timers, self).__init__()

                self.yang_name = "timers"
                self.yang_parent_name = "default-vrf"

                self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                self.holddown_timer = YLeaf(YType.uint32, "holddown-timer")

                self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                self.update_timer = YLeaf(YType.uint32, "update-timer")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("flush_timer",
                                "holddown_timer",
                                "invalid_timer",
                                "update_timer") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rip.DefaultVrf.Timers, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rip.DefaultVrf.Timers, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.flush_timer.is_set or
                    self.holddown_timer.is_set or
                    self.invalid_timer.is_set or
                    self.update_timer.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.flush_timer.yfilter != YFilter.not_set or
                    self.holddown_timer.yfilter != YFilter.not_set or
                    self.invalid_timer.yfilter != YFilter.not_set or
                    self.update_timer.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "timers" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.flush_timer.is_set or self.flush_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.flush_timer.get_name_leafdata())
                if (self.holddown_timer.is_set or self.holddown_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.holddown_timer.get_name_leafdata())
                if (self.invalid_timer.is_set or self.invalid_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.invalid_timer.get_name_leafdata())
                if (self.update_timer.is_set or self.update_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.update_timer.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "flush-timer" or name == "holddown-timer" or name == "invalid-timer" or name == "update-timer"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "flush-timer"):
                    self.flush_timer = value
                    self.flush_timer.value_namespace = name_space
                    self.flush_timer.value_namespace_prefix = name_space_prefix
                if(value_path == "holddown-timer"):
                    self.holddown_timer = value
                    self.holddown_timer.value_namespace = name_space
                    self.holddown_timer.value_namespace_prefix = name_space_prefix
                if(value_path == "invalid-timer"):
                    self.invalid_timer = value
                    self.invalid_timer.value_namespace = name_space
                    self.invalid_timer.value_namespace_prefix = name_space_prefix
                if(value_path == "update-timer"):
                    self.update_timer = value
                    self.update_timer.value_namespace = name_space
                    self.update_timer.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.auto_summary.is_set or
                self.broadcast_for_v2.is_set or
                self.default_metric.is_set or
                self.distance.is_set or
                self.enable.is_set or
                self.maximum_paths.is_set or
                self.nsf.is_set or
                self.output_delay.is_set or
                self.policy_in.is_set or
                self.policy_out.is_set or
                self.validate_source_disable.is_set or
                (self.interfaces is not None and self.interfaces.has_data()) or
                (self.ip_distances is not None and self.ip_distances.has_data()) or
                (self.neighbors is not None and self.neighbors.has_data()) or
                (self.redistribution is not None and self.redistribution.has_data()) or
                (self.timers is not None and self.timers.has_data()) or
                (self.default_information is not None))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.auto_summary.yfilter != YFilter.not_set or
                self.broadcast_for_v2.yfilter != YFilter.not_set or
                self.default_metric.yfilter != YFilter.not_set or
                self.distance.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set or
                self.maximum_paths.yfilter != YFilter.not_set or
                self.nsf.yfilter != YFilter.not_set or
                self.output_delay.yfilter != YFilter.not_set or
                self.policy_in.yfilter != YFilter.not_set or
                self.policy_out.yfilter != YFilter.not_set or
                self.validate_source_disable.yfilter != YFilter.not_set or
                (self.default_information is not None and self.default_information.has_operation()) or
                (self.interfaces is not None and self.interfaces.has_operation()) or
                (self.ip_distances is not None and self.ip_distances.has_operation()) or
                (self.neighbors is not None and self.neighbors.has_operation()) or
                (self.redistribution is not None and self.redistribution.has_operation()) or
                (self.timers is not None and self.timers.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "default-vrf" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.auto_summary.is_set or self.auto_summary.yfilter != YFilter.not_set):
                leaf_name_data.append(self.auto_summary.get_name_leafdata())
            if (self.broadcast_for_v2.is_set or self.broadcast_for_v2.yfilter != YFilter.not_set):
                leaf_name_data.append(self.broadcast_for_v2.get_name_leafdata())
            if (self.default_metric.is_set or self.default_metric.yfilter != YFilter.not_set):
                leaf_name_data.append(self.default_metric.get_name_leafdata())
            if (self.distance.is_set or self.distance.yfilter != YFilter.not_set):
                leaf_name_data.append(self.distance.get_name_leafdata())
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())
            if (self.maximum_paths.is_set or self.maximum_paths.yfilter != YFilter.not_set):
                leaf_name_data.append(self.maximum_paths.get_name_leafdata())
            if (self.nsf.is_set or self.nsf.yfilter != YFilter.not_set):
                leaf_name_data.append(self.nsf.get_name_leafdata())
            if (self.output_delay.is_set or self.output_delay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.output_delay.get_name_leafdata())
            if (self.policy_in.is_set or self.policy_in.yfilter != YFilter.not_set):
                leaf_name_data.append(self.policy_in.get_name_leafdata())
            if (self.policy_out.is_set or self.policy_out.yfilter != YFilter.not_set):
                leaf_name_data.append(self.policy_out.get_name_leafdata())
            if (self.validate_source_disable.is_set or self.validate_source_disable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.validate_source_disable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "default-information"):
                if (self.default_information is None):
                    self.default_information = Rip.DefaultVrf.DefaultInformation()
                    self.default_information.parent = self
                    self._children_name_map["default_information"] = "default-information"
                return self.default_information

            if (child_yang_name == "interfaces"):
                if (self.interfaces is None):
                    self.interfaces = Rip.DefaultVrf.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                return self.interfaces

            if (child_yang_name == "ip-distances"):
                if (self.ip_distances is None):
                    self.ip_distances = Rip.DefaultVrf.IpDistances()
                    self.ip_distances.parent = self
                    self._children_name_map["ip_distances"] = "ip-distances"
                return self.ip_distances

            if (child_yang_name == "neighbors"):
                if (self.neighbors is None):
                    self.neighbors = Rip.DefaultVrf.Neighbors()
                    self.neighbors.parent = self
                    self._children_name_map["neighbors"] = "neighbors"
                return self.neighbors

            if (child_yang_name == "redistribution"):
                if (self.redistribution is None):
                    self.redistribution = Rip.DefaultVrf.Redistribution()
                    self.redistribution.parent = self
                    self._children_name_map["redistribution"] = "redistribution"
                return self.redistribution

            if (child_yang_name == "timers"):
                if (self.timers is None):
                    self.timers = Rip.DefaultVrf.Timers()
                    self.timers.parent = self
                    self._children_name_map["timers"] = "timers"
                return self.timers

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "default-information" or name == "interfaces" or name == "ip-distances" or name == "neighbors" or name == "redistribution" or name == "timers" or name == "auto-summary" or name == "broadcast-for-v2" or name == "default-metric" or name == "distance" or name == "enable" or name == "maximum-paths" or name == "nsf" or name == "output-delay" or name == "policy-in" or name == "policy-out" or name == "validate-source-disable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "auto-summary"):
                self.auto_summary = value
                self.auto_summary.value_namespace = name_space
                self.auto_summary.value_namespace_prefix = name_space_prefix
            if(value_path == "broadcast-for-v2"):
                self.broadcast_for_v2 = value
                self.broadcast_for_v2.value_namespace = name_space
                self.broadcast_for_v2.value_namespace_prefix = name_space_prefix
            if(value_path == "default-metric"):
                self.default_metric = value
                self.default_metric.value_namespace = name_space
                self.default_metric.value_namespace_prefix = name_space_prefix
            if(value_path == "distance"):
                self.distance = value
                self.distance.value_namespace = name_space
                self.distance.value_namespace_prefix = name_space_prefix
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix
            if(value_path == "maximum-paths"):
                self.maximum_paths = value
                self.maximum_paths.value_namespace = name_space
                self.maximum_paths.value_namespace_prefix = name_space_prefix
            if(value_path == "nsf"):
                self.nsf = value
                self.nsf.value_namespace = name_space
                self.nsf.value_namespace_prefix = name_space_prefix
            if(value_path == "output-delay"):
                self.output_delay = value
                self.output_delay.value_namespace = name_space
                self.output_delay.value_namespace_prefix = name_space_prefix
            if(value_path == "policy-in"):
                self.policy_in = value
                self.policy_in.value_namespace = name_space
                self.policy_in.value_namespace_prefix = name_space_prefix
            if(value_path == "policy-out"):
                self.policy_out = value
                self.policy_out.value_namespace = name_space
                self.policy_out.value_namespace_prefix = name_space_prefix
            if(value_path == "validate-source-disable"):
                self.validate_source_disable = value
                self.validate_source_disable.value_namespace = name_space
                self.validate_source_disable.value_namespace_prefix = name_space_prefix


    class Vrfs(Entity):
        """
        VRF related RIP configuration
        
        .. attribute:: vrf
        
        	RIP configuration for a particular VRF
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ip-rip-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rip.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "rip"

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
                        super(Rip.Vrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rip.Vrfs, self).__setattr__(name, value)


        class Vrf(Entity):
            """
            RIP configuration for a particular VRF
            
            .. attribute:: vrf_name  <key>
            
            	VRF Name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: auto_summary
            
            	Enable automatic network number summarization
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: broadcast_for_v2
            
            	Send RIP v2 output packets to broadcast address
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: default_information
            
            	Controls default information origination
            	**type**\:   :py:class:`DefaultInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.DefaultInformation>`
            
            	**presence node**\: True
            
            .. attribute:: default_metric
            
            	Default metric of redistributed routes
            	**type**\:  int
            
            	**range:** 0..16
            
            .. attribute:: distance
            
            	Administrative distance
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 120
            
            .. attribute:: enable
            
            	Starts RIP configuration for a particular VRF
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: interfaces
            
            	Table of RIP interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces>`
            
            .. attribute:: ip_distances
            
            	Table of IP specific administrative distances
            	**type**\:   :py:class:`IpDistances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.IpDistances>`
            
            .. attribute:: maximum_paths
            
            	Maximum number of paths allowed per route
            	**type**\:  int
            
            	**range:** 1..128
            
            	**default value**\: 4
            
            .. attribute:: neighbors
            
            	Configure RIP Neighbors
            	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Neighbors>`
            
            .. attribute:: nsf
            
            	Enable Cisco Non Stop Forwarding
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: output_delay
            
            	Inter\-packet delay for RIP updates
            	**type**\:  int
            
            	**range:** 8..50
            
            	**units**\: millisecond
            
            .. attribute:: policy_in
            
            	Route Policy for inbbound routing updates
            	**type**\:  str
            
            .. attribute:: policy_out
            
            	Route Policy for outbound routing updates
            	**type**\:  str
            
            .. attribute:: redistribution
            
            	Redistribute information from another routing protocol
            	**type**\:   :py:class:`Redistribution <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution>`
            
            .. attribute:: timers
            
            	Various routing timers
            	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Timers>`
            
            .. attribute:: validate_source_disable
            
            	Disable validation of source address of routing updates
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.auto_summary = YLeaf(YType.empty, "auto-summary")

                self.broadcast_for_v2 = YLeaf(YType.empty, "broadcast-for-v2")

                self.default_metric = YLeaf(YType.uint32, "default-metric")

                self.distance = YLeaf(YType.uint32, "distance")

                self.enable = YLeaf(YType.empty, "enable")

                self.maximum_paths = YLeaf(YType.uint32, "maximum-paths")

                self.nsf = YLeaf(YType.empty, "nsf")

                self.output_delay = YLeaf(YType.uint32, "output-delay")

                self.policy_in = YLeaf(YType.str, "policy-in")

                self.policy_out = YLeaf(YType.str, "policy-out")

                self.validate_source_disable = YLeaf(YType.empty, "validate-source-disable")

                self.default_information = None
                self._children_name_map["default_information"] = "default-information"
                self._children_yang_names.add("default-information")

                self.interfaces = Rip.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.ip_distances = Rip.Vrfs.Vrf.IpDistances()
                self.ip_distances.parent = self
                self._children_name_map["ip_distances"] = "ip-distances"
                self._children_yang_names.add("ip-distances")

                self.neighbors = Rip.Vrfs.Vrf.Neighbors()
                self.neighbors.parent = self
                self._children_name_map["neighbors"] = "neighbors"
                self._children_yang_names.add("neighbors")

                self.redistribution = Rip.Vrfs.Vrf.Redistribution()
                self.redistribution.parent = self
                self._children_name_map["redistribution"] = "redistribution"
                self._children_yang_names.add("redistribution")

                self.timers = Rip.Vrfs.Vrf.Timers()
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
                    if name in ("vrf_name",
                                "auto_summary",
                                "broadcast_for_v2",
                                "default_metric",
                                "distance",
                                "enable",
                                "maximum_paths",
                                "nsf",
                                "output_delay",
                                "policy_in",
                                "policy_out",
                                "validate_source_disable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rip.Vrfs.Vrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rip.Vrfs.Vrf, self).__setattr__(name, value)


            class DefaultInformation(Entity):
                """
                Controls default information origination
                
                .. attribute:: option
                
                	Origination option
                	**type**\:   :py:class:`DefaultInformationOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultInformationOption>`
                
                	**mandatory**\: True
                
                .. attribute:: route_policy_name
                
                	Route policy name
                	**type**\:  str
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.DefaultInformation, self).__init__()

                    self.yang_name = "default-information"
                    self.yang_parent_name = "vrf"
                    self.is_presence_container = True

                    self.option = YLeaf(YType.enumeration, "option")

                    self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("option",
                                    "route_policy_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.Vrfs.Vrf.DefaultInformation, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Vrfs.Vrf.DefaultInformation, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.option.is_set or
                        self.route_policy_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.option.yfilter != YFilter.not_set or
                        self.route_policy_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "default-information" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.option.is_set or self.option.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.option.get_name_leafdata())
                    if (self.route_policy_name.is_set or self.route_policy_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_policy_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "option" or name == "route-policy-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "option"):
                        self.option = value
                        self.option.value_namespace = name_space
                        self.option.value_namespace_prefix = name_space_prefix
                    if(value_path == "route-policy-name"):
                        self.route_policy_name = value
                        self.route_policy_name.value_namespace = name_space
                        self.route_policy_name.value_namespace_prefix = name_space_prefix


            class Redistribution(Entity):
                """
                Redistribute information from another routing
                protocol
                
                .. attribute:: bgps
                
                	Redistribute BGP routes
                	**type**\:   :py:class:`Bgps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Bgps>`
                
                .. attribute:: connected
                
                	Redistribute connected routes
                	**type**\:   :py:class:`Connected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Connected>`
                
                	**presence node**\: True
                
                .. attribute:: eigrp_s
                
                	Redistribute EIGRP routes
                	**type**\:   :py:class:`EigrpS <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.EigrpS>`
                
                .. attribute:: isises
                
                	Redistribute IS\-IS routes
                	**type**\:   :py:class:`Isises <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Isises>`
                
                .. attribute:: ospfs
                
                	Redistribute OSPF routes
                	**type**\:   :py:class:`Ospfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Ospfs>`
                
                .. attribute:: static
                
                	Redistribute static routes
                	**type**\:   :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Static>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Redistribution, self).__init__()

                    self.yang_name = "redistribution"
                    self.yang_parent_name = "vrf"

                    self.bgps = Rip.Vrfs.Vrf.Redistribution.Bgps()
                    self.bgps.parent = self
                    self._children_name_map["bgps"] = "bgps"
                    self._children_yang_names.add("bgps")

                    self.connected = None
                    self._children_name_map["connected"] = "connected"
                    self._children_yang_names.add("connected")

                    self.eigrp_s = Rip.Vrfs.Vrf.Redistribution.EigrpS()
                    self.eigrp_s.parent = self
                    self._children_name_map["eigrp_s"] = "eigrp-s"
                    self._children_yang_names.add("eigrp-s")

                    self.isises = Rip.Vrfs.Vrf.Redistribution.Isises()
                    self.isises.parent = self
                    self._children_name_map["isises"] = "isises"
                    self._children_yang_names.add("isises")

                    self.ospfs = Rip.Vrfs.Vrf.Redistribution.Ospfs()
                    self.ospfs.parent = self
                    self._children_name_map["ospfs"] = "ospfs"
                    self._children_yang_names.add("ospfs")

                    self.static = None
                    self._children_name_map["static"] = "static"
                    self._children_yang_names.add("static")


                class Connected(Entity):
                    """
                    Redistribute connected routes
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:   :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.Connected, self).__init__()

                        self.yang_name = "connected"
                        self.yang_parent_name = "redistribution"
                        self.is_presence_container = True

                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                        self.route_type = YLeaf(YType.enumeration, "route-type")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("route_policy_name",
                                        "route_type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.Vrfs.Vrf.Redistribution.Connected, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Vrfs.Vrf.Redistribution.Connected, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.route_policy_name.is_set or
                            self.route_type.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.route_policy_name.yfilter != YFilter.not_set or
                            self.route_type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "connected" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.route_policy_name.is_set or self.route_policy_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_policy_name.get_name_leafdata())
                        if (self.route_type.is_set or self.route_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "route-policy-name" or name == "route-type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "route-policy-name"):
                            self.route_policy_name = value
                            self.route_policy_name.value_namespace = name_space
                            self.route_policy_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-type"):
                            self.route_type = value
                            self.route_type.value_namespace = name_space
                            self.route_type.value_namespace_prefix = name_space_prefix


                class Bgps(Entity):
                    """
                    Redistribute BGP routes
                    
                    .. attribute:: bgp
                    
                    	Autonomous system number
                    	**type**\: list of    :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.Bgps, self).__init__()

                        self.yang_name = "bgps"
                        self.yang_parent_name = "redistribution"

                        self.bgp = YList(self)

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
                                    super(Rip.Vrfs.Vrf.Redistribution.Bgps, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Vrfs.Vrf.Redistribution.Bgps, self).__setattr__(name, value)


                    class Bgp(Entity):
                        """
                        Autonomous system number
                        
                        .. attribute:: asnxx  <key>
                        
                        	Higher 16 bits of 4\-byte BGP AS number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: asnyy  <key>
                        
                        	2\-byte or 4\-byte BGP AS number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: policy
                        
                        	Route Policy name
                        	**type**\:  str
                        
                        .. attribute:: type
                        
                        	Route type
                        	**type**\:   :py:class:`BgpRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.BgpRedistRoute>`
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp, self).__init__()

                            self.yang_name = "bgp"
                            self.yang_parent_name = "bgps"

                            self.asnxx = YLeaf(YType.uint32, "asnxx")

                            self.asnyy = YLeaf(YType.uint32, "asnyy")

                            self.policy = YLeaf(YType.str, "policy")

                            self.type = YLeaf(YType.enumeration, "type")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("asnxx",
                                            "asnyy",
                                            "policy",
                                            "type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.asnxx.is_set or
                                self.asnyy.is_set or
                                self.policy.is_set or
                                self.type.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.asnxx.yfilter != YFilter.not_set or
                                self.asnyy.yfilter != YFilter.not_set or
                                self.policy.yfilter != YFilter.not_set or
                                self.type.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "bgp" + "[asnxx='" + self.asnxx.get() + "']" + "[asnyy='" + self.asnyy.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.asnxx.is_set or self.asnxx.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.asnxx.get_name_leafdata())
                            if (self.asnyy.is_set or self.asnyy.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.asnyy.get_name_leafdata())
                            if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policy.get_name_leafdata())
                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "asnxx" or name == "asnyy" or name == "policy" or name == "type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "asnxx"):
                                self.asnxx = value
                                self.asnxx.value_namespace = name_space
                                self.asnxx.value_namespace_prefix = name_space_prefix
                            if(value_path == "asnyy"):
                                self.asnyy = value
                                self.asnyy.value_namespace = name_space
                                self.asnyy.value_namespace_prefix = name_space_prefix
                            if(value_path == "policy"):
                                self.policy = value
                                self.policy.value_namespace = name_space
                                self.policy.value_namespace_prefix = name_space_prefix
                            if(value_path == "type"):
                                self.type = value
                                self.type.value_namespace = name_space
                                self.type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.bgp:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.bgp:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bgps" + path_buffer

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

                        if (child_yang_name == "bgp"):
                            for c in self.bgp:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.bgp.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bgp"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Isises(Entity):
                    """
                    Redistribute IS\-IS routes
                    
                    .. attribute:: isis
                    
                    	Redistribute IS\-IS routes
                    	**type**\: list of    :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Isises.Isis>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.Isises, self).__init__()

                        self.yang_name = "isises"
                        self.yang_parent_name = "redistribution"

                        self.isis = YList(self)

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
                                    super(Rip.Vrfs.Vrf.Redistribution.Isises, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Vrfs.Vrf.Redistribution.Isises, self).__setattr__(name, value)


                    class Isis(Entity):
                        """
                        Redistribute IS\-IS routes
                        
                        .. attribute:: isis_name  <key>
                        
                        	IS\-IS instance name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: route_policy_name
                        
                        	Route Policy name
                        	**type**\:  str
                        
                        .. attribute:: route_type
                        
                        	Route type
                        	**type**\:   :py:class:`IsisRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.IsisRedistRoute>`
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Redistribution.Isises.Isis, self).__init__()

                            self.yang_name = "isis"
                            self.yang_parent_name = "isises"

                            self.isis_name = YLeaf(YType.str, "isis-name")

                            self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                            self.route_type = YLeaf(YType.enumeration, "route-type")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("isis_name",
                                            "route_policy_name",
                                            "route_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Rip.Vrfs.Vrf.Redistribution.Isises.Isis, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Rip.Vrfs.Vrf.Redistribution.Isises.Isis, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.isis_name.is_set or
                                self.route_policy_name.is_set or
                                self.route_type.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.isis_name.yfilter != YFilter.not_set or
                                self.route_policy_name.yfilter != YFilter.not_set or
                                self.route_type.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "isis" + "[isis-name='" + self.isis_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.isis_name.is_set or self.isis_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.isis_name.get_name_leafdata())
                            if (self.route_policy_name.is_set or self.route_policy_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.route_policy_name.get_name_leafdata())
                            if (self.route_type.is_set or self.route_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.route_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "isis-name" or name == "route-policy-name" or name == "route-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "isis-name"):
                                self.isis_name = value
                                self.isis_name.value_namespace = name_space
                                self.isis_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "route-policy-name"):
                                self.route_policy_name = value
                                self.route_policy_name.value_namespace = name_space
                                self.route_policy_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "route-type"):
                                self.route_type = value
                                self.route_type.value_namespace = name_space
                                self.route_type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.isis:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.isis:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "isises" + path_buffer

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

                        if (child_yang_name == "isis"):
                            for c in self.isis:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Rip.Vrfs.Vrf.Redistribution.Isises.Isis()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.isis.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "isis"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class EigrpS(Entity):
                    """
                    Redistribute EIGRP routes
                    
                    .. attribute:: eigrp
                    
                    	Redistribute EIGRP routes
                    	**type**\: list of    :py:class:`Eigrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.EigrpS, self).__init__()

                        self.yang_name = "eigrp-s"
                        self.yang_parent_name = "redistribution"

                        self.eigrp = YList(self)

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
                                    super(Rip.Vrfs.Vrf.Redistribution.EigrpS, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Vrfs.Vrf.Redistribution.EigrpS, self).__setattr__(name, value)


                    class Eigrp(Entity):
                        """
                        Redistribute EIGRP routes
                        
                        .. attribute:: as_  <key>
                        
                        	Autonomous system number
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: route_policy_name
                        
                        	Route Policy name
                        	**type**\:  str
                        
                        .. attribute:: route_type
                        
                        	Route type
                        	**type**\:   :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp, self).__init__()

                            self.yang_name = "eigrp"
                            self.yang_parent_name = "eigrp-s"

                            self.as_ = YLeaf(YType.uint32, "as")

                            self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                            self.route_type = YLeaf(YType.enumeration, "route-type")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("as_",
                                            "route_policy_name",
                                            "route_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.as_.is_set or
                                self.route_policy_name.is_set or
                                self.route_type.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.as_.yfilter != YFilter.not_set or
                                self.route_policy_name.yfilter != YFilter.not_set or
                                self.route_type.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "eigrp" + "[as='" + self.as_.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.as_.is_set or self.as_.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.as_.get_name_leafdata())
                            if (self.route_policy_name.is_set or self.route_policy_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.route_policy_name.get_name_leafdata())
                            if (self.route_type.is_set or self.route_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.route_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "as" or name == "route-policy-name" or name == "route-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "as"):
                                self.as_ = value
                                self.as_.value_namespace = name_space
                                self.as_.value_namespace_prefix = name_space_prefix
                            if(value_path == "route-policy-name"):
                                self.route_policy_name = value
                                self.route_policy_name.value_namespace = name_space
                                self.route_policy_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "route-type"):
                                self.route_type = value
                                self.route_type.value_namespace = name_space
                                self.route_type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.eigrp:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.eigrp:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "eigrp-s" + path_buffer

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

                        if (child_yang_name == "eigrp"):
                            for c in self.eigrp:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.eigrp.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "eigrp"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Static(Entity):
                    """
                    Redistribute static routes
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:   :py:class:`DefaultRedistRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRoute>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.Static, self).__init__()

                        self.yang_name = "static"
                        self.yang_parent_name = "redistribution"
                        self.is_presence_container = True

                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                        self.route_type = YLeaf(YType.enumeration, "route-type")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("route_policy_name",
                                        "route_type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.Vrfs.Vrf.Redistribution.Static, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Vrfs.Vrf.Redistribution.Static, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.route_policy_name.is_set or
                            self.route_type.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.route_policy_name.yfilter != YFilter.not_set or
                            self.route_type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "static" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.route_policy_name.is_set or self.route_policy_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_policy_name.get_name_leafdata())
                        if (self.route_type.is_set or self.route_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "route-policy-name" or name == "route-type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "route-policy-name"):
                            self.route_policy_name = value
                            self.route_policy_name.value_namespace = name_space
                            self.route_policy_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-type"):
                            self.route_type = value
                            self.route_type.value_namespace = name_space
                            self.route_type.value_namespace_prefix = name_space_prefix


                class Ospfs(Entity):
                    """
                    Redistribute OSPF routes
                    
                    .. attribute:: ospf
                    
                    	Redistribute OSPF routes
                    	**type**\: list of    :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Redistribution.Ospfs, self).__init__()

                        self.yang_name = "ospfs"
                        self.yang_parent_name = "redistribution"

                        self.ospf = YList(self)

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
                                    super(Rip.Vrfs.Vrf.Redistribution.Ospfs, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Vrfs.Vrf.Redistribution.Ospfs, self).__setattr__(name, value)


                    class Ospf(Entity):
                        """
                        Redistribute OSPF routes
                        
                        .. attribute:: ospf_name  <key>
                        
                        	Process ID for the OSPF instance
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: external
                        
                        	External routes
                        	**type**\:  bool
                        
                        .. attribute:: external_type
                        
                        	External route type
                        	**type**\:  int
                        
                        	**range:** 0..2
                        
                        .. attribute:: internal
                        
                        	Internal routes
                        	**type**\:  bool
                        
                        .. attribute:: nssa_external
                        
                        	NSSA External routes
                        	**type**\:  bool
                        
                        .. attribute:: nssa_external_type
                        
                        	NSSA External route type
                        	**type**\:  int
                        
                        	**range:** 0..2
                        
                        .. attribute:: route_policy_name
                        
                        	Route Policy name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf, self).__init__()

                            self.yang_name = "ospf"
                            self.yang_parent_name = "ospfs"

                            self.ospf_name = YLeaf(YType.str, "ospf-name")

                            self.external = YLeaf(YType.boolean, "external")

                            self.external_type = YLeaf(YType.uint32, "external-type")

                            self.internal = YLeaf(YType.boolean, "internal")

                            self.nssa_external = YLeaf(YType.boolean, "nssa-external")

                            self.nssa_external_type = YLeaf(YType.uint32, "nssa-external-type")

                            self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ospf_name",
                                            "external",
                                            "external_type",
                                            "internal",
                                            "nssa_external",
                                            "nssa_external_type",
                                            "route_policy_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ospf_name.is_set or
                                self.external.is_set or
                                self.external_type.is_set or
                                self.internal.is_set or
                                self.nssa_external.is_set or
                                self.nssa_external_type.is_set or
                                self.route_policy_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ospf_name.yfilter != YFilter.not_set or
                                self.external.yfilter != YFilter.not_set or
                                self.external_type.yfilter != YFilter.not_set or
                                self.internal.yfilter != YFilter.not_set or
                                self.nssa_external.yfilter != YFilter.not_set or
                                self.nssa_external_type.yfilter != YFilter.not_set or
                                self.route_policy_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ospf" + "[ospf-name='" + self.ospf_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ospf_name.is_set or self.ospf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ospf_name.get_name_leafdata())
                            if (self.external.is_set or self.external.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.external.get_name_leafdata())
                            if (self.external_type.is_set or self.external_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.external_type.get_name_leafdata())
                            if (self.internal.is_set or self.internal.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.internal.get_name_leafdata())
                            if (self.nssa_external.is_set or self.nssa_external.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.nssa_external.get_name_leafdata())
                            if (self.nssa_external_type.is_set or self.nssa_external_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.nssa_external_type.get_name_leafdata())
                            if (self.route_policy_name.is_set or self.route_policy_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.route_policy_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ospf-name" or name == "external" or name == "external-type" or name == "internal" or name == "nssa-external" or name == "nssa-external-type" or name == "route-policy-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ospf-name"):
                                self.ospf_name = value
                                self.ospf_name.value_namespace = name_space
                                self.ospf_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "external"):
                                self.external = value
                                self.external.value_namespace = name_space
                                self.external.value_namespace_prefix = name_space_prefix
                            if(value_path == "external-type"):
                                self.external_type = value
                                self.external_type.value_namespace = name_space
                                self.external_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "internal"):
                                self.internal = value
                                self.internal.value_namespace = name_space
                                self.internal.value_namespace_prefix = name_space_prefix
                            if(value_path == "nssa-external"):
                                self.nssa_external = value
                                self.nssa_external.value_namespace = name_space
                                self.nssa_external.value_namespace_prefix = name_space_prefix
                            if(value_path == "nssa-external-type"):
                                self.nssa_external_type = value
                                self.nssa_external_type.value_namespace = name_space
                                self.nssa_external_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "route-policy-name"):
                                self.route_policy_name = value
                                self.route_policy_name.value_namespace = name_space
                                self.route_policy_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.ospf:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.ospf:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ospfs" + path_buffer

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

                        if (child_yang_name == "ospf"):
                            for c in self.ospf:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.ospf.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ospf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.bgps is not None and self.bgps.has_data()) or
                        (self.eigrp_s is not None and self.eigrp_s.has_data()) or
                        (self.isises is not None and self.isises.has_data()) or
                        (self.ospfs is not None and self.ospfs.has_data()) or
                        (self.connected is not None) or
                        (self.static is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.bgps is not None and self.bgps.has_operation()) or
                        (self.connected is not None and self.connected.has_operation()) or
                        (self.eigrp_s is not None and self.eigrp_s.has_operation()) or
                        (self.isises is not None and self.isises.has_operation()) or
                        (self.ospfs is not None and self.ospfs.has_operation()) or
                        (self.static is not None and self.static.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "redistribution" + path_buffer

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

                    if (child_yang_name == "bgps"):
                        if (self.bgps is None):
                            self.bgps = Rip.Vrfs.Vrf.Redistribution.Bgps()
                            self.bgps.parent = self
                            self._children_name_map["bgps"] = "bgps"
                        return self.bgps

                    if (child_yang_name == "connected"):
                        if (self.connected is None):
                            self.connected = Rip.Vrfs.Vrf.Redistribution.Connected()
                            self.connected.parent = self
                            self._children_name_map["connected"] = "connected"
                        return self.connected

                    if (child_yang_name == "eigrp-s"):
                        if (self.eigrp_s is None):
                            self.eigrp_s = Rip.Vrfs.Vrf.Redistribution.EigrpS()
                            self.eigrp_s.parent = self
                            self._children_name_map["eigrp_s"] = "eigrp-s"
                        return self.eigrp_s

                    if (child_yang_name == "isises"):
                        if (self.isises is None):
                            self.isises = Rip.Vrfs.Vrf.Redistribution.Isises()
                            self.isises.parent = self
                            self._children_name_map["isises"] = "isises"
                        return self.isises

                    if (child_yang_name == "ospfs"):
                        if (self.ospfs is None):
                            self.ospfs = Rip.Vrfs.Vrf.Redistribution.Ospfs()
                            self.ospfs.parent = self
                            self._children_name_map["ospfs"] = "ospfs"
                        return self.ospfs

                    if (child_yang_name == "static"):
                        if (self.static is None):
                            self.static = Rip.Vrfs.Vrf.Redistribution.Static()
                            self.static.parent = self
                            self._children_name_map["static"] = "static"
                        return self.static

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bgps" or name == "connected" or name == "eigrp-s" or name == "isises" or name == "ospfs" or name == "static"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class IpDistances(Entity):
                """
                Table of IP specific administrative distances
                
                .. attribute:: ip_distance
                
                	IP specific administrative distance
                	**type**\: list of    :py:class:`IpDistance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.IpDistances.IpDistance>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.IpDistances, self).__init__()

                    self.yang_name = "ip-distances"
                    self.yang_parent_name = "vrf"

                    self.ip_distance = YList(self)

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
                                super(Rip.Vrfs.Vrf.IpDistances, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Vrfs.Vrf.IpDistances, self).__setattr__(name, value)


                class IpDistance(Entity):
                    """
                    IP specific administrative distance
                    
                    .. attribute:: address  <key>
                    
                    	IP Source address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: netmask  <key>
                    
                    	IP address mask
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: distance
                    
                    	Administrative distance
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.IpDistances.IpDistance, self).__init__()

                        self.yang_name = "ip-distance"
                        self.yang_parent_name = "ip-distances"

                        self.address = YLeaf(YType.str, "address")

                        self.netmask = YLeaf(YType.str, "netmask")

                        self.distance = YLeaf(YType.uint32, "distance")

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
                                        "netmask",
                                        "distance") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.Vrfs.Vrf.IpDistances.IpDistance, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Vrfs.Vrf.IpDistances.IpDistance, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.netmask.is_set or
                            self.distance.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.netmask.yfilter != YFilter.not_set or
                            self.distance.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ip-distance" + "[address='" + self.address.get() + "']" + "[netmask='" + self.netmask.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.netmask.is_set or self.netmask.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.netmask.get_name_leafdata())
                        if (self.distance.is_set or self.distance.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.distance.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "netmask" or name == "distance"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "netmask"):
                            self.netmask = value
                            self.netmask.value_namespace = name_space
                            self.netmask.value_namespace_prefix = name_space_prefix
                        if(value_path == "distance"):
                            self.distance = value
                            self.distance.value_namespace = name_space
                            self.distance.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ip_distance:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ip_distance:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ip-distances" + path_buffer

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

                    if (child_yang_name == "ip-distance"):
                        for c in self.ip_distance:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.Vrfs.Vrf.IpDistances.IpDistance()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ip_distance.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip-distance"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Interfaces(Entity):
                """
                Table of RIP interfaces
                
                .. attribute:: interface
                
                	RIP interface name
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "vrf"

                    self.interface = YList(self)

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
                                super(Rip.Vrfs.Vrf.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Vrfs.Vrf.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    RIP interface name
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: accept_metric_zero
                    
                    	Accept RIP updates with metric 0
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: authentication
                    
                    	Authentication keychain and mode
                    	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.Authentication>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: broadcast_for_v2
                    
                    	Send RIP v2 output packets to broadcast address
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: enable
                    
                    	Starts RIP interface configuration
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: passive
                    
                    	Suppress routing updates on this interface
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: poison_reverse
                    
                    	Enable poison reverse
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: policy_in
                    
                    	Route Policy for inbound routing updates
                    	**type**\:  str
                    
                    .. attribute:: policy_out
                    
                    	Route Policy for outbound routing updates
                    	**type**\:  str
                    
                    .. attribute:: receive_version
                    
                    	RIP versions supported for receiving advertisements
                    	**type**\:   :py:class:`ReceiveVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion>`
                    
                    .. attribute:: send_version
                    
                    	RIP versions supported for sending advertisements
                    	**type**\:   :py:class:`SendVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion>`
                    
                    .. attribute:: site_of_origin
                    
                    	SOO community for prefixes learned over this interface
                    	**type**\:   :py:class:`SiteOfOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin>`
                    
                    .. attribute:: split_horizon_disable
                    
                    	Disable split horizon
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.accept_metric_zero = YLeaf(YType.empty, "accept-metric-zero")

                        self.broadcast_for_v2 = YLeaf(YType.empty, "broadcast-for-v2")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.passive = YLeaf(YType.empty, "passive")

                        self.poison_reverse = YLeaf(YType.empty, "poison-reverse")

                        self.policy_in = YLeaf(YType.str, "policy-in")

                        self.policy_out = YLeaf(YType.str, "policy-out")

                        self.split_horizon_disable = YLeaf(YType.empty, "split-horizon-disable")

                        self.authentication = None
                        self._children_name_map["authentication"] = "authentication"
                        self._children_yang_names.add("authentication")

                        self.receive_version = Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion()
                        self.receive_version.parent = self
                        self._children_name_map["receive_version"] = "receive-version"
                        self._children_yang_names.add("receive-version")

                        self.send_version = Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion()
                        self.send_version.parent = self
                        self._children_name_map["send_version"] = "send-version"
                        self._children_yang_names.add("send-version")

                        self.site_of_origin = Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin()
                        self.site_of_origin.parent = self
                        self._children_name_map["site_of_origin"] = "site-of-origin"
                        self._children_yang_names.add("site-of-origin")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "accept_metric_zero",
                                        "broadcast_for_v2",
                                        "enable",
                                        "passive",
                                        "poison_reverse",
                                        "policy_in",
                                        "policy_out",
                                        "split_horizon_disable") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.Vrfs.Vrf.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Vrfs.Vrf.Interfaces.Interface, self).__setattr__(name, value)


                    class Authentication(Entity):
                        """
                        Authentication keychain and mode
                        
                        .. attribute:: keychain
                        
                        	Name of keychain
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: mode
                        
                        	Authentication mode
                        	**type**\:   :py:class:`RipAuthMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipAuthMode>`
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Interfaces.Interface.Authentication, self).__init__()

                            self.yang_name = "authentication"
                            self.yang_parent_name = "interface"
                            self.is_presence_container = True

                            self.keychain = YLeaf(YType.str, "keychain")

                            self.mode = YLeaf(YType.enumeration, "mode")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("keychain",
                                            "mode") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Rip.Vrfs.Vrf.Interfaces.Interface.Authentication, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Rip.Vrfs.Vrf.Interfaces.Interface.Authentication, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.keychain.is_set or
                                self.mode.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.keychain.yfilter != YFilter.not_set or
                                self.mode.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "authentication" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.keychain.is_set or self.keychain.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.keychain.get_name_leafdata())
                            if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mode.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "keychain" or name == "mode"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "keychain"):
                                self.keychain = value
                                self.keychain.value_namespace = name_space
                                self.keychain.value_namespace_prefix = name_space_prefix
                            if(value_path == "mode"):
                                self.mode = value
                                self.mode.value_namespace = name_space
                                self.mode.value_namespace_prefix = name_space_prefix


                    class SiteOfOrigin(Entity):
                        """
                        SOO community for prefixes learned over this
                        interface
                        
                        .. attribute:: address
                        
                        	IPV4 address for IPV4Address\:nn format
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: address_index
                        
                        	16bit value for IPV4Address\:nn format
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: as_index
                        
                        	AS Number Index
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: as_xx
                        
                        	AS Number for AS\:nn format
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: as_yy
                        
                        	32 bit value for AS\:nn format
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Extended community type
                        	**type**\:   :py:class:`RipExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipExtCommunity>`
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin, self).__init__()

                            self.yang_name = "site-of-origin"
                            self.yang_parent_name = "interface"

                            self.address = YLeaf(YType.str, "address")

                            self.address_index = YLeaf(YType.uint32, "address-index")

                            self.as_index = YLeaf(YType.uint32, "as-index")

                            self.as_xx = YLeaf(YType.uint32, "as-xx")

                            self.as_yy = YLeaf(YType.uint32, "as-yy")

                            self.type = YLeaf(YType.enumeration, "type")

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
                                            "address_index",
                                            "as_index",
                                            "as_xx",
                                            "as_yy",
                                            "type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.address.is_set or
                                self.address_index.is_set or
                                self.as_index.is_set or
                                self.as_xx.is_set or
                                self.as_yy.is_set or
                                self.type.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.address.yfilter != YFilter.not_set or
                                self.address_index.yfilter != YFilter.not_set or
                                self.as_index.yfilter != YFilter.not_set or
                                self.as_xx.yfilter != YFilter.not_set or
                                self.as_yy.yfilter != YFilter.not_set or
                                self.type.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "site-of-origin" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.address.get_name_leafdata())
                            if (self.address_index.is_set or self.address_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.address_index.get_name_leafdata())
                            if (self.as_index.is_set or self.as_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.as_index.get_name_leafdata())
                            if (self.as_xx.is_set or self.as_xx.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.as_xx.get_name_leafdata())
                            if (self.as_yy.is_set or self.as_yy.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.as_yy.get_name_leafdata())
                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address" or name == "address-index" or name == "as-index" or name == "as-xx" or name == "as-yy" or name == "type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "address"):
                                self.address = value
                                self.address.value_namespace = name_space
                                self.address.value_namespace_prefix = name_space_prefix
                            if(value_path == "address-index"):
                                self.address_index = value
                                self.address_index.value_namespace = name_space
                                self.address_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "as-index"):
                                self.as_index = value
                                self.as_index.value_namespace = name_space
                                self.as_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "as-xx"):
                                self.as_xx = value
                                self.as_xx.value_namespace = name_space
                                self.as_xx.value_namespace_prefix = name_space_prefix
                            if(value_path == "as-yy"):
                                self.as_yy = value
                                self.as_yy.value_namespace = name_space
                                self.as_yy.value_namespace_prefix = name_space_prefix
                            if(value_path == "type"):
                                self.type = value
                                self.type.value_namespace = name_space
                                self.type.value_namespace_prefix = name_space_prefix


                    class ReceiveVersion(Entity):
                        """
                        RIP versions supported for receiving
                        advertisements
                        
                        .. attribute:: version1
                        
                        	Support RIP version 1
                        	**type**\:  bool
                        
                        .. attribute:: version2
                        
                        	Support RIP version 2
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion, self).__init__()

                            self.yang_name = "receive-version"
                            self.yang_parent_name = "interface"

                            self.version1 = YLeaf(YType.boolean, "version1")

                            self.version2 = YLeaf(YType.boolean, "version2")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("version1",
                                            "version2") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.version1.is_set or
                                self.version2.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.version1.yfilter != YFilter.not_set or
                                self.version2.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "receive-version" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.version1.is_set or self.version1.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.version1.get_name_leafdata())
                            if (self.version2.is_set or self.version2.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.version2.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "version1" or name == "version2"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "version1"):
                                self.version1 = value
                                self.version1.value_namespace = name_space
                                self.version1.value_namespace_prefix = name_space_prefix
                            if(value_path == "version2"):
                                self.version2 = value
                                self.version2.value_namespace = name_space
                                self.version2.value_namespace_prefix = name_space_prefix


                    class SendVersion(Entity):
                        """
                        RIP versions supported for sending
                        advertisements
                        
                        .. attribute:: version1
                        
                        	Support RIP version 1
                        	**type**\:  bool
                        
                        .. attribute:: version2
                        
                        	Support RIP version 2
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion, self).__init__()

                            self.yang_name = "send-version"
                            self.yang_parent_name = "interface"

                            self.version1 = YLeaf(YType.boolean, "version1")

                            self.version2 = YLeaf(YType.boolean, "version2")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("version1",
                                            "version2") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.version1.is_set or
                                self.version2.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.version1.yfilter != YFilter.not_set or
                                self.version2.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "send-version" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.version1.is_set or self.version1.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.version1.get_name_leafdata())
                            if (self.version2.is_set or self.version2.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.version2.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "version1" or name == "version2"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "version1"):
                                self.version1 = value
                                self.version1.value_namespace = name_space
                                self.version1.value_namespace_prefix = name_space_prefix
                            if(value_path == "version2"):
                                self.version2 = value
                                self.version2.value_namespace = name_space
                                self.version2.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.accept_metric_zero.is_set or
                            self.broadcast_for_v2.is_set or
                            self.enable.is_set or
                            self.passive.is_set or
                            self.poison_reverse.is_set or
                            self.policy_in.is_set or
                            self.policy_out.is_set or
                            self.split_horizon_disable.is_set or
                            (self.receive_version is not None and self.receive_version.has_data()) or
                            (self.send_version is not None and self.send_version.has_data()) or
                            (self.site_of_origin is not None and self.site_of_origin.has_data()) or
                            (self.authentication is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.accept_metric_zero.yfilter != YFilter.not_set or
                            self.broadcast_for_v2.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set or
                            self.passive.yfilter != YFilter.not_set or
                            self.poison_reverse.yfilter != YFilter.not_set or
                            self.policy_in.yfilter != YFilter.not_set or
                            self.policy_out.yfilter != YFilter.not_set or
                            self.split_horizon_disable.yfilter != YFilter.not_set or
                            (self.authentication is not None and self.authentication.has_operation()) or
                            (self.receive_version is not None and self.receive_version.has_operation()) or
                            (self.send_version is not None and self.send_version.has_operation()) or
                            (self.site_of_origin is not None and self.site_of_origin.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.accept_metric_zero.is_set or self.accept_metric_zero.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accept_metric_zero.get_name_leafdata())
                        if (self.broadcast_for_v2.is_set or self.broadcast_for_v2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.broadcast_for_v2.get_name_leafdata())
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())
                        if (self.passive.is_set or self.passive.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.passive.get_name_leafdata())
                        if (self.poison_reverse.is_set or self.poison_reverse.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.poison_reverse.get_name_leafdata())
                        if (self.policy_in.is_set or self.policy_in.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.policy_in.get_name_leafdata())
                        if (self.policy_out.is_set or self.policy_out.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.policy_out.get_name_leafdata())
                        if (self.split_horizon_disable.is_set or self.split_horizon_disable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.split_horizon_disable.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "authentication"):
                            if (self.authentication is None):
                                self.authentication = Rip.Vrfs.Vrf.Interfaces.Interface.Authentication()
                                self.authentication.parent = self
                                self._children_name_map["authentication"] = "authentication"
                            return self.authentication

                        if (child_yang_name == "receive-version"):
                            if (self.receive_version is None):
                                self.receive_version = Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion()
                                self.receive_version.parent = self
                                self._children_name_map["receive_version"] = "receive-version"
                            return self.receive_version

                        if (child_yang_name == "send-version"):
                            if (self.send_version is None):
                                self.send_version = Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion()
                                self.send_version.parent = self
                                self._children_name_map["send_version"] = "send-version"
                            return self.send_version

                        if (child_yang_name == "site-of-origin"):
                            if (self.site_of_origin is None):
                                self.site_of_origin = Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin()
                                self.site_of_origin.parent = self
                                self._children_name_map["site_of_origin"] = "site-of-origin"
                            return self.site_of_origin

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "authentication" or name == "receive-version" or name == "send-version" or name == "site-of-origin" or name == "interface-name" or name == "accept-metric-zero" or name == "broadcast-for-v2" or name == "enable" or name == "passive" or name == "poison-reverse" or name == "policy-in" or name == "policy-out" or name == "split-horizon-disable"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "accept-metric-zero"):
                            self.accept_metric_zero = value
                            self.accept_metric_zero.value_namespace = name_space
                            self.accept_metric_zero.value_namespace_prefix = name_space_prefix
                        if(value_path == "broadcast-for-v2"):
                            self.broadcast_for_v2 = value
                            self.broadcast_for_v2.value_namespace = name_space
                            self.broadcast_for_v2.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix
                        if(value_path == "passive"):
                            self.passive = value
                            self.passive.value_namespace = name_space
                            self.passive.value_namespace_prefix = name_space_prefix
                        if(value_path == "poison-reverse"):
                            self.poison_reverse = value
                            self.poison_reverse.value_namespace = name_space
                            self.poison_reverse.value_namespace_prefix = name_space_prefix
                        if(value_path == "policy-in"):
                            self.policy_in = value
                            self.policy_in.value_namespace = name_space
                            self.policy_in.value_namespace_prefix = name_space_prefix
                        if(value_path == "policy-out"):
                            self.policy_out = value
                            self.policy_out.value_namespace = name_space
                            self.policy_out.value_namespace_prefix = name_space_prefix
                        if(value_path == "split-horizon-disable"):
                            self.split_horizon_disable = value
                            self.split_horizon_disable.value_namespace = name_space
                            self.split_horizon_disable.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interfaces" + path_buffer

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

                    if (child_yang_name == "interface"):
                        for c in self.interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.Vrfs.Vrf.Interfaces.Interface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Neighbors(Entity):
                """
                Configure RIP Neighbors
                
                .. attribute:: neighbor
                
                	Neighbor address
                	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Neighbors.Neighbor>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Neighbors, self).__init__()

                    self.yang_name = "neighbors"
                    self.yang_parent_name = "vrf"

                    self.neighbor = YList(self)

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
                                super(Rip.Vrfs.Vrf.Neighbors, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Vrfs.Vrf.Neighbors, self).__setattr__(name, value)


                class Neighbor(Entity):
                    """
                    Neighbor address
                    
                    .. attribute:: neighbor_address  <key>
                    
                    	IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Neighbors.Neighbor, self).__init__()

                        self.yang_name = "neighbor"
                        self.yang_parent_name = "neighbors"

                        self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("neighbor_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.Vrfs.Vrf.Neighbors.Neighbor, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Vrfs.Vrf.Neighbors.Neighbor, self).__setattr__(name, value)

                    def has_data(self):
                        return self.neighbor_address.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.neighbor_address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "neighbor" + "[neighbor-address='" + self.neighbor_address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.neighbor_address.is_set or self.neighbor_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.neighbor_address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "neighbor-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "neighbor-address"):
                            self.neighbor_address = value
                            self.neighbor_address.value_namespace = name_space
                            self.neighbor_address.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.neighbor:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.neighbor:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "neighbors" + path_buffer

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

                    if (child_yang_name == "neighbor"):
                        for c in self.neighbor:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.Vrfs.Vrf.Neighbors.Neighbor()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.neighbor.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "neighbor"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Timers(Entity):
                """
                Various routing timers
                
                .. attribute:: flush_timer
                
                	Flush
                	**type**\:  int
                
                	**range:** 16..250000
                
                	**default value**\: 240
                
                .. attribute:: holddown_timer
                
                	Holddown
                	**type**\:  int
                
                	**range:** 15..200000
                
                	**default value**\: 180
                
                .. attribute:: invalid_timer
                
                	Invalid
                	**type**\:  int
                
                	**range:** 15..200000
                
                	**default value**\: 180
                
                .. attribute:: update_timer
                
                	Interval between updates
                	**type**\:  int
                
                	**range:** 5..50000
                
                	**default value**\: 30
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Timers, self).__init__()

                    self.yang_name = "timers"
                    self.yang_parent_name = "vrf"

                    self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                    self.holddown_timer = YLeaf(YType.uint32, "holddown-timer")

                    self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                    self.update_timer = YLeaf(YType.uint32, "update-timer")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("flush_timer",
                                    "holddown_timer",
                                    "invalid_timer",
                                    "update_timer") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.Vrfs.Vrf.Timers, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Vrfs.Vrf.Timers, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.flush_timer.is_set or
                        self.holddown_timer.is_set or
                        self.invalid_timer.is_set or
                        self.update_timer.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.flush_timer.yfilter != YFilter.not_set or
                        self.holddown_timer.yfilter != YFilter.not_set or
                        self.invalid_timer.yfilter != YFilter.not_set or
                        self.update_timer.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "timers" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.flush_timer.is_set or self.flush_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flush_timer.get_name_leafdata())
                    if (self.holddown_timer.is_set or self.holddown_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.holddown_timer.get_name_leafdata())
                    if (self.invalid_timer.is_set or self.invalid_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_timer.get_name_leafdata())
                    if (self.update_timer.is_set or self.update_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.update_timer.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "flush-timer" or name == "holddown-timer" or name == "invalid-timer" or name == "update-timer"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "flush-timer"):
                        self.flush_timer = value
                        self.flush_timer.value_namespace = name_space
                        self.flush_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "holddown-timer"):
                        self.holddown_timer = value
                        self.holddown_timer.value_namespace = name_space
                        self.holddown_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-timer"):
                        self.invalid_timer = value
                        self.invalid_timer.value_namespace = name_space
                        self.invalid_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "update-timer"):
                        self.update_timer = value
                        self.update_timer.value_namespace = name_space
                        self.update_timer.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    self.auto_summary.is_set or
                    self.broadcast_for_v2.is_set or
                    self.default_metric.is_set or
                    self.distance.is_set or
                    self.enable.is_set or
                    self.maximum_paths.is_set or
                    self.nsf.is_set or
                    self.output_delay.is_set or
                    self.policy_in.is_set or
                    self.policy_out.is_set or
                    self.validate_source_disable.is_set or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.ip_distances is not None and self.ip_distances.has_data()) or
                    (self.neighbors is not None and self.neighbors.has_data()) or
                    (self.redistribution is not None and self.redistribution.has_data()) or
                    (self.timers is not None and self.timers.has_data()) or
                    (self.default_information is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.auto_summary.yfilter != YFilter.not_set or
                    self.broadcast_for_v2.yfilter != YFilter.not_set or
                    self.default_metric.yfilter != YFilter.not_set or
                    self.distance.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    self.maximum_paths.yfilter != YFilter.not_set or
                    self.nsf.yfilter != YFilter.not_set or
                    self.output_delay.yfilter != YFilter.not_set or
                    self.policy_in.yfilter != YFilter.not_set or
                    self.policy_out.yfilter != YFilter.not_set or
                    self.validate_source_disable.yfilter != YFilter.not_set or
                    (self.default_information is not None and self.default_information.has_operation()) or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.ip_distances is not None and self.ip_distances.has_operation()) or
                    (self.neighbors is not None and self.neighbors.has_operation()) or
                    (self.redistribution is not None and self.redistribution.has_operation()) or
                    (self.timers is not None and self.timers.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.auto_summary.is_set or self.auto_summary.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.auto_summary.get_name_leafdata())
                if (self.broadcast_for_v2.is_set or self.broadcast_for_v2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.broadcast_for_v2.get_name_leafdata())
                if (self.default_metric.is_set or self.default_metric.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.default_metric.get_name_leafdata())
                if (self.distance.is_set or self.distance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.distance.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())
                if (self.maximum_paths.is_set or self.maximum_paths.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maximum_paths.get_name_leafdata())
                if (self.nsf.is_set or self.nsf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nsf.get_name_leafdata())
                if (self.output_delay.is_set or self.output_delay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.output_delay.get_name_leafdata())
                if (self.policy_in.is_set or self.policy_in.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.policy_in.get_name_leafdata())
                if (self.policy_out.is_set or self.policy_out.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.policy_out.get_name_leafdata())
                if (self.validate_source_disable.is_set or self.validate_source_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.validate_source_disable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "default-information"):
                    if (self.default_information is None):
                        self.default_information = Rip.Vrfs.Vrf.DefaultInformation()
                        self.default_information.parent = self
                        self._children_name_map["default_information"] = "default-information"
                    return self.default_information

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = Rip.Vrfs.Vrf.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "ip-distances"):
                    if (self.ip_distances is None):
                        self.ip_distances = Rip.Vrfs.Vrf.IpDistances()
                        self.ip_distances.parent = self
                        self._children_name_map["ip_distances"] = "ip-distances"
                    return self.ip_distances

                if (child_yang_name == "neighbors"):
                    if (self.neighbors is None):
                        self.neighbors = Rip.Vrfs.Vrf.Neighbors()
                        self.neighbors.parent = self
                        self._children_name_map["neighbors"] = "neighbors"
                    return self.neighbors

                if (child_yang_name == "redistribution"):
                    if (self.redistribution is None):
                        self.redistribution = Rip.Vrfs.Vrf.Redistribution()
                        self.redistribution.parent = self
                        self._children_name_map["redistribution"] = "redistribution"
                    return self.redistribution

                if (child_yang_name == "timers"):
                    if (self.timers is None):
                        self.timers = Rip.Vrfs.Vrf.Timers()
                        self.timers.parent = self
                        self._children_name_map["timers"] = "timers"
                    return self.timers

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "default-information" or name == "interfaces" or name == "ip-distances" or name == "neighbors" or name == "redistribution" or name == "timers" or name == "vrf-name" or name == "auto-summary" or name == "broadcast-for-v2" or name == "default-metric" or name == "distance" or name == "enable" or name == "maximum-paths" or name == "nsf" or name == "output-delay" or name == "policy-in" or name == "policy-out" or name == "validate-source-disable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "auto-summary"):
                    self.auto_summary = value
                    self.auto_summary.value_namespace = name_space
                    self.auto_summary.value_namespace_prefix = name_space_prefix
                if(value_path == "broadcast-for-v2"):
                    self.broadcast_for_v2 = value
                    self.broadcast_for_v2.value_namespace = name_space
                    self.broadcast_for_v2.value_namespace_prefix = name_space_prefix
                if(value_path == "default-metric"):
                    self.default_metric = value
                    self.default_metric.value_namespace = name_space
                    self.default_metric.value_namespace_prefix = name_space_prefix
                if(value_path == "distance"):
                    self.distance = value
                    self.distance.value_namespace = name_space
                    self.distance.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix
                if(value_path == "maximum-paths"):
                    self.maximum_paths = value
                    self.maximum_paths.value_namespace = name_space
                    self.maximum_paths.value_namespace_prefix = name_space_prefix
                if(value_path == "nsf"):
                    self.nsf = value
                    self.nsf.value_namespace = name_space
                    self.nsf.value_namespace_prefix = name_space_prefix
                if(value_path == "output-delay"):
                    self.output_delay = value
                    self.output_delay.value_namespace = name_space
                    self.output_delay.value_namespace_prefix = name_space_prefix
                if(value_path == "policy-in"):
                    self.policy_in = value
                    self.policy_in.value_namespace = name_space
                    self.policy_in.value_namespace_prefix = name_space_prefix
                if(value_path == "policy-out"):
                    self.policy_out = value
                    self.policy_out.value_namespace = name_space
                    self.policy_out.value_namespace_prefix = name_space_prefix
                if(value_path == "validate-source-disable"):
                    self.validate_source_disable = value
                    self.validate_source_disable.value_namespace = name_space
                    self.validate_source_disable.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip/%s" % self.get_segment_path()
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
                c = Rip.Vrfs.Vrf()
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
            (self.default_vrf is not None and self.default_vrf.has_data()) or
            (self.vrfs is not None and self.vrfs.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.default_vrf is not None and self.default_vrf.has_operation()) or
            (self.vrfs is not None and self.vrfs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-rip-cfg:rip" + path_buffer

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

        if (child_yang_name == "default-vrf"):
            if (self.default_vrf is None):
                self.default_vrf = Rip.DefaultVrf()
                self.default_vrf.parent = self
                self._children_name_map["default_vrf"] = "default-vrf"
            return self.default_vrf

        if (child_yang_name == "vrfs"):
            if (self.vrfs is None):
                self.vrfs = Rip.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
            return self.vrfs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "default-vrf" or name == "vrfs"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Rip()
        return self._top_entity


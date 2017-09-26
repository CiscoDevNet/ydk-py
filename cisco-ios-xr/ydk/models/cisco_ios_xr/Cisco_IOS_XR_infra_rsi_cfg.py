""" Cisco_IOS_XR_infra_rsi_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rsi package configuration.

This module contains definitions
for the following management objects\:
  vrfs\: VRF configuration
  global\-af\: global af
  srlg\: srlg
  vrf\-groups\: vrf groups
  selective\-vrf\-download\: selective vrf download

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
modules with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SrlgPriority(Enum):
    """
    SrlgPriority

    Srlg priority

    .. data:: critical = 0

    	Critical

    .. data:: high = 1

    	High

    .. data:: default = 2

    	Default

    .. data:: low = 3

    	Low

    .. data:: very_low = 4

    	Very low

    """

    critical = Enum.YLeaf(0, "critical")

    high = Enum.YLeaf(1, "high")

    default = Enum.YLeaf(2, "default")

    low = Enum.YLeaf(3, "low")

    very_low = Enum.YLeaf(4, "very-low")


class VrfAddressFamily(Enum):
    """
    VrfAddressFamily

    Vrf address family

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class VrfSubAddressFamily(Enum):
    """
    VrfSubAddressFamily

    Vrf sub address family

    .. data:: unicast = 1

    	Unicast

    .. data:: multicast = 2

    	Multicast

    .. data:: flow_spec = 133

    	Flow spec

    """

    unicast = Enum.YLeaf(1, "unicast")

    multicast = Enum.YLeaf(2, "multicast")

    flow_spec = Enum.YLeaf(133, "flow-spec")



class GlobalAf(Entity):
    """
    global af
    
    .. attribute:: afs
    
    	VRF address family configuration
    	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(GlobalAf, self).__init__()
        self._top_entity = None

        self.yang_name = "global-af"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"afs" : ("afs", GlobalAf.Afs)}
        self._child_list_classes = {}

        self.afs = GlobalAf.Afs()
        self.afs.parent = self
        self._children_name_map["afs"] = "afs"
        self._children_yang_names.add("afs")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:global-af"


    class Afs(Entity):
        """
        VRF address family configuration
        
        .. attribute:: af
        
        	VRF address family configuration
        	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(GlobalAf.Afs, self).__init__()

            self.yang_name = "afs"
            self.yang_parent_name = "global-af"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"af" : ("af", GlobalAf.Afs.Af)}

            self.af = YList(self)
            self._segment_path = lambda: "afs"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:global-af/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(GlobalAf.Afs, [], name, value)


        class Af(Entity):
            """
            VRF address family configuration
            
            .. attribute:: af_name  <key>
            
            	Address family
            	**type**\:   :py:class:`VrfAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfAddressFamily>`
            
            .. attribute:: saf_name  <key>
            
            	Sub\-Address family
            	**type**\:   :py:class:`VrfSubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfSubAddressFamily>`
            
            .. attribute:: topology_name  <key>
            
            	Topology name
            	**type**\:  str
            
            	**length:** 1..244
            
            .. attribute:: create
            
            	VRF configuration for a particular address family
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(GlobalAf.Afs.Af, self).__init__()

                self.yang_name = "af"
                self.yang_parent_name = "afs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.af_name = YLeaf(YType.enumeration, "af-name")

                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                self.topology_name = YLeaf(YType.str, "topology-name")

                self.create = YLeaf(YType.empty, "create")
                self._segment_path = lambda: "af" + "[af-name='" + self.af_name.get() + "']" + "[saf-name='" + self.saf_name.get() + "']" + "[topology-name='" + self.topology_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:global-af/afs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(GlobalAf.Afs.Af, ['af_name', 'saf_name', 'topology_name', 'create'], name, value)

    def clone_ptr(self):
        self._top_entity = GlobalAf()
        return self._top_entity

class SelectiveVrfDownload(Entity):
    """
    selective vrf download
    
    .. attribute:: disable
    
    	Disable selective VRF download
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(SelectiveVrfDownload, self).__init__()
        self._top_entity = None

        self.yang_name = "selective-vrf-download"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.disable = YLeaf(YType.empty, "disable")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:selective-vrf-download"

    def __setattr__(self, name, value):
        self._perform_setattr(SelectiveVrfDownload, ['disable'], name, value)

    def clone_ptr(self):
        self._top_entity = SelectiveVrfDownload()
        return self._top_entity

class Srlg(Entity):
    """
    srlg
    
    .. attribute:: enable
    
    	Enable SRLG
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: groups
    
    	Set of groups configured with SRLG
    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups>`
    
    .. attribute:: inherit_nodes
    
    	Set of inherit nodes configured with SRLG
    	**type**\:   :py:class:`InheritNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes>`
    
    .. attribute:: interfaces
    
    	Set of interfaces configured with SRLG
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces>`
    
    .. attribute:: srlg_names
    
    	Set of SRLG name configuration
    	**type**\:   :py:class:`SrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.SrlgNames>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Srlg, self).__init__()
        self._top_entity = None

        self.yang_name = "srlg"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"groups" : ("groups", Srlg.Groups), "inherit-nodes" : ("inherit_nodes", Srlg.InheritNodes), "interfaces" : ("interfaces", Srlg.Interfaces), "srlg-names" : ("srlg_names", Srlg.SrlgNames)}
        self._child_list_classes = {}

        self.enable = YLeaf(YType.empty, "enable")

        self.groups = Srlg.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"
        self._children_yang_names.add("groups")

        self.inherit_nodes = Srlg.InheritNodes()
        self.inherit_nodes.parent = self
        self._children_name_map["inherit_nodes"] = "inherit-nodes"
        self._children_yang_names.add("inherit-nodes")

        self.interfaces = Srlg.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.srlg_names = Srlg.SrlgNames()
        self.srlg_names.parent = self
        self._children_name_map["srlg_names"] = "srlg-names"
        self._children_yang_names.add("srlg-names")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg"

    def __setattr__(self, name, value):
        self._perform_setattr(Srlg, ['enable'], name, value)


    class Groups(Entity):
        """
        Set of groups configured with SRLG
        
        .. attribute:: group
        
        	Group configurations
        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups.Group>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Srlg.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"group" : ("group", Srlg.Groups.Group)}

            self.group = YList(self)
            self._segment_path = lambda: "groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.Groups, [], name, value)


        class Group(Entity):
            """
            Group configurations
            
            .. attribute:: group_name  <key>
            
            	Group name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: enable
            
            	Enable SRLG group
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: group_values
            
            	Set of SRLG values configured under a group
            	**type**\:   :py:class:`GroupValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups.Group.GroupValues>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Srlg.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"group-values" : ("group_values", Srlg.Groups.Group.GroupValues)}
                self._child_list_classes = {}

                self.group_name = YLeaf(YType.str, "group-name")

                self.enable = YLeaf(YType.empty, "enable")

                self.group_values = Srlg.Groups.Group.GroupValues()
                self.group_values.parent = self
                self._children_name_map["group_values"] = "group-values"
                self._children_yang_names.add("group-values")
                self._segment_path = lambda: "group" + "[group-name='" + self.group_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/groups/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.Groups.Group, ['group_name', 'enable'], name, value)


            class GroupValues(Entity):
                """
                Set of SRLG values configured under a group
                
                .. attribute:: group_value
                
                	Group SRLG values with attribute
                	**type**\: list of    :py:class:`GroupValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups.Group.GroupValues.GroupValue>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Groups.Group.GroupValues, self).__init__()

                    self.yang_name = "group-values"
                    self.yang_parent_name = "group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"group-value" : ("group_value", Srlg.Groups.Group.GroupValues.GroupValue)}

                    self.group_value = YList(self)
                    self._segment_path = lambda: "group-values"

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Groups.Group.GroupValues, [], name, value)


                class GroupValue(Entity):
                    """
                    Group SRLG values with attribute
                    
                    .. attribute:: srlg_index  <key>
                    
                    	SRLG index
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: srlg_priority
                    
                    	SRLG priority
                    	**type**\:   :py:class:`SrlgPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriority>`
                    
                    	**default value**\: default
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.Groups.Group.GroupValues.GroupValue, self).__init__()

                        self.yang_name = "group-value"
                        self.yang_parent_name = "group-values"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.srlg_index = YLeaf(YType.uint32, "srlg-index")

                        self.srlg_priority = YLeaf(YType.enumeration, "srlg-priority")

                        self.srlg_value = YLeaf(YType.uint32, "srlg-value")
                        self._segment_path = lambda: "group-value" + "[srlg-index='" + self.srlg_index.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Groups.Group.GroupValues.GroupValue, ['srlg_index', 'srlg_priority', 'srlg_value'], name, value)


    class InheritNodes(Entity):
        """
        Set of inherit nodes configured with SRLG
        
        .. attribute:: inherit_node
        
        	Inherit node configurations
        	**type**\: list of    :py:class:`InheritNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes.InheritNode>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Srlg.InheritNodes, self).__init__()

            self.yang_name = "inherit-nodes"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"inherit-node" : ("inherit_node", Srlg.InheritNodes.InheritNode)}

            self.inherit_node = YList(self)
            self._segment_path = lambda: "inherit-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.InheritNodes, [], name, value)


        class InheritNode(Entity):
            """
            Inherit node configurations
            
            .. attribute:: inherit_node_name  <key>
            
            	The inherit node name
            	**type**\:  str
            
            	**pattern:** ((([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))/){2}(([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))
            
            .. attribute:: enable
            
            	Enable SRLG inherit node
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: inherit_node_values
            
            	Set of SRLG values configured under an inherit node
            	**type**\:   :py:class:`InheritNodeValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes.InheritNode.InheritNodeValues>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Srlg.InheritNodes.InheritNode, self).__init__()

                self.yang_name = "inherit-node"
                self.yang_parent_name = "inherit-nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"inherit-node-values" : ("inherit_node_values", Srlg.InheritNodes.InheritNode.InheritNodeValues)}
                self._child_list_classes = {}

                self.inherit_node_name = YLeaf(YType.str, "inherit-node-name")

                self.enable = YLeaf(YType.empty, "enable")

                self.inherit_node_values = Srlg.InheritNodes.InheritNode.InheritNodeValues()
                self.inherit_node_values.parent = self
                self._children_name_map["inherit_node_values"] = "inherit-node-values"
                self._children_yang_names.add("inherit-node-values")
                self._segment_path = lambda: "inherit-node" + "[inherit-node-name='" + self.inherit_node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/inherit-nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.InheritNodes.InheritNode, ['inherit_node_name', 'enable'], name, value)


            class InheritNodeValues(Entity):
                """
                Set of SRLG values configured under an inherit
                node
                
                .. attribute:: inherit_node_value
                
                	Inherit node SRLG value with attributes
                	**type**\: list of    :py:class:`InheritNodeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.InheritNodes.InheritNode.InheritNodeValues, self).__init__()

                    self.yang_name = "inherit-node-values"
                    self.yang_parent_name = "inherit-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"inherit-node-value" : ("inherit_node_value", Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue)}

                    self.inherit_node_value = YList(self)
                    self._segment_path = lambda: "inherit-node-values"

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.InheritNodes.InheritNode.InheritNodeValues, [], name, value)


                class InheritNodeValue(Entity):
                    """
                    Inherit node SRLG value with attributes
                    
                    .. attribute:: srlg_index  <key>
                    
                    	SRLG index
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: srlg_priority
                    
                    	SRLG priority
                    	**type**\:   :py:class:`SrlgPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriority>`
                    
                    	**default value**\: default
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue, self).__init__()

                        self.yang_name = "inherit-node-value"
                        self.yang_parent_name = "inherit-node-values"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.srlg_index = YLeaf(YType.uint32, "srlg-index")

                        self.srlg_priority = YLeaf(YType.enumeration, "srlg-priority")

                        self.srlg_value = YLeaf(YType.uint32, "srlg-value")
                        self._segment_path = lambda: "inherit-node-value" + "[srlg-index='" + self.srlg_index.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue, ['srlg_index', 'srlg_priority', 'srlg_value'], name, value)


    class Interfaces(Entity):
        """
        Set of interfaces configured with SRLG
        
        .. attribute:: interface
        
        	Interface configurations
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Srlg.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", Srlg.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Interface configurations
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: enable
            
            	Enable SRLG interface
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: include_optical
            
            	Include optical configuration for an interface
            	**type**\:   :py:class:`IncludeOptical <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.IncludeOptical>`
            
            .. attribute:: interface_group
            
            	Group configuration for an interface
            	**type**\:   :py:class:`InterfaceGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceGroup>`
            
            .. attribute:: interface_srlg_names
            
            	SRLG Name configuration for an interface
            	**type**\:   :py:class:`InterfaceSrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceSrlgNames>`
            
            .. attribute:: values
            
            	SRLG Value configuration for an interface
            	**type**\:   :py:class:`Values <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.Values>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Srlg.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"include-optical" : ("include_optical", Srlg.Interfaces.Interface.IncludeOptical), "interface-group" : ("interface_group", Srlg.Interfaces.Interface.InterfaceGroup), "interface-srlg-names" : ("interface_srlg_names", Srlg.Interfaces.Interface.InterfaceSrlgNames), "values" : ("values", Srlg.Interfaces.Interface.Values)}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.enable = YLeaf(YType.empty, "enable")

                self.include_optical = Srlg.Interfaces.Interface.IncludeOptical()
                self.include_optical.parent = self
                self._children_name_map["include_optical"] = "include-optical"
                self._children_yang_names.add("include-optical")

                self.interface_group = Srlg.Interfaces.Interface.InterfaceGroup()
                self.interface_group.parent = self
                self._children_name_map["interface_group"] = "interface-group"
                self._children_yang_names.add("interface-group")

                self.interface_srlg_names = Srlg.Interfaces.Interface.InterfaceSrlgNames()
                self.interface_srlg_names.parent = self
                self._children_name_map["interface_srlg_names"] = "interface-srlg-names"
                self._children_yang_names.add("interface-srlg-names")

                self.values = Srlg.Interfaces.Interface.Values()
                self.values.parent = self
                self._children_name_map["values"] = "values"
                self._children_yang_names.add("values")
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.Interfaces.Interface, ['interface_name', 'enable'], name, value)


            class IncludeOptical(Entity):
                """
                Include optical configuration for an interface
                
                .. attribute:: enable
                
                	Enable SRLG interface include optical
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: priority
                
                	Priority for optical domain values
                	**type**\:   :py:class:`SrlgPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriority>`
                
                	**default value**\: default
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Interfaces.Interface.IncludeOptical, self).__init__()

                    self.yang_name = "include-optical"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.enable = YLeaf(YType.empty, "enable")

                    self.priority = YLeaf(YType.enumeration, "priority")
                    self._segment_path = lambda: "include-optical"

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Interfaces.Interface.IncludeOptical, ['enable', 'priority'], name, value)


            class InterfaceGroup(Entity):
                """
                Group configuration for an interface
                
                .. attribute:: enable
                
                	Enable SRLG interface group submode
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: group_names
                
                	Set of group name under an interface
                	**type**\:   :py:class:`GroupNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceGroup.GroupNames>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Interfaces.Interface.InterfaceGroup, self).__init__()

                    self.yang_name = "interface-group"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"group-names" : ("group_names", Srlg.Interfaces.Interface.InterfaceGroup.GroupNames)}
                    self._child_list_classes = {}

                    self.enable = YLeaf(YType.empty, "enable")

                    self.group_names = Srlg.Interfaces.Interface.InterfaceGroup.GroupNames()
                    self.group_names.parent = self
                    self._children_name_map["group_names"] = "group-names"
                    self._children_yang_names.add("group-names")
                    self._segment_path = lambda: "interface-group"

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Interfaces.Interface.InterfaceGroup, ['enable'], name, value)


                class GroupNames(Entity):
                    """
                    Set of group name under an interface
                    
                    .. attribute:: group_name
                    
                    	Group name included under interface
                    	**type**\: list of    :py:class:`GroupName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName>`
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.Interfaces.Interface.InterfaceGroup.GroupNames, self).__init__()

                        self.yang_name = "group-names"
                        self.yang_parent_name = "interface-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"group-name" : ("group_name", Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName)}

                        self.group_name = YList(self)
                        self._segment_path = lambda: "group-names"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Interfaces.Interface.InterfaceGroup.GroupNames, [], name, value)


                    class GroupName(Entity):
                        """
                        Group name included under interface
                        
                        .. attribute:: group_name_index  <key>
                        
                        	Group name index
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: group_name
                        
                        	Group name
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: srlg_priority
                        
                        	SRLG priority
                        	**type**\:   :py:class:`SrlgPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriority>`
                        
                        	**default value**\: default
                        
                        

                        """

                        _prefix = 'infra-rsi-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName, self).__init__()

                            self.yang_name = "group-name"
                            self.yang_parent_name = "group-names"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_name_index = YLeaf(YType.uint32, "group-name-index")

                            self.group_name = YLeaf(YType.str, "group-name")

                            self.srlg_priority = YLeaf(YType.enumeration, "srlg-priority")
                            self._segment_path = lambda: "group-name" + "[group-name-index='" + self.group_name_index.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName, ['group_name_index', 'group_name', 'srlg_priority'], name, value)


            class InterfaceSrlgNames(Entity):
                """
                SRLG Name configuration for an interface
                
                .. attribute:: interface_srlg_name
                
                	SRLG name data
                	**type**\: list of    :py:class:`InterfaceSrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Interfaces.Interface.InterfaceSrlgNames, self).__init__()

                    self.yang_name = "interface-srlg-names"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface-srlg-name" : ("interface_srlg_name", Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName)}

                    self.interface_srlg_name = YList(self)
                    self._segment_path = lambda: "interface-srlg-names"

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Interfaces.Interface.InterfaceSrlgNames, [], name, value)


                class InterfaceSrlgName(Entity):
                    """
                    SRLG name data
                    
                    .. attribute:: srlg_name  <key>
                    
                    	SRLG name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName, self).__init__()

                        self.yang_name = "interface-srlg-name"
                        self.yang_parent_name = "interface-srlg-names"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.srlg_name = YLeaf(YType.str, "srlg-name")
                        self._segment_path = lambda: "interface-srlg-name" + "[srlg-name='" + self.srlg_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName, ['srlg_name'], name, value)


            class Values(Entity):
                """
                SRLG Value configuration for an interface
                
                .. attribute:: value
                
                	SRLG value data
                	**type**\: list of    :py:class:`Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.Values.Value>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Interfaces.Interface.Values, self).__init__()

                    self.yang_name = "values"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"value" : ("value", Srlg.Interfaces.Interface.Values.Value)}

                    self.value = YList(self)
                    self._segment_path = lambda: "values"

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Interfaces.Interface.Values, [], name, value)


                class Value(Entity):
                    """
                    SRLG value data
                    
                    .. attribute:: srlg_index  <key>
                    
                    	SRLG index
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: srlg_priority
                    
                    	SRLG priority
                    	**type**\:   :py:class:`SrlgPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriority>`
                    
                    	**default value**\: default
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.Interfaces.Interface.Values.Value, self).__init__()

                        self.yang_name = "value"
                        self.yang_parent_name = "values"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.srlg_index = YLeaf(YType.uint32, "srlg-index")

                        self.srlg_priority = YLeaf(YType.enumeration, "srlg-priority")

                        self.srlg_value = YLeaf(YType.uint32, "srlg-value")
                        self._segment_path = lambda: "value" + "[srlg-index='" + self.srlg_index.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Interfaces.Interface.Values.Value, ['srlg_index', 'srlg_priority', 'srlg_value'], name, value)


    class SrlgNames(Entity):
        """
        Set of SRLG name configuration
        
        .. attribute:: srlg_name
        
        	SRLG name configuration
        	**type**\: list of    :py:class:`SrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.SrlgNames.SrlgName>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Srlg.SrlgNames, self).__init__()

            self.yang_name = "srlg-names"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"srlg-name" : ("srlg_name", Srlg.SrlgNames.SrlgName)}

            self.srlg_name = YList(self)
            self._segment_path = lambda: "srlg-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.SrlgNames, [], name, value)


        class SrlgName(Entity):
            """
            SRLG name configuration
            
            .. attribute:: srlg_name  <key>
            
            	SRLG name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: srlg_value
            
            	SRLG value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Srlg.SrlgNames.SrlgName, self).__init__()

                self.yang_name = "srlg-name"
                self.yang_parent_name = "srlg-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.srlg_name = YLeaf(YType.str, "srlg-name")

                self.srlg_value = YLeaf(YType.uint32, "srlg-value")
                self._segment_path = lambda: "srlg-name" + "[srlg-name='" + self.srlg_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/srlg-names/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.SrlgNames.SrlgName, ['srlg_name', 'srlg_value'], name, value)

    def clone_ptr(self):
        self._top_entity = Srlg()
        return self._top_entity

class VrfGroups(Entity):
    """
    vrf groups
    
    .. attribute:: vrf_group
    
    	VRF group configuration
    	**type**\: list of    :py:class:`VrfGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfGroups.VrfGroup>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(VrfGroups, self).__init__()
        self._top_entity = None

        self.yang_name = "vrf-groups"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"vrf-group" : ("vrf_group", VrfGroups.VrfGroup)}

        self.vrf_group = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:vrf-groups"

    def __setattr__(self, name, value):
        self._perform_setattr(VrfGroups, [], name, value)


    class VrfGroup(Entity):
        """
        VRF group configuration
        
        .. attribute:: vrf_group_name  <key>
        
        	VRF group name
        	**type**\:  str
        
        	**length:** 1..32
        
        .. attribute:: enable
        
        	Enable VRF group
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: vrfs
        
        	Set of VRFs configured under a VRF group
        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfGroups.VrfGroup.Vrfs>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(VrfGroups.VrfGroup, self).__init__()

            self.yang_name = "vrf-group"
            self.yang_parent_name = "vrf-groups"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"vrfs" : ("vrfs", VrfGroups.VrfGroup.Vrfs)}
            self._child_list_classes = {}

            self.vrf_group_name = YLeaf(YType.str, "vrf-group-name")

            self.enable = YLeaf(YType.empty, "enable")

            self.vrfs = VrfGroups.VrfGroup.Vrfs()
            self.vrfs.parent = self
            self._children_name_map["vrfs"] = "vrfs"
            self._children_yang_names.add("vrfs")
            self._segment_path = lambda: "vrf-group" + "[vrf-group-name='" + self.vrf_group_name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:vrf-groups/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(VrfGroups.VrfGroup, ['vrf_group_name', 'enable'], name, value)


        class Vrfs(Entity):
            """
            Set of VRFs configured under a VRF group
            
            .. attribute:: vrf
            
            	VRF configuration
            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfGroups.VrfGroup.Vrfs.Vrf>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(VrfGroups.VrfGroup.Vrfs, self).__init__()

                self.yang_name = "vrfs"
                self.yang_parent_name = "vrf-group"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"vrf" : ("vrf", VrfGroups.VrfGroup.Vrfs.Vrf)}

                self.vrf = YList(self)
                self._segment_path = lambda: "vrfs"

            def __setattr__(self, name, value):
                self._perform_setattr(VrfGroups.VrfGroup.Vrfs, [], name, value)


            class Vrf(Entity):
                """
                VRF configuration
                
                .. attribute:: vrf_name  <key>
                
                	VRF name
                	**type**\:  str
                
                	**length:** 1..32
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(VrfGroups.VrfGroup.Vrfs.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrfs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.vrf_name = YLeaf(YType.str, "vrf-name")
                    self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(VrfGroups.VrfGroup.Vrfs.Vrf, ['vrf_name'], name, value)

    def clone_ptr(self):
        self._top_entity = VrfGroups()
        return self._top_entity

class Vrfs(Entity):
    """
    VRF configuration
    
    .. attribute:: vrf
    
    	VRF configuration
    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Vrfs, self).__init__()
        self._top_entity = None

        self.yang_name = "vrfs"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"vrf" : ("vrf", Vrfs.Vrf)}

        self.vrf = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:vrfs"

    def __setattr__(self, name, value):
        self._perform_setattr(Vrfs, [], name, value)


    class Vrf(Entity):
        """
        VRF configuration
        
        .. attribute:: vrf_name  <key>
        
        	VRF name
        	**type**\:  str
        
        	**length:** 1..32
        
        .. attribute:: afs
        
        	VRF address family configuration
        	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs>`
        
        .. attribute:: create
        
        	VRF global configuration
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: description
        
        	A textual description of the VRF
        	**type**\:  str
        
        	**length:** 1..244
        
        .. attribute:: fallback_vrf
        
        	Fallback VRF
        	**type**\:  str
        
        	**length:** 1..32
        
        .. attribute:: mode_big
        
        	Configuration enable of big VRF
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: multicast_host
        
        	Multicast host stack configuration
        	**type**\:   :py:class:`MulticastHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.MulticastHost>`
        
        .. attribute:: remote_route_filter_disable
        
        	For disabling remote route filtering for this VRF on core\-facing card
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: vpn_id
        
        	VPN\-ID for the VRF
        	**type**\:   :py:class:`VpnId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.VpnId>`
        
        	**presence node**\: True
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Vrfs.Vrf, self).__init__()

            self.yang_name = "vrf"
            self.yang_parent_name = "vrfs"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"afs" : ("afs", Vrfs.Vrf.Afs), "multicast-host" : ("multicast_host", Vrfs.Vrf.MulticastHost), "vpn-id" : ("vpn_id", Vrfs.Vrf.VpnId)}
            self._child_list_classes = {}

            self.vrf_name = YLeaf(YType.str, "vrf-name")

            self.create = YLeaf(YType.empty, "create")

            self.description = YLeaf(YType.str, "description")

            self.fallback_vrf = YLeaf(YType.str, "fallback-vrf")

            self.mode_big = YLeaf(YType.empty, "mode-big")

            self.remote_route_filter_disable = YLeaf(YType.empty, "remote-route-filter-disable")

            self.afs = Vrfs.Vrf.Afs()
            self.afs.parent = self
            self._children_name_map["afs"] = "afs"
            self._children_yang_names.add("afs")

            self.multicast_host = Vrfs.Vrf.MulticastHost()
            self.multicast_host.parent = self
            self._children_name_map["multicast_host"] = "multicast-host"
            self._children_yang_names.add("multicast-host")

            self.vpn_id = None
            self._children_name_map["vpn_id"] = "vpn-id"
            self._children_yang_names.add("vpn-id")
            self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:vrfs/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Vrfs.Vrf, ['vrf_name', 'create', 'description', 'fallback_vrf', 'mode_big', 'remote_route_filter_disable'], name, value)


        class Afs(Entity):
            """
            VRF address family configuration
            
            .. attribute:: af
            
            	VRF address family configuration
            	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Vrfs.Vrf.Afs, self).__init__()

                self.yang_name = "afs"
                self.yang_parent_name = "vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"af" : ("af", Vrfs.Vrf.Afs.Af)}

                self.af = YList(self)
                self._segment_path = lambda: "afs"

            def __setattr__(self, name, value):
                self._perform_setattr(Vrfs.Vrf.Afs, [], name, value)


            class Af(Entity):
                """
                VRF address family configuration
                
                .. attribute:: af_name  <key>
                
                	Address family
                	**type**\:   :py:class:`VrfAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfAddressFamily>`
                
                .. attribute:: saf_name  <key>
                
                	Sub\-Address family
                	**type**\:   :py:class:`VrfSubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfSubAddressFamily>`
                
                .. attribute:: topology_name  <key>
                
                	Topology name
                	**type**\:  str
                
                	**length:** 1..244
                
                .. attribute:: bgp
                
                	BGP AF VRF config
                	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp>`
                
                .. attribute:: create
                
                	VRF configuration for a particular address family
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: maximum_prefix
                
                	Set maximum prefix limits
                	**type**\:   :py:class:`MaximumPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.MaximumPrefix>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Vrfs.Vrf.Afs.Af, self).__init__()

                    self.yang_name = "af"
                    self.yang_parent_name = "afs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"bgp" : ("bgp", Vrfs.Vrf.Afs.Af.Bgp), "maximum-prefix" : ("maximum_prefix", Vrfs.Vrf.Afs.Af.MaximumPrefix)}
                    self._child_list_classes = {}

                    self.af_name = YLeaf(YType.enumeration, "af-name")

                    self.saf_name = YLeaf(YType.enumeration, "saf-name")

                    self.topology_name = YLeaf(YType.str, "topology-name")

                    self.create = YLeaf(YType.empty, "create")

                    self.bgp = Vrfs.Vrf.Afs.Af.Bgp()
                    self.bgp.parent = self
                    self._children_name_map["bgp"] = "bgp"
                    self._children_yang_names.add("bgp")

                    self.maximum_prefix = None
                    self._children_name_map["maximum_prefix"] = "maximum-prefix"
                    self._children_yang_names.add("maximum-prefix")
                    self._segment_path = lambda: "af" + "[af-name='" + self.af_name.get() + "']" + "[saf-name='" + self.saf_name.get() + "']" + "[topology-name='" + self.topology_name.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrfs.Vrf.Afs.Af, ['af_name', 'saf_name', 'topology_name', 'create'], name, value)


                class Bgp(Entity):
                    """
                    BGP AF VRF config
                    
                    .. attribute:: export_route_policy
                    
                    	Route policy for export filtering
                    	**type**\:  str
                    
                    .. attribute:: export_route_targets
                    
                    	Export Route targets
                    	**type**\:   :py:class:`ExportRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets>`
                    
                    .. attribute:: export_vrf_options
                    
                    	Export VRF options
                    	**type**\:   :py:class:`ExportVrfOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions>`
                    
                    .. attribute:: global_to_vrf_import_route_policy
                    
                    	Route policy for global to vrf import filtering
                    	**type**\:   :py:class:`GlobalToVrfImportRoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: import_route_policy
                    
                    	Route policy for import filtering
                    	**type**\:  str
                    
                    .. attribute:: import_route_targets
                    
                    	Import Route targets
                    	**type**\:   :py:class:`ImportRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets>`
                    
                    .. attribute:: import_vrf_options
                    
                    	TRUE Enable advertising imported paths to PEsFALSE Disable advertising imported paths to PEs
                    	**type**\:  bool
                    
                    .. attribute:: vrf_to_global_export_route_policy
                    
                    	Route policy for vrf to global export filtering
                    	**type**\:   :py:class:`VrfToGlobalExportRoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ipv4-bgp-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Vrfs.Vrf.Afs.Af.Bgp, self).__init__()

                        self.yang_name = "bgp"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"export-route-targets" : ("export_route_targets", Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets), "export-vrf-options" : ("export_vrf_options", Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions), "global-to-vrf-import-route-policy" : ("global_to_vrf_import_route_policy", Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy), "import-route-targets" : ("import_route_targets", Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets), "vrf-to-global-export-route-policy" : ("vrf_to_global_export_route_policy", Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy)}
                        self._child_list_classes = {}

                        self.export_route_policy = YLeaf(YType.str, "export-route-policy")

                        self.import_route_policy = YLeaf(YType.str, "import-route-policy")

                        self.import_vrf_options = YLeaf(YType.boolean, "import-vrf-options")

                        self.export_route_targets = Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets()
                        self.export_route_targets.parent = self
                        self._children_name_map["export_route_targets"] = "export-route-targets"
                        self._children_yang_names.add("export-route-targets")

                        self.export_vrf_options = Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions()
                        self.export_vrf_options.parent = self
                        self._children_name_map["export_vrf_options"] = "export-vrf-options"
                        self._children_yang_names.add("export-vrf-options")

                        self.global_to_vrf_import_route_policy = None
                        self._children_name_map["global_to_vrf_import_route_policy"] = "global-to-vrf-import-route-policy"
                        self._children_yang_names.add("global-to-vrf-import-route-policy")

                        self.import_route_targets = Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets()
                        self.import_route_targets.parent = self
                        self._children_name_map["import_route_targets"] = "import-route-targets"
                        self._children_yang_names.add("import-route-targets")

                        self.vrf_to_global_export_route_policy = None
                        self._children_name_map["vrf_to_global_export_route_policy"] = "vrf-to-global-export-route-policy"
                        self._children_yang_names.add("vrf-to-global-export-route-policy")
                        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-bgp-cfg:bgp"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp, ['export_route_policy', 'import_route_policy', 'import_vrf_options'], name, value)


                    class ExportRouteTargets(Entity):
                        """
                        Export Route targets
                        
                        .. attribute:: route_targets
                        
                        	Route target table
                        	**type**\:   :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets>`
                        
                        

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets, self).__init__()

                            self.yang_name = "export-route-targets"
                            self.yang_parent_name = "bgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"route-targets" : ("route_targets", Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets)}
                            self._child_list_classes = {}

                            self.route_targets = Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets()
                            self.route_targets.parent = self
                            self._children_name_map["route_targets"] = "route-targets"
                            self._children_yang_names.add("route-targets")
                            self._segment_path = lambda: "export-route-targets"


                        class RouteTargets(Entity):
                            """
                            Route target table
                            
                            .. attribute:: route_target
                            
                            	Route target
                            	**type**\: list of    :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets, self).__init__()

                                self.yang_name = "route-targets"
                                self.yang_parent_name = "export-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"route-target" : ("route_target", Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget)}

                                self.route_target = YList(self)
                                self._segment_path = lambda: "route-targets"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets, [], name, value)


                            class RouteTarget(Entity):
                                """
                                Route target
                                
                                .. attribute:: type  <key>
                                
                                	Type of RT
                                	**type**\:   :py:class:`BgpVrfRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg.BgpVrfRouteTarget>`
                                
                                .. attribute:: as_or_four_byte_as
                                
                                	as or four byte as
                                	**type**\: list of    :py:class:`AsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs>`
                                
                                .. attribute:: ipv4_address
                                
                                	ipv4 address
                                	**type**\: list of    :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget, self).__init__()

                                    self.yang_name = "route-target"
                                    self.yang_parent_name = "route-targets"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"as-or-four-byte-as" : ("as_or_four_byte_as", Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs), "ipv4-address" : ("ipv4_address", Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address)}

                                    self.type = YLeaf(YType.enumeration, "type")

                                    self.as_or_four_byte_as = YList(self)
                                    self.ipv4_address = YList(self)
                                    self._segment_path = lambda: "route-target" + "[type='" + self.type.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget, ['type'], name, value)


                                class AsOrFourByteAs(Entity):
                                    """
                                    as or four byte as
                                    
                                    .. attribute:: as_xx  <key>
                                    
                                    	AS number
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: as_  <key>
                                    
                                    	AS number
                                    	**type**\:  int
                                    
                                    	**range:** 1..4294967295
                                    
                                    .. attribute:: as_index  <key>
                                    
                                    	AS number Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: stitching_rt  <key>
                                    
                                    	Stitching RT
                                    	**type**\:  int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, self).__init__()

                                        self.yang_name = "as-or-four-byte-as"
                                        self.yang_parent_name = "route-target"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.as_xx = YLeaf(YType.uint32, "as-xx")

                                        self.as_ = YLeaf(YType.uint32, "as")

                                        self.as_index = YLeaf(YType.uint32, "as-index")

                                        self.stitching_rt = YLeaf(YType.uint32, "stitching-rt")
                                        self._segment_path = lambda: "as-or-four-byte-as" + "[as-xx='" + self.as_xx.get() + "']" + "[as='" + self.as_.get() + "']" + "[as-index='" + self.as_index.get() + "']" + "[stitching-rt='" + self.stitching_rt.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, ['as_xx', 'as_', 'as_index', 'stitching_rt'], name, value)


                                class Ipv4Address(Entity):
                                    """
                                    ipv4 address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	IP address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_index  <key>
                                    
                                    	IP address Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: stitching_rt  <key>
                                    
                                    	Stitching RT
                                    	**type**\:  int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, self).__init__()

                                        self.yang_name = "ipv4-address"
                                        self.yang_parent_name = "route-target"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.address = YLeaf(YType.str, "address")

                                        self.address_index = YLeaf(YType.uint32, "address-index")

                                        self.stitching_rt = YLeaf(YType.uint32, "stitching-rt")
                                        self._segment_path = lambda: "ipv4-address" + "[address='" + self.address.get() + "']" + "[address-index='" + self.address_index.get() + "']" + "[stitching-rt='" + self.stitching_rt.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, ['address', 'address_index', 'stitching_rt'], name, value)


                    class ExportVrfOptions(Entity):
                        """
                        Export VRF options
                        
                        .. attribute:: allow_imported_vpn
                        
                        	TRUE Enable imported VPN paths to be exported to non\-default VRFFALSE Disable imported VPN paths to be exported to non\-default VRF
                        	**type**\:  bool
                        
                        .. attribute:: import_stitching_rt
                        
                        	TRUE Use stitchng RTs to import extranet pathsFALSE Use regular RTs to import extranet paths
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions, self).__init__()

                            self.yang_name = "export-vrf-options"
                            self.yang_parent_name = "bgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.allow_imported_vpn = YLeaf(YType.boolean, "allow-imported-vpn")

                            self.import_stitching_rt = YLeaf(YType.boolean, "import-stitching-rt")
                            self._segment_path = lambda: "export-vrf-options"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions, ['allow_imported_vpn', 'import_stitching_rt'], name, value)


                    class GlobalToVrfImportRoutePolicy(Entity):
                        """
                        Route policy for global to vrf import filtering
                        
                        .. attribute:: advertise_as_vpn
                        
                        	TRUE Enable advertising imported paths to PEsFALSE Disable advertising imported paths to PEs
                        	**type**\:  bool
                        
                        .. attribute:: route_policy_name
                        
                        	Global to vrf import route policy
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy, self).__init__()

                            self.yang_name = "global-to-vrf-import-route-policy"
                            self.yang_parent_name = "bgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.advertise_as_vpn = YLeaf(YType.boolean, "advertise-as-vpn")

                            self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                            self._segment_path = lambda: "global-to-vrf-import-route-policy"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy, ['advertise_as_vpn', 'route_policy_name'], name, value)


                    class ImportRouteTargets(Entity):
                        """
                        Import Route targets
                        
                        .. attribute:: route_targets
                        
                        	Route target table
                        	**type**\:   :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets>`
                        
                        

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets, self).__init__()

                            self.yang_name = "import-route-targets"
                            self.yang_parent_name = "bgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"route-targets" : ("route_targets", Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets)}
                            self._child_list_classes = {}

                            self.route_targets = Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets()
                            self.route_targets.parent = self
                            self._children_name_map["route_targets"] = "route-targets"
                            self._children_yang_names.add("route-targets")
                            self._segment_path = lambda: "import-route-targets"


                        class RouteTargets(Entity):
                            """
                            Route target table
                            
                            .. attribute:: route_target
                            
                            	Route target
                            	**type**\: list of    :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets, self).__init__()

                                self.yang_name = "route-targets"
                                self.yang_parent_name = "import-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"route-target" : ("route_target", Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget)}

                                self.route_target = YList(self)
                                self._segment_path = lambda: "route-targets"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets, [], name, value)


                            class RouteTarget(Entity):
                                """
                                Route target
                                
                                .. attribute:: type  <key>
                                
                                	Type of RT
                                	**type**\:   :py:class:`BgpVrfRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg.BgpVrfRouteTarget>`
                                
                                .. attribute:: as_or_four_byte_as
                                
                                	as or four byte as
                                	**type**\: list of    :py:class:`AsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs>`
                                
                                .. attribute:: ipv4_address
                                
                                	ipv4 address
                                	**type**\: list of    :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget, self).__init__()

                                    self.yang_name = "route-target"
                                    self.yang_parent_name = "route-targets"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"as-or-four-byte-as" : ("as_or_four_byte_as", Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs), "ipv4-address" : ("ipv4_address", Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address)}

                                    self.type = YLeaf(YType.enumeration, "type")

                                    self.as_or_four_byte_as = YList(self)
                                    self.ipv4_address = YList(self)
                                    self._segment_path = lambda: "route-target" + "[type='" + self.type.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget, ['type'], name, value)


                                class AsOrFourByteAs(Entity):
                                    """
                                    as or four byte as
                                    
                                    .. attribute:: as_xx  <key>
                                    
                                    	AS number
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: as_  <key>
                                    
                                    	AS number
                                    	**type**\:  int
                                    
                                    	**range:** 1..4294967295
                                    
                                    .. attribute:: as_index  <key>
                                    
                                    	AS number Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: stitching_rt  <key>
                                    
                                    	Stitching RT
                                    	**type**\:  int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, self).__init__()

                                        self.yang_name = "as-or-four-byte-as"
                                        self.yang_parent_name = "route-target"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.as_xx = YLeaf(YType.uint32, "as-xx")

                                        self.as_ = YLeaf(YType.uint32, "as")

                                        self.as_index = YLeaf(YType.uint32, "as-index")

                                        self.stitching_rt = YLeaf(YType.uint32, "stitching-rt")
                                        self._segment_path = lambda: "as-or-four-byte-as" + "[as-xx='" + self.as_xx.get() + "']" + "[as='" + self.as_.get() + "']" + "[as-index='" + self.as_index.get() + "']" + "[stitching-rt='" + self.stitching_rt.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, ['as_xx', 'as_', 'as_index', 'stitching_rt'], name, value)


                                class Ipv4Address(Entity):
                                    """
                                    ipv4 address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	IP address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_index  <key>
                                    
                                    	IP address Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: stitching_rt  <key>
                                    
                                    	Stitching RT
                                    	**type**\:  int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, self).__init__()

                                        self.yang_name = "ipv4-address"
                                        self.yang_parent_name = "route-target"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.address = YLeaf(YType.str, "address")

                                        self.address_index = YLeaf(YType.uint32, "address-index")

                                        self.stitching_rt = YLeaf(YType.uint32, "stitching-rt")
                                        self._segment_path = lambda: "ipv4-address" + "[address='" + self.address.get() + "']" + "[address-index='" + self.address_index.get() + "']" + "[stitching-rt='" + self.stitching_rt.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, ['address', 'address_index', 'stitching_rt'], name, value)


                    class VrfToGlobalExportRoutePolicy(Entity):
                        """
                        Route policy for vrf to global export filtering
                        
                        .. attribute:: allow_imported_vpn
                        
                        	TRUE Enable imported VPN paths to be exported to Default VRF.FALSE Disable imported VPN paths to be exported to Default VRF
                        	**type**\:  bool
                        
                        .. attribute:: route_policy_name
                        
                        	Vrf to global export route policy
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy, self).__init__()

                            self.yang_name = "vrf-to-global-export-route-policy"
                            self.yang_parent_name = "bgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.allow_imported_vpn = YLeaf(YType.boolean, "allow-imported-vpn")

                            self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                            self._segment_path = lambda: "vrf-to-global-export-route-policy"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy, ['allow_imported_vpn', 'route_policy_name'], name, value)


                class MaximumPrefix(Entity):
                    """
                    Set maximum prefix limits
                    
                    .. attribute:: mid_threshold
                    
                    	Mid\-threshold (% of maximum)
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    .. attribute:: prefix_limit
                    
                    	Set table's maximum prefix limit
                    	**type**\:  int
                    
                    	**range:** 32..5000000
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-rib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vrfs.Vrf.Afs.Af.MaximumPrefix, self).__init__()

                        self.yang_name = "maximum-prefix"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.mid_threshold = YLeaf(YType.uint32, "mid-threshold")

                        self.prefix_limit = YLeaf(YType.uint32, "prefix-limit")
                        self._segment_path = lambda: "Cisco-IOS-XR-ip-rib-cfg:maximum-prefix"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrfs.Vrf.Afs.Af.MaximumPrefix, ['mid_threshold', 'prefix_limit'], name, value)


        class MulticastHost(Entity):
            """
            Multicast host stack configuration
            
            .. attribute:: ipv4
            
            	IPv4 configuration
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.MulticastHost.Ipv4>`
            
            .. attribute:: ipv6
            
            	IPv6 configuration
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.MulticastHost.Ipv6>`
            
            

            """

            _prefix = 'ip-iarm-vrf-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vrfs.Vrf.MulticastHost, self).__init__()

                self.yang_name = "multicast-host"
                self.yang_parent_name = "vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"ipv4" : ("ipv4", Vrfs.Vrf.MulticastHost.Ipv4), "ipv6" : ("ipv6", Vrfs.Vrf.MulticastHost.Ipv6)}
                self._child_list_classes = {}

                self.ipv4 = Vrfs.Vrf.MulticastHost.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._children_yang_names.add("ipv4")

                self.ipv6 = Vrfs.Vrf.MulticastHost.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._children_yang_names.add("ipv6")
                self._segment_path = lambda: "Cisco-IOS-XR-ip-iarm-vrf-cfg:multicast-host"


            class Ipv4(Entity):
                """
                IPv4 configuration
                
                .. attribute:: interface
                
                	Default multicast host interface name
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                

                """

                _prefix = 'ip-iarm-vrf-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vrfs.Vrf.MulticastHost.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "multicast-host"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface = YLeaf(YType.str, "interface")
                    self._segment_path = lambda: "ipv4"

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrfs.Vrf.MulticastHost.Ipv4, ['interface'], name, value)


            class Ipv6(Entity):
                """
                IPv6 configuration
                
                .. attribute:: interface
                
                	Default multicast host interface name
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                

                """

                _prefix = 'ip-iarm-vrf-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vrfs.Vrf.MulticastHost.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "multicast-host"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface = YLeaf(YType.str, "interface")
                    self._segment_path = lambda: "ipv6"

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrfs.Vrf.MulticastHost.Ipv6, ['interface'], name, value)


        class VpnId(Entity):
            """
            VPN\-ID for the VRF
            
            .. attribute:: vpn_index
            
            	Index of VPNID Index
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            .. attribute:: vpn_oui
            
            	OUI of VPNID OUI
            	**type**\:  int
            
            	**range:** 0..16777215
            
            	**mandatory**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Vrfs.Vrf.VpnId, self).__init__()

                self.yang_name = "vpn-id"
                self.yang_parent_name = "vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}
                self.is_presence_container = True

                self.vpn_index = YLeaf(YType.uint32, "vpn-index")

                self.vpn_oui = YLeaf(YType.uint32, "vpn-oui")
                self._segment_path = lambda: "vpn-id"

            def __setattr__(self, name, value):
                self._perform_setattr(Vrfs.Vrf.VpnId, ['vpn_index', 'vpn_oui'], name, value)

    def clone_ptr(self):
        self._top_entity = Vrfs()
        return self._top_entity


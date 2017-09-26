""" Cisco_IOS_XR_infra_rsi_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rsi package operational data.

This module contains definitions
for the following management objects\:
  vrf\-group\: VRF group operational data
  srlg\: srlg
  selective\-vrf\-download\: selective vrf download

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Priority(Enum):
    """
    Priority

    Priority

    .. data:: critical = 0

    	Critical

    .. data:: high = 1

    	High

    .. data:: medium = 2

    	Medium

    .. data:: low = 3

    	Low

    .. data:: very_low = 4

    	Very low

    """

    critical = Enum.YLeaf(0, "critical")

    high = Enum.YLeaf(1, "high")

    medium = Enum.YLeaf(2, "medium")

    low = Enum.YLeaf(3, "low")

    very_low = Enum.YLeaf(4, "very-low")


class Source(Enum):
    """
    Source

    Source

    .. data:: configured = 1

    	Configured

    .. data:: from_group = 2

    	From group

    .. data:: inherited = 4

    	Inherited

    .. data:: from_optical = 8

    	From optical

    .. data:: configured_and_notified = 17

    	Configured and notified

    .. data:: from_group_and_notified = 18

    	From group and notified

    .. data:: inherited_and_notified = 20

    	Inherited and notified

    .. data:: from_optical_and_notified = 24

    	From optical and notified

    """

    configured = Enum.YLeaf(1, "configured")

    from_group = Enum.YLeaf(2, "from-group")

    inherited = Enum.YLeaf(4, "inherited")

    from_optical = Enum.YLeaf(8, "from-optical")

    configured_and_notified = Enum.YLeaf(17, "configured-and-notified")

    from_group_and_notified = Enum.YLeaf(18, "from-group-and-notified")

    inherited_and_notified = Enum.YLeaf(20, "inherited-and-notified")

    from_optical_and_notified = Enum.YLeaf(24, "from-optical-and-notified")



class SelectiveVrfDownload(Entity):
    """
    selective vrf download
    
    .. attribute:: state
    
    	Selective VRF Download feature state details
    	**type**\:   :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.SelectiveVrfDownload.State>`
    
    

    """

    _prefix = 'infra-rsi-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(SelectiveVrfDownload, self).__init__()
        self._top_entity = None

        self.yang_name = "selective-vrf-download"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"state" : ("state", SelectiveVrfDownload.State)}
        self._child_list_classes = {}

        self.state = SelectiveVrfDownload.State()
        self.state.parent = self
        self._children_name_map["state"] = "state"
        self._children_yang_names.add("state")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:selective-vrf-download"


    class State(Entity):
        """
        Selective VRF Download feature state details
        
        .. attribute:: is_svd_enabled
        
        	Is SVD Enabled Operational
        	**type**\:  bool
        
        .. attribute:: is_svd_enabled_cfg
        
        	Is SVD Enabled Config
        	**type**\:  bool
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(SelectiveVrfDownload.State, self).__init__()

            self.yang_name = "state"
            self.yang_parent_name = "selective-vrf-download"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.is_svd_enabled = YLeaf(YType.boolean, "is-svd-enabled")

            self.is_svd_enabled_cfg = YLeaf(YType.boolean, "is-svd-enabled-cfg")
            self._segment_path = lambda: "state"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:selective-vrf-download/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SelectiveVrfDownload.State, ['is_svd_enabled', 'is_svd_enabled_cfg'], name, value)

    def clone_ptr(self):
        self._top_entity = SelectiveVrfDownload()
        return self._top_entity

class Srlg(Entity):
    """
    srlg
    
    .. attribute:: interface_srlg_names
    
    	Set of SRLG names configured
    	**type**\:   :py:class:`InterfaceSrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceSrlgNames>`
    
    .. attribute:: nodes
    
    	RSI SRLG operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes>`
    
    .. attribute:: srlg_maps
    
    	Set of SRLG name, value maps configured
    	**type**\:   :py:class:`SrlgMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.SrlgMaps>`
    
    

    """

    _prefix = 'infra-rsi-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Srlg, self).__init__()
        self._top_entity = None

        self.yang_name = "srlg"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"interface-srlg-names" : ("interface_srlg_names", Srlg.InterfaceSrlgNames), "nodes" : ("nodes", Srlg.Nodes), "srlg-maps" : ("srlg_maps", Srlg.SrlgMaps)}
        self._child_list_classes = {}

        self.interface_srlg_names = Srlg.InterfaceSrlgNames()
        self.interface_srlg_names.parent = self
        self._children_name_map["interface_srlg_names"] = "interface-srlg-names"
        self._children_yang_names.add("interface-srlg-names")

        self.nodes = Srlg.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")

        self.srlg_maps = Srlg.SrlgMaps()
        self.srlg_maps.parent = self
        self._children_name_map["srlg_maps"] = "srlg-maps"
        self._children_yang_names.add("srlg-maps")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg"


    class InterfaceSrlgNames(Entity):
        """
        Set of SRLG names configured
        
        .. attribute:: interface_srlg_name
        
        	Configured SRLG name details 
        	**type**\: list of    :py:class:`InterfaceSrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceSrlgNames.InterfaceSrlgName>`
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Srlg.InterfaceSrlgNames, self).__init__()

            self.yang_name = "interface-srlg-names"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface-srlg-name" : ("interface_srlg_name", Srlg.InterfaceSrlgNames.InterfaceSrlgName)}

            self.interface_srlg_name = YList(self)
            self._segment_path = lambda: "interface-srlg-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.InterfaceSrlgNames, [], name, value)


        class InterfaceSrlgName(Entity):
            """
            Configured SRLG name details 
            
            .. attribute:: srlg_name  <key>
            
            	SRLG name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: interfaces
            
            	Interfaces information
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces>`
            
            .. attribute:: srlg_name_xr
            
            	SRLG name
            	**type**\:  str
            
            .. attribute:: srlg_value
            
            	SRLG value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Srlg.InterfaceSrlgNames.InterfaceSrlgName, self).__init__()

                self.yang_name = "interface-srlg-name"
                self.yang_parent_name = "interface-srlg-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"interfaces" : ("interfaces", Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces)}
                self._child_list_classes = {}

                self.srlg_name = YLeaf(YType.str, "srlg-name")

                self.srlg_name_xr = YLeaf(YType.str, "srlg-name-xr")

                self.srlg_value = YLeaf(YType.uint32, "srlg-value")

                self.interfaces = Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")
                self._segment_path = lambda: "interface-srlg-name" + "[srlg-name='" + self.srlg_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/interface-srlg-names/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.InterfaceSrlgNames.InterfaceSrlgName, ['srlg_name', 'srlg_name_xr', 'srlg_value'], name, value)


            class Interfaces(Entity):
                """
                Interfaces information
                
                .. attribute:: interface_name
                
                	Interface name
                	**type**\:  list of str
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "interface-srlg-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface_name = YLeafList(YType.str, "interface-name")
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces, ['interface_name'], name, value)


    class Nodes(Entity):
        """
        RSI SRLG operational data
        
        .. attribute:: node
        
        	RSI SRLG operational data
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node>`
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Srlg.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", Srlg.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.Nodes, [], name, value)


        class Node(Entity):
            """
            RSI SRLG operational data
            
            .. attribute:: node_name  <key>
            
            	Node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: groups
            
            	Set of Groups configured for SRLG
            	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Groups>`
            
            .. attribute:: inherit_nodes
            
            	Set of inherit locations configured for SRLG
            	**type**\:   :py:class:`InheritNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InheritNodes>`
            
            .. attribute:: interface_details
            
            	Set of interfaces configured for SRLG
            	**type**\:   :py:class:`InterfaceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceDetails>`
            
            .. attribute:: interface_srlg_names
            
            	Set of SRLG names configured
            	**type**\:   :py:class:`InterfaceSrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceSrlgNames>`
            
            .. attribute:: interfaces
            
            	Set of interfaces configured for SRLG
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Interfaces>`
            
            .. attribute:: srlg_maps
            
            	Set of SRLG name, value maps configured
            	**type**\:   :py:class:`SrlgMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgMaps>`
            
            .. attribute:: srlg_values
            
            	Set of SRLG values configured
            	**type**\:   :py:class:`SrlgValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgValues>`
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Srlg.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"groups" : ("groups", Srlg.Nodes.Node.Groups), "inherit-nodes" : ("inherit_nodes", Srlg.Nodes.Node.InheritNodes), "interface-details" : ("interface_details", Srlg.Nodes.Node.InterfaceDetails), "interface-srlg-names" : ("interface_srlg_names", Srlg.Nodes.Node.InterfaceSrlgNames), "interfaces" : ("interfaces", Srlg.Nodes.Node.Interfaces), "srlg-maps" : ("srlg_maps", Srlg.Nodes.Node.SrlgMaps), "srlg-values" : ("srlg_values", Srlg.Nodes.Node.SrlgValues)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.groups = Srlg.Nodes.Node.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"
                self._children_yang_names.add("groups")

                self.inherit_nodes = Srlg.Nodes.Node.InheritNodes()
                self.inherit_nodes.parent = self
                self._children_name_map["inherit_nodes"] = "inherit-nodes"
                self._children_yang_names.add("inherit-nodes")

                self.interface_details = Srlg.Nodes.Node.InterfaceDetails()
                self.interface_details.parent = self
                self._children_name_map["interface_details"] = "interface-details"
                self._children_yang_names.add("interface-details")

                self.interface_srlg_names = Srlg.Nodes.Node.InterfaceSrlgNames()
                self.interface_srlg_names.parent = self
                self._children_name_map["interface_srlg_names"] = "interface-srlg-names"
                self._children_yang_names.add("interface-srlg-names")

                self.interfaces = Srlg.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.srlg_maps = Srlg.Nodes.Node.SrlgMaps()
                self.srlg_maps.parent = self
                self._children_name_map["srlg_maps"] = "srlg-maps"
                self._children_yang_names.add("srlg-maps")

                self.srlg_values = Srlg.Nodes.Node.SrlgValues()
                self.srlg_values.parent = self
                self._children_name_map["srlg_values"] = "srlg-values"
                self._children_yang_names.add("srlg-values")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.Nodes.Node, ['node_name'], name, value)


            class Groups(Entity):
                """
                Set of Groups configured for SRLG
                
                .. attribute:: group
                
                	SRLG group details
                	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Groups.Group>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Nodes.Node.Groups, self).__init__()

                    self.yang_name = "groups"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"group" : ("group", Srlg.Nodes.Node.Groups.Group)}

                    self.group = YList(self)
                    self._segment_path = lambda: "groups"

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Nodes.Node.Groups, [], name, value)


                class Group(Entity):
                    """
                    SRLG group details
                    
                    .. attribute:: group_name  <key>
                    
                    	Group name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: group_name_xr
                    
                    	Group name
                    	**type**\:  str
                    
                    .. attribute:: group_values
                    
                    	Group values
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srlg_attribute
                    
                    	SRLG attribute
                    	**type**\: list of    :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Groups.Group.SrlgAttribute>`
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.Nodes.Node.Groups.Group, self).__init__()

                        self.yang_name = "group"
                        self.yang_parent_name = "groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"srlg-attribute" : ("srlg_attribute", Srlg.Nodes.Node.Groups.Group.SrlgAttribute)}

                        self.group_name = YLeaf(YType.str, "group-name")

                        self.group_name_xr = YLeaf(YType.str, "group-name-xr")

                        self.group_values = YLeaf(YType.uint32, "group-values")

                        self.srlg_attribute = YList(self)
                        self._segment_path = lambda: "group" + "[group-name='" + self.group_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Nodes.Node.Groups.Group, ['group_name', 'group_name_xr', 'group_values'], name, value)


                    class SrlgAttribute(Entity):
                        """
                        SRLG attribute
                        
                        .. attribute:: priority
                        
                        	Priority
                        	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Priority>`
                        
                        .. attribute:: srlg_index
                        
                        	Index
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: srlg_value
                        
                        	SRLG value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Srlg.Nodes.Node.Groups.Group.SrlgAttribute, self).__init__()

                            self.yang_name = "srlg-attribute"
                            self.yang_parent_name = "group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.priority = YLeaf(YType.enumeration, "priority")

                            self.srlg_index = YLeaf(YType.uint16, "srlg-index")

                            self.srlg_value = YLeaf(YType.uint32, "srlg-value")
                            self._segment_path = lambda: "srlg-attribute"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srlg.Nodes.Node.Groups.Group.SrlgAttribute, ['priority', 'srlg_index', 'srlg_value'], name, value)


            class InheritNodes(Entity):
                """
                Set of inherit locations configured for SRLG
                
                .. attribute:: inherit_node
                
                	SRLG inherit location details
                	**type**\: list of    :py:class:`InheritNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InheritNodes.InheritNode>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Nodes.Node.InheritNodes, self).__init__()

                    self.yang_name = "inherit-nodes"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"inherit-node" : ("inherit_node", Srlg.Nodes.Node.InheritNodes.InheritNode)}

                    self.inherit_node = YList(self)
                    self._segment_path = lambda: "inherit-nodes"

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Nodes.Node.InheritNodes, [], name, value)


                class InheritNode(Entity):
                    """
                    SRLG inherit location details
                    
                    .. attribute:: inherit_node_name  <key>
                    
                    	Inherit node
                    	**type**\:  str
                    
                    	**pattern:** ((([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))/){2}(([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))
                    
                    .. attribute:: node_name
                    
                    	Inherit node name
                    	**type**\:  str
                    
                    .. attribute:: node_values
                    
                    	Node values
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srlg_attribute
                    
                    	SRLG attribute
                    	**type**\: list of    :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute>`
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.Nodes.Node.InheritNodes.InheritNode, self).__init__()

                        self.yang_name = "inherit-node"
                        self.yang_parent_name = "inherit-nodes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"srlg-attribute" : ("srlg_attribute", Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute)}

                        self.inherit_node_name = YLeaf(YType.str, "inherit-node-name")

                        self.node_name = YLeaf(YType.str, "node-name")

                        self.node_values = YLeaf(YType.uint32, "node-values")

                        self.srlg_attribute = YList(self)
                        self._segment_path = lambda: "inherit-node" + "[inherit-node-name='" + self.inherit_node_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Nodes.Node.InheritNodes.InheritNode, ['inherit_node_name', 'node_name', 'node_values'], name, value)


                    class SrlgAttribute(Entity):
                        """
                        SRLG attribute
                        
                        .. attribute:: priority
                        
                        	Priority
                        	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Priority>`
                        
                        .. attribute:: srlg_index
                        
                        	Index
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: srlg_value
                        
                        	SRLG value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute, self).__init__()

                            self.yang_name = "srlg-attribute"
                            self.yang_parent_name = "inherit-node"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.priority = YLeaf(YType.enumeration, "priority")

                            self.srlg_index = YLeaf(YType.uint16, "srlg-index")

                            self.srlg_value = YLeaf(YType.uint32, "srlg-value")
                            self._segment_path = lambda: "srlg-attribute"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute, ['priority', 'srlg_index', 'srlg_value'], name, value)


            class InterfaceDetails(Entity):
                """
                Set of interfaces configured for SRLG
                
                .. attribute:: interface_detail
                
                	SRLG interface details
                	**type**\: list of    :py:class:`InterfaceDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Nodes.Node.InterfaceDetails, self).__init__()

                    self.yang_name = "interface-details"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface-detail" : ("interface_detail", Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail)}

                    self.interface_detail = YList(self)
                    self._segment_path = lambda: "interface-details"

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Nodes.Node.InterfaceDetails, [], name, value)


                class InterfaceDetail(Entity):
                    """
                    SRLG interface details
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: groups
                    
                    	Groups
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nodes
                    
                    	Nodes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srlg_attribute
                    
                    	SRLG attributes
                    	**type**\: list of    :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute>`
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail, self).__init__()

                        self.yang_name = "interface-detail"
                        self.yang_parent_name = "interface-details"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"srlg-attribute" : ("srlg_attribute", Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute)}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.groups = YLeaf(YType.uint32, "groups")

                        self.nodes = YLeaf(YType.uint32, "nodes")

                        self.srlg_attribute = YList(self)
                        self._segment_path = lambda: "interface-detail" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail, ['interface_name', 'groups', 'nodes'], name, value)


                    class SrlgAttribute(Entity):
                        """
                        SRLG attributes
                        
                        .. attribute:: priority
                        
                        	Priority
                        	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Priority>`
                        
                        .. attribute:: source
                        
                        	Source
                        	**type**\:   :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Source>`
                        
                        .. attribute:: source_name
                        
                        	Source name
                        	**type**\:  str
                        
                        .. attribute:: srlg_index
                        
                        	Index
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: srlg_value
                        
                        	SRLG value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute, self).__init__()

                            self.yang_name = "srlg-attribute"
                            self.yang_parent_name = "interface-detail"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.priority = YLeaf(YType.enumeration, "priority")

                            self.source = YLeaf(YType.enumeration, "source")

                            self.source_name = YLeaf(YType.str, "source-name")

                            self.srlg_index = YLeaf(YType.uint16, "srlg-index")

                            self.srlg_value = YLeaf(YType.uint32, "srlg-value")
                            self._segment_path = lambda: "srlg-attribute"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute, ['priority', 'source', 'source_name', 'srlg_index', 'srlg_value'], name, value)


            class InterfaceSrlgNames(Entity):
                """
                Set of SRLG names configured
                
                .. attribute:: interface_srlg_name
                
                	Configured SRLG name details 
                	**type**\: list of    :py:class:`InterfaceSrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Nodes.Node.InterfaceSrlgNames, self).__init__()

                    self.yang_name = "interface-srlg-names"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface-srlg-name" : ("interface_srlg_name", Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName)}

                    self.interface_srlg_name = YList(self)
                    self._segment_path = lambda: "interface-srlg-names"

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Nodes.Node.InterfaceSrlgNames, [], name, value)


                class InterfaceSrlgName(Entity):
                    """
                    Configured SRLG name details 
                    
                    .. attribute:: srlg_name  <key>
                    
                    	SRLG name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: interfaces
                    
                    	Interfaces information
                    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces>`
                    
                    .. attribute:: srlg_name_xr
                    
                    	SRLG name
                    	**type**\:  str
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName, self).__init__()

                        self.yang_name = "interface-srlg-name"
                        self.yang_parent_name = "interface-srlg-names"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"interfaces" : ("interfaces", Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces)}
                        self._child_list_classes = {}

                        self.srlg_name = YLeaf(YType.str, "srlg-name")

                        self.srlg_name_xr = YLeaf(YType.str, "srlg-name-xr")

                        self.srlg_value = YLeaf(YType.uint32, "srlg-value")

                        self.interfaces = Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                        self._children_yang_names.add("interfaces")
                        self._segment_path = lambda: "interface-srlg-name" + "[srlg-name='" + self.srlg_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName, ['srlg_name', 'srlg_name_xr', 'srlg_value'], name, value)


                    class Interfaces(Entity):
                        """
                        Interfaces information
                        
                        .. attribute:: interface_name
                        
                        	Interface name
                        	**type**\:  list of str
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces, self).__init__()

                            self.yang_name = "interfaces"
                            self.yang_parent_name = "interface-srlg-name"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeafList(YType.str, "interface-name")
                            self._segment_path = lambda: "interfaces"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces, ['interface_name'], name, value)


            class Interfaces(Entity):
                """
                Set of interfaces configured for SRLG
                
                .. attribute:: interface
                
                	SRLG interface summary
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", Srlg.Nodes.Node.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    SRLG interface summary
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface name
                    	**type**\:  str
                    
                    .. attribute:: registrations
                    
                    	Registrations
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srlg_value
                    
                    	SRLG values
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: value_count
                    
                    	Values
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                        self.registrations = YLeaf(YType.uint32, "registrations")

                        self.srlg_value = YLeafList(YType.uint32, "srlg-value")

                        self.value_count = YLeaf(YType.uint32, "value-count")
                        self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Nodes.Node.Interfaces.Interface, ['interface_name', 'interface_name_xr', 'registrations', 'srlg_value', 'value_count'], name, value)


            class SrlgMaps(Entity):
                """
                Set of SRLG name, value maps configured
                
                .. attribute:: srlg_map
                
                	Configured SRLG name details 
                	**type**\: list of    :py:class:`SrlgMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgMaps.SrlgMap>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Nodes.Node.SrlgMaps, self).__init__()

                    self.yang_name = "srlg-maps"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"srlg-map" : ("srlg_map", Srlg.Nodes.Node.SrlgMaps.SrlgMap)}

                    self.srlg_map = YList(self)
                    self._segment_path = lambda: "srlg-maps"

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Nodes.Node.SrlgMaps, [], name, value)


                class SrlgMap(Entity):
                    """
                    Configured SRLG name details 
                    
                    .. attribute:: srlg_name  <key>
                    
                    	SRLG name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: srlg_name_xr
                    
                    	SRLG name
                    	**type**\:  str
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.Nodes.Node.SrlgMaps.SrlgMap, self).__init__()

                        self.yang_name = "srlg-map"
                        self.yang_parent_name = "srlg-maps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.srlg_name = YLeaf(YType.str, "srlg-name")

                        self.srlg_name_xr = YLeaf(YType.str, "srlg-name-xr")

                        self.srlg_value = YLeaf(YType.uint32, "srlg-value")
                        self._segment_path = lambda: "srlg-map" + "[srlg-name='" + self.srlg_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Nodes.Node.SrlgMaps.SrlgMap, ['srlg_name', 'srlg_name_xr', 'srlg_value'], name, value)


            class SrlgValues(Entity):
                """
                Set of SRLG values configured
                
                .. attribute:: srlg_value
                
                	Configured SRLG value details 
                	**type**\: list of    :py:class:`SrlgValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgValues.SrlgValue>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Nodes.Node.SrlgValues, self).__init__()

                    self.yang_name = "srlg-values"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"srlg-value" : ("srlg_value", Srlg.Nodes.Node.SrlgValues.SrlgValue)}

                    self.srlg_value = YList(self)
                    self._segment_path = lambda: "srlg-values"

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Nodes.Node.SrlgValues, [], name, value)


                class SrlgValue(Entity):
                    """
                    Configured SRLG value details 
                    
                    .. attribute:: value  <key>
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  list of str
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.Nodes.Node.SrlgValues.SrlgValue, self).__init__()

                        self.yang_name = "srlg-value"
                        self.yang_parent_name = "srlg-values"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.value = YLeaf(YType.int32, "value")

                        self.interface_name = YLeafList(YType.str, "interface-name")
                        self._segment_path = lambda: "srlg-value" + "[value='" + self.value.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Nodes.Node.SrlgValues.SrlgValue, ['value', 'interface_name'], name, value)


    class SrlgMaps(Entity):
        """
        Set of SRLG name, value maps configured
        
        .. attribute:: srlg_map
        
        	Configured SRLG name details 
        	**type**\: list of    :py:class:`SrlgMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.SrlgMaps.SrlgMap>`
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Srlg.SrlgMaps, self).__init__()

            self.yang_name = "srlg-maps"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"srlg-map" : ("srlg_map", Srlg.SrlgMaps.SrlgMap)}

            self.srlg_map = YList(self)
            self._segment_path = lambda: "srlg-maps"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.SrlgMaps, [], name, value)


        class SrlgMap(Entity):
            """
            Configured SRLG name details 
            
            .. attribute:: srlg_name  <key>
            
            	SRLG name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: srlg_name_xr
            
            	SRLG name
            	**type**\:  str
            
            .. attribute:: srlg_value
            
            	SRLG value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Srlg.SrlgMaps.SrlgMap, self).__init__()

                self.yang_name = "srlg-map"
                self.yang_parent_name = "srlg-maps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.srlg_name = YLeaf(YType.str, "srlg-name")

                self.srlg_name_xr = YLeaf(YType.str, "srlg-name-xr")

                self.srlg_value = YLeaf(YType.uint32, "srlg-value")
                self._segment_path = lambda: "srlg-map" + "[srlg-name='" + self.srlg_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/srlg-maps/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.SrlgMaps.SrlgMap, ['srlg_name', 'srlg_name_xr', 'srlg_value'], name, value)

    def clone_ptr(self):
        self._top_entity = Srlg()
        return self._top_entity

class VrfGroup(Entity):
    """
    VRF group operational data
    
    .. attribute:: nodes
    
    	Node operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes>`
    
    

    """

    _prefix = 'infra-rsi-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(VrfGroup, self).__init__()
        self._top_entity = None

        self.yang_name = "vrf-group"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", VrfGroup.Nodes)}
        self._child_list_classes = {}

        self.nodes = VrfGroup.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:vrf-group"


    class Nodes(Entity):
        """
        Node operational data
        
        .. attribute:: node
        
        	Node details
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node>`
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(VrfGroup.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "vrf-group"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", VrfGroup.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:vrf-group/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(VrfGroup.Nodes, [], name, value)


        class Node(Entity):
            """
            Node details
            
            .. attribute:: node_name  <key>
            
            	Node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: groups
            
            	Group operational data
            	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node.Groups>`
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(VrfGroup.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"groups" : ("groups", VrfGroup.Nodes.Node.Groups)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.groups = VrfGroup.Nodes.Node.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"
                self._children_yang_names.add("groups")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:vrf-group/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(VrfGroup.Nodes.Node, ['node_name'], name, value)


            class Groups(Entity):
                """
                Group operational data
                
                .. attribute:: group
                
                	Group details
                	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node.Groups.Group>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(VrfGroup.Nodes.Node.Groups, self).__init__()

                    self.yang_name = "groups"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"group" : ("group", VrfGroup.Nodes.Node.Groups.Group)}

                    self.group = YList(self)
                    self._segment_path = lambda: "groups"

                def __setattr__(self, name, value):
                    self._perform_setattr(VrfGroup.Nodes.Node.Groups, [], name, value)


                class Group(Entity):
                    """
                    Group details
                    
                    .. attribute:: group_name  <key>
                    
                    	Group name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: forward_reference
                    
                    	VRF group not present but used
                    	**type**\:  bool
                    
                    .. attribute:: vr_fs
                    
                    	Number of VRFs in this VRF group
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	VRF group's VRF
                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node.Groups.Group.Vrf>`
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(VrfGroup.Nodes.Node.Groups.Group, self).__init__()

                        self.yang_name = "group"
                        self.yang_parent_name = "groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"vrf" : ("vrf", VrfGroup.Nodes.Node.Groups.Group.Vrf)}

                        self.group_name = YLeaf(YType.str, "group-name")

                        self.forward_reference = YLeaf(YType.boolean, "forward-reference")

                        self.vr_fs = YLeaf(YType.uint32, "vr-fs")

                        self.vrf = YList(self)
                        self._segment_path = lambda: "group" + "[group-name='" + self.group_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(VrfGroup.Nodes.Node.Groups.Group, ['group_name', 'forward_reference', 'vr_fs'], name, value)


                    class Vrf(Entity):
                        """
                        VRF group's VRF
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(VrfGroup.Nodes.Node.Groups.Group.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.vrf_name = YLeaf(YType.str, "vrf-name")
                            self._segment_path = lambda: "vrf"

                        def __setattr__(self, name, value):
                            self._perform_setattr(VrfGroup.Nodes.Node.Groups.Group.Vrf, ['vrf_name'], name, value)

    def clone_ptr(self):
        self._top_entity = VrfGroup()
        return self._top_entity


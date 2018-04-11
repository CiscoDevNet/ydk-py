""" Cisco_IOS_XR_asr9k_prm_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-prm package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\-qos\-mode\: QoS mode in hardware module port(s)
  hardware\-module\-tcp\-mss\-adjust\: hardware module tcp mss adjust
  hardware\-module\-tcam\: hardware module tcam
  hardware\-module\-efd\: hardware module efd

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Asr9kEfdMode(Enum):
    """
    Asr9kEfdMode (Enum Class)

    Asr9k efd mode

    .. data:: only_outer_encap = 0

    	Only check outer encap

    .. data:: include_inner_encap = 1

    	Check outer and inner encap

    """

    only_outer_encap = Enum.YLeaf(0, "only-outer-encap")

    include_inner_encap = Enum.YLeaf(1, "include-inner-encap")


class Asr9kEfdOperation(Enum):
    """
    Asr9kEfdOperation (Enum Class)

    Asr9k efd operation

    .. data:: less_than = 2

    	Less than

    .. data:: greater_than_or_equal = 3

    	Greater than or equal

    """

    less_than = Enum.YLeaf(2, "less-than")

    greater_than_or_equal = Enum.YLeaf(3, "greater-than-or-equal")


class PrmTcamProfile(Enum):
    """
    PrmTcamProfile (Enum Class)

    Prm tcam profile

    .. data:: profile0 = 0

    	Profile 0

    .. data:: profile1 = 1

    	Profile 1

    .. data:: profile2 = 2

    	Profile 2

    """

    profile0 = Enum.YLeaf(0, "profile0")

    profile1 = Enum.YLeaf(1, "profile1")

    profile2 = Enum.YLeaf(2, "profile2")



class HardwareModuleQosMode(Entity):
    """
    QoS mode in hardware module port(s)
    
    .. attribute:: nodes
    
    	QoS applicable nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleQosMode.Nodes>`
    
    

    """

    _prefix = 'asr9k-prm-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModuleQosMode, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module-qos-mode"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-prm-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", HardwareModuleQosMode.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = HardwareModuleQosMode.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-qos-mode"


    class Nodes(Entity):
        """
        QoS applicable nodes
        
        .. attribute:: node
        
        	A node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleQosMode.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModuleQosMode.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "hardware-module-qos-mode"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", HardwareModuleQosMode.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-qos-mode/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModuleQosMode.Nodes, [], name, value)


        class Node(Entity):
            """
            A node
            
            .. attribute:: node_name  (key)
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: child_shaping_disable
            
            	Disable child level/flat policy shaping
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: lowburst_enable
            
            	Enable low burst mode for TM entity
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleQosMode.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                    ('child_shaping_disable', YLeaf(YType.empty, 'child-shaping-disable')),
                    ('lowburst_enable', YLeaf(YType.empty, 'lowburst-enable')),
                ])
                self.node_name = None
                self.child_shaping_disable = None
                self.lowburst_enable = None
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-qos-mode/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModuleQosMode.Nodes.Node, ['node_name', 'child_shaping_disable', 'lowburst_enable'], name, value)

    def clone_ptr(self):
        self._top_entity = HardwareModuleQosMode()
        return self._top_entity

class HardwareModuleTcpMssAdjust(Entity):
    """
    hardware module tcp mss adjust
    
    .. attribute:: nodes
    
    	TCP MSS Adjust applicable nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcpMssAdjust.Nodes>`
    
    

    """

    _prefix = 'asr9k-prm-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModuleTcpMssAdjust, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module-tcp-mss-adjust"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-prm-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", HardwareModuleTcpMssAdjust.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = HardwareModuleTcpMssAdjust.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcp-mss-adjust"


    class Nodes(Entity):
        """
        TCP MSS Adjust applicable nodes
        
        .. attribute:: node
        
        	A node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcpMssAdjust.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModuleTcpMssAdjust.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "hardware-module-tcp-mss-adjust"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", HardwareModuleTcpMssAdjust.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcp-mss-adjust/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModuleTcpMssAdjust.Nodes, [], name, value)


        class Node(Entity):
            """
            A node
            
            .. attribute:: node_name  (key)
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: nps
            
            	TCP MSS Adjust NPs
            	**type**\:  :py:class:`Nps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcpMssAdjust.Nodes.Node.Nps>`
            
            

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleTcpMssAdjust.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([("nps", ("nps", HardwareModuleTcpMssAdjust.Nodes.Node.Nps))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.node_name = None

                self.nps = HardwareModuleTcpMssAdjust.Nodes.Node.Nps()
                self.nps.parent = self
                self._children_name_map["nps"] = "nps"
                self._children_yang_names.add("nps")
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcp-mss-adjust/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModuleTcpMssAdjust.Nodes.Node, ['node_name'], name, value)


            class Nps(Entity):
                """
                TCP MSS Adjust NPs
                
                .. attribute:: np
                
                	NP number
                	**type**\: list of  		 :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcpMssAdjust.Nodes.Node.Nps.Np>`
                
                

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleTcpMssAdjust.Nodes.Node.Nps, self).__init__()

                    self.yang_name = "nps"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("np", ("np", HardwareModuleTcpMssAdjust.Nodes.Node.Nps.Np))])
                    self._leafs = OrderedDict()

                    self.np = YList(self)
                    self._segment_path = lambda: "nps"

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModuleTcpMssAdjust.Nodes.Node.Nps, [], name, value)


                class Np(Entity):
                    """
                    NP number
                    
                    .. attribute:: np_id  (key)
                    
                    	Number between 0\-7
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: adjust_value
                    
                    	TCP MSS Adjust value
                    	**type**\: int
                    
                    	**range:** 1280..1535
                    
                    	**units**\: byte
                    
                    

                    """

                    _prefix = 'asr9k-prm-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(HardwareModuleTcpMssAdjust.Nodes.Node.Nps.Np, self).__init__()

                        self.yang_name = "np"
                        self.yang_parent_name = "nps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['np_id']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('np_id', YLeaf(YType.uint32, 'np-id')),
                            ('adjust_value', YLeaf(YType.uint32, 'adjust-value')),
                        ])
                        self.np_id = None
                        self.adjust_value = None
                        self._segment_path = lambda: "np" + "[np-id='" + str(self.np_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(HardwareModuleTcpMssAdjust.Nodes.Node.Nps.Np, ['np_id', 'adjust_value'], name, value)

    def clone_ptr(self):
        self._top_entity = HardwareModuleTcpMssAdjust()
        return self._top_entity

class HardwareModuleTcam(Entity):
    """
    hardware module tcam
    
    .. attribute:: nodes
    
    	TCAM applicable nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcam.Nodes>`
    
    .. attribute:: global_profile
    
    	Global TCAM partition profile for all TCAM applicable nodes
    	**type**\:  :py:class:`PrmTcamProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.PrmTcamProfile>`
    
    	**default value**\: profile0
    
    

    """

    _prefix = 'asr9k-prm-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModuleTcam, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module-tcam"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-prm-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", HardwareModuleTcam.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('global_profile', YLeaf(YType.enumeration, 'global-profile')),
        ])
        self.global_profile = None

        self.nodes = HardwareModuleTcam.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcam"

    def __setattr__(self, name, value):
        self._perform_setattr(HardwareModuleTcam, ['global_profile'], name, value)


    class Nodes(Entity):
        """
        TCAM applicable nodes
        
        .. attribute:: node
        
        	A TCAM applicable node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcam.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModuleTcam.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "hardware-module-tcam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", HardwareModuleTcam.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcam/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModuleTcam.Nodes, [], name, value)


        class Node(Entity):
            """
            A TCAM applicable node
            
            .. attribute:: node_name  (key)
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: profile
            
            	A TCAM partition profile
            	**type**\:  :py:class:`PrmTcamProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.PrmTcamProfile>`
            
            	**default value**\: profile0
            
            

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleTcam.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                    ('profile', YLeaf(YType.enumeration, 'profile')),
                ])
                self.node_name = None
                self.profile = None
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcam/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModuleTcam.Nodes.Node, ['node_name', 'profile'], name, value)

    def clone_ptr(self):
        self._top_entity = HardwareModuleTcam()
        return self._top_entity

class HardwareModuleEfd(Entity):
    """
    hardware module efd
    
    .. attribute:: node_all
    
    	All nodes
    	**type**\:  :py:class:`NodeAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll>`
    
    .. attribute:: nodes
    
    	EFD applicable nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes>`
    
    

    """

    _prefix = 'asr9k-prm-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModuleEfd, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module-efd"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-prm-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("node-all", ("node_all", HardwareModuleEfd.NodeAll)), ("nodes", ("nodes", HardwareModuleEfd.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.node_all = HardwareModuleEfd.NodeAll()
        self.node_all.parent = self
        self._children_name_map["node_all"] = "node-all"
        self._children_yang_names.add("node-all")

        self.nodes = HardwareModuleEfd.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd"


    class NodeAll(Entity):
        """
        All nodes
        
        .. attribute:: vlan_priority_mask
        
        	VLAN Priority Mask
        	**type**\:  :py:class:`VlanPriorityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll.VlanPriorityMask>`
        
        	**presence node**\: True
        
        .. attribute:: ip_precedence
        
        	EFD IP parameters
        	**type**\:  :py:class:`IpPrecedence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll.IpPrecedence>`
        
        	**presence node**\: True
        
        .. attribute:: vlan_cos
        
        	EFD VLAN parameters
        	**type**\:  :py:class:`VlanCos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll.VlanCos>`
        
        	**presence node**\: True
        
        .. attribute:: enable
        
        	Enable EFD for this node
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: ip_priority_mask
        
        	IP Priority Mask
        	**type**\:  :py:class:`IpPriorityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll.IpPriorityMask>`
        
        	**presence node**\: True
        
        .. attribute:: mpls_priority_mask
        
        	MPLS Priority Mask
        	**type**\:  :py:class:`MplsPriorityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll.MplsPriorityMask>`
        
        	**presence node**\: True
        
        .. attribute:: mode
        
        	EFD mode parameter
        	**type**\:  :py:class:`Asr9kEfdMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9kEfdMode>`
        
        .. attribute:: mpls_exp
        
        	EFD MPLS parameters
        	**type**\:  :py:class:`MplsExp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll.MplsExp>`
        
        	**presence node**\: True
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModuleEfd.NodeAll, self).__init__()

            self.yang_name = "node-all"
            self.yang_parent_name = "hardware-module-efd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("vlan-priority-mask", ("vlan_priority_mask", HardwareModuleEfd.NodeAll.VlanPriorityMask)), ("ip-precedence", ("ip_precedence", HardwareModuleEfd.NodeAll.IpPrecedence)), ("vlan-cos", ("vlan_cos", HardwareModuleEfd.NodeAll.VlanCos)), ("ip-priority-mask", ("ip_priority_mask", HardwareModuleEfd.NodeAll.IpPriorityMask)), ("mpls-priority-mask", ("mpls_priority_mask", HardwareModuleEfd.NodeAll.MplsPriorityMask)), ("mpls-exp", ("mpls_exp", HardwareModuleEfd.NodeAll.MplsExp))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('enable', YLeaf(YType.empty, 'enable')),
                ('mode', YLeaf(YType.enumeration, 'mode')),
            ])
            self.enable = None
            self.mode = None

            self.vlan_priority_mask = None
            self._children_name_map["vlan_priority_mask"] = "vlan-priority-mask"
            self._children_yang_names.add("vlan-priority-mask")

            self.ip_precedence = None
            self._children_name_map["ip_precedence"] = "ip-precedence"
            self._children_yang_names.add("ip-precedence")

            self.vlan_cos = None
            self._children_name_map["vlan_cos"] = "vlan-cos"
            self._children_yang_names.add("vlan-cos")

            self.ip_priority_mask = None
            self._children_name_map["ip_priority_mask"] = "ip-priority-mask"
            self._children_yang_names.add("ip-priority-mask")

            self.mpls_priority_mask = None
            self._children_name_map["mpls_priority_mask"] = "mpls-priority-mask"
            self._children_yang_names.add("mpls-priority-mask")

            self.mpls_exp = None
            self._children_name_map["mpls_exp"] = "mpls-exp"
            self._children_yang_names.add("mpls-exp")
            self._segment_path = lambda: "node-all"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModuleEfd.NodeAll, ['enable', 'mode'], name, value)


        class VlanPriorityMask(Entity):
            """
            VLAN Priority Mask
            
            .. attribute:: prec0
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec1
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec2
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec3
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec4
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec5
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec6
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec7
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleEfd.NodeAll.VlanPriorityMask, self).__init__()

                self.yang_name = "vlan-priority-mask"
                self.yang_parent_name = "node-all"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('prec0', YLeaf(YType.uint32, 'prec0')),
                    ('prec1', YLeaf(YType.uint32, 'prec1')),
                    ('prec2', YLeaf(YType.uint32, 'prec2')),
                    ('prec3', YLeaf(YType.uint32, 'prec3')),
                    ('prec4', YLeaf(YType.uint32, 'prec4')),
                    ('prec5', YLeaf(YType.uint32, 'prec5')),
                    ('prec6', YLeaf(YType.uint32, 'prec6')),
                    ('prec7', YLeaf(YType.uint32, 'prec7')),
                ])
                self.prec0 = None
                self.prec1 = None
                self.prec2 = None
                self.prec3 = None
                self.prec4 = None
                self.prec5 = None
                self.prec6 = None
                self.prec7 = None
                self._segment_path = lambda: "vlan-priority-mask"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/node-all/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModuleEfd.NodeAll.VlanPriorityMask, ['prec0', 'prec1', 'prec2', 'prec3', 'prec4', 'prec5', 'prec6', 'prec7'], name, value)


        class IpPrecedence(Entity):
            """
            EFD IP parameters
            
            .. attribute:: precedence
            
            	IP TOS precedence threshold
            	**type**\: int
            
            	**range:** 0..7
            
            	**mandatory**\: True
            
            .. attribute:: operation_
            
            	IP operation
            	**type**\:  :py:class:`Asr9kEfdOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9kEfdOperation>`
            
            	**default value**\: greater-than-or-equal
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleEfd.NodeAll.IpPrecedence, self).__init__()

                self.yang_name = "ip-precedence"
                self.yang_parent_name = "node-all"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('precedence', YLeaf(YType.uint32, 'precedence')),
                    ('operation_', YLeaf(YType.enumeration, 'operation')),
                ])
                self.precedence = None
                self.operation_ = None
                self._segment_path = lambda: "ip-precedence"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/node-all/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModuleEfd.NodeAll.IpPrecedence, ['precedence', 'operation_'], name, value)


        class VlanCos(Entity):
            """
            EFD VLAN parameters
            
            .. attribute:: cos
            
            	VLAN COS threshold
            	**type**\: int
            
            	**range:** 0..7
            
            	**mandatory**\: True
            
            .. attribute:: operation_
            
            	VLAN operation
            	**type**\:  :py:class:`Asr9kEfdOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9kEfdOperation>`
            
            	**default value**\: greater-than-or-equal
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleEfd.NodeAll.VlanCos, self).__init__()

                self.yang_name = "vlan-cos"
                self.yang_parent_name = "node-all"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('cos', YLeaf(YType.uint32, 'cos')),
                    ('operation_', YLeaf(YType.enumeration, 'operation')),
                ])
                self.cos = None
                self.operation_ = None
                self._segment_path = lambda: "vlan-cos"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/node-all/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModuleEfd.NodeAll.VlanCos, ['cos', 'operation_'], name, value)


        class IpPriorityMask(Entity):
            """
            IP Priority Mask
            
            .. attribute:: prec0
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec1
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec2
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec3
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec4
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec5
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec6
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec7
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleEfd.NodeAll.IpPriorityMask, self).__init__()

                self.yang_name = "ip-priority-mask"
                self.yang_parent_name = "node-all"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('prec0', YLeaf(YType.uint32, 'prec0')),
                    ('prec1', YLeaf(YType.uint32, 'prec1')),
                    ('prec2', YLeaf(YType.uint32, 'prec2')),
                    ('prec3', YLeaf(YType.uint32, 'prec3')),
                    ('prec4', YLeaf(YType.uint32, 'prec4')),
                    ('prec5', YLeaf(YType.uint32, 'prec5')),
                    ('prec6', YLeaf(YType.uint32, 'prec6')),
                    ('prec7', YLeaf(YType.uint32, 'prec7')),
                ])
                self.prec0 = None
                self.prec1 = None
                self.prec2 = None
                self.prec3 = None
                self.prec4 = None
                self.prec5 = None
                self.prec6 = None
                self.prec7 = None
                self._segment_path = lambda: "ip-priority-mask"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/node-all/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModuleEfd.NodeAll.IpPriorityMask, ['prec0', 'prec1', 'prec2', 'prec3', 'prec4', 'prec5', 'prec6', 'prec7'], name, value)


        class MplsPriorityMask(Entity):
            """
            MPLS Priority Mask
            
            .. attribute:: prec0
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec1
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec2
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec3
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec4
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec5
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec6
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec7
            
            	Prec
            	**type**\: int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleEfd.NodeAll.MplsPriorityMask, self).__init__()

                self.yang_name = "mpls-priority-mask"
                self.yang_parent_name = "node-all"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('prec0', YLeaf(YType.uint32, 'prec0')),
                    ('prec1', YLeaf(YType.uint32, 'prec1')),
                    ('prec2', YLeaf(YType.uint32, 'prec2')),
                    ('prec3', YLeaf(YType.uint32, 'prec3')),
                    ('prec4', YLeaf(YType.uint32, 'prec4')),
                    ('prec5', YLeaf(YType.uint32, 'prec5')),
                    ('prec6', YLeaf(YType.uint32, 'prec6')),
                    ('prec7', YLeaf(YType.uint32, 'prec7')),
                ])
                self.prec0 = None
                self.prec1 = None
                self.prec2 = None
                self.prec3 = None
                self.prec4 = None
                self.prec5 = None
                self.prec6 = None
                self.prec7 = None
                self._segment_path = lambda: "mpls-priority-mask"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/node-all/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModuleEfd.NodeAll.MplsPriorityMask, ['prec0', 'prec1', 'prec2', 'prec3', 'prec4', 'prec5', 'prec6', 'prec7'], name, value)


        class MplsExp(Entity):
            """
            EFD MPLS parameters
            
            .. attribute:: exp
            
            	MPLS EXP threshold
            	**type**\: int
            
            	**range:** 0..7
            
            	**mandatory**\: True
            
            .. attribute:: operation_
            
            	MPLS operation
            	**type**\:  :py:class:`Asr9kEfdOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9kEfdOperation>`
            
            	**default value**\: greater-than-or-equal
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleEfd.NodeAll.MplsExp, self).__init__()

                self.yang_name = "mpls-exp"
                self.yang_parent_name = "node-all"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('exp', YLeaf(YType.uint32, 'exp')),
                    ('operation_', YLeaf(YType.enumeration, 'operation')),
                ])
                self.exp = None
                self.operation_ = None
                self._segment_path = lambda: "mpls-exp"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/node-all/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModuleEfd.NodeAll.MplsExp, ['exp', 'operation_'], name, value)


    class Nodes(Entity):
        """
        EFD applicable nodes
        
        .. attribute:: node
        
        	A node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModuleEfd.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "hardware-module-efd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", HardwareModuleEfd.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModuleEfd.Nodes, [], name, value)


        class Node(Entity):
            """
            A node
            
            .. attribute:: node_name  (key)
            
            	Node Name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: vlan_priority_mask
            
            	VLAN Priority Mask
            	**type**\:  :py:class:`VlanPriorityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node.VlanPriorityMask>`
            
            	**presence node**\: True
            
            .. attribute:: ip_precedence
            
            	EFD IP parameters
            	**type**\:  :py:class:`IpPrecedence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node.IpPrecedence>`
            
            	**presence node**\: True
            
            .. attribute:: vlan_cos
            
            	EFD VLAN parameters
            	**type**\:  :py:class:`VlanCos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node.VlanCos>`
            
            	**presence node**\: True
            
            .. attribute:: enable
            
            	Enable EFD for this node
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: ip_priority_mask
            
            	IP Priority Mask
            	**type**\:  :py:class:`IpPriorityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node.IpPriorityMask>`
            
            	**presence node**\: True
            
            .. attribute:: mpls_priority_mask
            
            	MPLS Priority Mask
            	**type**\:  :py:class:`MplsPriorityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node.MplsPriorityMask>`
            
            	**presence node**\: True
            
            .. attribute:: mode
            
            	EFD mode parameter
            	**type**\:  :py:class:`Asr9kEfdMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9kEfdMode>`
            
            .. attribute:: mpls_exp
            
            	EFD MPLS parameters
            	**type**\:  :py:class:`MplsExp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node.MplsExp>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleEfd.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([("vlan-priority-mask", ("vlan_priority_mask", HardwareModuleEfd.Nodes.Node.VlanPriorityMask)), ("ip-precedence", ("ip_precedence", HardwareModuleEfd.Nodes.Node.IpPrecedence)), ("vlan-cos", ("vlan_cos", HardwareModuleEfd.Nodes.Node.VlanCos)), ("ip-priority-mask", ("ip_priority_mask", HardwareModuleEfd.Nodes.Node.IpPriorityMask)), ("mpls-priority-mask", ("mpls_priority_mask", HardwareModuleEfd.Nodes.Node.MplsPriorityMask)), ("mpls-exp", ("mpls_exp", HardwareModuleEfd.Nodes.Node.MplsExp))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                    ('enable', YLeaf(YType.empty, 'enable')),
                    ('mode', YLeaf(YType.enumeration, 'mode')),
                ])
                self.node_name = None
                self.enable = None
                self.mode = None

                self.vlan_priority_mask = None
                self._children_name_map["vlan_priority_mask"] = "vlan-priority-mask"
                self._children_yang_names.add("vlan-priority-mask")

                self.ip_precedence = None
                self._children_name_map["ip_precedence"] = "ip-precedence"
                self._children_yang_names.add("ip-precedence")

                self.vlan_cos = None
                self._children_name_map["vlan_cos"] = "vlan-cos"
                self._children_yang_names.add("vlan-cos")

                self.ip_priority_mask = None
                self._children_name_map["ip_priority_mask"] = "ip-priority-mask"
                self._children_yang_names.add("ip-priority-mask")

                self.mpls_priority_mask = None
                self._children_name_map["mpls_priority_mask"] = "mpls-priority-mask"
                self._children_yang_names.add("mpls-priority-mask")

                self.mpls_exp = None
                self._children_name_map["mpls_exp"] = "mpls-exp"
                self._children_yang_names.add("mpls-exp")
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModuleEfd.Nodes.Node, ['node_name', 'enable', 'mode'], name, value)


            class VlanPriorityMask(Entity):
                """
                VLAN Priority Mask
                
                .. attribute:: prec0
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec1
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec2
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec3
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec4
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec5
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec6
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec7
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleEfd.Nodes.Node.VlanPriorityMask, self).__init__()

                    self.yang_name = "vlan-priority-mask"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('prec0', YLeaf(YType.uint32, 'prec0')),
                        ('prec1', YLeaf(YType.uint32, 'prec1')),
                        ('prec2', YLeaf(YType.uint32, 'prec2')),
                        ('prec3', YLeaf(YType.uint32, 'prec3')),
                        ('prec4', YLeaf(YType.uint32, 'prec4')),
                        ('prec5', YLeaf(YType.uint32, 'prec5')),
                        ('prec6', YLeaf(YType.uint32, 'prec6')),
                        ('prec7', YLeaf(YType.uint32, 'prec7')),
                    ])
                    self.prec0 = None
                    self.prec1 = None
                    self.prec2 = None
                    self.prec3 = None
                    self.prec4 = None
                    self.prec5 = None
                    self.prec6 = None
                    self.prec7 = None
                    self._segment_path = lambda: "vlan-priority-mask"

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModuleEfd.Nodes.Node.VlanPriorityMask, ['prec0', 'prec1', 'prec2', 'prec3', 'prec4', 'prec5', 'prec6', 'prec7'], name, value)


            class IpPrecedence(Entity):
                """
                EFD IP parameters
                
                .. attribute:: precedence
                
                	IP TOS precedence threshold
                	**type**\: int
                
                	**range:** 0..7
                
                	**mandatory**\: True
                
                .. attribute:: operation_
                
                	IP operation
                	**type**\:  :py:class:`Asr9kEfdOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9kEfdOperation>`
                
                	**default value**\: greater-than-or-equal
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleEfd.Nodes.Node.IpPrecedence, self).__init__()

                    self.yang_name = "ip-precedence"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('precedence', YLeaf(YType.uint32, 'precedence')),
                        ('operation_', YLeaf(YType.enumeration, 'operation')),
                    ])
                    self.precedence = None
                    self.operation_ = None
                    self._segment_path = lambda: "ip-precedence"

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModuleEfd.Nodes.Node.IpPrecedence, ['precedence', 'operation_'], name, value)


            class VlanCos(Entity):
                """
                EFD VLAN parameters
                
                .. attribute:: cos
                
                	VLAN COS threshold
                	**type**\: int
                
                	**range:** 0..7
                
                	**mandatory**\: True
                
                .. attribute:: operation_
                
                	VLAN operation
                	**type**\:  :py:class:`Asr9kEfdOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9kEfdOperation>`
                
                	**default value**\: greater-than-or-equal
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleEfd.Nodes.Node.VlanCos, self).__init__()

                    self.yang_name = "vlan-cos"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('cos', YLeaf(YType.uint32, 'cos')),
                        ('operation_', YLeaf(YType.enumeration, 'operation')),
                    ])
                    self.cos = None
                    self.operation_ = None
                    self._segment_path = lambda: "vlan-cos"

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModuleEfd.Nodes.Node.VlanCos, ['cos', 'operation_'], name, value)


            class IpPriorityMask(Entity):
                """
                IP Priority Mask
                
                .. attribute:: prec0
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec1
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec2
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec3
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec4
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec5
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec6
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec7
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleEfd.Nodes.Node.IpPriorityMask, self).__init__()

                    self.yang_name = "ip-priority-mask"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('prec0', YLeaf(YType.uint32, 'prec0')),
                        ('prec1', YLeaf(YType.uint32, 'prec1')),
                        ('prec2', YLeaf(YType.uint32, 'prec2')),
                        ('prec3', YLeaf(YType.uint32, 'prec3')),
                        ('prec4', YLeaf(YType.uint32, 'prec4')),
                        ('prec5', YLeaf(YType.uint32, 'prec5')),
                        ('prec6', YLeaf(YType.uint32, 'prec6')),
                        ('prec7', YLeaf(YType.uint32, 'prec7')),
                    ])
                    self.prec0 = None
                    self.prec1 = None
                    self.prec2 = None
                    self.prec3 = None
                    self.prec4 = None
                    self.prec5 = None
                    self.prec6 = None
                    self.prec7 = None
                    self._segment_path = lambda: "ip-priority-mask"

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModuleEfd.Nodes.Node.IpPriorityMask, ['prec0', 'prec1', 'prec2', 'prec3', 'prec4', 'prec5', 'prec6', 'prec7'], name, value)


            class MplsPriorityMask(Entity):
                """
                MPLS Priority Mask
                
                .. attribute:: prec0
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec1
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec2
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec3
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec4
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec5
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec6
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec7
                
                	Prec
                	**type**\: int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleEfd.Nodes.Node.MplsPriorityMask, self).__init__()

                    self.yang_name = "mpls-priority-mask"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('prec0', YLeaf(YType.uint32, 'prec0')),
                        ('prec1', YLeaf(YType.uint32, 'prec1')),
                        ('prec2', YLeaf(YType.uint32, 'prec2')),
                        ('prec3', YLeaf(YType.uint32, 'prec3')),
                        ('prec4', YLeaf(YType.uint32, 'prec4')),
                        ('prec5', YLeaf(YType.uint32, 'prec5')),
                        ('prec6', YLeaf(YType.uint32, 'prec6')),
                        ('prec7', YLeaf(YType.uint32, 'prec7')),
                    ])
                    self.prec0 = None
                    self.prec1 = None
                    self.prec2 = None
                    self.prec3 = None
                    self.prec4 = None
                    self.prec5 = None
                    self.prec6 = None
                    self.prec7 = None
                    self._segment_path = lambda: "mpls-priority-mask"

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModuleEfd.Nodes.Node.MplsPriorityMask, ['prec0', 'prec1', 'prec2', 'prec3', 'prec4', 'prec5', 'prec6', 'prec7'], name, value)


            class MplsExp(Entity):
                """
                EFD MPLS parameters
                
                .. attribute:: exp
                
                	MPLS EXP threshold
                	**type**\: int
                
                	**range:** 0..7
                
                	**mandatory**\: True
                
                .. attribute:: operation_
                
                	MPLS operation
                	**type**\:  :py:class:`Asr9kEfdOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9kEfdOperation>`
                
                	**default value**\: greater-than-or-equal
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleEfd.Nodes.Node.MplsExp, self).__init__()

                    self.yang_name = "mpls-exp"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('exp', YLeaf(YType.uint32, 'exp')),
                        ('operation_', YLeaf(YType.enumeration, 'operation')),
                    ])
                    self.exp = None
                    self.operation_ = None
                    self._segment_path = lambda: "mpls-exp"

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModuleEfd.Nodes.Node.MplsExp, ['exp', 'operation_'], name, value)

    def clone_ptr(self):
        self._top_entity = HardwareModuleEfd()
        return self._top_entity


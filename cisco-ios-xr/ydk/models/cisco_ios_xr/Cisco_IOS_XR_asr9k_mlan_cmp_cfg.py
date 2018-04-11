""" Cisco_IOS_XR_asr9k_mlan_cmp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-mlan\-cmp package configuration.

This module contains definitions
for the following management objects\:
  mlan\-disable\-cmp\: Disable/Enable CMP

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MlanDisableCmp(Entity):
    """
    Disable/Enable CMP
    
    .. attribute:: nodes
    
    	Fully qualified RSP4/RSP4s/RP2 card specification
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_mlan_cmp_cfg.MlanDisableCmp.Nodes>`
    
    

    """

    _prefix = 'asr9k-mlan-cmp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(MlanDisableCmp, self).__init__()
        self._top_entity = None

        self.yang_name = "mlan-disable-cmp"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-mlan-cmp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", MlanDisableCmp.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = MlanDisableCmp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-mlan-cmp-cfg:mlan-disable-cmp"


    class Nodes(Entity):
        """
        Fully qualified RSP4/RSP4s/RP2 card
        specification
        
        .. attribute:: node
        
        	A node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_mlan_cmp_cfg.MlanDisableCmp.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-mlan-cmp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MlanDisableCmp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "mlan-disable-cmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", MlanDisableCmp.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-mlan-cmp-cfg:mlan-disable-cmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MlanDisableCmp.Nodes, [], name, value)


        class Node(Entity):
            """
            A node
            
            .. attribute:: node_name  (key)
            
            	NodeName
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: disable
            
            	Disable CMP
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'asr9k-mlan-cmp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MlanDisableCmp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                    ('disable', YLeaf(YType.empty, 'disable')),
                ])
                self.node_name = None
                self.disable = None
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-mlan-cmp-cfg:mlan-disable-cmp/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MlanDisableCmp.Nodes.Node, ['node_name', 'disable'], name, value)

    def clone_ptr(self):
        self._top_entity = MlanDisableCmp()
        return self._top_entity


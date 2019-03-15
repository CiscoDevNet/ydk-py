""" Cisco_IOS_XR_slice_mgr_proxy_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR slice\-mgr\-proxy package configuration.

This module contains definitions
for the following management objects\:
  node\-path\: Node act path

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class NodePath(Entity):
    """
    Node act path
    
    .. attribute:: node
    
    	Node (Physical location of the node in R\_S\_I format)
    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_slice_mgr_proxy_cfg.NodePath.Node>`
    
    

    """

    _prefix = 'slice-mgr-proxy-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(NodePath, self).__init__()
        self._top_entity = None

        self.yang_name = "node-path"
        self.yang_parent_name = "Cisco-IOS-XR-slice-mgr-proxy-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("node", ("node", NodePath.Node))])
        self._leafs = OrderedDict()

        self.node = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-slice-mgr-proxy-cfg:node-path"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(NodePath, [], name, value)


    class Node(Entity):
        """
        Node (Physical location of the node in R\_S\_I
        format)
        
        .. attribute:: node_name  (key)
        
        	Location in R\_S\_I format
        	**type**\: str
        
        .. attribute:: slice_ids
        
        	Slice
        	**type**\:  :py:class:`SliceIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_slice_mgr_proxy_cfg.NodePath.Node.SliceIds>`
        
        

        """

        _prefix = 'slice-mgr-proxy-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(NodePath.Node, self).__init__()

            self.yang_name = "node"
            self.yang_parent_name = "node-path"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['node_name']
            self._child_classes = OrderedDict([("slice-ids", ("slice_ids", NodePath.Node.SliceIds))])
            self._leafs = OrderedDict([
                ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
            ])
            self.node_name = None

            self.slice_ids = NodePath.Node.SliceIds()
            self.slice_ids.parent = self
            self._children_name_map["slice_ids"] = "slice-ids"
            self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-slice-mgr-proxy-cfg:node-path/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NodePath.Node, ['node_name'], name, value)


        class SliceIds(Entity):
            """
            Slice
            
            .. attribute:: slice_id
            
            	Slice Id on which configuration will be applied
            	**type**\: list of  		 :py:class:`SliceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_slice_mgr_proxy_cfg.NodePath.Node.SliceIds.SliceId>`
            
            

            """

            _prefix = 'slice-mgr-proxy-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(NodePath.Node.SliceIds, self).__init__()

                self.yang_name = "slice-ids"
                self.yang_parent_name = "node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("slice-id", ("slice_id", NodePath.Node.SliceIds.SliceId))])
                self._leafs = OrderedDict()

                self.slice_id = YList(self)
                self._segment_path = lambda: "slice-ids"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NodePath.Node.SliceIds, [], name, value)


            class SliceId(Entity):
                """
                Slice Id on which configuration will be
                applied
                
                .. attribute:: slice_id  (key)
                
                	The identifier for this slice
                	**type**\: int
                
                	**range:** 0..4
                
                .. attribute:: state
                
                	set val 0 to shutdown
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: breakout
                
                	10G Breakout Config
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: mode
                
                	set val 4 for OTU4 
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'slice-mgr-proxy-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NodePath.Node.SliceIds.SliceId, self).__init__()

                    self.yang_name = "slice-id"
                    self.yang_parent_name = "slice-ids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['slice_id']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('slice_id', (YLeaf(YType.uint32, 'slice-id'), ['int'])),
                        ('state', (YLeaf(YType.uint32, 'state'), ['int'])),
                        ('breakout', (YLeaf(YType.uint32, 'breakout'), ['int'])),
                        ('mode', (YLeaf(YType.uint32, 'mode'), ['int'])),
                    ])
                    self.slice_id = None
                    self.state = None
                    self.breakout = None
                    self.mode = None
                    self._segment_path = lambda: "slice-id" + "[slice-id='" + str(self.slice_id) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(NodePath.Node.SliceIds.SliceId, ['slice_id', 'state', 'breakout', 'mode'], name, value)




    def clone_ptr(self):
        self._top_entity = NodePath()
        return self._top_entity




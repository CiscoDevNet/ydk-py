""" Cisco_IOS_XR_cofo_csi_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR cofo\-csi\-ma package operational data.

This module contains definitions
for the following management objects\:
  cross\-sdr\-intf\-ma\: Csi\-ma operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CsiMaAfi(Enum):
    """
    CsiMaAfi (Enum Class)

    CSI MA Address family enum type

    .. data:: csi_afi_ipv4 = 1

    	IPv4 address family

    .. data:: csi_afi_ipv6 = 2

    	IPv6 address family

    .. data:: csi_afi_invalid = 3

    	Invalid address family

    """

    csi_afi_ipv4 = Enum.YLeaf(1, "csi-afi-ipv4")

    csi_afi_ipv6 = Enum.YLeaf(2, "csi-afi-ipv6")

    csi_afi_invalid = Enum.YLeaf(3, "csi-afi-invalid")


class CsiMaConnState(Enum):
    """
    CsiMaConnState (Enum Class)

    CSI\-MA connection state enum type

    .. data:: csi_ma_conn_default = 0

    	Default connection state

    .. data:: csi_ma_conn_closed = 1

    	Connection closed

    .. data:: csi_ma_conn_opened = 2

    	Connection opened

    .. data:: csi_ma_conn_synced = 3

    	Connection synced

    .. data:: csi_ma_conn_max = 4

    	Unknown connection state

    """

    csi_ma_conn_default = Enum.YLeaf(0, "csi-ma-conn-default")

    csi_ma_conn_closed = Enum.YLeaf(1, "csi-ma-conn-closed")

    csi_ma_conn_opened = Enum.YLeaf(2, "csi-ma-conn-opened")

    csi_ma_conn_synced = Enum.YLeaf(3, "csi-ma-conn-synced")

    csi_ma_conn_max = Enum.YLeaf(4, "csi-ma-conn-max")


class CsiMaFoTimerState(Enum):
    """
    CsiMaFoTimerState (Enum Class)

    Fail Over Timer state

    .. data:: csi_ma_fo_default = 1

    	Default state

    .. data:: csi_ma_fo_push_self_data = 2

    	Push self data

    .. data:: csi_ma_fo_sync_rem_data = 3

    	Sync remote data

    .. data:: csi_ma_fo_synced = 4

    	Synced

    .. data:: csi_ma_fo_max = 5

    	Max state

    """

    csi_ma_fo_default = Enum.YLeaf(1, "csi-ma-fo-default")

    csi_ma_fo_push_self_data = Enum.YLeaf(2, "csi-ma-fo-push-self-data")

    csi_ma_fo_sync_rem_data = Enum.YLeaf(3, "csi-ma-fo-sync-rem-data")

    csi_ma_fo_synced = Enum.YLeaf(4, "csi-ma-fo-synced")

    csi_ma_fo_max = Enum.YLeaf(5, "csi-ma-fo-max")


class CsiMaItemState(Enum):
    """
    CsiMaItemState (Enum Class)

    CSI MA item state enum type

    .. data:: csi_ma_item_create_req = 0

    	Interface create requested, wating for ack

    .. data:: csi_ma_item_attr_req = 1

    	Requested attributes passed from pub-sub admin

    .. data:: csi_ma_item_valid = 2

    	Valid entry

    .. data:: csi_ma_item_synced = 3

    	Replicated and synced to all nodes

    .. data:: csi_ma_item_mark_ed = 4

    	Marked for sweep at EOD

    .. data:: csi_ma_item_invalid = 5

    	Marked for delete in IM and then purge entry

    .. data:: csi_ma_item_delete_req = 6

    	Interface delete requested, wating for ack

    .. data:: csi_ma_item_max_states = 7

    	Invalid state

    """

    csi_ma_item_create_req = Enum.YLeaf(0, "csi-ma-item-create-req")

    csi_ma_item_attr_req = Enum.YLeaf(1, "csi-ma-item-attr-req")

    csi_ma_item_valid = Enum.YLeaf(2, "csi-ma-item-valid")

    csi_ma_item_synced = Enum.YLeaf(3, "csi-ma-item-synced")

    csi_ma_item_mark_ed = Enum.YLeaf(4, "csi-ma-item-mark-ed")

    csi_ma_item_invalid = Enum.YLeaf(5, "csi-ma-item-invalid")

    csi_ma_item_delete_req = Enum.YLeaf(6, "csi-ma-item-delete-req")

    csi_ma_item_max_states = Enum.YLeaf(7, "csi-ma-item-max-states")



class CrossSdrIntfMa(Entity):
    """
    Csi\-ma operational data
    
    .. attribute:: nodes
    
    	Node\-specific operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes>`
    
    

    """

    _prefix = 'cofo-csi-ma-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(CrossSdrIntfMa, self).__init__()
        self._top_entity = None

        self.yang_name = "cross-sdr-intf-ma"
        self.yang_parent_name = "Cisco-IOS-XR-cofo-csi-ma-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", CrossSdrIntfMa.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = CrossSdrIntfMa.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-cofo-csi-ma-oper:cross-sdr-intf-ma"

    def __setattr__(self, name, value):
        self._perform_setattr(CrossSdrIntfMa, [], name, value)


    class Nodes(Entity):
        """
        Node\-specific operational data
        
        .. attribute:: node
        
        	Operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node>`
        
        

        """

        _prefix = 'cofo-csi-ma-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(CrossSdrIntfMa.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "cross-sdr-intf-ma"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", CrossSdrIntfMa.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-cofo-csi-ma-oper:cross-sdr-intf-ma/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CrossSdrIntfMa.Nodes, [], name, value)


        class Node(Entity):
            """
            Operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	The node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: rack_ids
            
            	Connected node slices information
            	**type**\:  :py:class:`RackIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.RackIds>`
            
            .. attribute:: csi_indexes
            
            	Admin data for csi\-index
            	**type**\:  :py:class:`CsiIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.CsiIndexes>`
            
            .. attribute:: interface_names
            
            	Interface data for csi interfaces
            	**type**\:  :py:class:`InterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.InterfaceNames>`
            
            .. attribute:: global_
            
            	Global data associated with csi\-ma
            	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.Global>`
            
            .. attribute:: sdr_ids
            
            	Remote data for SDR ID
            	**type**\:  :py:class:`SdrIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.SdrIds>`
            
            

            """

            _prefix = 'cofo-csi-ma-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(CrossSdrIntfMa.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("rack-ids", ("rack_ids", CrossSdrIntfMa.Nodes.Node.RackIds)), ("csi-indexes", ("csi_indexes", CrossSdrIntfMa.Nodes.Node.CsiIndexes)), ("interface-names", ("interface_names", CrossSdrIntfMa.Nodes.Node.InterfaceNames)), ("global", ("global_", CrossSdrIntfMa.Nodes.Node.Global)), ("sdr-ids", ("sdr_ids", CrossSdrIntfMa.Nodes.Node.SdrIds))])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.node_name = None

                self.rack_ids = CrossSdrIntfMa.Nodes.Node.RackIds()
                self.rack_ids.parent = self
                self._children_name_map["rack_ids"] = "rack-ids"

                self.csi_indexes = CrossSdrIntfMa.Nodes.Node.CsiIndexes()
                self.csi_indexes.parent = self
                self._children_name_map["csi_indexes"] = "csi-indexes"

                self.interface_names = CrossSdrIntfMa.Nodes.Node.InterfaceNames()
                self.interface_names.parent = self
                self._children_name_map["interface_names"] = "interface-names"

                self.global_ = CrossSdrIntfMa.Nodes.Node.Global()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"

                self.sdr_ids = CrossSdrIntfMa.Nodes.Node.SdrIds()
                self.sdr_ids.parent = self
                self._children_name_map["sdr_ids"] = "sdr-ids"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-cofo-csi-ma-oper:cross-sdr-intf-ma/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CrossSdrIntfMa.Nodes.Node, ['node_name'], name, value)


            class RackIds(Entity):
                """
                Connected node slices information
                
                .. attribute:: rack_id
                
                	Connected node rack\-id
                	**type**\: list of  		 :py:class:`RackId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.RackIds.RackId>`
                
                

                """

                _prefix = 'cofo-csi-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(CrossSdrIntfMa.Nodes.Node.RackIds, self).__init__()

                    self.yang_name = "rack-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("rack-id", ("rack_id", CrossSdrIntfMa.Nodes.Node.RackIds.RackId))])
                    self._leafs = OrderedDict()

                    self.rack_id = YList(self)
                    self._segment_path = lambda: "rack-ids"

                def __setattr__(self, name, value):
                    self._perform_setattr(CrossSdrIntfMa.Nodes.Node.RackIds, [], name, value)


                class RackId(Entity):
                    """
                    Connected node rack\-id
                    
                    .. attribute:: rack_id  (key)
                    
                    	Rack Id
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: slot_id
                    
                    	NodeInfo for a NodeId
                    	**type**\: list of  		 :py:class:`SlotId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.RackIds.RackId.SlotId>`
                    
                    

                    """

                    _prefix = 'cofo-csi-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CrossSdrIntfMa.Nodes.Node.RackIds.RackId, self).__init__()

                        self.yang_name = "rack-id"
                        self.yang_parent_name = "rack-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['rack_id']
                        self._child_classes = OrderedDict([("slot-id", ("slot_id", CrossSdrIntfMa.Nodes.Node.RackIds.RackId.SlotId))])
                        self._leafs = OrderedDict([
                            ('rack_id', YLeaf(YType.uint32, 'rack-id')),
                        ])
                        self.rack_id = None

                        self.slot_id = YList(self)
                        self._segment_path = lambda: "rack-id" + "[rack-id='" + str(self.rack_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CrossSdrIntfMa.Nodes.Node.RackIds.RackId, ['rack_id'], name, value)


                    class SlotId(Entity):
                        """
                        NodeInfo for a NodeId
                        
                        .. attribute:: slot_id  (key)
                        
                        	Slot Id
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: rack_slot_id
                        
                        	Rack slot ID
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: node_id
                        
                        	Node id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: node_up
                        
                        	Node up flag
                        	**type**\: bool
                        
                        .. attribute:: slice_arr
                        
                        	Slice array associated with node
                        	**type**\: list of  		 :py:class:`SliceArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.RackIds.RackId.SlotId.SliceArr>`
                        
                        

                        """

                        _prefix = 'cofo-csi-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(CrossSdrIntfMa.Nodes.Node.RackIds.RackId.SlotId, self).__init__()

                            self.yang_name = "slot-id"
                            self.yang_parent_name = "rack-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['slot_id']
                            self._child_classes = OrderedDict([("slice-arr", ("slice_arr", CrossSdrIntfMa.Nodes.Node.RackIds.RackId.SlotId.SliceArr))])
                            self._leafs = OrderedDict([
                                ('slot_id', YLeaf(YType.uint32, 'slot-id')),
                                ('rack_slot_id', YLeaf(YType.uint64, 'rack-slot-id')),
                                ('node_id', YLeaf(YType.uint32, 'node-id')),
                                ('node_up', YLeaf(YType.boolean, 'node-up')),
                            ])
                            self.slot_id = None
                            self.rack_slot_id = None
                            self.node_id = None
                            self.node_up = None

                            self.slice_arr = YList(self)
                            self._segment_path = lambda: "slot-id" + "[slot-id='" + str(self.slot_id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(CrossSdrIntfMa.Nodes.Node.RackIds.RackId.SlotId, ['slot_id', u'rack_slot_id', u'node_id', u'node_up'], name, value)


                        class SliceArr(Entity):
                            """
                            Slice array associated with node
                            
                            .. attribute:: slice_node_id
                            
                            	Slice Node ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: admin_up
                            
                            	Admin state UP flag
                            	**type**\: bool
                            
                            .. attribute:: oper_up
                            
                            	Oper state UP flag
                            	**type**\: bool
                            
                            .. attribute:: pic
                            
                            	PIC value
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: csi_pic_arr
                            
                            	CSI PIC array
                            	**type**\: list of int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'cofo-csi-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossSdrIntfMa.Nodes.Node.RackIds.RackId.SlotId.SliceArr, self).__init__()

                                self.yang_name = "slice-arr"
                                self.yang_parent_name = "slot-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('slice_node_id', YLeaf(YType.uint32, 'slice-node-id')),
                                    ('admin_up', YLeaf(YType.boolean, 'admin-up')),
                                    ('oper_up', YLeaf(YType.boolean, 'oper-up')),
                                    ('pic', YLeaf(YType.uint64, 'pic')),
                                    ('csi_pic_arr', YLeafList(YType.uint64, 'csi-pic-arr')),
                                ])
                                self.slice_node_id = None
                                self.admin_up = None
                                self.oper_up = None
                                self.pic = None
                                self.csi_pic_arr = []
                                self._segment_path = lambda: "slice-arr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossSdrIntfMa.Nodes.Node.RackIds.RackId.SlotId.SliceArr, [u'slice_node_id', u'admin_up', u'oper_up', u'pic', u'csi_pic_arr'], name, value)


            class CsiIndexes(Entity):
                """
                Admin data for csi\-index
                
                .. attribute:: csi_index
                
                	Admin data for a csi\-index
                	**type**\: list of  		 :py:class:`CsiIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.CsiIndexes.CsiIndex>`
                
                

                """

                _prefix = 'cofo-csi-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(CrossSdrIntfMa.Nodes.Node.CsiIndexes, self).__init__()

                    self.yang_name = "csi-indexes"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("csi-index", ("csi_index", CrossSdrIntfMa.Nodes.Node.CsiIndexes.CsiIndex))])
                    self._leafs = OrderedDict()

                    self.csi_index = YList(self)
                    self._segment_path = lambda: "csi-indexes"

                def __setattr__(self, name, value):
                    self._perform_setattr(CrossSdrIntfMa.Nodes.Node.CsiIndexes, [], name, value)


                class CsiIndex(Entity):
                    """
                    Admin data for a csi\-index
                    
                    .. attribute:: csi_index  (key)
                    
                    	CSI Index
                    	**type**\: int
                    
                    	**range:** 1..15
                    
                    .. attribute:: csi_index_xr
                    
                    	CSI Index
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sdr_id
                    
                    	Local SDR ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_sdr_id
                    
                    	Peer SDR ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_sdr_name
                    
                    	Peer SDR name
                    	**type**\: str
                    
                    .. attribute:: item_state
                    
                    	Item State
                    	**type**\:  :py:class:`CsiMaItemState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CsiMaItemState>`
                    
                    .. attribute:: csi_helper_reg
                    
                    	CSI Helper reg flag
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'cofo-csi-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CrossSdrIntfMa.Nodes.Node.CsiIndexes.CsiIndex, self).__init__()

                        self.yang_name = "csi-index"
                        self.yang_parent_name = "csi-indexes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['csi_index']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('csi_index', YLeaf(YType.uint32, 'csi-index')),
                            ('csi_index_xr', YLeaf(YType.uint32, 'csi-index-xr')),
                            ('sdr_id', YLeaf(YType.uint32, 'sdr-id')),
                            ('peer_sdr_id', YLeaf(YType.uint32, 'peer-sdr-id')),
                            ('peer_sdr_name', YLeaf(YType.str, 'peer-sdr-name')),
                            ('item_state', YLeaf(YType.enumeration, 'item-state')),
                            ('csi_helper_reg', YLeaf(YType.boolean, 'csi-helper-reg')),
                        ])
                        self.csi_index = None
                        self.csi_index_xr = None
                        self.sdr_id = None
                        self.peer_sdr_id = None
                        self.peer_sdr_name = None
                        self.item_state = None
                        self.csi_helper_reg = None
                        self._segment_path = lambda: "csi-index" + "[csi-index='" + str(self.csi_index) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CrossSdrIntfMa.Nodes.Node.CsiIndexes.CsiIndex, ['csi_index', u'csi_index_xr', u'sdr_id', u'peer_sdr_id', u'peer_sdr_name', u'item_state', u'csi_helper_reg'], name, value)


            class InterfaceNames(Entity):
                """
                Interface data for csi interfaces
                
                .. attribute:: interface_name
                
                	Interface data for an Interface
                	**type**\: list of  		 :py:class:`InterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName>`
                
                

                """

                _prefix = 'cofo-csi-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(CrossSdrIntfMa.Nodes.Node.InterfaceNames, self).__init__()

                    self.yang_name = "interface-names"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-name", ("interface_name", CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName))])
                    self._leafs = OrderedDict()

                    self.interface_name = YList(self)
                    self._segment_path = lambda: "interface-names"

                def __setattr__(self, name, value):
                    self._perform_setattr(CrossSdrIntfMa.Nodes.Node.InterfaceNames, [], name, value)


                class InterfaceName(Entity):
                    """
                    Interface data for an Interface
                    
                    .. attribute:: csi_index  (key)
                    
                    	CSI Index
                    	**type**\: int
                    
                    	**range:** 1..15
                    
                    .. attribute:: pub_data
                    
                    	Remote published data
                    	**type**\:  :py:class:`PubData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PubData>`
                    
                    .. attribute:: name
                    
                    	Interface name
                    	**type**\: str
                    
                    .. attribute:: handle
                    
                    	Interface handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: csi_index_xr
                    
                    	CSI Index
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sdr_id
                    
                    	SDR ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_sdr_id
                    
                    	Peer SDR ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: repl_handle
                    
                    	Replication handle
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: repl_fail_count
                    
                    	Replication fail count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: item_state
                    
                    	Item state
                    	**type**\:  :py:class:`CsiMaItemState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CsiMaItemState>`
                    
                    .. attribute:: if_state
                    
                    	Interface state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rem_slice_attr
                    
                    	Rem slice attribute
                    	**type**\: bool
                    
                    .. attribute:: rem_ip_attr
                    
                    	Rem IP attribute
                    	**type**\: bool
                    
                    .. attribute:: local_ip_arr
                    
                    	Local IP addresses
                    	**type**\: list of  		 :py:class:`LocalIpArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.LocalIpArr>`
                    
                    .. attribute:: peer_ip_arr
                    
                    	Peer IP addresses
                    	**type**\: list of  		 :py:class:`PeerIpArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PeerIpArr>`
                    
                    

                    """

                    _prefix = 'cofo-csi-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName, self).__init__()

                        self.yang_name = "interface-name"
                        self.yang_parent_name = "interface-names"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['csi_index']
                        self._child_classes = OrderedDict([("pub-data", ("pub_data", CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PubData)), ("local-ip-arr", ("local_ip_arr", CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.LocalIpArr)), ("peer-ip-arr", ("peer_ip_arr", CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PeerIpArr))])
                        self._leafs = OrderedDict([
                            ('csi_index', YLeaf(YType.uint32, 'csi-index')),
                            ('name', YLeaf(YType.str, 'name')),
                            ('handle', YLeaf(YType.str, 'handle')),
                            ('csi_index_xr', YLeaf(YType.uint32, 'csi-index-xr')),
                            ('sdr_id', YLeaf(YType.uint32, 'sdr-id')),
                            ('peer_sdr_id', YLeaf(YType.uint32, 'peer-sdr-id')),
                            ('repl_handle', YLeaf(YType.uint32, 'repl-handle')),
                            ('repl_fail_count', YLeaf(YType.uint32, 'repl-fail-count')),
                            ('item_state', YLeaf(YType.enumeration, 'item-state')),
                            ('if_state', YLeaf(YType.uint32, 'if-state')),
                            ('rem_slice_attr', YLeaf(YType.boolean, 'rem-slice-attr')),
                            ('rem_ip_attr', YLeaf(YType.boolean, 'rem-ip-attr')),
                        ])
                        self.csi_index = None
                        self.name = None
                        self.handle = None
                        self.csi_index_xr = None
                        self.sdr_id = None
                        self.peer_sdr_id = None
                        self.repl_handle = None
                        self.repl_fail_count = None
                        self.item_state = None
                        self.if_state = None
                        self.rem_slice_attr = None
                        self.rem_ip_attr = None

                        self.pub_data = CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PubData()
                        self.pub_data.parent = self
                        self._children_name_map["pub_data"] = "pub-data"

                        self.local_ip_arr = YList(self)
                        self.peer_ip_arr = YList(self)
                        self._segment_path = lambda: "interface-name" + "[csi-index='" + str(self.csi_index) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName, ['csi_index', u'name', u'handle', u'csi_index_xr', u'sdr_id', u'peer_sdr_id', u'repl_handle', u'repl_fail_count', u'item_state', u'if_state', u'rem_slice_attr', u'rem_ip_attr'], name, value)


                    class PubData(Entity):
                        """
                        Remote published data
                        
                        .. attribute:: csi_pic_arr
                        
                        	CSI PIC Array
                        	**type**\: list of int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: csi_info_arr
                        
                        	CSI Index \- IP Array
                        	**type**\: list of  		 :py:class:`CsiInfoArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PubData.CsiInfoArr>`
                        
                        

                        """

                        _prefix = 'cofo-csi-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PubData, self).__init__()

                            self.yang_name = "pub-data"
                            self.yang_parent_name = "interface-name"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("csi-info-arr", ("csi_info_arr", CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PubData.CsiInfoArr))])
                            self._leafs = OrderedDict([
                                ('csi_pic_arr', YLeafList(YType.uint64, 'csi-pic-arr')),
                            ])
                            self.csi_pic_arr = []

                            self.csi_info_arr = YList(self)
                            self._segment_path = lambda: "pub-data"

                        def __setattr__(self, name, value):
                            self._perform_setattr(CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PubData, [u'csi_pic_arr'], name, value)


                        class CsiInfoArr(Entity):
                            """
                            CSI Index \- IP Array
                            
                            .. attribute:: csi_index
                            
                            	CSI Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ip_arr
                            
                            	CSI IP Array
                            	**type**\: list of  		 :py:class:`IpArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PubData.CsiInfoArr.IpArr>`
                            
                            

                            """

                            _prefix = 'cofo-csi-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PubData.CsiInfoArr, self).__init__()

                                self.yang_name = "csi-info-arr"
                                self.yang_parent_name = "pub-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("ip-arr", ("ip_arr", CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PubData.CsiInfoArr.IpArr))])
                                self._leafs = OrderedDict([
                                    ('csi_index', YLeaf(YType.uint32, 'csi-index')),
                                ])
                                self.csi_index = None

                                self.ip_arr = YList(self)
                                self._segment_path = lambda: "csi-info-arr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PubData.CsiInfoArr, [u'csi_index'], name, value)


                            class IpArr(Entity):
                                """
                                CSI IP Array
                                
                                .. attribute:: af
                                
                                	AF
                                	**type**\:  :py:class:`CsiMaAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CsiMaAfi>`
                                
                                .. attribute:: ipv4
                                
                                	IPv4
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6
                                
                                	IPv6
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'cofo-csi-ma-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PubData.CsiInfoArr.IpArr, self).__init__()

                                    self.yang_name = "ip-arr"
                                    self.yang_parent_name = "csi-info-arr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('af', YLeaf(YType.enumeration, 'af')),
                                        ('ipv4', YLeaf(YType.str, 'ipv4')),
                                        ('ipv6', YLeaf(YType.str, 'ipv6')),
                                    ])
                                    self.af = None
                                    self.ipv4 = None
                                    self.ipv6 = None
                                    self._segment_path = lambda: "ip-arr"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PubData.CsiInfoArr.IpArr, [u'af', u'ipv4', u'ipv6'], name, value)


                    class LocalIpArr(Entity):
                        """
                        Local IP addresses
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:  :py:class:`CsiMaAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CsiMaAfi>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'cofo-csi-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.LocalIpArr, self).__init__()

                            self.yang_name = "local-ip-arr"
                            self.yang_parent_name = "interface-name"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af', YLeaf(YType.enumeration, 'af')),
                                ('ipv4', YLeaf(YType.str, 'ipv4')),
                                ('ipv6', YLeaf(YType.str, 'ipv6')),
                            ])
                            self.af = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "local-ip-arr"

                        def __setattr__(self, name, value):
                            self._perform_setattr(CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.LocalIpArr, [u'af', u'ipv4', u'ipv6'], name, value)


                    class PeerIpArr(Entity):
                        """
                        Peer IP addresses
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:  :py:class:`CsiMaAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CsiMaAfi>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'cofo-csi-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PeerIpArr, self).__init__()

                            self.yang_name = "peer-ip-arr"
                            self.yang_parent_name = "interface-name"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af', YLeaf(YType.enumeration, 'af')),
                                ('ipv4', YLeaf(YType.str, 'ipv4')),
                                ('ipv6', YLeaf(YType.str, 'ipv6')),
                            ])
                            self.af = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "peer-ip-arr"

                        def __setattr__(self, name, value):
                            self._perform_setattr(CrossSdrIntfMa.Nodes.Node.InterfaceNames.InterfaceName.PeerIpArr, [u'af', u'ipv4', u'ipv6'], name, value)


            class Global(Entity):
                """
                Global data associated with csi\-ma
                
                .. attribute:: invmgr_conn_state
                
                	Inventory manager connection state
                	**type**\:  :py:class:`CsiMaConnState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CsiMaConnState>`
                
                .. attribute:: fail_over_timer_state
                
                	Fail Over Timer state for remote data
                	**type**\:  :py:class:`CsiMaFoTimerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CsiMaFoTimerState>`
                
                .. attribute:: own_im_conn_state
                
                	Owner channel IM connection state
                	**type**\:  :py:class:`CsiMaConnState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CsiMaConnState>`
                
                .. attribute:: gdp_im_conn_state
                
                	GDP IM connection state
                	**type**\:  :py:class:`CsiMaConnState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CsiMaConnState>`
                
                .. attribute:: l3p_im_conn_state
                
                	L3P IM connection state
                	**type**\:  :py:class:`CsiMaConnState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CsiMaConnState>`
                
                

                """

                _prefix = 'cofo-csi-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(CrossSdrIntfMa.Nodes.Node.Global, self).__init__()

                    self.yang_name = "global"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('invmgr_conn_state', YLeaf(YType.enumeration, 'invmgr-conn-state')),
                        ('fail_over_timer_state', YLeaf(YType.enumeration, 'fail-over-timer-state')),
                        ('own_im_conn_state', YLeaf(YType.enumeration, 'own-im-conn-state')),
                        ('gdp_im_conn_state', YLeaf(YType.enumeration, 'gdp-im-conn-state')),
                        ('l3p_im_conn_state', YLeaf(YType.enumeration, 'l3p-im-conn-state')),
                    ])
                    self.invmgr_conn_state = None
                    self.fail_over_timer_state = None
                    self.own_im_conn_state = None
                    self.gdp_im_conn_state = None
                    self.l3p_im_conn_state = None
                    self._segment_path = lambda: "global"

                def __setattr__(self, name, value):
                    self._perform_setattr(CrossSdrIntfMa.Nodes.Node.Global, [u'invmgr_conn_state', u'fail_over_timer_state', u'own_im_conn_state', u'gdp_im_conn_state', u'l3p_im_conn_state'], name, value)


            class SdrIds(Entity):
                """
                Remote data for SDR ID
                
                .. attribute:: sdr_id
                
                	Remote data for sdr\-id
                	**type**\: list of  		 :py:class:`SdrId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId>`
                
                

                """

                _prefix = 'cofo-csi-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(CrossSdrIntfMa.Nodes.Node.SdrIds, self).__init__()

                    self.yang_name = "sdr-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("sdr-id", ("sdr_id", CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId))])
                    self._leafs = OrderedDict()

                    self.sdr_id = YList(self)
                    self._segment_path = lambda: "sdr-ids"

                def __setattr__(self, name, value):
                    self._perform_setattr(CrossSdrIntfMa.Nodes.Node.SdrIds, [], name, value)


                class SdrId(Entity):
                    """
                    Remote data for sdr\-id
                    
                    .. attribute:: sdr_id  (key)
                    
                    	Sdr Id
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: pub_data
                    
                    	Published data
                    	**type**\:  :py:class:`PubData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId.PubData>`
                    
                    .. attribute:: sdr_id_xr
                    
                    	SDR ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: item_state
                    
                    	Remote data entry state
                    	**type**\:  :py:class:`CsiMaItemState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CsiMaItemState>`
                    
                    

                    """

                    _prefix = 'cofo-csi-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId, self).__init__()

                        self.yang_name = "sdr-id"
                        self.yang_parent_name = "sdr-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sdr_id']
                        self._child_classes = OrderedDict([("pub-data", ("pub_data", CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId.PubData))])
                        self._leafs = OrderedDict([
                            ('sdr_id', YLeaf(YType.uint32, 'sdr-id')),
                            ('sdr_id_xr', YLeaf(YType.uint32, 'sdr-id-xr')),
                            ('item_state', YLeaf(YType.enumeration, 'item-state')),
                        ])
                        self.sdr_id = None
                        self.sdr_id_xr = None
                        self.item_state = None

                        self.pub_data = CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId.PubData()
                        self.pub_data.parent = self
                        self._children_name_map["pub_data"] = "pub-data"
                        self._segment_path = lambda: "sdr-id" + "[sdr-id='" + str(self.sdr_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId, ['sdr_id', u'sdr_id_xr', u'item_state'], name, value)


                    class PubData(Entity):
                        """
                        Published data
                        
                        .. attribute:: csi_pic_arr
                        
                        	CSI PIC Array
                        	**type**\: list of int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: csi_info_arr
                        
                        	CSI Index \- IP Array
                        	**type**\: list of  		 :py:class:`CsiInfoArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId.PubData.CsiInfoArr>`
                        
                        

                        """

                        _prefix = 'cofo-csi-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId.PubData, self).__init__()

                            self.yang_name = "pub-data"
                            self.yang_parent_name = "sdr-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("csi-info-arr", ("csi_info_arr", CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId.PubData.CsiInfoArr))])
                            self._leafs = OrderedDict([
                                ('csi_pic_arr', YLeafList(YType.uint64, 'csi-pic-arr')),
                            ])
                            self.csi_pic_arr = []

                            self.csi_info_arr = YList(self)
                            self._segment_path = lambda: "pub-data"

                        def __setattr__(self, name, value):
                            self._perform_setattr(CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId.PubData, [u'csi_pic_arr'], name, value)


                        class CsiInfoArr(Entity):
                            """
                            CSI Index \- IP Array
                            
                            .. attribute:: csi_index
                            
                            	CSI Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ip_arr
                            
                            	CSI IP Array
                            	**type**\: list of  		 :py:class:`IpArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId.PubData.CsiInfoArr.IpArr>`
                            
                            

                            """

                            _prefix = 'cofo-csi-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId.PubData.CsiInfoArr, self).__init__()

                                self.yang_name = "csi-info-arr"
                                self.yang_parent_name = "pub-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("ip-arr", ("ip_arr", CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId.PubData.CsiInfoArr.IpArr))])
                                self._leafs = OrderedDict([
                                    ('csi_index', YLeaf(YType.uint32, 'csi-index')),
                                ])
                                self.csi_index = None

                                self.ip_arr = YList(self)
                                self._segment_path = lambda: "csi-info-arr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId.PubData.CsiInfoArr, [u'csi_index'], name, value)


                            class IpArr(Entity):
                                """
                                CSI IP Array
                                
                                .. attribute:: af
                                
                                	AF
                                	**type**\:  :py:class:`CsiMaAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_csi_ma_oper.CsiMaAfi>`
                                
                                .. attribute:: ipv4
                                
                                	IPv4
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6
                                
                                	IPv6
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'cofo-csi-ma-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId.PubData.CsiInfoArr.IpArr, self).__init__()

                                    self.yang_name = "ip-arr"
                                    self.yang_parent_name = "csi-info-arr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('af', YLeaf(YType.enumeration, 'af')),
                                        ('ipv4', YLeaf(YType.str, 'ipv4')),
                                        ('ipv6', YLeaf(YType.str, 'ipv6')),
                                    ])
                                    self.af = None
                                    self.ipv4 = None
                                    self.ipv6 = None
                                    self._segment_path = lambda: "ip-arr"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(CrossSdrIntfMa.Nodes.Node.SdrIds.SdrId.PubData.CsiInfoArr.IpArr, [u'af', u'ipv4', u'ipv6'], name, value)

    def clone_ptr(self):
        self._top_entity = CrossSdrIntfMa()
        return self._top_entity


""" Cisco_IOS_XR_cofo_infra_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR cofo\-infra package operational data.

This module contains definitions
for the following management objects\:
  cofo\: COFO operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Cofo(Entity):
    """
    COFO operational data
    
    .. attribute:: nodes
    
    	Node\-specific COFO operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_infra_oper.Cofo.Nodes>`
    
    

    """

    _prefix = 'cofo-infra-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Cofo, self).__init__()
        self._top_entity = None

        self.yang_name = "cofo"
        self.yang_parent_name = "Cisco-IOS-XR-cofo-infra-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Cofo.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Cofo.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-cofo-infra-oper:cofo"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Cofo, [], name, value)


    class Nodes(Entity):
        """
        Node\-specific COFO operational data
        
        .. attribute:: node
        
        	COFO operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_infra_oper.Cofo.Nodes.Node>`
        
        

        """

        _prefix = 'cofo-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Cofo.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "cofo"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Cofo.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-cofo-infra-oper:cofo/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Cofo.Nodes, [], name, value)


        class Node(Entity):
            """
            COFO operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	The node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: client_ids
            
            	COFO Client data
            	**type**\:  :py:class:`ClientIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_infra_oper.Cofo.Nodes.Node.ClientIds>`
            
            .. attribute:: topic_ids
            
            	COFO SDR database
            	**type**\:  :py:class:`TopicIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_infra_oper.Cofo.Nodes.Node.TopicIds>`
            
            

            """

            _prefix = 'cofo-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Cofo.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("client-ids", ("client_ids", Cofo.Nodes.Node.ClientIds)), ("topic-ids", ("topic_ids", Cofo.Nodes.Node.TopicIds))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.client_ids = Cofo.Nodes.Node.ClientIds()
                self.client_ids.parent = self
                self._children_name_map["client_ids"] = "client-ids"

                self.topic_ids = Cofo.Nodes.Node.TopicIds()
                self.topic_ids.parent = self
                self._children_name_map["topic_ids"] = "topic-ids"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-cofo-infra-oper:cofo/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Cofo.Nodes.Node, ['node_name'], name, value)


            class ClientIds(Entity):
                """
                COFO Client data
                
                .. attribute:: client_id
                
                	COFO client id
                	**type**\: list of  		 :py:class:`ClientId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_infra_oper.Cofo.Nodes.Node.ClientIds.ClientId>`
                
                

                """

                _prefix = 'cofo-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Cofo.Nodes.Node.ClientIds, self).__init__()

                    self.yang_name = "client-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("client-id", ("client_id", Cofo.Nodes.Node.ClientIds.ClientId))])
                    self._leafs = OrderedDict()

                    self.client_id = YList(self)
                    self._segment_path = lambda: "client-ids"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cofo.Nodes.Node.ClientIds, [], name, value)


                class ClientId(Entity):
                    """
                    COFO client id
                    
                    .. attribute:: id  (key)
                    
                    	Specific Client identifier
                    	**type**\: int
                    
                    	**range:** 1..7
                    
                    .. attribute:: connection_handle
                    
                    	Connection Handle
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_handle
                    
                    	Peer Handle
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: client_id
                    
                    	Client ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: purge_timeout
                    
                    	Purge timeout
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: host_client
                    
                    	host client
                    	**type**\: bool
                    
                    .. attribute:: connection_state
                    
                    	Connection state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: topic_subscribed
                    
                    	Topic Subscribed
                    	**type**\: list of int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: topic_published
                    
                    	Topic Published
                    	**type**\: list of int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'cofo-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Cofo.Nodes.Node.ClientIds.ClientId, self).__init__()

                        self.yang_name = "client-id"
                        self.yang_parent_name = "client-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('connection_handle', (YLeaf(YType.uint32, 'connection-handle'), ['int'])),
                            ('peer_handle', (YLeaf(YType.uint32, 'peer-handle'), ['int'])),
                            ('client_id', (YLeaf(YType.uint32, 'client-id'), ['int'])),
                            ('purge_timeout', (YLeaf(YType.uint32, 'purge-timeout'), ['int'])),
                            ('host_client', (YLeaf(YType.boolean, 'host-client'), ['bool'])),
                            ('connection_state', (YLeaf(YType.uint32, 'connection-state'), ['int'])),
                            ('topic_subscribed', (YLeafList(YType.uint32, 'topic-subscribed'), ['int'])),
                            ('topic_published', (YLeafList(YType.uint32, 'topic-published'), ['int'])),
                        ])
                        self.id = None
                        self.connection_handle = None
                        self.peer_handle = None
                        self.client_id = None
                        self.purge_timeout = None
                        self.host_client = None
                        self.connection_state = None
                        self.topic_subscribed = []
                        self.topic_published = []
                        self._segment_path = lambda: "client-id" + "[id='" + str(self.id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cofo.Nodes.Node.ClientIds.ClientId, ['id', 'connection_handle', 'peer_handle', 'client_id', 'purge_timeout', 'host_client', 'connection_state', 'topic_subscribed', 'topic_published'], name, value)


            class TopicIds(Entity):
                """
                COFO SDR database
                
                .. attribute:: topic_id
                
                	COFO topic id
                	**type**\: list of  		 :py:class:`TopicId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_infra_oper.Cofo.Nodes.Node.TopicIds.TopicId>`
                
                

                """

                _prefix = 'cofo-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Cofo.Nodes.Node.TopicIds, self).__init__()

                    self.yang_name = "topic-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("topic-id", ("topic_id", Cofo.Nodes.Node.TopicIds.TopicId))])
                    self._leafs = OrderedDict()

                    self.topic_id = YList(self)
                    self._segment_path = lambda: "topic-ids"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cofo.Nodes.Node.TopicIds, [], name, value)


                class TopicId(Entity):
                    """
                    COFO topic id
                    
                    .. attribute:: id  (key)
                    
                    	Specific Topic identifier
                    	**type**\: int
                    
                    	**range:** 1..8
                    
                    .. attribute:: topic_id
                    
                    	Topic ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: database_info_struct
                    
                    	Database info struct
                    	**type**\: list of  		 :py:class:`DatabaseInfoStruct <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_infra_oper.Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct>`
                    
                    

                    """

                    _prefix = 'cofo-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Cofo.Nodes.Node.TopicIds.TopicId, self).__init__()

                        self.yang_name = "topic-id"
                        self.yang_parent_name = "topic-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['id']
                        self._child_classes = OrderedDict([("database-info-struct", ("database_info_struct", Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct))])
                        self._leafs = OrderedDict([
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('topic_id', (YLeaf(YType.uint32, 'topic-id'), ['int'])),
                        ])
                        self.id = None
                        self.topic_id = None

                        self.database_info_struct = YList(self)
                        self._segment_path = lambda: "topic-id" + "[id='" + str(self.id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cofo.Nodes.Node.TopicIds.TopicId, ['id', 'topic_id'], name, value)


                    class DatabaseInfoStruct(Entity):
                        """
                        Database info struct
                        
                        .. attribute:: sdr_id
                        
                        	SDR ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: client_db_info_struct
                        
                        	Client db info struct
                        	**type**\: list of  		 :py:class:`ClientDbInfoStruct <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_infra_oper.Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct>`
                        
                        

                        """

                        _prefix = 'cofo-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct, self).__init__()

                            self.yang_name = "database-info-struct"
                            self.yang_parent_name = "topic-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("client-db-info-struct", ("client_db_info_struct", Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct))])
                            self._leafs = OrderedDict([
                                ('sdr_id', (YLeaf(YType.uint32, 'sdr-id'), ['int'])),
                            ])
                            self.sdr_id = None

                            self.client_db_info_struct = YList(self)
                            self._segment_path = lambda: "database-info-struct"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct, ['sdr_id'], name, value)


                        class ClientDbInfoStruct(Entity):
                            """
                            Client db info struct
                            
                            .. attribute:: total_objects
                            
                            	Total objects
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_valid_items_in_db
                            
                            	Total valid items in db
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cofo_object_published_array
                            
                            	Cofo object published array
                            	**type**\: list of  		 :py:class:`CofoObjectPublishedArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_infra_oper.Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray>`
                            
                            

                            """

                            _prefix = 'cofo-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct, self).__init__()

                                self.yang_name = "client-db-info-struct"
                                self.yang_parent_name = "database-info-struct"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("cofo-object-published-array", ("cofo_object_published_array", Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray))])
                                self._leafs = OrderedDict([
                                    ('total_objects', (YLeaf(YType.uint32, 'total-objects'), ['int'])),
                                    ('total_valid_items_in_db', (YLeaf(YType.uint32, 'total-valid-items-in-db'), ['int'])),
                                ])
                                self.total_objects = None
                                self.total_valid_items_in_db = None

                                self.cofo_object_published_array = YList(self)
                                self._segment_path = lambda: "client-db-info-struct"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct, ['total_objects', 'total_valid_items_in_db'], name, value)


                            class CofoObjectPublishedArray(Entity):
                                """
                                Cofo object published array
                                
                                .. attribute:: object_add_time
                                
                                	Cofo object add time
                                	**type**\:  :py:class:`ObjectAddTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_infra_oper.Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectAddTime>`
                                
                                .. attribute:: object_delete_time
                                
                                	Cofo object delete time
                                	**type**\:  :py:class:`ObjectDeleteTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_infra_oper.Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectDeleteTime>`
                                
                                .. attribute:: object_txl_add_time
                                
                                	Cofo object txl add time
                                	**type**\:  :py:class:`ObjectTxlAddTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_infra_oper.Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectTxlAddTime>`
                                
                                .. attribute:: object_txl_encode_time
                                
                                	Cofo object txl encode time
                                	**type**\:  :py:class:`ObjectTxlEncodeTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cofo_infra_oper.Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectTxlEncodeTime>`
                                
                                .. attribute:: client_id
                                
                                	Client ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: object_id
                                
                                	Object ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: insert_count
                                
                                	Insert Count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: item_state
                                
                                	Item State
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: cofo_infra_object_key
                                
                                	Cofo infra object key
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: cofo_infra_object_value
                                
                                	Cofo infra object value
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                

                                """

                                _prefix = 'cofo-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray, self).__init__()

                                    self.yang_name = "cofo-object-published-array"
                                    self.yang_parent_name = "client-db-info-struct"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("object-add-time", ("object_add_time", Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectAddTime)), ("object-delete-time", ("object_delete_time", Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectDeleteTime)), ("object-txl-add-time", ("object_txl_add_time", Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectTxlAddTime)), ("object-txl-encode-time", ("object_txl_encode_time", Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectTxlEncodeTime))])
                                    self._leafs = OrderedDict([
                                        ('client_id', (YLeaf(YType.uint32, 'client-id'), ['int'])),
                                        ('object_id', (YLeaf(YType.uint32, 'object-id'), ['int'])),
                                        ('insert_count', (YLeaf(YType.uint32, 'insert-count'), ['int'])),
                                        ('item_state', (YLeaf(YType.uint32, 'item-state'), ['int'])),
                                        ('cofo_infra_object_key', (YLeaf(YType.str, 'cofo-infra-object-key'), ['str'])),
                                        ('cofo_infra_object_value', (YLeaf(YType.str, 'cofo-infra-object-value'), ['str'])),
                                    ])
                                    self.client_id = None
                                    self.object_id = None
                                    self.insert_count = None
                                    self.item_state = None
                                    self.cofo_infra_object_key = None
                                    self.cofo_infra_object_value = None

                                    self.object_add_time = Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectAddTime()
                                    self.object_add_time.parent = self
                                    self._children_name_map["object_add_time"] = "object-add-time"

                                    self.object_delete_time = Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectDeleteTime()
                                    self.object_delete_time.parent = self
                                    self._children_name_map["object_delete_time"] = "object-delete-time"

                                    self.object_txl_add_time = Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectTxlAddTime()
                                    self.object_txl_add_time.parent = self
                                    self._children_name_map["object_txl_add_time"] = "object-txl-add-time"

                                    self.object_txl_encode_time = Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectTxlEncodeTime()
                                    self.object_txl_encode_time.parent = self
                                    self._children_name_map["object_txl_encode_time"] = "object-txl-encode-time"
                                    self._segment_path = lambda: "cofo-object-published-array"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray, ['client_id', 'object_id', 'insert_count', 'item_state', 'cofo_infra_object_key', 'cofo_infra_object_value'], name, value)


                                class ObjectAddTime(Entity):
                                    """
                                    Cofo object add time
                                    
                                    .. attribute:: tv_sec
                                    
                                    	tv sec
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: tv_nsec
                                    
                                    	tv nsec
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'cofo-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectAddTime, self).__init__()

                                        self.yang_name = "object-add-time"
                                        self.yang_parent_name = "cofo-object-published-array"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('tv_sec', (YLeaf(YType.uint32, 'tv-sec'), ['int'])),
                                            ('tv_nsec', (YLeaf(YType.uint32, 'tv-nsec'), ['int'])),
                                        ])
                                        self.tv_sec = None
                                        self.tv_nsec = None
                                        self._segment_path = lambda: "object-add-time"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectAddTime, ['tv_sec', 'tv_nsec'], name, value)


                                class ObjectDeleteTime(Entity):
                                    """
                                    Cofo object delete time
                                    
                                    .. attribute:: tv_sec
                                    
                                    	tv sec
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: tv_nsec
                                    
                                    	tv nsec
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'cofo-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectDeleteTime, self).__init__()

                                        self.yang_name = "object-delete-time"
                                        self.yang_parent_name = "cofo-object-published-array"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('tv_sec', (YLeaf(YType.uint32, 'tv-sec'), ['int'])),
                                            ('tv_nsec', (YLeaf(YType.uint32, 'tv-nsec'), ['int'])),
                                        ])
                                        self.tv_sec = None
                                        self.tv_nsec = None
                                        self._segment_path = lambda: "object-delete-time"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectDeleteTime, ['tv_sec', 'tv_nsec'], name, value)


                                class ObjectTxlAddTime(Entity):
                                    """
                                    Cofo object txl add time
                                    
                                    .. attribute:: tv_sec
                                    
                                    	tv sec
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: tv_nsec
                                    
                                    	tv nsec
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'cofo-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectTxlAddTime, self).__init__()

                                        self.yang_name = "object-txl-add-time"
                                        self.yang_parent_name = "cofo-object-published-array"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('tv_sec', (YLeaf(YType.uint32, 'tv-sec'), ['int'])),
                                            ('tv_nsec', (YLeaf(YType.uint32, 'tv-nsec'), ['int'])),
                                        ])
                                        self.tv_sec = None
                                        self.tv_nsec = None
                                        self._segment_path = lambda: "object-txl-add-time"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectTxlAddTime, ['tv_sec', 'tv_nsec'], name, value)


                                class ObjectTxlEncodeTime(Entity):
                                    """
                                    Cofo object txl encode time
                                    
                                    .. attribute:: tv_sec
                                    
                                    	tv sec
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: tv_nsec
                                    
                                    	tv nsec
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'cofo-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectTxlEncodeTime, self).__init__()

                                        self.yang_name = "object-txl-encode-time"
                                        self.yang_parent_name = "cofo-object-published-array"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('tv_sec', (YLeaf(YType.uint32, 'tv-sec'), ['int'])),
                                            ('tv_nsec', (YLeaf(YType.uint32, 'tv-nsec'), ['int'])),
                                        ])
                                        self.tv_sec = None
                                        self.tv_nsec = None
                                        self._segment_path = lambda: "object-txl-encode-time"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Cofo.Nodes.Node.TopicIds.TopicId.DatabaseInfoStruct.ClientDbInfoStruct.CofoObjectPublishedArray.ObjectTxlEncodeTime, ['tv_sec', 'tv_nsec'], name, value)

    def clone_ptr(self):
        self._top_entity = Cofo()
        return self._top_entity


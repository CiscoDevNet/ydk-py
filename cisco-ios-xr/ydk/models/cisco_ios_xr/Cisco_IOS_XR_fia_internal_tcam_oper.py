""" Cisco_IOS_XR_fia_internal_tcam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fia\-internal\-tcam package operational data.

This module contains definitions
for the following management objects\:
  controller\: Controller Resources

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Controller(Entity):
    """
    Controller Resources
    
    .. attribute:: dpa
    
    	Controller DPA operational data
    	**type**\:  :py:class:`Dpa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa>`
    
    

    """

    _prefix = 'fia-internal-tcam-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Controller, self).__init__()
        self._top_entity = None

        self.yang_name = "controller"
        self.yang_parent_name = "Cisco-IOS-XR-fia-internal-tcam-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("dpa", ("dpa", Controller.Dpa))])
        self._leafs = OrderedDict()

        self.dpa = Controller.Dpa()
        self.dpa.parent = self
        self._children_name_map["dpa"] = "dpa"
        self._segment_path = lambda: "Cisco-IOS-XR-fia-internal-tcam-oper:controller"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Controller, [], name, value)


    class Dpa(Entity):
        """
        Controller DPA operational data
        
        .. attribute:: nodes
        
        	DPA data for available nodes
        	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes>`
        
        

        """

        _prefix = 'fia-internal-tcam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Controller.Dpa, self).__init__()

            self.yang_name = "dpa"
            self.yang_parent_name = "controller"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nodes", ("nodes", Controller.Dpa.Nodes))])
            self._leafs = OrderedDict()

            self.nodes = Controller.Dpa.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._segment_path = lambda: "dpa"
            self._absolute_path = lambda: "Cisco-IOS-XR-fia-internal-tcam-oper:controller/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Controller.Dpa, [], name, value)


        class Nodes(Entity):
            """
            DPA data for available nodes
            
            .. attribute:: node
            
            	DPA operational data for a particular node
            	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node>`
            
            

            """

            _prefix = 'fia-internal-tcam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Controller.Dpa.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "dpa"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("node", ("node", Controller.Dpa.Nodes.Node))])
                self._leafs = OrderedDict()

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-internal-tcam-oper:controller/dpa/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Controller.Dpa.Nodes, [], name, value)


            class Node(Entity):
                """
                DPA operational data for a particular node
                
                .. attribute:: node_name  (key)
                
                	Node ID
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: external_tcam_resources
                
                	External TCAM Resource Information
                	**type**\:  :py:class:`ExternalTcamResources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.ExternalTcamResources>`
                
                .. attribute:: internal_tcam_resources
                
                	Internal TCAM Resource Information
                	**type**\:  :py:class:`InternalTcamResources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.InternalTcamResources>`
                
                

                """

                _prefix = 'fia-internal-tcam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Controller.Dpa.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['node_name']
                    self._child_classes = OrderedDict([("external-tcam-resources", ("external_tcam_resources", Controller.Dpa.Nodes.Node.ExternalTcamResources)), ("internal-tcam-resources", ("internal_tcam_resources", Controller.Dpa.Nodes.Node.InternalTcamResources))])
                    self._leafs = OrderedDict([
                        ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                    ])
                    self.node_name = None

                    self.external_tcam_resources = Controller.Dpa.Nodes.Node.ExternalTcamResources()
                    self.external_tcam_resources.parent = self
                    self._children_name_map["external_tcam_resources"] = "external-tcam-resources"

                    self.internal_tcam_resources = Controller.Dpa.Nodes.Node.InternalTcamResources()
                    self.internal_tcam_resources.parent = self
                    self._children_name_map["internal_tcam_resources"] = "internal-tcam-resources"
                    self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-internal-tcam-oper:controller/dpa/nodes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.Dpa.Nodes.Node, ['node_name'], name, value)


                class ExternalTcamResources(Entity):
                    """
                    External TCAM Resource Information
                    
                    .. attribute:: npu_tcam
                    
                    	npu tcam
                    	**type**\: list of  		 :py:class:`NpuTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam>`
                    
                    

                    """

                    _prefix = 'fia-internal-tcam-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Controller.Dpa.Nodes.Node.ExternalTcamResources, self).__init__()

                        self.yang_name = "external-tcam-resources"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("npu-tcam", ("npu_tcam", Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam))])
                        self._leafs = OrderedDict()

                        self.npu_tcam = YList(self)
                        self._segment_path = lambda: "external-tcam-resources"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Dpa.Nodes.Node.ExternalTcamResources, [], name, value)


                    class NpuTcam(Entity):
                        """
                        npu tcam
                        
                        .. attribute:: npu_id
                        
                        	npu id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tcam_bank
                        
                        	tcam bank
                        	**type**\: list of  		 :py:class:`TcamBank <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank>`
                        
                        

                        """

                        _prefix = 'fia-internal-tcam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam, self).__init__()

                            self.yang_name = "npu-tcam"
                            self.yang_parent_name = "external-tcam-resources"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("tcam-bank", ("tcam_bank", Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank))])
                            self._leafs = OrderedDict([
                                ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                            ])
                            self.npu_id = None

                            self.tcam_bank = YList(self)
                            self._segment_path = lambda: "npu-tcam"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam, ['npu_id'], name, value)


                        class TcamBank(Entity):
                            """
                            tcam bank
                            
                            .. attribute:: bank_id
                            
                            	bank id
                            	**type**\: str
                            
                            .. attribute:: bank_key_size
                            
                            	bank key size
                            	**type**\: str
                            
                            .. attribute:: bank_free_entries
                            
                            	bank free entries
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bank_inuse_entries
                            
                            	bank inuse entries
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: owner
                            
                            	owner
                            	**type**\: str
                            
                            .. attribute:: nof_dbs
                            
                            	nof dbs
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bank_db
                            
                            	bank db
                            	**type**\: list of  		 :py:class:`BankDb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank.BankDb>`
                            
                            

                            """

                            _prefix = 'fia-internal-tcam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank, self).__init__()

                                self.yang_name = "tcam-bank"
                                self.yang_parent_name = "npu-tcam"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("bank-db", ("bank_db", Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank.BankDb))])
                                self._leafs = OrderedDict([
                                    ('bank_id', (YLeaf(YType.str, 'bank-id'), ['str'])),
                                    ('bank_key_size', (YLeaf(YType.str, 'bank-key-size'), ['str'])),
                                    ('bank_free_entries', (YLeaf(YType.uint32, 'bank-free-entries'), ['int'])),
                                    ('bank_inuse_entries', (YLeaf(YType.uint32, 'bank-inuse-entries'), ['int'])),
                                    ('owner', (YLeaf(YType.str, 'owner'), ['str'])),
                                    ('nof_dbs', (YLeaf(YType.uint32, 'nof-dbs'), ['int'])),
                                ])
                                self.bank_id = None
                                self.bank_key_size = None
                                self.bank_free_entries = None
                                self.bank_inuse_entries = None
                                self.owner = None
                                self.nof_dbs = None

                                self.bank_db = YList(self)
                                self._segment_path = lambda: "tcam-bank"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank, ['bank_id', 'bank_key_size', 'bank_free_entries', 'bank_inuse_entries', 'owner', 'nof_dbs'], name, value)


                            class BankDb(Entity):
                                """
                                bank db
                                
                                .. attribute:: db_id
                                
                                	db id
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: db_inuse_entries
                                
                                	db inuse entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: db_prefix
                                
                                	db prefix
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'fia-internal-tcam-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank.BankDb, self).__init__()

                                    self.yang_name = "bank-db"
                                    self.yang_parent_name = "tcam-bank"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('db_id', (YLeaf(YType.uint32, 'db-id'), ['int'])),
                                        ('db_inuse_entries', (YLeaf(YType.uint32, 'db-inuse-entries'), ['int'])),
                                        ('db_prefix', (YLeaf(YType.str, 'db-prefix'), ['str'])),
                                    ])
                                    self.db_id = None
                                    self.db_inuse_entries = None
                                    self.db_prefix = None
                                    self._segment_path = lambda: "bank-db"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank.BankDb, ['db_id', 'db_inuse_entries', 'db_prefix'], name, value)


                class InternalTcamResources(Entity):
                    """
                    Internal TCAM Resource Information
                    
                    .. attribute:: npu_tcam
                    
                    	npu tcam
                    	**type**\: list of  		 :py:class:`NpuTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam>`
                    
                    

                    """

                    _prefix = 'fia-internal-tcam-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Controller.Dpa.Nodes.Node.InternalTcamResources, self).__init__()

                        self.yang_name = "internal-tcam-resources"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("npu-tcam", ("npu_tcam", Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam))])
                        self._leafs = OrderedDict()

                        self.npu_tcam = YList(self)
                        self._segment_path = lambda: "internal-tcam-resources"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Dpa.Nodes.Node.InternalTcamResources, [], name, value)


                    class NpuTcam(Entity):
                        """
                        npu tcam
                        
                        .. attribute:: npu_id
                        
                        	npu id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tcam_bank
                        
                        	tcam bank
                        	**type**\: list of  		 :py:class:`TcamBank <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank>`
                        
                        

                        """

                        _prefix = 'fia-internal-tcam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam, self).__init__()

                            self.yang_name = "npu-tcam"
                            self.yang_parent_name = "internal-tcam-resources"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("tcam-bank", ("tcam_bank", Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank))])
                            self._leafs = OrderedDict([
                                ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                            ])
                            self.npu_id = None

                            self.tcam_bank = YList(self)
                            self._segment_path = lambda: "npu-tcam"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam, ['npu_id'], name, value)


                        class TcamBank(Entity):
                            """
                            tcam bank
                            
                            .. attribute:: bank_id
                            
                            	bank id
                            	**type**\: str
                            
                            .. attribute:: bank_key_size
                            
                            	bank key size
                            	**type**\: str
                            
                            .. attribute:: bank_free_entries
                            
                            	bank free entries
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bank_inuse_entries
                            
                            	bank inuse entries
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: owner
                            
                            	owner
                            	**type**\: str
                            
                            .. attribute:: nof_dbs
                            
                            	nof dbs
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bank_db
                            
                            	bank db
                            	**type**\: list of  		 :py:class:`BankDb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank.BankDb>`
                            
                            

                            """

                            _prefix = 'fia-internal-tcam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank, self).__init__()

                                self.yang_name = "tcam-bank"
                                self.yang_parent_name = "npu-tcam"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("bank-db", ("bank_db", Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank.BankDb))])
                                self._leafs = OrderedDict([
                                    ('bank_id', (YLeaf(YType.str, 'bank-id'), ['str'])),
                                    ('bank_key_size', (YLeaf(YType.str, 'bank-key-size'), ['str'])),
                                    ('bank_free_entries', (YLeaf(YType.uint32, 'bank-free-entries'), ['int'])),
                                    ('bank_inuse_entries', (YLeaf(YType.uint32, 'bank-inuse-entries'), ['int'])),
                                    ('owner', (YLeaf(YType.str, 'owner'), ['str'])),
                                    ('nof_dbs', (YLeaf(YType.uint32, 'nof-dbs'), ['int'])),
                                ])
                                self.bank_id = None
                                self.bank_key_size = None
                                self.bank_free_entries = None
                                self.bank_inuse_entries = None
                                self.owner = None
                                self.nof_dbs = None

                                self.bank_db = YList(self)
                                self._segment_path = lambda: "tcam-bank"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank, ['bank_id', 'bank_key_size', 'bank_free_entries', 'bank_inuse_entries', 'owner', 'nof_dbs'], name, value)


                            class BankDb(Entity):
                                """
                                bank db
                                
                                .. attribute:: db_id
                                
                                	db id
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: db_inuse_entries
                                
                                	db inuse entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: db_prefix
                                
                                	db prefix
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'fia-internal-tcam-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank.BankDb, self).__init__()

                                    self.yang_name = "bank-db"
                                    self.yang_parent_name = "tcam-bank"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('db_id', (YLeaf(YType.uint32, 'db-id'), ['int'])),
                                        ('db_inuse_entries', (YLeaf(YType.uint32, 'db-inuse-entries'), ['int'])),
                                        ('db_prefix', (YLeaf(YType.str, 'db-prefix'), ['str'])),
                                    ])
                                    self.db_id = None
                                    self.db_inuse_entries = None
                                    self.db_prefix = None
                                    self._segment_path = lambda: "bank-db"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank.BankDb, ['db_id', 'db_inuse_entries', 'db_prefix'], name, value)

    def clone_ptr(self):
        self._top_entity = Controller()
        return self._top_entity


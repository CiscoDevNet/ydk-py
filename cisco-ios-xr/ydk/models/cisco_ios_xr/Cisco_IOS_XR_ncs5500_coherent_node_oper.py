""" Cisco_IOS_XR_ncs5500_coherent_node_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5500\-coherent\-node package operational data.

This module contains definitions
for the following management objects\:
  coherent\: Coherent node  operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Coherent(Entity):
    """
    Coherent node  operational data
    
    .. attribute:: nodes
    
    	Coherent list of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ncs5500-coherent-node-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Coherent, self).__init__()
        self._top_entity = None

        self.yang_name = "coherent"
        self.yang_parent_name = "Cisco-IOS-XR-ncs5500-coherent-node-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Coherent.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Coherent.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ncs5500-coherent-node-oper:coherent"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Coherent, [], name, value)


    class Nodes(Entity):
        """
        Coherent list of nodes
        
        .. attribute:: node
        
        	Coherent discovery operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ncs5500-coherent-node-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Coherent.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "coherent"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Coherent.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs5500-coherent-node-oper:coherent/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Coherent.Nodes, [], name, value)


        class Node(Entity):
            """
            Coherent discovery operational data for a
            particular node
            
            .. attribute:: node_name  (key)
            
            	The node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: coherent_time_stats
            
            	Coherent driver performace information
            	**type**\:  :py:class:`CoherentTimeStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats>`
            
            	**config**\: False
            
            .. attribute:: coherenthealth
            
            	Coherent node data for driver health
            	**type**\:  :py:class:`Coherenthealth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ncs5500-coherent-node-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Coherent.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("coherent-time-stats", ("coherent_time_stats", Coherent.Nodes.Node.CoherentTimeStats)), ("coherenthealth", ("coherenthealth", Coherent.Nodes.Node.Coherenthealth))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.coherent_time_stats = Coherent.Nodes.Node.CoherentTimeStats()
                self.coherent_time_stats.parent = self
                self._children_name_map["coherent_time_stats"] = "coherent-time-stats"

                self.coherenthealth = Coherent.Nodes.Node.Coherenthealth()
                self.coherenthealth.parent = self
                self._children_name_map["coherenthealth"] = "coherenthealth"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs5500-coherent-node-oper:coherent/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Coherent.Nodes.Node, ['node_name'], name, value)


            class CoherentTimeStats(Entity):
                """
                Coherent driver performace information
                
                .. attribute:: opts_ea_bulk_create
                
                	opts ea bulk create
                	**type**\:  :py:class:`OptsEaBulkCreate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate>`
                
                	**config**\: False
                
                .. attribute:: opts_ea_bulk_update
                
                	opts ea bulk update
                	**type**\:  :py:class:`OptsEaBulkUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate>`
                
                	**config**\: False
                
                .. attribute:: dsp_ea_bulk_create
                
                	dsp ea bulk create
                	**type**\:  :py:class:`DspEaBulkCreate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate>`
                
                	**config**\: False
                
                .. attribute:: dsp_ea_bulk_update
                
                	dsp ea bulk update
                	**type**\:  :py:class:`DspEaBulkUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate>`
                
                	**config**\: False
                
                .. attribute:: driver_init
                
                	driver init
                	**type**\: str
                
                	**length:** 0..255
                
                	**config**\: False
                
                .. attribute:: driver_operational
                
                	driver operational
                	**type**\: str
                
                	**length:** 0..255
                
                	**config**\: False
                
                .. attribute:: device_created
                
                	device created
                	**type**\: str
                
                	**length:** 0..255
                
                	**config**\: False
                
                .. attribute:: optics_controllers_created
                
                	optics controllers created
                	**type**\: str
                
                	**length:** 0..255
                
                	**config**\: False
                
                .. attribute:: dsp_controllers_created
                
                	dsp controllers created
                	**type**\: str
                
                	**length:** 0..255
                
                	**config**\: False
                
                .. attribute:: eth_intf_created
                
                	eth intf created
                	**type**\: str
                
                	**length:** 0..255
                
                	**config**\: False
                
                .. attribute:: port_stat
                
                	port stat
                	**type**\: list of  		 :py:class:`PortStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ncs5500-coherent-node-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Coherent.Nodes.Node.CoherentTimeStats, self).__init__()

                    self.yang_name = "coherent-time-stats"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("opts-ea-bulk-create", ("opts_ea_bulk_create", Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate)), ("opts-ea-bulk-update", ("opts_ea_bulk_update", Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate)), ("dsp-ea-bulk-create", ("dsp_ea_bulk_create", Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate)), ("dsp-ea-bulk-update", ("dsp_ea_bulk_update", Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate)), ("port-stat", ("port_stat", Coherent.Nodes.Node.CoherentTimeStats.PortStat))])
                    self._leafs = OrderedDict([
                        ('driver_init', (YLeaf(YType.str, 'driver-init'), ['str'])),
                        ('driver_operational', (YLeaf(YType.str, 'driver-operational'), ['str'])),
                        ('device_created', (YLeaf(YType.str, 'device-created'), ['str'])),
                        ('optics_controllers_created', (YLeaf(YType.str, 'optics-controllers-created'), ['str'])),
                        ('dsp_controllers_created', (YLeaf(YType.str, 'dsp-controllers-created'), ['str'])),
                        ('eth_intf_created', (YLeaf(YType.str, 'eth-intf-created'), ['str'])),
                    ])
                    self.driver_init = None
                    self.driver_operational = None
                    self.device_created = None
                    self.optics_controllers_created = None
                    self.dsp_controllers_created = None
                    self.eth_intf_created = None

                    self.opts_ea_bulk_create = Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate()
                    self.opts_ea_bulk_create.parent = self
                    self._children_name_map["opts_ea_bulk_create"] = "opts-ea-bulk-create"

                    self.opts_ea_bulk_update = Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate()
                    self.opts_ea_bulk_update.parent = self
                    self._children_name_map["opts_ea_bulk_update"] = "opts-ea-bulk-update"

                    self.dsp_ea_bulk_create = Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate()
                    self.dsp_ea_bulk_create.parent = self
                    self._children_name_map["dsp_ea_bulk_create"] = "dsp-ea-bulk-create"

                    self.dsp_ea_bulk_update = Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate()
                    self.dsp_ea_bulk_update.parent = self
                    self._children_name_map["dsp_ea_bulk_update"] = "dsp-ea-bulk-update"

                    self.port_stat = YList(self)
                    self._segment_path = lambda: "coherent-time-stats"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats, [u'driver_init', u'driver_operational', u'device_created', u'optics_controllers_created', u'dsp_controllers_created', u'eth_intf_created'], name, value)


                class OptsEaBulkCreate(Entity):
                    """
                    opts ea bulk create
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate, self).__init__()

                        self.yang_name = "opts-ea-bulk-create"
                        self.yang_parent_name = "coherent-time-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('start', (YLeaf(YType.str, 'start'), ['str'])),
                            ('end', (YLeaf(YType.str, 'end'), ['str'])),
                            ('time_taken', (YLeaf(YType.str, 'time-taken'), ['str'])),
                            ('worst_time', (YLeaf(YType.str, 'worst-time'), ['str'])),
                        ])
                        self.start = None
                        self.end = None
                        self.time_taken = None
                        self.worst_time = None
                        self._segment_path = lambda: "opts-ea-bulk-create"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate, [u'start', u'end', u'time_taken', u'worst_time'], name, value)



                class OptsEaBulkUpdate(Entity):
                    """
                    opts ea bulk update
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate, self).__init__()

                        self.yang_name = "opts-ea-bulk-update"
                        self.yang_parent_name = "coherent-time-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('start', (YLeaf(YType.str, 'start'), ['str'])),
                            ('end', (YLeaf(YType.str, 'end'), ['str'])),
                            ('time_taken', (YLeaf(YType.str, 'time-taken'), ['str'])),
                            ('worst_time', (YLeaf(YType.str, 'worst-time'), ['str'])),
                        ])
                        self.start = None
                        self.end = None
                        self.time_taken = None
                        self.worst_time = None
                        self._segment_path = lambda: "opts-ea-bulk-update"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate, [u'start', u'end', u'time_taken', u'worst_time'], name, value)



                class DspEaBulkCreate(Entity):
                    """
                    dsp ea bulk create
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate, self).__init__()

                        self.yang_name = "dsp-ea-bulk-create"
                        self.yang_parent_name = "coherent-time-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('start', (YLeaf(YType.str, 'start'), ['str'])),
                            ('end', (YLeaf(YType.str, 'end'), ['str'])),
                            ('time_taken', (YLeaf(YType.str, 'time-taken'), ['str'])),
                            ('worst_time', (YLeaf(YType.str, 'worst-time'), ['str'])),
                        ])
                        self.start = None
                        self.end = None
                        self.time_taken = None
                        self.worst_time = None
                        self._segment_path = lambda: "dsp-ea-bulk-create"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate, [u'start', u'end', u'time_taken', u'worst_time'], name, value)



                class DspEaBulkUpdate(Entity):
                    """
                    dsp ea bulk update
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate, self).__init__()

                        self.yang_name = "dsp-ea-bulk-update"
                        self.yang_parent_name = "coherent-time-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('start', (YLeaf(YType.str, 'start'), ['str'])),
                            ('end', (YLeaf(YType.str, 'end'), ['str'])),
                            ('time_taken', (YLeaf(YType.str, 'time-taken'), ['str'])),
                            ('worst_time', (YLeaf(YType.str, 'worst-time'), ['str'])),
                        ])
                        self.start = None
                        self.end = None
                        self.time_taken = None
                        self.worst_time = None
                        self._segment_path = lambda: "dsp-ea-bulk-update"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate, [u'start', u'end', u'time_taken', u'worst_time'], name, value)



                class PortStat(Entity):
                    """
                    port stat
                    
                    .. attribute:: laser_on_stats
                    
                    	laser on stats
                    	**type**\:  :py:class:`LaserOnStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats>`
                    
                    	**config**\: False
                    
                    .. attribute:: laser_off_stats
                    
                    	laser off stats
                    	**type**\:  :py:class:`LaserOffStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats>`
                    
                    	**config**\: False
                    
                    .. attribute:: wl_op_stats
                    
                    	wl op stats
                    	**type**\:  :py:class:`WlOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats>`
                    
                    	**config**\: False
                    
                    .. attribute:: txpwr_op_stats
                    
                    	txpwr op stats
                    	**type**\:  :py:class:`TxpwrOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats>`
                    
                    	**config**\: False
                    
                    .. attribute:: cdmin_op_stats
                    
                    	cdmin op stats
                    	**type**\:  :py:class:`CdminOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats>`
                    
                    	**config**\: False
                    
                    .. attribute:: cdmax_op_stats
                    
                    	cdmax op stats
                    	**type**\:  :py:class:`CdmaxOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats>`
                    
                    	**config**\: False
                    
                    .. attribute:: traffictype_op_stats
                    
                    	traffictype op stats
                    	**type**\:  :py:class:`TraffictypeOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats>`
                    
                    	**config**\: False
                    
                    .. attribute:: rsip
                    
                    	rsip
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: fp_port_idx
                    
                    	fp port idx
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: laser_state
                    
                    	laser state
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: provisioned_frequency
                    
                    	provisioned frequency
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: tx_power
                    
                    	tx power
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: cd_min
                    
                    	cd min
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: cd_max
                    
                    	cd max
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: traffic_type
                    
                    	traffic type
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.CoherentTimeStats.PortStat, self).__init__()

                        self.yang_name = "port-stat"
                        self.yang_parent_name = "coherent-time-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("laser-on-stats", ("laser_on_stats", Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats)), ("laser-off-stats", ("laser_off_stats", Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats)), ("wl-op-stats", ("wl_op_stats", Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats)), ("txpwr-op-stats", ("txpwr_op_stats", Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats)), ("cdmin-op-stats", ("cdmin_op_stats", Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats)), ("cdmax-op-stats", ("cdmax_op_stats", Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats)), ("traffictype-op-stats", ("traffictype_op_stats", Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats))])
                        self._leafs = OrderedDict([
                            ('rsip', (YLeaf(YType.uint32, 'rsip'), ['int'])),
                            ('fp_port_idx', (YLeaf(YType.uint32, 'fp-port-idx'), ['int'])),
                            ('laser_state', (YLeaf(YType.boolean, 'laser-state'), ['bool'])),
                            ('provisioned_frequency', (YLeaf(YType.uint32, 'provisioned-frequency'), ['int'])),
                            ('tx_power', (YLeaf(YType.int32, 'tx-power'), ['int'])),
                            ('cd_min', (YLeaf(YType.int32, 'cd-min'), ['int'])),
                            ('cd_max', (YLeaf(YType.int32, 'cd-max'), ['int'])),
                            ('traffic_type', (YLeaf(YType.str, 'traffic-type'), ['str'])),
                        ])
                        self.rsip = None
                        self.fp_port_idx = None
                        self.laser_state = None
                        self.provisioned_frequency = None
                        self.tx_power = None
                        self.cd_min = None
                        self.cd_max = None
                        self.traffic_type = None

                        self.laser_on_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats()
                        self.laser_on_stats.parent = self
                        self._children_name_map["laser_on_stats"] = "laser-on-stats"

                        self.laser_off_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats()
                        self.laser_off_stats.parent = self
                        self._children_name_map["laser_off_stats"] = "laser-off-stats"

                        self.wl_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats()
                        self.wl_op_stats.parent = self
                        self._children_name_map["wl_op_stats"] = "wl-op-stats"

                        self.txpwr_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats()
                        self.txpwr_op_stats.parent = self
                        self._children_name_map["txpwr_op_stats"] = "txpwr-op-stats"

                        self.cdmin_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats()
                        self.cdmin_op_stats.parent = self
                        self._children_name_map["cdmin_op_stats"] = "cdmin-op-stats"

                        self.cdmax_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats()
                        self.cdmax_op_stats.parent = self
                        self._children_name_map["cdmax_op_stats"] = "cdmax-op-stats"

                        self.traffictype_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats()
                        self.traffictype_op_stats.parent = self
                        self._children_name_map["traffictype_op_stats"] = "traffictype-op-stats"
                        self._segment_path = lambda: "port-stat"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat, [u'rsip', u'fp_port_idx', u'laser_state', u'provisioned_frequency', u'tx_power', u'cd_min', u'cd_max', u'traffic_type'], name, value)


                    class LaserOnStats(Entity):
                        """
                        laser on stats
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats, self).__init__()

                            self.yang_name = "laser-on-stats"
                            self.yang_parent_name = "port-stat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start', (YLeaf(YType.str, 'start'), ['str'])),
                                ('end', (YLeaf(YType.str, 'end'), ['str'])),
                                ('time_taken', (YLeaf(YType.str, 'time-taken'), ['str'])),
                                ('worst_time', (YLeaf(YType.str, 'worst-time'), ['str'])),
                            ])
                            self.start = None
                            self.end = None
                            self.time_taken = None
                            self.worst_time = None
                            self._segment_path = lambda: "laser-on-stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats, [u'start', u'end', u'time_taken', u'worst_time'], name, value)



                    class LaserOffStats(Entity):
                        """
                        laser off stats
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats, self).__init__()

                            self.yang_name = "laser-off-stats"
                            self.yang_parent_name = "port-stat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start', (YLeaf(YType.str, 'start'), ['str'])),
                                ('end', (YLeaf(YType.str, 'end'), ['str'])),
                                ('time_taken', (YLeaf(YType.str, 'time-taken'), ['str'])),
                                ('worst_time', (YLeaf(YType.str, 'worst-time'), ['str'])),
                            ])
                            self.start = None
                            self.end = None
                            self.time_taken = None
                            self.worst_time = None
                            self._segment_path = lambda: "laser-off-stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats, [u'start', u'end', u'time_taken', u'worst_time'], name, value)



                    class WlOpStats(Entity):
                        """
                        wl op stats
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats, self).__init__()

                            self.yang_name = "wl-op-stats"
                            self.yang_parent_name = "port-stat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start', (YLeaf(YType.str, 'start'), ['str'])),
                                ('end', (YLeaf(YType.str, 'end'), ['str'])),
                                ('time_taken', (YLeaf(YType.str, 'time-taken'), ['str'])),
                                ('worst_time', (YLeaf(YType.str, 'worst-time'), ['str'])),
                            ])
                            self.start = None
                            self.end = None
                            self.time_taken = None
                            self.worst_time = None
                            self._segment_path = lambda: "wl-op-stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats, [u'start', u'end', u'time_taken', u'worst_time'], name, value)



                    class TxpwrOpStats(Entity):
                        """
                        txpwr op stats
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats, self).__init__()

                            self.yang_name = "txpwr-op-stats"
                            self.yang_parent_name = "port-stat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start', (YLeaf(YType.str, 'start'), ['str'])),
                                ('end', (YLeaf(YType.str, 'end'), ['str'])),
                                ('time_taken', (YLeaf(YType.str, 'time-taken'), ['str'])),
                                ('worst_time', (YLeaf(YType.str, 'worst-time'), ['str'])),
                            ])
                            self.start = None
                            self.end = None
                            self.time_taken = None
                            self.worst_time = None
                            self._segment_path = lambda: "txpwr-op-stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats, [u'start', u'end', u'time_taken', u'worst_time'], name, value)



                    class CdminOpStats(Entity):
                        """
                        cdmin op stats
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats, self).__init__()

                            self.yang_name = "cdmin-op-stats"
                            self.yang_parent_name = "port-stat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start', (YLeaf(YType.str, 'start'), ['str'])),
                                ('end', (YLeaf(YType.str, 'end'), ['str'])),
                                ('time_taken', (YLeaf(YType.str, 'time-taken'), ['str'])),
                                ('worst_time', (YLeaf(YType.str, 'worst-time'), ['str'])),
                            ])
                            self.start = None
                            self.end = None
                            self.time_taken = None
                            self.worst_time = None
                            self._segment_path = lambda: "cdmin-op-stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats, [u'start', u'end', u'time_taken', u'worst_time'], name, value)



                    class CdmaxOpStats(Entity):
                        """
                        cdmax op stats
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats, self).__init__()

                            self.yang_name = "cdmax-op-stats"
                            self.yang_parent_name = "port-stat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start', (YLeaf(YType.str, 'start'), ['str'])),
                                ('end', (YLeaf(YType.str, 'end'), ['str'])),
                                ('time_taken', (YLeaf(YType.str, 'time-taken'), ['str'])),
                                ('worst_time', (YLeaf(YType.str, 'worst-time'), ['str'])),
                            ])
                            self.start = None
                            self.end = None
                            self.time_taken = None
                            self.worst_time = None
                            self._segment_path = lambda: "cdmax-op-stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats, [u'start', u'end', u'time_taken', u'worst_time'], name, value)



                    class TraffictypeOpStats(Entity):
                        """
                        traffictype op stats
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats, self).__init__()

                            self.yang_name = "traffictype-op-stats"
                            self.yang_parent_name = "port-stat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start', (YLeaf(YType.str, 'start'), ['str'])),
                                ('end', (YLeaf(YType.str, 'end'), ['str'])),
                                ('time_taken', (YLeaf(YType.str, 'time-taken'), ['str'])),
                                ('worst_time', (YLeaf(YType.str, 'worst-time'), ['str'])),
                            ])
                            self.start = None
                            self.end = None
                            self.time_taken = None
                            self.worst_time = None
                            self._segment_path = lambda: "traffictype-op-stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats, [u'start', u'end', u'time_taken', u'worst_time'], name, value)





            class Coherenthealth(Entity):
                """
                Coherent node data for driver health
                
                .. attribute:: is_peyto
                
                	is peyto
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: im_state
                
                	im state
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: aipc_srvr_state
                
                	aipc srvr state
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: sysdb_state
                
                	sysdb state
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: pm_state
                
                	pm state
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: optics_ea_conn
                
                	optics ea conn
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: dsp_ea_conn
                
                	dsp ea conn
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: vether_state
                
                	vether state
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: morgoth_alive
                
                	morgoth alive
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: prov_infra_state
                
                	prov infra state
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: sdk_fpga_compatible
                
                	sdk fpga compatible
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: pending_provision
                
                	pending provision
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: pulse_sent
                
                	pulse sent
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: inside_prov_loop
                
                	inside prov loop
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: fpd_in_progress
                
                	fpd in progress
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: prov_run_count
                
                	prov run count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sdk_version
                
                	sdk version
                	**type**\: str
                
                	**length:** 0..255
                
                	**config**\: False
                
                .. attribute:: morgoth_running_version
                
                	morgoth running version
                	**type**\: str
                
                	**length:** 0..255
                
                	**config**\: False
                
                .. attribute:: morgoth_downloaded_version
                
                	morgoth downloaded version
                	**type**\: str
                
                	**length:** 0..255
                
                	**config**\: False
                
                .. attribute:: morgoth_golden_version
                
                	morgoth golden version
                	**type**\: str
                
                	**length:** 0..255
                
                	**config**\: False
                
                .. attribute:: dsp0_version
                
                	dsp0 version
                	**type**\: str
                
                	**length:** 0..255
                
                	**config**\: False
                
                .. attribute:: dsp1_version
                
                	dsp1 version
                	**type**\: str
                
                	**length:** 0..255
                
                	**config**\: False
                
                .. attribute:: dsp2_version
                
                	dsp2 version
                	**type**\: str
                
                	**length:** 0..255
                
                	**config**\: False
                
                .. attribute:: board_type
                
                	board type
                	**type**\: str
                
                	**length:** 0..255
                
                	**config**\: False
                
                .. attribute:: jlink_op
                
                	jlink op
                	**type**\: str
                
                	**length:** 0..6144
                
                	**config**\: False
                
                .. attribute:: port_data
                
                	port data
                	**type**\: list of  		 :py:class:`PortData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ncs5500-coherent-node-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Coherent.Nodes.Node.Coherenthealth, self).__init__()

                    self.yang_name = "coherenthealth"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("port-data", ("port_data", Coherent.Nodes.Node.Coherenthealth.PortData))])
                    self._leafs = OrderedDict([
                        ('is_peyto', (YLeaf(YType.boolean, 'is-peyto'), ['bool'])),
                        ('im_state', (YLeaf(YType.boolean, 'im-state'), ['bool'])),
                        ('aipc_srvr_state', (YLeaf(YType.boolean, 'aipc-srvr-state'), ['bool'])),
                        ('sysdb_state', (YLeaf(YType.boolean, 'sysdb-state'), ['bool'])),
                        ('pm_state', (YLeaf(YType.boolean, 'pm-state'), ['bool'])),
                        ('optics_ea_conn', (YLeaf(YType.boolean, 'optics-ea-conn'), ['bool'])),
                        ('dsp_ea_conn', (YLeaf(YType.boolean, 'dsp-ea-conn'), ['bool'])),
                        ('vether_state', (YLeaf(YType.boolean, 'vether-state'), ['bool'])),
                        ('morgoth_alive', (YLeaf(YType.boolean, 'morgoth-alive'), ['bool'])),
                        ('prov_infra_state', (YLeaf(YType.boolean, 'prov-infra-state'), ['bool'])),
                        ('sdk_fpga_compatible', (YLeaf(YType.boolean, 'sdk-fpga-compatible'), ['bool'])),
                        ('pending_provision', (YLeaf(YType.boolean, 'pending-provision'), ['bool'])),
                        ('pulse_sent', (YLeaf(YType.boolean, 'pulse-sent'), ['bool'])),
                        ('inside_prov_loop', (YLeaf(YType.boolean, 'inside-prov-loop'), ['bool'])),
                        ('fpd_in_progress', (YLeaf(YType.boolean, 'fpd-in-progress'), ['bool'])),
                        ('prov_run_count', (YLeaf(YType.uint32, 'prov-run-count'), ['int'])),
                        ('sdk_version', (YLeaf(YType.str, 'sdk-version'), ['str'])),
                        ('morgoth_running_version', (YLeaf(YType.str, 'morgoth-running-version'), ['str'])),
                        ('morgoth_downloaded_version', (YLeaf(YType.str, 'morgoth-downloaded-version'), ['str'])),
                        ('morgoth_golden_version', (YLeaf(YType.str, 'morgoth-golden-version'), ['str'])),
                        ('dsp0_version', (YLeaf(YType.str, 'dsp0-version'), ['str'])),
                        ('dsp1_version', (YLeaf(YType.str, 'dsp1-version'), ['str'])),
                        ('dsp2_version', (YLeaf(YType.str, 'dsp2-version'), ['str'])),
                        ('board_type', (YLeaf(YType.str, 'board-type'), ['str'])),
                        ('jlink_op', (YLeaf(YType.str, 'jlink-op'), ['str'])),
                    ])
                    self.is_peyto = None
                    self.im_state = None
                    self.aipc_srvr_state = None
                    self.sysdb_state = None
                    self.pm_state = None
                    self.optics_ea_conn = None
                    self.dsp_ea_conn = None
                    self.vether_state = None
                    self.morgoth_alive = None
                    self.prov_infra_state = None
                    self.sdk_fpga_compatible = None
                    self.pending_provision = None
                    self.pulse_sent = None
                    self.inside_prov_loop = None
                    self.fpd_in_progress = None
                    self.prov_run_count = None
                    self.sdk_version = None
                    self.morgoth_running_version = None
                    self.morgoth_downloaded_version = None
                    self.morgoth_golden_version = None
                    self.dsp0_version = None
                    self.dsp1_version = None
                    self.dsp2_version = None
                    self.board_type = None
                    self.jlink_op = None

                    self.port_data = YList(self)
                    self._segment_path = lambda: "coherenthealth"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Coherent.Nodes.Node.Coherenthealth, [u'is_peyto', u'im_state', u'aipc_srvr_state', u'sysdb_state', u'pm_state', u'optics_ea_conn', u'dsp_ea_conn', u'vether_state', u'morgoth_alive', u'prov_infra_state', u'sdk_fpga_compatible', u'pending_provision', u'pulse_sent', u'inside_prov_loop', u'fpd_in_progress', u'prov_run_count', u'sdk_version', u'morgoth_running_version', u'morgoth_downloaded_version', u'morgoth_golden_version', u'dsp0_version', u'dsp1_version', u'dsp2_version', u'board_type', u'jlink_op'], name, value)


                class PortData(Entity):
                    """
                    port data
                    
                    .. attribute:: ctp_info
                    
                    	ctp info
                    	**type**\:  :py:class:`CtpInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo>`
                    
                    	**config**\: False
                    
                    .. attribute:: interface_info
                    
                    	interface info
                    	**type**\:  :py:class:`InterfaceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo>`
                    
                    	**config**\: False
                    
                    .. attribute:: rsip
                    
                    	rsip
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: optics_ctrl_created
                    
                    	optics ctrl created
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: dsp_ctrl_created
                    
                    	dsp ctrl created
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: has_pluggable
                    
                    	has pluggable
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: optics_admin_up
                    
                    	optics admin up
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: dsp_admin_up
                    
                    	dsp admin up
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: end_of_config
                    
                    	end of config
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: optics_laser_state
                    
                    	optics laser state
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: laser_state
                    
                    	laser state
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: laser_on_pending
                    
                    	laser on pending
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: provisioning_needed
                    
                    	provisioning needed
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: force_reprovision
                    
                    	force reprovision
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: fp_port_idx
                    
                    	fp port idx
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: configured_frequency
                    
                    	configured frequency
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: provisioned_frequency
                    
                    	provisioned frequency
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: configured_tx_power
                    
                    	configured tx power
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    	**config**\: False
                    
                    .. attribute:: provisioned_tx_power
                    
                    	provisioned tx power
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    	**config**\: False
                    
                    .. attribute:: configured_cd_min
                    
                    	configured cd min
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    	**config**\: False
                    
                    .. attribute:: provisioned_cd_min
                    
                    	provisioned cd min
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    	**config**\: False
                    
                    .. attribute:: configured_cd_max
                    
                    	configured cd max
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    	**config**\: False
                    
                    .. attribute:: provisioned_cd_max
                    
                    	provisioned cd max
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    	**config**\: False
                    
                    .. attribute:: configured_traffic_type
                    
                    	configured traffic type
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    	**config**\: False
                    
                    .. attribute:: provisioned_traffic_type
                    
                    	provisioned traffic type
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    	**config**\: False
                    
                    .. attribute:: configured_loopback_mode
                    
                    	configured loopback mode
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    	**config**\: False
                    
                    .. attribute:: provisioned_loopback_mode
                    
                    	provisioned loopback mode
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    	**config**\: False
                    
                    .. attribute:: expected_ctp2_led_state
                    
                    	expected ctp2 led state
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    	**config**\: False
                    
                    .. attribute:: provisioned_ctp2_led_state
                    
                    	provisioned ctp2 led state
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    	**config**\: False
                    
                    .. attribute:: led_op_rc
                    
                    	led op rc
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: laser_op_rc
                    
                    	laser op rc
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: wlen_op_rc
                    
                    	wlen op rc
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: traffic_op_rc
                    
                    	traffic op rc
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: loopback_op_rc
                    
                    	loopback op rc
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: tx_power_op_rc
                    
                    	tx power op rc
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: cd_min_op_rc
                    
                    	cd min op rc
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: cd_max_op_rc
                    
                    	cd max op rc
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: provisioning_failed
                    
                    	provisioning failed
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: ctp2_hw_alarms
                    
                    	ctp2 hw alarms
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    	**config**\: False
                    
                    .. attribute:: dsp_hw_alarms
                    
                    	dsp hw alarms
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: is_pm_port_created_opt
                    
                    	is pm port created opt
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: rc_pm_port_opt
                    
                    	rc pm port opt
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: pm_port_state_opt
                    
                    	pm port state opt
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: rc_pm_provision_opt
                    
                    	rc pm provision opt
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: is_alarm_port_created_opt
                    
                    	is alarm port created opt
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: rc_alarm_port_opt
                    
                    	rc alarm port opt
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: is_pm_port_created_dsp
                    
                    	is pm port created dsp
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: rc_pm_port_dsp
                    
                    	rc pm port dsp
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: pm_port_state_dsp
                    
                    	pm port state dsp
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: rc_pm_provision_dsp
                    
                    	rc pm provision dsp
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: is_alarm_port_created_dsp
                    
                    	is alarm port created dsp
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: rc_alarm_port_dsp
                    
                    	rc alarm port dsp
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.Coherenthealth.PortData, self).__init__()

                        self.yang_name = "port-data"
                        self.yang_parent_name = "coherenthealth"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ctp-info", ("ctp_info", Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo)), ("interface-info", ("interface_info", Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo))])
                        self._leafs = OrderedDict([
                            ('rsip', (YLeaf(YType.uint32, 'rsip'), ['int'])),
                            ('optics_ctrl_created', (YLeaf(YType.boolean, 'optics-ctrl-created'), ['bool'])),
                            ('dsp_ctrl_created', (YLeaf(YType.boolean, 'dsp-ctrl-created'), ['bool'])),
                            ('has_pluggable', (YLeaf(YType.boolean, 'has-pluggable'), ['bool'])),
                            ('optics_admin_up', (YLeaf(YType.boolean, 'optics-admin-up'), ['bool'])),
                            ('dsp_admin_up', (YLeaf(YType.boolean, 'dsp-admin-up'), ['bool'])),
                            ('end_of_config', (YLeaf(YType.boolean, 'end-of-config'), ['bool'])),
                            ('optics_laser_state', (YLeaf(YType.boolean, 'optics-laser-state'), ['bool'])),
                            ('laser_state', (YLeaf(YType.boolean, 'laser-state'), ['bool'])),
                            ('laser_on_pending', (YLeaf(YType.boolean, 'laser-on-pending'), ['bool'])),
                            ('provisioning_needed', (YLeaf(YType.boolean, 'provisioning-needed'), ['bool'])),
                            ('force_reprovision', (YLeaf(YType.boolean, 'force-reprovision'), ['bool'])),
                            ('fp_port_idx', (YLeaf(YType.uint32, 'fp-port-idx'), ['int'])),
                            ('configured_frequency', (YLeaf(YType.uint32, 'configured-frequency'), ['int'])),
                            ('provisioned_frequency', (YLeaf(YType.uint32, 'provisioned-frequency'), ['int'])),
                            ('configured_tx_power', (YLeaf(YType.str, 'configured-tx-power'), ['str'])),
                            ('provisioned_tx_power', (YLeaf(YType.str, 'provisioned-tx-power'), ['str'])),
                            ('configured_cd_min', (YLeaf(YType.str, 'configured-cd-min'), ['str'])),
                            ('provisioned_cd_min', (YLeaf(YType.str, 'provisioned-cd-min'), ['str'])),
                            ('configured_cd_max', (YLeaf(YType.str, 'configured-cd-max'), ['str'])),
                            ('provisioned_cd_max', (YLeaf(YType.str, 'provisioned-cd-max'), ['str'])),
                            ('configured_traffic_type', (YLeaf(YType.str, 'configured-traffic-type'), ['str'])),
                            ('provisioned_traffic_type', (YLeaf(YType.str, 'provisioned-traffic-type'), ['str'])),
                            ('configured_loopback_mode', (YLeaf(YType.str, 'configured-loopback-mode'), ['str'])),
                            ('provisioned_loopback_mode', (YLeaf(YType.str, 'provisioned-loopback-mode'), ['str'])),
                            ('expected_ctp2_led_state', (YLeaf(YType.str, 'expected-ctp2-led-state'), ['str'])),
                            ('provisioned_ctp2_led_state', (YLeaf(YType.str, 'provisioned-ctp2-led-state'), ['str'])),
                            ('led_op_rc', (YLeaf(YType.int32, 'led-op-rc'), ['int'])),
                            ('laser_op_rc', (YLeaf(YType.int32, 'laser-op-rc'), ['int'])),
                            ('wlen_op_rc', (YLeaf(YType.int32, 'wlen-op-rc'), ['int'])),
                            ('traffic_op_rc', (YLeaf(YType.int32, 'traffic-op-rc'), ['int'])),
                            ('loopback_op_rc', (YLeaf(YType.int32, 'loopback-op-rc'), ['int'])),
                            ('tx_power_op_rc', (YLeaf(YType.int32, 'tx-power-op-rc'), ['int'])),
                            ('cd_min_op_rc', (YLeaf(YType.int32, 'cd-min-op-rc'), ['int'])),
                            ('cd_max_op_rc', (YLeaf(YType.int32, 'cd-max-op-rc'), ['int'])),
                            ('provisioning_failed', (YLeaf(YType.boolean, 'provisioning-failed'), ['bool'])),
                            ('ctp2_hw_alarms', (YLeaf(YType.str, 'ctp2-hw-alarms'), ['str'])),
                            ('dsp_hw_alarms', (YLeaf(YType.str, 'dsp-hw-alarms'), ['str'])),
                            ('is_pm_port_created_opt', (YLeaf(YType.boolean, 'is-pm-port-created-opt'), ['bool'])),
                            ('rc_pm_port_opt', (YLeaf(YType.int32, 'rc-pm-port-opt'), ['int'])),
                            ('pm_port_state_opt', (YLeaf(YType.int32, 'pm-port-state-opt'), ['int'])),
                            ('rc_pm_provision_opt', (YLeaf(YType.int32, 'rc-pm-provision-opt'), ['int'])),
                            ('is_alarm_port_created_opt', (YLeaf(YType.boolean, 'is-alarm-port-created-opt'), ['bool'])),
                            ('rc_alarm_port_opt', (YLeaf(YType.int32, 'rc-alarm-port-opt'), ['int'])),
                            ('is_pm_port_created_dsp', (YLeaf(YType.boolean, 'is-pm-port-created-dsp'), ['bool'])),
                            ('rc_pm_port_dsp', (YLeaf(YType.int32, 'rc-pm-port-dsp'), ['int'])),
                            ('pm_port_state_dsp', (YLeaf(YType.int32, 'pm-port-state-dsp'), ['int'])),
                            ('rc_pm_provision_dsp', (YLeaf(YType.int32, 'rc-pm-provision-dsp'), ['int'])),
                            ('is_alarm_port_created_dsp', (YLeaf(YType.boolean, 'is-alarm-port-created-dsp'), ['bool'])),
                            ('rc_alarm_port_dsp', (YLeaf(YType.int32, 'rc-alarm-port-dsp'), ['int'])),
                        ])
                        self.rsip = None
                        self.optics_ctrl_created = None
                        self.dsp_ctrl_created = None
                        self.has_pluggable = None
                        self.optics_admin_up = None
                        self.dsp_admin_up = None
                        self.end_of_config = None
                        self.optics_laser_state = None
                        self.laser_state = None
                        self.laser_on_pending = None
                        self.provisioning_needed = None
                        self.force_reprovision = None
                        self.fp_port_idx = None
                        self.configured_frequency = None
                        self.provisioned_frequency = None
                        self.configured_tx_power = None
                        self.provisioned_tx_power = None
                        self.configured_cd_min = None
                        self.provisioned_cd_min = None
                        self.configured_cd_max = None
                        self.provisioned_cd_max = None
                        self.configured_traffic_type = None
                        self.provisioned_traffic_type = None
                        self.configured_loopback_mode = None
                        self.provisioned_loopback_mode = None
                        self.expected_ctp2_led_state = None
                        self.provisioned_ctp2_led_state = None
                        self.led_op_rc = None
                        self.laser_op_rc = None
                        self.wlen_op_rc = None
                        self.traffic_op_rc = None
                        self.loopback_op_rc = None
                        self.tx_power_op_rc = None
                        self.cd_min_op_rc = None
                        self.cd_max_op_rc = None
                        self.provisioning_failed = None
                        self.ctp2_hw_alarms = None
                        self.dsp_hw_alarms = None
                        self.is_pm_port_created_opt = None
                        self.rc_pm_port_opt = None
                        self.pm_port_state_opt = None
                        self.rc_pm_provision_opt = None
                        self.is_alarm_port_created_opt = None
                        self.rc_alarm_port_opt = None
                        self.is_pm_port_created_dsp = None
                        self.rc_pm_port_dsp = None
                        self.pm_port_state_dsp = None
                        self.rc_pm_provision_dsp = None
                        self.is_alarm_port_created_dsp = None
                        self.rc_alarm_port_dsp = None

                        self.ctp_info = Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo()
                        self.ctp_info.parent = self
                        self._children_name_map["ctp_info"] = "ctp-info"

                        self.interface_info = Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo()
                        self.interface_info.parent = self
                        self._children_name_map["interface_info"] = "interface-info"
                        self._segment_path = lambda: "port-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Coherent.Nodes.Node.Coherenthealth.PortData, [u'rsip', u'optics_ctrl_created', u'dsp_ctrl_created', u'has_pluggable', u'optics_admin_up', u'dsp_admin_up', u'end_of_config', u'optics_laser_state', u'laser_state', u'laser_on_pending', u'provisioning_needed', u'force_reprovision', u'fp_port_idx', u'configured_frequency', u'provisioned_frequency', u'configured_tx_power', u'provisioned_tx_power', u'configured_cd_min', u'provisioned_cd_min', u'configured_cd_max', u'provisioned_cd_max', u'configured_traffic_type', u'provisioned_traffic_type', u'configured_loopback_mode', u'provisioned_loopback_mode', u'expected_ctp2_led_state', u'provisioned_ctp2_led_state', u'led_op_rc', u'laser_op_rc', u'wlen_op_rc', u'traffic_op_rc', u'loopback_op_rc', u'tx_power_op_rc', u'cd_min_op_rc', u'cd_max_op_rc', u'provisioning_failed', u'ctp2_hw_alarms', u'dsp_hw_alarms', u'is_pm_port_created_opt', u'rc_pm_port_opt', u'pm_port_state_opt', u'rc_pm_provision_opt', u'is_alarm_port_created_opt', u'rc_alarm_port_opt', u'is_pm_port_created_dsp', u'rc_pm_port_dsp', u'pm_port_state_dsp', u'rc_pm_provision_dsp', u'is_alarm_port_created_dsp', u'rc_alarm_port_dsp'], name, value)


                    class CtpInfo(Entity):
                        """
                        ctp info
                        
                        .. attribute:: deviation
                        
                        	deviation
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        	**config**\: False
                        
                        .. attribute:: part_number
                        
                        	part number
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        	**config**\: False
                        
                        .. attribute:: serial_number
                        
                        	serial number
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        	**config**\: False
                        
                        .. attribute:: date_code_number
                        
                        	date code number
                        	**type**\: str
                        
                        	**length:** 0..10
                        
                        	**config**\: False
                        
                        .. attribute:: clei_code_number
                        
                        	CLEI code number
                        	**type**\: str
                        
                        	**length:** 0..10
                        
                        	**config**\: False
                        
                        .. attribute:: vendorname
                        
                        	vendorname
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        	**config**\: False
                        
                        .. attribute:: description
                        
                        	description
                        	**type**\: str
                        
                        	**length:** 0..64
                        
                        	**config**\: False
                        
                        .. attribute:: pid
                        
                        	pid
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        	**config**\: False
                        
                        .. attribute:: vid
                        
                        	vid
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        	**config**\: False
                        
                        .. attribute:: module_hardware_version_number
                        
                        	module hardware version number
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        	**config**\: False
                        
                        .. attribute:: module_firmware_running_version_number
                        
                        	module firmware running version number
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        	**config**\: False
                        
                        .. attribute:: module_firmware_committed_version_number
                        
                        	module firmware committed version number
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        	**config**\: False
                        
                        .. attribute:: ctp_type
                        
                        	ctp type
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo, self).__init__()

                            self.yang_name = "ctp-info"
                            self.yang_parent_name = "port-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('deviation', (YLeaf(YType.str, 'deviation'), ['str'])),
                                ('part_number', (YLeaf(YType.str, 'part-number'), ['str'])),
                                ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                ('date_code_number', (YLeaf(YType.str, 'date-code-number'), ['str'])),
                                ('clei_code_number', (YLeaf(YType.str, 'clei-code-number'), ['str'])),
                                ('vendorname', (YLeaf(YType.str, 'vendorname'), ['str'])),
                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ('pid', (YLeaf(YType.str, 'pid'), ['str'])),
                                ('vid', (YLeaf(YType.str, 'vid'), ['str'])),
                                ('module_hardware_version_number', (YLeaf(YType.str, 'module-hardware-version-number'), ['str'])),
                                ('module_firmware_running_version_number', (YLeaf(YType.str, 'module-firmware-running-version-number'), ['str'])),
                                ('module_firmware_committed_version_number', (YLeaf(YType.str, 'module-firmware-committed-version-number'), ['str'])),
                                ('ctp_type', (YLeaf(YType.uint32, 'ctp-type'), ['int'])),
                            ])
                            self.deviation = None
                            self.part_number = None
                            self.serial_number = None
                            self.date_code_number = None
                            self.clei_code_number = None
                            self.vendorname = None
                            self.description = None
                            self.pid = None
                            self.vid = None
                            self.module_hardware_version_number = None
                            self.module_firmware_running_version_number = None
                            self.module_firmware_committed_version_number = None
                            self.ctp_type = None
                            self._segment_path = lambda: "ctp-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo, [u'deviation', u'part_number', u'serial_number', u'date_code_number', u'clei_code_number', u'vendorname', u'description', u'pid', u'vid', u'module_hardware_version_number', u'module_firmware_running_version_number', u'module_firmware_committed_version_number', u'ctp_type'], name, value)



                    class InterfaceInfo(Entity):
                        """
                        interface info
                        
                        .. attribute:: eth_data
                        
                        	eth data
                        	**type**\: list of  		 :py:class:`EthData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo, self).__init__()

                            self.yang_name = "interface-info"
                            self.yang_parent_name = "port-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("eth-data", ("eth_data", Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData))])
                            self._leafs = OrderedDict()

                            self.eth_data = YList(self)
                            self._segment_path = lambda: "interface-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo, [], name, value)


                        class EthData(Entity):
                            """
                            eth data
                            
                            .. attribute:: ifname
                            
                            	ifname
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            	**config**\: False
                            
                            .. attribute:: intf_handle
                            
                            	intf handle
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            	**config**\: False
                            
                            .. attribute:: admin_state
                            
                            	admin state
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            	**config**\: False
                            
                            .. attribute:: admin_up
                            
                            	admin up
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: is_created
                            
                            	is created
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ncs5500-coherent-node-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData, self).__init__()

                                self.yang_name = "eth-data"
                                self.yang_parent_name = "interface-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ifname', (YLeaf(YType.str, 'ifname'), ['str'])),
                                    ('intf_handle', (YLeaf(YType.str, 'intf-handle'), ['str'])),
                                    ('admin_state', (YLeaf(YType.str, 'admin-state'), ['str'])),
                                    ('admin_up', (YLeaf(YType.boolean, 'admin-up'), ['bool'])),
                                    ('is_created', (YLeaf(YType.boolean, 'is-created'), ['bool'])),
                                ])
                                self.ifname = None
                                self.intf_handle = None
                                self.admin_state = None
                                self.admin_up = None
                                self.is_created = None
                                self._segment_path = lambda: "eth-data"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData, [u'ifname', u'intf_handle', u'admin_state', u'admin_up', u'is_created'], name, value)







    def clone_ptr(self):
        self._top_entity = Coherent()
        return self._top_entity




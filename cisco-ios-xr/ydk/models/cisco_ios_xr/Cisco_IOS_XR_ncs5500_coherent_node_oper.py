""" Cisco_IOS_XR_ncs5500_coherent_node_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5500\-coherent\-node package operational data.

This module contains definitions
for the following management objects\:
  coherent\: Coherent node  operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Coherent(Entity):
    """
    Coherent node  operational data
    
    .. attribute:: nodes
    
    	Coherent list of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes>`
    
    

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
        self._child_container_classes = {"nodes" : ("nodes", Coherent.Nodes)}
        self._child_list_classes = {}

        self.nodes = Coherent.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-ncs5500-coherent-node-oper:coherent"


    class Nodes(Entity):
        """
        Coherent list of nodes
        
        .. attribute:: node
        
        	Coherent discovery operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node>`
        
        

        """

        _prefix = 'ncs5500-coherent-node-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Coherent.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "coherent"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", Coherent.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs5500-coherent-node-oper:coherent/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Coherent.Nodes, [], name, value)


        class Node(Entity):
            """
            Coherent discovery operational data for a
            particular node
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: coherent_time_stats
            
            	Coherent driver performace information
            	**type**\:   :py:class:`CoherentTimeStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats>`
            
            .. attribute:: coherenthealth
            
            	Coherent node data for driver health
            	**type**\:   :py:class:`Coherenthealth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth>`
            
            .. attribute:: devicemapping
            
            	Coherent node data for device \_mapping
            	**type**\:   :py:class:`Devicemapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Devicemapping>`
            
            .. attribute:: port_mode_all_info
            
            	PortMode all operational data
            	**type**\:   :py:class:`PortModeAllInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.PortModeAllInfo>`
            
            

            """

            _prefix = 'ncs5500-coherent-node-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Coherent.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"coherent-time-stats" : ("coherent_time_stats", Coherent.Nodes.Node.CoherentTimeStats), "coherenthealth" : ("coherenthealth", Coherent.Nodes.Node.Coherenthealth), "devicemapping" : ("devicemapping", Coherent.Nodes.Node.Devicemapping), "port-mode-all-info" : ("port_mode_all_info", Coherent.Nodes.Node.PortModeAllInfo)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.coherent_time_stats = Coherent.Nodes.Node.CoherentTimeStats()
                self.coherent_time_stats.parent = self
                self._children_name_map["coherent_time_stats"] = "coherent-time-stats"
                self._children_yang_names.add("coherent-time-stats")

                self.coherenthealth = Coherent.Nodes.Node.Coherenthealth()
                self.coherenthealth.parent = self
                self._children_name_map["coherenthealth"] = "coherenthealth"
                self._children_yang_names.add("coherenthealth")

                self.devicemapping = Coherent.Nodes.Node.Devicemapping()
                self.devicemapping.parent = self
                self._children_name_map["devicemapping"] = "devicemapping"
                self._children_yang_names.add("devicemapping")

                self.port_mode_all_info = Coherent.Nodes.Node.PortModeAllInfo()
                self.port_mode_all_info.parent = self
                self._children_name_map["port_mode_all_info"] = "port-mode-all-info"
                self._children_yang_names.add("port-mode-all-info")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs5500-coherent-node-oper:coherent/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Coherent.Nodes.Node, ['node_name'], name, value)


            class CoherentTimeStats(Entity):
                """
                Coherent driver performace information
                
                .. attribute:: device_created
                
                	device created
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: driver_init
                
                	driver init
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: driver_operational
                
                	driver operational
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dsp_controllers_created
                
                	dsp controllers created
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dsp_ea_bulk_create
                
                	dsp ea bulk create
                	**type**\:   :py:class:`DspEaBulkCreate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate>`
                
                .. attribute:: dsp_ea_bulk_update
                
                	dsp ea bulk update
                	**type**\:   :py:class:`DspEaBulkUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate>`
                
                .. attribute:: eth_intf_created
                
                	eth intf created
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: optics_controllers_created
                
                	optics controllers created
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: opts_ea_bulk_create
                
                	opts ea bulk create
                	**type**\:   :py:class:`OptsEaBulkCreate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate>`
                
                .. attribute:: opts_ea_bulk_update
                
                	opts ea bulk update
                	**type**\:   :py:class:`OptsEaBulkUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate>`
                
                .. attribute:: port_stat
                
                	port stat
                	**type**\: list of    :py:class:`PortStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat>`
                
                

                """

                _prefix = 'ncs5500-coherent-node-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Coherent.Nodes.Node.CoherentTimeStats, self).__init__()

                    self.yang_name = "coherent-time-stats"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"dsp-ea-bulk-create" : ("dsp_ea_bulk_create", Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate), "dsp-ea-bulk-update" : ("dsp_ea_bulk_update", Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate), "opts-ea-bulk-create" : ("opts_ea_bulk_create", Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate), "opts-ea-bulk-update" : ("opts_ea_bulk_update", Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate)}
                    self._child_list_classes = {"port-stat" : ("port_stat", Coherent.Nodes.Node.CoherentTimeStats.PortStat)}

                    self.device_created = YLeaf(YType.str, "device-created")

                    self.driver_init = YLeaf(YType.str, "driver-init")

                    self.driver_operational = YLeaf(YType.str, "driver-operational")

                    self.dsp_controllers_created = YLeaf(YType.str, "dsp-controllers-created")

                    self.eth_intf_created = YLeaf(YType.str, "eth-intf-created")

                    self.optics_controllers_created = YLeaf(YType.str, "optics-controllers-created")

                    self.dsp_ea_bulk_create = Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate()
                    self.dsp_ea_bulk_create.parent = self
                    self._children_name_map["dsp_ea_bulk_create"] = "dsp-ea-bulk-create"
                    self._children_yang_names.add("dsp-ea-bulk-create")

                    self.dsp_ea_bulk_update = Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate()
                    self.dsp_ea_bulk_update.parent = self
                    self._children_name_map["dsp_ea_bulk_update"] = "dsp-ea-bulk-update"
                    self._children_yang_names.add("dsp-ea-bulk-update")

                    self.opts_ea_bulk_create = Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate()
                    self.opts_ea_bulk_create.parent = self
                    self._children_name_map["opts_ea_bulk_create"] = "opts-ea-bulk-create"
                    self._children_yang_names.add("opts-ea-bulk-create")

                    self.opts_ea_bulk_update = Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate()
                    self.opts_ea_bulk_update.parent = self
                    self._children_name_map["opts_ea_bulk_update"] = "opts-ea-bulk-update"
                    self._children_yang_names.add("opts-ea-bulk-update")

                    self.port_stat = YList(self)
                    self._segment_path = lambda: "coherent-time-stats"

                def __setattr__(self, name, value):
                    self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats, ['device_created', 'driver_init', 'driver_operational', 'dsp_controllers_created', 'eth_intf_created', 'optics_controllers_created'], name, value)


                class DspEaBulkCreate(Entity):
                    """
                    dsp ea bulk create
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate, self).__init__()

                        self.yang_name = "dsp-ea-bulk-create"
                        self.yang_parent_name = "coherent-time-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.end = YLeaf(YType.str, "end")

                        self.start = YLeaf(YType.str, "start")

                        self.time_taken = YLeaf(YType.str, "time-taken")

                        self.worst_time = YLeaf(YType.str, "worst-time")
                        self._segment_path = lambda: "dsp-ea-bulk-create"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate, ['end', 'start', 'time_taken', 'worst_time'], name, value)


                class DspEaBulkUpdate(Entity):
                    """
                    dsp ea bulk update
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate, self).__init__()

                        self.yang_name = "dsp-ea-bulk-update"
                        self.yang_parent_name = "coherent-time-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.end = YLeaf(YType.str, "end")

                        self.start = YLeaf(YType.str, "start")

                        self.time_taken = YLeaf(YType.str, "time-taken")

                        self.worst_time = YLeaf(YType.str, "worst-time")
                        self._segment_path = lambda: "dsp-ea-bulk-update"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate, ['end', 'start', 'time_taken', 'worst_time'], name, value)


                class OptsEaBulkCreate(Entity):
                    """
                    opts ea bulk create
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate, self).__init__()

                        self.yang_name = "opts-ea-bulk-create"
                        self.yang_parent_name = "coherent-time-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.end = YLeaf(YType.str, "end")

                        self.start = YLeaf(YType.str, "start")

                        self.time_taken = YLeaf(YType.str, "time-taken")

                        self.worst_time = YLeaf(YType.str, "worst-time")
                        self._segment_path = lambda: "opts-ea-bulk-create"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate, ['end', 'start', 'time_taken', 'worst_time'], name, value)


                class OptsEaBulkUpdate(Entity):
                    """
                    opts ea bulk update
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate, self).__init__()

                        self.yang_name = "opts-ea-bulk-update"
                        self.yang_parent_name = "coherent-time-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.end = YLeaf(YType.str, "end")

                        self.start = YLeaf(YType.str, "start")

                        self.time_taken = YLeaf(YType.str, "time-taken")

                        self.worst_time = YLeaf(YType.str, "worst-time")
                        self._segment_path = lambda: "opts-ea-bulk-update"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate, ['end', 'start', 'time_taken', 'worst_time'], name, value)


                class PortStat(Entity):
                    """
                    port stat
                    
                    .. attribute:: cd_max
                    
                    	cd max
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cd_min
                    
                    	cd min
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cdmax_op_stats
                    
                    	cdmax op stats
                    	**type**\:   :py:class:`CdmaxOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats>`
                    
                    .. attribute:: cdmin_op_stats
                    
                    	cdmin op stats
                    	**type**\:   :py:class:`CdminOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats>`
                    
                    .. attribute:: laser_off_stats
                    
                    	laser off stats
                    	**type**\:   :py:class:`LaserOffStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats>`
                    
                    .. attribute:: laser_on_stats
                    
                    	laser on stats
                    	**type**\:   :py:class:`LaserOnStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats>`
                    
                    .. attribute:: laser_state
                    
                    	laser state
                    	**type**\:  bool
                    
                    .. attribute:: provisioned_frequency
                    
                    	provisioned frequency
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: traffic_type
                    
                    	traffic type
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: traffictype_op_stats
                    
                    	traffictype op stats
                    	**type**\:   :py:class:`TraffictypeOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats>`
                    
                    .. attribute:: tx_power
                    
                    	tx power
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: txpwr_op_stats
                    
                    	txpwr op stats
                    	**type**\:   :py:class:`TxpwrOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats>`
                    
                    .. attribute:: wl_op_stats
                    
                    	wl op stats
                    	**type**\:   :py:class:`WlOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats>`
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.CoherentTimeStats.PortStat, self).__init__()

                        self.yang_name = "port-stat"
                        self.yang_parent_name = "coherent-time-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"cdmax-op-stats" : ("cdmax_op_stats", Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats), "cdmin-op-stats" : ("cdmin_op_stats", Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats), "laser-off-stats" : ("laser_off_stats", Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats), "laser-on-stats" : ("laser_on_stats", Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats), "traffictype-op-stats" : ("traffictype_op_stats", Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats), "txpwr-op-stats" : ("txpwr_op_stats", Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats), "wl-op-stats" : ("wl_op_stats", Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats)}
                        self._child_list_classes = {}

                        self.cd_max = YLeaf(YType.uint32, "cd-max")

                        self.cd_min = YLeaf(YType.uint32, "cd-min")

                        self.laser_state = YLeaf(YType.boolean, "laser-state")

                        self.provisioned_frequency = YLeaf(YType.uint32, "provisioned-frequency")

                        self.traffic_type = YLeaf(YType.str, "traffic-type")

                        self.tx_power = YLeaf(YType.uint32, "tx-power")

                        self.cdmax_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats()
                        self.cdmax_op_stats.parent = self
                        self._children_name_map["cdmax_op_stats"] = "cdmax-op-stats"
                        self._children_yang_names.add("cdmax-op-stats")

                        self.cdmin_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats()
                        self.cdmin_op_stats.parent = self
                        self._children_name_map["cdmin_op_stats"] = "cdmin-op-stats"
                        self._children_yang_names.add("cdmin-op-stats")

                        self.laser_off_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats()
                        self.laser_off_stats.parent = self
                        self._children_name_map["laser_off_stats"] = "laser-off-stats"
                        self._children_yang_names.add("laser-off-stats")

                        self.laser_on_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats()
                        self.laser_on_stats.parent = self
                        self._children_name_map["laser_on_stats"] = "laser-on-stats"
                        self._children_yang_names.add("laser-on-stats")

                        self.traffictype_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats()
                        self.traffictype_op_stats.parent = self
                        self._children_name_map["traffictype_op_stats"] = "traffictype-op-stats"
                        self._children_yang_names.add("traffictype-op-stats")

                        self.txpwr_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats()
                        self.txpwr_op_stats.parent = self
                        self._children_name_map["txpwr_op_stats"] = "txpwr-op-stats"
                        self._children_yang_names.add("txpwr-op-stats")

                        self.wl_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats()
                        self.wl_op_stats.parent = self
                        self._children_name_map["wl_op_stats"] = "wl-op-stats"
                        self._children_yang_names.add("wl-op-stats")
                        self._segment_path = lambda: "port-stat"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat, ['cd_max', 'cd_min', 'laser_state', 'provisioned_frequency', 'traffic_type', 'tx_power'], name, value)


                    class CdmaxOpStats(Entity):
                        """
                        cdmax op stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats, self).__init__()

                            self.yang_name = "cdmax-op-stats"
                            self.yang_parent_name = "port-stat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.end = YLeaf(YType.str, "end")

                            self.start = YLeaf(YType.str, "start")

                            self.time_taken = YLeaf(YType.str, "time-taken")

                            self.worst_time = YLeaf(YType.str, "worst-time")
                            self._segment_path = lambda: "cdmax-op-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats, ['end', 'start', 'time_taken', 'worst_time'], name, value)


                    class CdminOpStats(Entity):
                        """
                        cdmin op stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats, self).__init__()

                            self.yang_name = "cdmin-op-stats"
                            self.yang_parent_name = "port-stat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.end = YLeaf(YType.str, "end")

                            self.start = YLeaf(YType.str, "start")

                            self.time_taken = YLeaf(YType.str, "time-taken")

                            self.worst_time = YLeaf(YType.str, "worst-time")
                            self._segment_path = lambda: "cdmin-op-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats, ['end', 'start', 'time_taken', 'worst_time'], name, value)


                    class LaserOffStats(Entity):
                        """
                        laser off stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats, self).__init__()

                            self.yang_name = "laser-off-stats"
                            self.yang_parent_name = "port-stat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.end = YLeaf(YType.str, "end")

                            self.start = YLeaf(YType.str, "start")

                            self.time_taken = YLeaf(YType.str, "time-taken")

                            self.worst_time = YLeaf(YType.str, "worst-time")
                            self._segment_path = lambda: "laser-off-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats, ['end', 'start', 'time_taken', 'worst_time'], name, value)


                    class LaserOnStats(Entity):
                        """
                        laser on stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats, self).__init__()

                            self.yang_name = "laser-on-stats"
                            self.yang_parent_name = "port-stat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.end = YLeaf(YType.str, "end")

                            self.start = YLeaf(YType.str, "start")

                            self.time_taken = YLeaf(YType.str, "time-taken")

                            self.worst_time = YLeaf(YType.str, "worst-time")
                            self._segment_path = lambda: "laser-on-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats, ['end', 'start', 'time_taken', 'worst_time'], name, value)


                    class TraffictypeOpStats(Entity):
                        """
                        traffictype op stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats, self).__init__()

                            self.yang_name = "traffictype-op-stats"
                            self.yang_parent_name = "port-stat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.end = YLeaf(YType.str, "end")

                            self.start = YLeaf(YType.str, "start")

                            self.time_taken = YLeaf(YType.str, "time-taken")

                            self.worst_time = YLeaf(YType.str, "worst-time")
                            self._segment_path = lambda: "traffictype-op-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats, ['end', 'start', 'time_taken', 'worst_time'], name, value)


                    class TxpwrOpStats(Entity):
                        """
                        txpwr op stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats, self).__init__()

                            self.yang_name = "txpwr-op-stats"
                            self.yang_parent_name = "port-stat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.end = YLeaf(YType.str, "end")

                            self.start = YLeaf(YType.str, "start")

                            self.time_taken = YLeaf(YType.str, "time-taken")

                            self.worst_time = YLeaf(YType.str, "worst-time")
                            self._segment_path = lambda: "txpwr-op-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats, ['end', 'start', 'time_taken', 'worst_time'], name, value)


                    class WlOpStats(Entity):
                        """
                        wl op stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats, self).__init__()

                            self.yang_name = "wl-op-stats"
                            self.yang_parent_name = "port-stat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.end = YLeaf(YType.str, "end")

                            self.start = YLeaf(YType.str, "start")

                            self.time_taken = YLeaf(YType.str, "time-taken")

                            self.worst_time = YLeaf(YType.str, "worst-time")
                            self._segment_path = lambda: "wl-op-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats, ['end', 'start', 'time_taken', 'worst_time'], name, value)


            class Coherenthealth(Entity):
                """
                Coherent node data for driver health
                
                .. attribute:: aipc_srvr_state
                
                	aipc srvr state
                	**type**\:  bool
                
                .. attribute:: board_type
                
                	board type
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: denali0_version
                
                	denali0 version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: denali1_version
                
                	denali1 version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: denali2_version
                
                	denali2 version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dsp_ea_conn
                
                	dsp ea conn
                	**type**\:  bool
                
                .. attribute:: fpd_in_progress
                
                	fpd in progress
                	**type**\:  bool
                
                .. attribute:: im_state
                
                	im state
                	**type**\:  bool
                
                .. attribute:: inside_prov_loop
                
                	inside prov loop
                	**type**\:  bool
                
                .. attribute:: jlink_op
                
                	jlink op
                	**type**\:  str
                
                	**length:** 0..6144
                
                .. attribute:: morgoth_alive
                
                	morgoth alive
                	**type**\:  bool
                
                .. attribute:: morgoth_downloaded_version
                
                	morgoth downloaded version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: morgoth_golden_version
                
                	morgoth golden version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: morgoth_running_version
                
                	morgoth running version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: optics_ea_conn
                
                	optics ea conn
                	**type**\:  bool
                
                .. attribute:: pending_provision
                
                	pending provision
                	**type**\:  bool
                
                .. attribute:: pm_state
                
                	pm state
                	**type**\:  bool
                
                .. attribute:: port_data
                
                	port data
                	**type**\: list of    :py:class:`PortData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData>`
                
                .. attribute:: prov_infra_state
                
                	prov infra state
                	**type**\:  bool
                
                .. attribute:: prov_run_count
                
                	prov run count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pulse_sent
                
                	pulse sent
                	**type**\:  bool
                
                .. attribute:: sdk_fpga_compatible
                
                	sdk fpga compatible
                	**type**\:  bool
                
                .. attribute:: sdk_version
                
                	sdk version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: sysdb_state
                
                	sysdb state
                	**type**\:  bool
                
                .. attribute:: vether_state
                
                	vether state
                	**type**\:  bool
                
                

                """

                _prefix = 'ncs5500-coherent-node-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Coherent.Nodes.Node.Coherenthealth, self).__init__()

                    self.yang_name = "coherenthealth"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"port-data" : ("port_data", Coherent.Nodes.Node.Coherenthealth.PortData)}

                    self.aipc_srvr_state = YLeaf(YType.boolean, "aipc-srvr-state")

                    self.board_type = YLeaf(YType.str, "board-type")

                    self.denali0_version = YLeaf(YType.str, "denali0-version")

                    self.denali1_version = YLeaf(YType.str, "denali1-version")

                    self.denali2_version = YLeaf(YType.str, "denali2-version")

                    self.dsp_ea_conn = YLeaf(YType.boolean, "dsp-ea-conn")

                    self.fpd_in_progress = YLeaf(YType.boolean, "fpd-in-progress")

                    self.im_state = YLeaf(YType.boolean, "im-state")

                    self.inside_prov_loop = YLeaf(YType.boolean, "inside-prov-loop")

                    self.jlink_op = YLeaf(YType.str, "jlink-op")

                    self.morgoth_alive = YLeaf(YType.boolean, "morgoth-alive")

                    self.morgoth_downloaded_version = YLeaf(YType.str, "morgoth-downloaded-version")

                    self.morgoth_golden_version = YLeaf(YType.str, "morgoth-golden-version")

                    self.morgoth_running_version = YLeaf(YType.str, "morgoth-running-version")

                    self.optics_ea_conn = YLeaf(YType.boolean, "optics-ea-conn")

                    self.pending_provision = YLeaf(YType.boolean, "pending-provision")

                    self.pm_state = YLeaf(YType.boolean, "pm-state")

                    self.prov_infra_state = YLeaf(YType.boolean, "prov-infra-state")

                    self.prov_run_count = YLeaf(YType.uint32, "prov-run-count")

                    self.pulse_sent = YLeaf(YType.boolean, "pulse-sent")

                    self.sdk_fpga_compatible = YLeaf(YType.boolean, "sdk-fpga-compatible")

                    self.sdk_version = YLeaf(YType.str, "sdk-version")

                    self.sysdb_state = YLeaf(YType.boolean, "sysdb-state")

                    self.vether_state = YLeaf(YType.boolean, "vether-state")

                    self.port_data = YList(self)
                    self._segment_path = lambda: "coherenthealth"

                def __setattr__(self, name, value):
                    self._perform_setattr(Coherent.Nodes.Node.Coherenthealth, ['aipc_srvr_state', 'board_type', 'denali0_version', 'denali1_version', 'denali2_version', 'dsp_ea_conn', 'fpd_in_progress', 'im_state', 'inside_prov_loop', 'jlink_op', 'morgoth_alive', 'morgoth_downloaded_version', 'morgoth_golden_version', 'morgoth_running_version', 'optics_ea_conn', 'pending_provision', 'pm_state', 'prov_infra_state', 'prov_run_count', 'pulse_sent', 'sdk_fpga_compatible', 'sdk_version', 'sysdb_state', 'vether_state'], name, value)


                class PortData(Entity):
                    """
                    port data
                    
                    .. attribute:: cd_max_op_rc
                    
                    	cd max op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: cd_min_op_rc
                    
                    	cd min op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: configured_cd_max
                    
                    	configured cd max
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: configured_cd_min
                    
                    	configured cd min
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: configured_frequency
                    
                    	configured frequency
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: configured_loopback_mode
                    
                    	configured loopback mode
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: configured_traffic_type
                    
                    	configured traffic type
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: configured_tx_power
                    
                    	configured tx power
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: ctp2_hw_alarms
                    
                    	ctp2 hw alarms
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: ctp_info
                    
                    	ctp info
                    	**type**\:   :py:class:`CtpInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo>`
                    
                    .. attribute:: denali_hw_alarms
                    
                    	denali hw alarms
                    	**type**\:  str
                    
                    	**length:** 0..256
                    
                    .. attribute:: dsp_admin_up
                    
                    	dsp admin up
                    	**type**\:  bool
                    
                    .. attribute:: dsp_ctrl_created
                    
                    	dsp ctrl created
                    	**type**\:  bool
                    
                    .. attribute:: expected_ctp2_led_state
                    
                    	expected ctp2 led state
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: force_reprovision
                    
                    	force reprovision
                    	**type**\:  bool
                    
                    .. attribute:: fp_port_idx
                    
                    	fp port idx
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: has_pluggable
                    
                    	has pluggable
                    	**type**\:  bool
                    
                    .. attribute:: interface_info
                    
                    	interface info
                    	**type**\:   :py:class:`InterfaceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo>`
                    
                    .. attribute:: is_alarm_port_created_dsp
                    
                    	is alarm port created dsp
                    	**type**\:  bool
                    
                    .. attribute:: is_alarm_port_created_opt
                    
                    	is alarm port created opt
                    	**type**\:  bool
                    
                    .. attribute:: is_pm_port_created_dsp
                    
                    	is pm port created dsp
                    	**type**\:  bool
                    
                    .. attribute:: is_pm_port_created_opt
                    
                    	is pm port created opt
                    	**type**\:  bool
                    
                    .. attribute:: laser_on_pending
                    
                    	laser on pending
                    	**type**\:  bool
                    
                    .. attribute:: laser_op_rc
                    
                    	laser op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_state
                    
                    	laser state
                    	**type**\:  bool
                    
                    .. attribute:: led_op_rc
                    
                    	led op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: loopback_op_rc
                    
                    	loopback op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: optics_admin_up
                    
                    	optics admin up
                    	**type**\:  bool
                    
                    .. attribute:: optics_ctrl_created
                    
                    	optics ctrl created
                    	**type**\:  bool
                    
                    .. attribute:: pm_port_state_dsp
                    
                    	pm port state dsp
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: pm_port_state_opt
                    
                    	pm port state opt
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: provisioned_cd_max
                    
                    	provisioned cd max
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: provisioned_cd_min
                    
                    	provisioned cd min
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: provisioned_ctp2_led_state
                    
                    	provisioned ctp2 led state
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: provisioned_frequency
                    
                    	provisioned frequency
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: provisioned_loopback_mode
                    
                    	provisioned loopback mode
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: provisioned_traffic_type
                    
                    	provisioned traffic type
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: provisioned_tx_power
                    
                    	provisioned tx power
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: provisioning_failed
                    
                    	provisioning failed
                    	**type**\:  bool
                    
                    .. attribute:: provisioning_needed
                    
                    	provisioning needed
                    	**type**\:  bool
                    
                    .. attribute:: rc_alarm_port_dsp
                    
                    	rc alarm port dsp
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: rc_alarm_port_opt
                    
                    	rc alarm port opt
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: rc_pm_port_dsp
                    
                    	rc pm port dsp
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: rc_pm_port_opt
                    
                    	rc pm port opt
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: rc_pm_provision_dsp
                    
                    	rc pm provision dsp
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: rc_pm_provision_opt
                    
                    	rc pm provision opt
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: traffic_op_rc
                    
                    	traffic op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tx_power_op_rc
                    
                    	tx power op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: wlen_op_rc
                    
                    	wlen op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.Coherenthealth.PortData, self).__init__()

                        self.yang_name = "port-data"
                        self.yang_parent_name = "coherenthealth"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"ctp-info" : ("ctp_info", Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo), "interface-info" : ("interface_info", Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo)}
                        self._child_list_classes = {}

                        self.cd_max_op_rc = YLeaf(YType.int32, "cd-max-op-rc")

                        self.cd_min_op_rc = YLeaf(YType.int32, "cd-min-op-rc")

                        self.configured_cd_max = YLeaf(YType.str, "configured-cd-max")

                        self.configured_cd_min = YLeaf(YType.str, "configured-cd-min")

                        self.configured_frequency = YLeaf(YType.uint32, "configured-frequency")

                        self.configured_loopback_mode = YLeaf(YType.str, "configured-loopback-mode")

                        self.configured_traffic_type = YLeaf(YType.str, "configured-traffic-type")

                        self.configured_tx_power = YLeaf(YType.str, "configured-tx-power")

                        self.ctp2_hw_alarms = YLeaf(YType.str, "ctp2-hw-alarms")

                        self.denali_hw_alarms = YLeaf(YType.str, "denali-hw-alarms")

                        self.dsp_admin_up = YLeaf(YType.boolean, "dsp-admin-up")

                        self.dsp_ctrl_created = YLeaf(YType.boolean, "dsp-ctrl-created")

                        self.expected_ctp2_led_state = YLeaf(YType.str, "expected-ctp2-led-state")

                        self.force_reprovision = YLeaf(YType.boolean, "force-reprovision")

                        self.fp_port_idx = YLeaf(YType.uint32, "fp-port-idx")

                        self.has_pluggable = YLeaf(YType.boolean, "has-pluggable")

                        self.is_alarm_port_created_dsp = YLeaf(YType.boolean, "is-alarm-port-created-dsp")

                        self.is_alarm_port_created_opt = YLeaf(YType.boolean, "is-alarm-port-created-opt")

                        self.is_pm_port_created_dsp = YLeaf(YType.boolean, "is-pm-port-created-dsp")

                        self.is_pm_port_created_opt = YLeaf(YType.boolean, "is-pm-port-created-opt")

                        self.laser_on_pending = YLeaf(YType.boolean, "laser-on-pending")

                        self.laser_op_rc = YLeaf(YType.int32, "laser-op-rc")

                        self.laser_state = YLeaf(YType.boolean, "laser-state")

                        self.led_op_rc = YLeaf(YType.int32, "led-op-rc")

                        self.loopback_op_rc = YLeaf(YType.int32, "loopback-op-rc")

                        self.optics_admin_up = YLeaf(YType.boolean, "optics-admin-up")

                        self.optics_ctrl_created = YLeaf(YType.boolean, "optics-ctrl-created")

                        self.pm_port_state_dsp = YLeaf(YType.int32, "pm-port-state-dsp")

                        self.pm_port_state_opt = YLeaf(YType.int32, "pm-port-state-opt")

                        self.provisioned_cd_max = YLeaf(YType.str, "provisioned-cd-max")

                        self.provisioned_cd_min = YLeaf(YType.str, "provisioned-cd-min")

                        self.provisioned_ctp2_led_state = YLeaf(YType.str, "provisioned-ctp2-led-state")

                        self.provisioned_frequency = YLeaf(YType.uint32, "provisioned-frequency")

                        self.provisioned_loopback_mode = YLeaf(YType.str, "provisioned-loopback-mode")

                        self.provisioned_traffic_type = YLeaf(YType.str, "provisioned-traffic-type")

                        self.provisioned_tx_power = YLeaf(YType.str, "provisioned-tx-power")

                        self.provisioning_failed = YLeaf(YType.boolean, "provisioning-failed")

                        self.provisioning_needed = YLeaf(YType.boolean, "provisioning-needed")

                        self.rc_alarm_port_dsp = YLeaf(YType.int32, "rc-alarm-port-dsp")

                        self.rc_alarm_port_opt = YLeaf(YType.int32, "rc-alarm-port-opt")

                        self.rc_pm_port_dsp = YLeaf(YType.int32, "rc-pm-port-dsp")

                        self.rc_pm_port_opt = YLeaf(YType.int32, "rc-pm-port-opt")

                        self.rc_pm_provision_dsp = YLeaf(YType.int32, "rc-pm-provision-dsp")

                        self.rc_pm_provision_opt = YLeaf(YType.int32, "rc-pm-provision-opt")

                        self.traffic_op_rc = YLeaf(YType.int32, "traffic-op-rc")

                        self.tx_power_op_rc = YLeaf(YType.int32, "tx-power-op-rc")

                        self.wlen_op_rc = YLeaf(YType.int32, "wlen-op-rc")

                        self.ctp_info = Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo()
                        self.ctp_info.parent = self
                        self._children_name_map["ctp_info"] = "ctp-info"
                        self._children_yang_names.add("ctp-info")

                        self.interface_info = Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo()
                        self.interface_info.parent = self
                        self._children_name_map["interface_info"] = "interface-info"
                        self._children_yang_names.add("interface-info")
                        self._segment_path = lambda: "port-data"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Coherent.Nodes.Node.Coherenthealth.PortData, ['cd_max_op_rc', 'cd_min_op_rc', 'configured_cd_max', 'configured_cd_min', 'configured_frequency', 'configured_loopback_mode', 'configured_traffic_type', 'configured_tx_power', 'ctp2_hw_alarms', 'denali_hw_alarms', 'dsp_admin_up', 'dsp_ctrl_created', 'expected_ctp2_led_state', 'force_reprovision', 'fp_port_idx', 'has_pluggable', 'is_alarm_port_created_dsp', 'is_alarm_port_created_opt', 'is_pm_port_created_dsp', 'is_pm_port_created_opt', 'laser_on_pending', 'laser_op_rc', 'laser_state', 'led_op_rc', 'loopback_op_rc', 'optics_admin_up', 'optics_ctrl_created', 'pm_port_state_dsp', 'pm_port_state_opt', 'provisioned_cd_max', 'provisioned_cd_min', 'provisioned_ctp2_led_state', 'provisioned_frequency', 'provisioned_loopback_mode', 'provisioned_traffic_type', 'provisioned_tx_power', 'provisioning_failed', 'provisioning_needed', 'rc_alarm_port_dsp', 'rc_alarm_port_opt', 'rc_pm_port_dsp', 'rc_pm_port_opt', 'rc_pm_provision_dsp', 'rc_pm_provision_opt', 'traffic_op_rc', 'tx_power_op_rc', 'wlen_op_rc'], name, value)


                    class CtpInfo(Entity):
                        """
                        ctp info
                        
                        .. attribute:: clei_code_number
                        
                        	CLEI code number
                        	**type**\:  str
                        
                        	**length:** 0..10
                        
                        .. attribute:: ctp_type
                        
                        	ctp type
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: date_code_number
                        
                        	date code number
                        	**type**\:  str
                        
                        	**length:** 0..10
                        
                        .. attribute:: description
                        
                        	description
                        	**type**\:  str
                        
                        	**length:** 0..64
                        
                        .. attribute:: deviation
                        
                        	deviation
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        .. attribute:: module_firmware_committed_version_number
                        
                        	module firmware committed version number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: module_firmware_running_version_number
                        
                        	module firmware running version number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: module_hardware_version_number
                        
                        	module hardware version number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: part_number
                        
                        	part number
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        .. attribute:: pid
                        
                        	pid
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        .. attribute:: serial_number
                        
                        	serial number
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        .. attribute:: vendorname
                        
                        	vendorname
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        .. attribute:: vid
                        
                        	vid
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo, self).__init__()

                            self.yang_name = "ctp-info"
                            self.yang_parent_name = "port-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.clei_code_number = YLeaf(YType.str, "clei-code-number")

                            self.ctp_type = YLeaf(YType.uint32, "ctp-type")

                            self.date_code_number = YLeaf(YType.str, "date-code-number")

                            self.description = YLeaf(YType.str, "description")

                            self.deviation = YLeaf(YType.str, "deviation")

                            self.module_firmware_committed_version_number = YLeaf(YType.uint16, "module-firmware-committed-version-number")

                            self.module_firmware_running_version_number = YLeaf(YType.uint16, "module-firmware-running-version-number")

                            self.module_hardware_version_number = YLeaf(YType.uint16, "module-hardware-version-number")

                            self.part_number = YLeaf(YType.str, "part-number")

                            self.pid = YLeaf(YType.str, "pid")

                            self.serial_number = YLeaf(YType.str, "serial-number")

                            self.vendorname = YLeaf(YType.str, "vendorname")

                            self.vid = YLeaf(YType.str, "vid")
                            self._segment_path = lambda: "ctp-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo, ['clei_code_number', 'ctp_type', 'date_code_number', 'description', 'deviation', 'module_firmware_committed_version_number', 'module_firmware_running_version_number', 'module_hardware_version_number', 'part_number', 'pid', 'serial_number', 'vendorname', 'vid'], name, value)


                    class InterfaceInfo(Entity):
                        """
                        interface info
                        
                        .. attribute:: eth_data
                        
                        	eth data
                        	**type**\: list of    :py:class:`EthData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData>`
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo, self).__init__()

                            self.yang_name = "interface-info"
                            self.yang_parent_name = "port-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"eth-data" : ("eth_data", Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData)}

                            self.eth_data = YList(self)
                            self._segment_path = lambda: "interface-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo, [], name, value)


                        class EthData(Entity):
                            """
                            eth data
                            
                            .. attribute:: admin_state
                            
                            	admin state
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: admin_up
                            
                            	admin up
                            	**type**\:  bool
                            
                            .. attribute:: ifname
                            
                            	ifname
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: intf_handle
                            
                            	intf handle
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: is_created
                            
                            	is created
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'ncs5500-coherent-node-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData, self).__init__()

                                self.yang_name = "eth-data"
                                self.yang_parent_name = "interface-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.admin_state = YLeaf(YType.str, "admin-state")

                                self.admin_up = YLeaf(YType.boolean, "admin-up")

                                self.ifname = YLeaf(YType.str, "ifname")

                                self.intf_handle = YLeaf(YType.str, "intf-handle")

                                self.is_created = YLeaf(YType.boolean, "is-created")
                                self._segment_path = lambda: "eth-data"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData, ['admin_state', 'admin_up', 'ifname', 'intf_handle', 'is_created'], name, value)


            class Devicemapping(Entity):
                """
                Coherent node data for device \_mapping
                
                .. attribute:: dev_map
                
                	dev map
                	**type**\: list of    :py:class:`DevMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Devicemapping.DevMap>`
                
                .. attribute:: idx
                
                	idx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ncs5500-coherent-node-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Coherent.Nodes.Node.Devicemapping, self).__init__()

                    self.yang_name = "devicemapping"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"dev-map" : ("dev_map", Coherent.Nodes.Node.Devicemapping.DevMap)}

                    self.idx = YLeaf(YType.uint32, "idx")

                    self.dev_map = YList(self)
                    self._segment_path = lambda: "devicemapping"

                def __setattr__(self, name, value):
                    self._perform_setattr(Coherent.Nodes.Node.Devicemapping, ['idx'], name, value)


                class DevMap(Entity):
                    """
                    dev map
                    
                    .. attribute:: device_address
                    
                    	device address
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: ifhandle
                    
                    	ifhandle
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: intf_name
                    
                    	intf name
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.Devicemapping.DevMap, self).__init__()

                        self.yang_name = "dev-map"
                        self.yang_parent_name = "devicemapping"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.device_address = YLeaf(YType.str, "device-address")

                        self.ifhandle = YLeaf(YType.str, "ifhandle")

                        self.intf_name = YLeaf(YType.str, "intf-name")
                        self._segment_path = lambda: "dev-map"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Coherent.Nodes.Node.Devicemapping.DevMap, ['device_address', 'ifhandle', 'intf_name'], name, value)


            class PortModeAllInfo(Entity):
                """
                PortMode all operational data
                
                .. attribute:: idx
                
                	dev map idx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: portmode_entry
                
                	portmode entry
                	**type**\: list of    :py:class:`PortmodeEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.PortModeAllInfo.PortmodeEntry>`
                
                

                """

                _prefix = 'ncs5500-coherent-node-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Coherent.Nodes.Node.PortModeAllInfo, self).__init__()

                    self.yang_name = "port-mode-all-info"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"portmode-entry" : ("portmode_entry", Coherent.Nodes.Node.PortModeAllInfo.PortmodeEntry)}

                    self.idx = YLeaf(YType.uint32, "idx")

                    self.portmode_entry = YList(self)
                    self._segment_path = lambda: "port-mode-all-info"

                def __setattr__(self, name, value):
                    self._perform_setattr(Coherent.Nodes.Node.PortModeAllInfo, ['idx'], name, value)


                class PortmodeEntry(Entity):
                    """
                    portmode entry
                    
                    .. attribute:: diff
                    
                    	diff
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: fec
                    
                    	fec
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: intf_name
                    
                    	intf name
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: modulation
                    
                    	modulation
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: speed
                    
                    	speed
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Coherent.Nodes.Node.PortModeAllInfo.PortmodeEntry, self).__init__()

                        self.yang_name = "portmode-entry"
                        self.yang_parent_name = "port-mode-all-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.diff = YLeaf(YType.str, "diff")

                        self.fec = YLeaf(YType.str, "fec")

                        self.intf_name = YLeaf(YType.str, "intf-name")

                        self.modulation = YLeaf(YType.str, "modulation")

                        self.speed = YLeaf(YType.str, "speed")
                        self._segment_path = lambda: "portmode-entry"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Coherent.Nodes.Node.PortModeAllInfo.PortmodeEntry, ['diff', 'fec', 'intf_name', 'modulation', 'speed'], name, value)

    def clone_ptr(self):
        self._top_entity = Coherent()
        return self._top_entity


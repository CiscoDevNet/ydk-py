""" Cisco_IOS_XR_dnx_driver_fabric_plane_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dnx\-driver\-fabric\-plane package operational data.

This module contains definitions
for the following management objects\:
  fabric\: Admin fabric oper data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FsdbPlaneAdminState(Enum):
    """
    FsdbPlaneAdminState (Enum Class)

    FSDB Plane admin state enum

    .. data:: plane_state_admin_up = 0

    	plane state admin up

    .. data:: plane_state_admin_down = 1

    	plane state admin down

    """

    plane_state_admin_up = Enum.YLeaf(0, "plane-state-admin-up")

    plane_state_admin_down = Enum.YLeaf(1, "plane-state-admin-down")


class FsdbPlaneMode(Enum):
    """
    FsdbPlaneMode (Enum Class)

    FSDB plane mode enum

    .. data:: plane_mode_unknown = 0

    	plane mode unknown

    .. data:: plane_mode_sc = 1

    	plane mode sc

    .. data:: plane_mode_b2b = 2

    	plane mode b2b

    .. data:: plane_mode_mc = 3

    	plane mode mc

    .. data:: plane_mode_folded = 4

    	plane mode folded

    """

    plane_mode_unknown = Enum.YLeaf(0, "plane-mode-unknown")

    plane_mode_sc = Enum.YLeaf(1, "plane-mode-sc")

    plane_mode_b2b = Enum.YLeaf(2, "plane-mode-b2b")

    plane_mode_mc = Enum.YLeaf(3, "plane-mode-mc")

    plane_mode_folded = Enum.YLeaf(4, "plane-mode-folded")


class FsdbPlaneOperState(Enum):
    """
    FsdbPlaneOperState (Enum Class)

    FSDB plane oper state enum

    .. data:: plane_state_oper_up = 0

    	plane state oper up

    .. data:: plane_state_oper_down = 1

    	plane state oper down

    .. data:: plane_state_oper_mcast_down = 2

    	plane state oper mcast down

    """

    plane_state_oper_up = Enum.YLeaf(0, "plane-state-oper-up")

    plane_state_oper_down = Enum.YLeaf(1, "plane-state-oper-down")

    plane_state_oper_mcast_down = Enum.YLeaf(2, "plane-state-oper-mcast-down")



class Fabric(Entity):
    """
    Admin fabric oper data
    
    .. attribute:: plane_table
    
    	Plane state table for Fabric 
    	**type**\:  :py:class:`PlaneTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_fabric_plane_oper.Fabric.PlaneTable>`
    
    

    """

    _prefix = 'dnx-driver-fabric-plane-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Fabric, self).__init__()
        self._top_entity = None

        self.yang_name = "fabric"
        self.yang_parent_name = "Cisco-IOS-XR-dnx-driver-fabric-plane-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("plane-table", ("plane_table", Fabric.PlaneTable))])
        self._leafs = OrderedDict()

        self.plane_table = Fabric.PlaneTable()
        self.plane_table.parent = self
        self._children_name_map["plane_table"] = "plane-table"
        self._segment_path = lambda: "Cisco-IOS-XR-dnx-driver-fabric-plane-oper:fabric"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Fabric, [], name, value)


    class PlaneTable(Entity):
        """
        Plane state table for Fabric 
        
        .. attribute:: statistics
        
        	Show Calvados Plane Statistics
        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_fabric_plane_oper.Fabric.PlaneTable.Statistics>`
        
        .. attribute:: plane
        
        	Show Calvados Plane State
        	**type**\:  :py:class:`Plane <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_fabric_plane_oper.Fabric.PlaneTable.Plane>`
        
        

        """

        _prefix = 'dnx-driver-fabric-plane-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Fabric.PlaneTable, self).__init__()

            self.yang_name = "plane-table"
            self.yang_parent_name = "fabric"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("statistics", ("statistics", Fabric.PlaneTable.Statistics)), ("plane", ("plane", Fabric.PlaneTable.Plane))])
            self._leafs = OrderedDict()

            self.statistics = Fabric.PlaneTable.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"

            self.plane = Fabric.PlaneTable.Plane()
            self.plane.parent = self
            self._children_name_map["plane"] = "plane"
            self._segment_path = lambda: "plane-table"
            self._absolute_path = lambda: "Cisco-IOS-XR-dnx-driver-fabric-plane-oper:fabric/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Fabric.PlaneTable, [], name, value)


        class Statistics(Entity):
            """
            Show Calvados Plane Statistics
            
            .. attribute:: plane_stats_info
            
            	plane stats info
            	**type**\: list of  		 :py:class:`PlaneStatsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_fabric_plane_oper.Fabric.PlaneTable.Statistics.PlaneStatsInfo>`
            
            

            """

            _prefix = 'dnx-driver-fabric-plane-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Fabric.PlaneTable.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "plane-table"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("plane-stats-info", ("plane_stats_info", Fabric.PlaneTable.Statistics.PlaneStatsInfo))])
                self._leafs = OrderedDict()

                self.plane_stats_info = YList(self)
                self._segment_path = lambda: "statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-dnx-driver-fabric-plane-oper:fabric/plane-table/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Fabric.PlaneTable.Statistics, [], name, value)


            class PlaneStatsInfo(Entity):
                """
                plane stats info
                
                .. attribute:: plane_id
                
                	plane id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: rx_data_cells
                
                	RxDataCells
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_data_cells
                
                	TxDataCells
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_correctable_error_cells
                
                	RxCorrectableErrorCells
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: rx_un_correctable_error_cells
                
                	RxUnCorrectableErrorCells
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: rx_parity_error_cells
                
                	RxParityErrorCells
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'dnx-driver-fabric-plane-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Fabric.PlaneTable.Statistics.PlaneStatsInfo, self).__init__()

                    self.yang_name = "plane-stats-info"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('plane_id', (YLeaf(YType.uint32, 'plane-id'), ['int'])),
                        ('rx_data_cells', (YLeaf(YType.uint64, 'rx-data-cells'), ['int'])),
                        ('tx_data_cells', (YLeaf(YType.uint64, 'tx-data-cells'), ['int'])),
                        ('rx_correctable_error_cells', (YLeaf(YType.uint32, 'rx-correctable-error-cells'), ['int'])),
                        ('rx_un_correctable_error_cells', (YLeaf(YType.uint32, 'rx-un-correctable-error-cells'), ['int'])),
                        ('rx_parity_error_cells', (YLeaf(YType.uint32, 'rx-parity-error-cells'), ['int'])),
                    ])
                    self.plane_id = None
                    self.rx_data_cells = None
                    self.tx_data_cells = None
                    self.rx_correctable_error_cells = None
                    self.rx_un_correctable_error_cells = None
                    self.rx_parity_error_cells = None
                    self._segment_path = lambda: "plane-stats-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-dnx-driver-fabric-plane-oper:fabric/plane-table/statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Fabric.PlaneTable.Statistics.PlaneStatsInfo, ['plane_id', 'rx_data_cells', 'tx_data_cells', 'rx_correctable_error_cells', 'rx_un_correctable_error_cells', 'rx_parity_error_cells'], name, value)


        class Plane(Entity):
            """
            Show Calvados Plane State
            
            .. attribute:: detail_plane_info
            
            	detail plane info
            	**type**\: list of  		 :py:class:`DetailPlaneInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_fabric_plane_oper.Fabric.PlaneTable.Plane.DetailPlaneInfo>`
            
            

            """

            _prefix = 'dnx-driver-fabric-plane-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Fabric.PlaneTable.Plane, self).__init__()

                self.yang_name = "plane"
                self.yang_parent_name = "plane-table"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("detail-plane-info", ("detail_plane_info", Fabric.PlaneTable.Plane.DetailPlaneInfo))])
                self._leafs = OrderedDict()

                self.detail_plane_info = YList(self)
                self._segment_path = lambda: "plane"
                self._absolute_path = lambda: "Cisco-IOS-XR-dnx-driver-fabric-plane-oper:fabric/plane-table/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Fabric.PlaneTable.Plane, [], name, value)


            class DetailPlaneInfo(Entity):
                """
                detail plane info
                
                .. attribute:: plane_id
                
                	plane id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: plane_oper_status
                
                	PlaneOperStatus
                	**type**\:  :py:class:`FsdbPlaneOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_fabric_plane_oper.FsdbPlaneOperState>`
                
                .. attribute:: plane_admin_status
                
                	PlaneAdminStatus
                	**type**\:  :py:class:`FsdbPlaneAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_fabric_plane_oper.FsdbPlaneAdminState>`
                
                .. attribute:: plane_mode
                
                	Plane Mode Configuration
                	**type**\:  :py:class:`FsdbPlaneMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_fabric_plane_oper.FsdbPlaneMode>`
                
                .. attribute:: bundles
                
                	Total number of bundles
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: down_bundles
                
                	Total down bundles
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: plane_up_down_count
                
                	Plane up down count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: up_multicast_count
                
                	Plane up multicast count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ppu_state
                
                	Plane PPU State
                	**type**\: str
                
                

                """

                _prefix = 'dnx-driver-fabric-plane-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Fabric.PlaneTable.Plane.DetailPlaneInfo, self).__init__()

                    self.yang_name = "detail-plane-info"
                    self.yang_parent_name = "plane"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('plane_id', (YLeaf(YType.uint32, 'plane-id'), ['int'])),
                        ('plane_oper_status', (YLeaf(YType.enumeration, 'plane-oper-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_fabric_plane_oper', 'FsdbPlaneOperState', '')])),
                        ('plane_admin_status', (YLeaf(YType.enumeration, 'plane-admin-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_fabric_plane_oper', 'FsdbPlaneAdminState', '')])),
                        ('plane_mode', (YLeaf(YType.enumeration, 'plane-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_fabric_plane_oper', 'FsdbPlaneMode', '')])),
                        ('bundles', (YLeaf(YType.uint16, 'bundles'), ['int'])),
                        ('down_bundles', (YLeaf(YType.uint16, 'down-bundles'), ['int'])),
                        ('plane_up_down_count', (YLeaf(YType.uint32, 'plane-up-down-count'), ['int'])),
                        ('up_multicast_count', (YLeaf(YType.uint32, 'up-multicast-count'), ['int'])),
                        ('ppu_state', (YLeaf(YType.str, 'ppu-state'), ['str'])),
                    ])
                    self.plane_id = None
                    self.plane_oper_status = None
                    self.plane_admin_status = None
                    self.plane_mode = None
                    self.bundles = None
                    self.down_bundles = None
                    self.plane_up_down_count = None
                    self.up_multicast_count = None
                    self.ppu_state = None
                    self._segment_path = lambda: "detail-plane-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-dnx-driver-fabric-plane-oper:fabric/plane-table/plane/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Fabric.PlaneTable.Plane.DetailPlaneInfo, ['plane_id', 'plane_oper_status', 'plane_admin_status', 'plane_mode', 'bundles', 'down_bundles', 'plane_up_down_count', 'up_multicast_count', 'ppu_state'], name, value)

    def clone_ptr(self):
        self._top_entity = Fabric()
        return self._top_entity


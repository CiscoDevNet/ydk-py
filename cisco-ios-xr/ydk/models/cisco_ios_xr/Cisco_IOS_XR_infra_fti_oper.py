""" Cisco_IOS_XR_infra_fti_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-fti package operational data.

This module contains definitions
for the following management objects\:
  dci\-fabric\-interconnect\: Display FTI operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FtiBagFabricConfigState(Enum):
    """
    FtiBagFabricConfigState (Enum Class)

    FTI Fabric Config States

    .. data:: fti_bag_config_complete = 0

    	Config Complete

    .. data:: fti_bag_config_incomplete = 1

    	Config Incomplete

    """

    fti_bag_config_complete = Enum.YLeaf(0, "fti-bag-config-complete")

    fti_bag_config_incomplete = Enum.YLeaf(1, "fti-bag-config-incomplete")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
        return meta._meta_table['FtiBagFabricConfigState']


class FtiBagFabricPeerState(Enum):
    """
    FtiBagFabricPeerState (Enum Class)

    FTI Fabric Peer States

    .. data:: fti_bag_fabric_peer_status_disconnected = 0

    	Disconnected

    .. data:: fti_bag_fabric_peer_status_connecting = 1

    	Connecting

    .. data:: fti_bag_fabric_peer_status_connected = 2

    	Connected

    .. data:: fti_bag_fabric_peer_status_ready = 3

    	Ready

    .. data:: fti_bag_fabric_peer_status_closing = 4

    	Closing

    """

    fti_bag_fabric_peer_status_disconnected = Enum.YLeaf(0, "fti-bag-fabric-peer-status-disconnected")

    fti_bag_fabric_peer_status_connecting = Enum.YLeaf(1, "fti-bag-fabric-peer-status-connecting")

    fti_bag_fabric_peer_status_connected = Enum.YLeaf(2, "fti-bag-fabric-peer-status-connected")

    fti_bag_fabric_peer_status_ready = Enum.YLeaf(3, "fti-bag-fabric-peer-status-ready")

    fti_bag_fabric_peer_status_closing = Enum.YLeaf(4, "fti-bag-fabric-peer-status-closing")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
        return meta._meta_table['FtiBagFabricPeerState']


class FtiBagFabricState(Enum):
    """
    FtiBagFabricState (Enum Class)

    FTI Fabric States

    .. data:: fti_bag_fabric_state_active_down = 0

    	Active (Down)

    .. data:: fti_bag_fabric_state_active_degraded = 1

    	Active (Degraded)

    .. data:: fti_bag_fabric_state_active_healthy = 2

    	Active (Healthy)

    .. data:: fti_bag_fabric_state_inactive = 3

    	Inactive

    """

    fti_bag_fabric_state_active_down = Enum.YLeaf(0, "fti-bag-fabric-state-active-down")

    fti_bag_fabric_state_active_degraded = Enum.YLeaf(1, "fti-bag-fabric-state-active-degraded")

    fti_bag_fabric_state_active_healthy = Enum.YLeaf(2, "fti-bag-fabric-state-active-healthy")

    fti_bag_fabric_state_inactive = Enum.YLeaf(3, "fti-bag-fabric-state-inactive")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
        return meta._meta_table['FtiBagFabricState']



class DciFabricInterconnect(_Entity_):
    """
    Display FTI operational data
    
    .. attribute:: opflex_session_infos
    
    	FTI Opflex Session Info for all fabrics
    	**type**\:  :py:class:`OpflexSessionInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.OpflexSessionInfos>`
    
    	**config**\: False
    
    .. attribute:: fabric_vrf_dbs
    
    	FTI Fabric\-VRF DB for all fabrics
    	**type**\:  :py:class:`FabricVrfDbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.FabricVrfDbs>`
    
    	**config**\: False
    
    .. attribute:: dci_vrfs
    
    	FTI DCI\-VRF DB for all VRFs
    	**type**\:  :py:class:`DciVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.DciVrfs>`
    
    	**config**\: False
    
    .. attribute:: acp
    
    	Auto Config Pool Info
    	**type**\:  :py:class:`Acp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.Acp>`
    
    	**config**\: False
    
    

    """

    _prefix = 'infra-fti-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(DciFabricInterconnect, self).__init__()
        self._top_entity = None

        self.yang_name = "dci-fabric-interconnect"
        self.yang_parent_name = "Cisco-IOS-XR-infra-fti-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("opflex-session-infos", ("opflex_session_infos", DciFabricInterconnect.OpflexSessionInfos)), ("fabric-vrf-dbs", ("fabric_vrf_dbs", DciFabricInterconnect.FabricVrfDbs)), ("dci-vrfs", ("dci_vrfs", DciFabricInterconnect.DciVrfs)), ("acp", ("acp", DciFabricInterconnect.Acp))])
        self._leafs = OrderedDict()

        self.opflex_session_infos = DciFabricInterconnect.OpflexSessionInfos()
        self.opflex_session_infos.parent = self
        self._children_name_map["opflex_session_infos"] = "opflex-session-infos"

        self.fabric_vrf_dbs = DciFabricInterconnect.FabricVrfDbs()
        self.fabric_vrf_dbs.parent = self
        self._children_name_map["fabric_vrf_dbs"] = "fabric-vrf-dbs"

        self.dci_vrfs = DciFabricInterconnect.DciVrfs()
        self.dci_vrfs.parent = self
        self._children_name_map["dci_vrfs"] = "dci-vrfs"

        self.acp = DciFabricInterconnect.Acp()
        self.acp.parent = self
        self._children_name_map["acp"] = "acp"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-fti-oper:dci-fabric-interconnect"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(DciFabricInterconnect, [], name, value)


    class OpflexSessionInfos(_Entity_):
        """
        FTI Opflex Session Info for all fabrics
        
        .. attribute:: opflex_session_info
        
        	FTI Opflex Session Info for a particular fabric
        	**type**\: list of  		 :py:class:`OpflexSessionInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.OpflexSessionInfos.OpflexSessionInfo>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-fti-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(DciFabricInterconnect.OpflexSessionInfos, self).__init__()

            self.yang_name = "opflex-session-infos"
            self.yang_parent_name = "dci-fabric-interconnect"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("opflex-session-info", ("opflex_session_info", DciFabricInterconnect.OpflexSessionInfos.OpflexSessionInfo))])
            self._leafs = OrderedDict()

            self.opflex_session_info = YList(self)
            self._segment_path = lambda: "opflex-session-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-fti-oper:dci-fabric-interconnect/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DciFabricInterconnect.OpflexSessionInfos, [], name, value)


        class OpflexSessionInfo(_Entity_):
            """
            FTI Opflex Session Info for a particular fabric
            
            .. attribute:: id1  (key)
            
            	fabric identifier
            	**type**\: int
            
            	**range:** 1000..9999
            
            	**config**\: False
            
            .. attribute:: fabric_id
            
            	Fabric Id
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: config_state
            
            	Config State
            	**type**\:  :py:class:`FtiBagFabricConfigState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.FtiBagFabricConfigState>`
            
            	**config**\: False
            
            .. attribute:: last_upd_ts_config
            
            	Config Last Update Timestamp
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: fabric_state
            
            	Fabric State
            	**type**\:  :py:class:`FtiBagFabricState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.FtiBagFabricState>`
            
            	**config**\: False
            
            .. attribute:: last_upd_ts_fabric
            
            	Fabric Last Update Timestamp
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: peer_info
            
            	Fabric Per Peer Info
            	**type**\: list of  		 :py:class:`PeerInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.OpflexSessionInfos.OpflexSessionInfo.PeerInfo>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-fti-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(DciFabricInterconnect.OpflexSessionInfos.OpflexSessionInfo, self).__init__()

                self.yang_name = "opflex-session-info"
                self.yang_parent_name = "opflex-session-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['id1']
                self._child_classes = OrderedDict([("peer-info", ("peer_info", DciFabricInterconnect.OpflexSessionInfos.OpflexSessionInfo.PeerInfo))])
                self._leafs = OrderedDict([
                    ('id1', (YLeaf(YType.uint32, 'id1'), ['int'])),
                    ('fabric_id', (YLeaf(YType.uint32, 'fabric-id'), ['int'])),
                    ('config_state', (YLeaf(YType.enumeration, 'config-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper', 'FtiBagFabricConfigState', '')])),
                    ('last_upd_ts_config', (YLeaf(YType.uint64, 'last-upd-ts-config'), ['int'])),
                    ('fabric_state', (YLeaf(YType.enumeration, 'fabric-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper', 'FtiBagFabricState', '')])),
                    ('last_upd_ts_fabric', (YLeaf(YType.uint64, 'last-upd-ts-fabric'), ['int'])),
                ])
                self.id1 = None
                self.fabric_id = None
                self.config_state = None
                self.last_upd_ts_config = None
                self.fabric_state = None
                self.last_upd_ts_fabric = None

                self.peer_info = YList(self)
                self._segment_path = lambda: "opflex-session-info" + "[id1='" + str(self.id1) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-fti-oper:dci-fabric-interconnect/opflex-session-infos/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DciFabricInterconnect.OpflexSessionInfos.OpflexSessionInfo, ['id1', 'fabric_id', 'config_state', 'last_upd_ts_config', 'fabric_state', 'last_upd_ts_fabric'], name, value)


            class PeerInfo(_Entity_):
                """
                Fabric Per Peer Info
                
                .. attribute:: peer_ip
                
                	Peer IP
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: peer_port
                
                	Peer Port
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peer_state
                
                	Peer State
                	**type**\:  :py:class:`FtiBagFabricPeerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.FtiBagFabricPeerState>`
                
                	**config**\: False
                
                .. attribute:: last_upd_ts_peer_status
                
                	Peer Status Last Update Timestamp
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-fti-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DciFabricInterconnect.OpflexSessionInfos.OpflexSessionInfo.PeerInfo, self).__init__()

                    self.yang_name = "peer-info"
                    self.yang_parent_name = "opflex-session-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('peer_ip', (YLeaf(YType.str, 'peer-ip'), ['str'])),
                        ('peer_port', (YLeaf(YType.uint32, 'peer-port'), ['int'])),
                        ('peer_state', (YLeaf(YType.enumeration, 'peer-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper', 'FtiBagFabricPeerState', '')])),
                        ('last_upd_ts_peer_status', (YLeaf(YType.uint64, 'last-upd-ts-peer-status'), ['int'])),
                    ])
                    self.peer_ip = None
                    self.peer_port = None
                    self.peer_state = None
                    self.last_upd_ts_peer_status = None
                    self._segment_path = lambda: "peer-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DciFabricInterconnect.OpflexSessionInfos.OpflexSessionInfo.PeerInfo, ['peer_ip', 'peer_port', 'peer_state', 'last_upd_ts_peer_status'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
                    return meta._meta_table['DciFabricInterconnect.OpflexSessionInfos.OpflexSessionInfo.PeerInfo']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
                return meta._meta_table['DciFabricInterconnect.OpflexSessionInfos.OpflexSessionInfo']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
            return meta._meta_table['DciFabricInterconnect.OpflexSessionInfos']['meta_info']


    class FabricVrfDbs(_Entity_):
        """
        FTI Fabric\-VRF DB for all fabrics
        
        .. attribute:: fabric_vrf_db
        
        	FTI Fabric\-VRF DB for a particular fabric
        	**type**\: list of  		 :py:class:`FabricVrfDb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.FabricVrfDbs.FabricVrfDb>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-fti-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(DciFabricInterconnect.FabricVrfDbs, self).__init__()

            self.yang_name = "fabric-vrf-dbs"
            self.yang_parent_name = "dci-fabric-interconnect"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("fabric-vrf-db", ("fabric_vrf_db", DciFabricInterconnect.FabricVrfDbs.FabricVrfDb))])
            self._leafs = OrderedDict()

            self.fabric_vrf_db = YList(self)
            self._segment_path = lambda: "fabric-vrf-dbs"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-fti-oper:dci-fabric-interconnect/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DciFabricInterconnect.FabricVrfDbs, [], name, value)


        class FabricVrfDb(_Entity_):
            """
            FTI Fabric\-VRF DB for a particular fabric
            
            .. attribute:: id1  (key)
            
            	fabric identifier
            	**type**\: int
            
            	**range:** 1000..9999
            
            	**config**\: False
            
            .. attribute:: fabric_id
            
            	Fabric Id
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: fabric_vrf
            
            	Fabric VRFs
            	**type**\: list of  		 :py:class:`FabricVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-fti-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(DciFabricInterconnect.FabricVrfDbs.FabricVrfDb, self).__init__()

                self.yang_name = "fabric-vrf-db"
                self.yang_parent_name = "fabric-vrf-dbs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['id1']
                self._child_classes = OrderedDict([("fabric-vrf", ("fabric_vrf", DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf))])
                self._leafs = OrderedDict([
                    ('id1', (YLeaf(YType.uint32, 'id1'), ['int'])),
                    ('fabric_id', (YLeaf(YType.uint32, 'fabric-id'), ['int'])),
                ])
                self.id1 = None
                self.fabric_id = None

                self.fabric_vrf = YList(self)
                self._segment_path = lambda: "fabric-vrf-db" + "[id1='" + str(self.id1) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-fti-oper:dci-fabric-interconnect/fabric-vrf-dbs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DciFabricInterconnect.FabricVrfDbs.FabricVrfDb, ['id1', 'fabric_id'], name, value)


            class FabricVrf(_Entity_):
                """
                Fabric VRFs
                
                .. attribute:: fabric_vrf
                
                	Fabric VRF
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: dci_vrf
                
                	Dci VRF
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: fabric_vrf_flags
                
                	Fabric VRF Flags
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: v4_import_rt
                
                	V4 Import Route Targets
                	**type**\: list of  		 :py:class:`V4ImportRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V4ImportRt>`
                
                	**config**\: False
                
                .. attribute:: v4_export_rt
                
                	V4 Export Route Targets
                	**type**\: list of  		 :py:class:`V4ExportRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V4ExportRt>`
                
                	**config**\: False
                
                .. attribute:: v6_import_rt
                
                	V6 Import Route Targets
                	**type**\: list of  		 :py:class:`V6ImportRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V6ImportRt>`
                
                	**config**\: False
                
                .. attribute:: v6_export_rt
                
                	V6 Export Route Targets
                	**type**\: list of  		 :py:class:`V6ExportRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V6ExportRt>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-fti-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf, self).__init__()

                    self.yang_name = "fabric-vrf"
                    self.yang_parent_name = "fabric-vrf-db"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("v4-import-rt", ("v4_import_rt", DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V4ImportRt)), ("v4-export-rt", ("v4_export_rt", DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V4ExportRt)), ("v6-import-rt", ("v6_import_rt", DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V6ImportRt)), ("v6-export-rt", ("v6_export_rt", DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V6ExportRt))])
                    self._leafs = OrderedDict([
                        ('fabric_vrf', (YLeaf(YType.str, 'fabric-vrf'), ['str'])),
                        ('dci_vrf', (YLeaf(YType.str, 'dci-vrf'), ['str'])),
                        ('fabric_vrf_flags', (YLeaf(YType.str, 'fabric-vrf-flags'), ['str'])),
                    ])
                    self.fabric_vrf = None
                    self.dci_vrf = None
                    self.fabric_vrf_flags = None

                    self.v4_import_rt = YList(self)
                    self.v4_export_rt = YList(self)
                    self.v6_import_rt = YList(self)
                    self.v6_export_rt = YList(self)
                    self._segment_path = lambda: "fabric-vrf"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf, ['fabric_vrf', 'dci_vrf', 'fabric_vrf_flags'], name, value)


                class V4ImportRt(_Entity_):
                    """
                    V4 Import Route Targets
                    
                    .. attribute:: rt_value
                    
                    	RT Value
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: rt_flags
                    
                    	RT Flags
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-fti-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V4ImportRt, self).__init__()

                        self.yang_name = "v4-import-rt"
                        self.yang_parent_name = "fabric-vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rt_value', (YLeaf(YType.str, 'rt-value'), ['str'])),
                            ('rt_flags', (YLeaf(YType.str, 'rt-flags'), ['str'])),
                        ])
                        self.rt_value = None
                        self.rt_flags = None
                        self._segment_path = lambda: "v4-import-rt"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V4ImportRt, ['rt_value', 'rt_flags'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
                        return meta._meta_table['DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V4ImportRt']['meta_info']


                class V4ExportRt(_Entity_):
                    """
                    V4 Export Route Targets
                    
                    .. attribute:: rt_value
                    
                    	RT Value
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: rt_flags
                    
                    	RT Flags
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-fti-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V4ExportRt, self).__init__()

                        self.yang_name = "v4-export-rt"
                        self.yang_parent_name = "fabric-vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rt_value', (YLeaf(YType.str, 'rt-value'), ['str'])),
                            ('rt_flags', (YLeaf(YType.str, 'rt-flags'), ['str'])),
                        ])
                        self.rt_value = None
                        self.rt_flags = None
                        self._segment_path = lambda: "v4-export-rt"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V4ExportRt, ['rt_value', 'rt_flags'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
                        return meta._meta_table['DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V4ExportRt']['meta_info']


                class V6ImportRt(_Entity_):
                    """
                    V6 Import Route Targets
                    
                    .. attribute:: rt_value
                    
                    	RT Value
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: rt_flags
                    
                    	RT Flags
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-fti-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V6ImportRt, self).__init__()

                        self.yang_name = "v6-import-rt"
                        self.yang_parent_name = "fabric-vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rt_value', (YLeaf(YType.str, 'rt-value'), ['str'])),
                            ('rt_flags', (YLeaf(YType.str, 'rt-flags'), ['str'])),
                        ])
                        self.rt_value = None
                        self.rt_flags = None
                        self._segment_path = lambda: "v6-import-rt"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V6ImportRt, ['rt_value', 'rt_flags'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
                        return meta._meta_table['DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V6ImportRt']['meta_info']


                class V6ExportRt(_Entity_):
                    """
                    V6 Export Route Targets
                    
                    .. attribute:: rt_value
                    
                    	RT Value
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: rt_flags
                    
                    	RT Flags
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-fti-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V6ExportRt, self).__init__()

                        self.yang_name = "v6-export-rt"
                        self.yang_parent_name = "fabric-vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rt_value', (YLeaf(YType.str, 'rt-value'), ['str'])),
                            ('rt_flags', (YLeaf(YType.str, 'rt-flags'), ['str'])),
                        ])
                        self.rt_value = None
                        self.rt_flags = None
                        self._segment_path = lambda: "v6-export-rt"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V6ExportRt, ['rt_value', 'rt_flags'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
                        return meta._meta_table['DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf.V6ExportRt']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
                    return meta._meta_table['DciFabricInterconnect.FabricVrfDbs.FabricVrfDb.FabricVrf']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
                return meta._meta_table['DciFabricInterconnect.FabricVrfDbs.FabricVrfDb']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
            return meta._meta_table['DciFabricInterconnect.FabricVrfDbs']['meta_info']


    class DciVrfs(_Entity_):
        """
        FTI DCI\-VRF DB for all VRFs
        
        .. attribute:: dci_vrf
        
        	FTI DCI\-VRF Info for a particular VRF
        	**type**\: list of  		 :py:class:`DciVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.DciVrfs.DciVrf>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-fti-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(DciFabricInterconnect.DciVrfs, self).__init__()

            self.yang_name = "dci-vrfs"
            self.yang_parent_name = "dci-fabric-interconnect"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dci-vrf", ("dci_vrf", DciFabricInterconnect.DciVrfs.DciVrf))])
            self._leafs = OrderedDict()

            self.dci_vrf = YList(self)
            self._segment_path = lambda: "dci-vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-fti-oper:dci-fabric-interconnect/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DciFabricInterconnect.DciVrfs, [], name, value)


        class DciVrf(_Entity_):
            """
            FTI DCI\-VRF Info for a particular VRF
            
            .. attribute:: vrf1  (key)
            
            	vrf name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            	**config**\: False
            
            .. attribute:: dci_vrf
            
            	DCI VRF
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: num_fabric_vrf
            
            	Number of Fabric VRFs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: faric_vrfs_id_name
            
            	Associated Fabric Vrfs Info
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: vni_id
            
            	VNI Id
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: bd_name
            
            	BD Name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: bvi_id
            
            	BVI Id
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: bvi_ip
            
            	BVI Override IP
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: bvi_ip_v6
            
            	BVI IPV6. False is disabled, True is enabled
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: dci_vrf_flags
            
            	DCI VRF Flags
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: v4_import_rt
            
            	V4 Import Route Targets
            	**type**\: list of  		 :py:class:`V4ImportRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.DciVrfs.DciVrf.V4ImportRt>`
            
            	**config**\: False
            
            .. attribute:: v4_export_rt
            
            	V4 Export Route Targets
            	**type**\: list of  		 :py:class:`V4ExportRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.DciVrfs.DciVrf.V4ExportRt>`
            
            	**config**\: False
            
            .. attribute:: v6_import_rt
            
            	V6 Import Route Targets
            	**type**\: list of  		 :py:class:`V6ImportRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.DciVrfs.DciVrf.V6ImportRt>`
            
            	**config**\: False
            
            .. attribute:: v6_export_rt
            
            	V6 Export Route Targets
            	**type**\: list of  		 :py:class:`V6ExportRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_oper.DciFabricInterconnect.DciVrfs.DciVrf.V6ExportRt>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-fti-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(DciFabricInterconnect.DciVrfs.DciVrf, self).__init__()

                self.yang_name = "dci-vrf"
                self.yang_parent_name = "dci-vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf1']
                self._child_classes = OrderedDict([("v4-import-rt", ("v4_import_rt", DciFabricInterconnect.DciVrfs.DciVrf.V4ImportRt)), ("v4-export-rt", ("v4_export_rt", DciFabricInterconnect.DciVrfs.DciVrf.V4ExportRt)), ("v6-import-rt", ("v6_import_rt", DciFabricInterconnect.DciVrfs.DciVrf.V6ImportRt)), ("v6-export-rt", ("v6_export_rt", DciFabricInterconnect.DciVrfs.DciVrf.V6ExportRt))])
                self._leafs = OrderedDict([
                    ('vrf1', (YLeaf(YType.str, 'vrf1'), ['str'])),
                    ('dci_vrf', (YLeaf(YType.str, 'dci-vrf'), ['str'])),
                    ('num_fabric_vrf', (YLeaf(YType.uint32, 'num-fabric-vrf'), ['int'])),
                    ('faric_vrfs_id_name', (YLeaf(YType.str, 'faric-vrfs-id-name'), ['str'])),
                    ('vni_id', (YLeaf(YType.uint32, 'vni-id'), ['int'])),
                    ('bd_name', (YLeaf(YType.str, 'bd-name'), ['str'])),
                    ('bvi_id', (YLeaf(YType.uint32, 'bvi-id'), ['int'])),
                    ('bvi_ip', (YLeaf(YType.str, 'bvi-ip'), ['str'])),
                    ('bvi_ip_v6', (YLeaf(YType.boolean, 'bvi-ip-v6'), ['bool'])),
                    ('dci_vrf_flags', (YLeaf(YType.str, 'dci-vrf-flags'), ['str'])),
                ])
                self.vrf1 = None
                self.dci_vrf = None
                self.num_fabric_vrf = None
                self.faric_vrfs_id_name = None
                self.vni_id = None
                self.bd_name = None
                self.bvi_id = None
                self.bvi_ip = None
                self.bvi_ip_v6 = None
                self.dci_vrf_flags = None

                self.v4_import_rt = YList(self)
                self.v4_export_rt = YList(self)
                self.v6_import_rt = YList(self)
                self.v6_export_rt = YList(self)
                self._segment_path = lambda: "dci-vrf" + "[vrf1='" + str(self.vrf1) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-fti-oper:dci-fabric-interconnect/dci-vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DciFabricInterconnect.DciVrfs.DciVrf, ['vrf1', 'dci_vrf', 'num_fabric_vrf', 'faric_vrfs_id_name', 'vni_id', 'bd_name', 'bvi_id', 'bvi_ip', 'bvi_ip_v6', 'dci_vrf_flags'], name, value)


            class V4ImportRt(_Entity_):
                """
                V4 Import Route Targets
                
                .. attribute:: rt_value
                
                	RT Value
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: rt_flags
                
                	RT Flags
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-fti-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DciFabricInterconnect.DciVrfs.DciVrf.V4ImportRt, self).__init__()

                    self.yang_name = "v4-import-rt"
                    self.yang_parent_name = "dci-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rt_value', (YLeaf(YType.str, 'rt-value'), ['str'])),
                        ('rt_flags', (YLeaf(YType.str, 'rt-flags'), ['str'])),
                    ])
                    self.rt_value = None
                    self.rt_flags = None
                    self._segment_path = lambda: "v4-import-rt"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DciFabricInterconnect.DciVrfs.DciVrf.V4ImportRt, ['rt_value', 'rt_flags'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
                    return meta._meta_table['DciFabricInterconnect.DciVrfs.DciVrf.V4ImportRt']['meta_info']


            class V4ExportRt(_Entity_):
                """
                V4 Export Route Targets
                
                .. attribute:: rt_value
                
                	RT Value
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: rt_flags
                
                	RT Flags
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-fti-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DciFabricInterconnect.DciVrfs.DciVrf.V4ExportRt, self).__init__()

                    self.yang_name = "v4-export-rt"
                    self.yang_parent_name = "dci-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rt_value', (YLeaf(YType.str, 'rt-value'), ['str'])),
                        ('rt_flags', (YLeaf(YType.str, 'rt-flags'), ['str'])),
                    ])
                    self.rt_value = None
                    self.rt_flags = None
                    self._segment_path = lambda: "v4-export-rt"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DciFabricInterconnect.DciVrfs.DciVrf.V4ExportRt, ['rt_value', 'rt_flags'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
                    return meta._meta_table['DciFabricInterconnect.DciVrfs.DciVrf.V4ExportRt']['meta_info']


            class V6ImportRt(_Entity_):
                """
                V6 Import Route Targets
                
                .. attribute:: rt_value
                
                	RT Value
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: rt_flags
                
                	RT Flags
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-fti-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DciFabricInterconnect.DciVrfs.DciVrf.V6ImportRt, self).__init__()

                    self.yang_name = "v6-import-rt"
                    self.yang_parent_name = "dci-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rt_value', (YLeaf(YType.str, 'rt-value'), ['str'])),
                        ('rt_flags', (YLeaf(YType.str, 'rt-flags'), ['str'])),
                    ])
                    self.rt_value = None
                    self.rt_flags = None
                    self._segment_path = lambda: "v6-import-rt"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DciFabricInterconnect.DciVrfs.DciVrf.V6ImportRt, ['rt_value', 'rt_flags'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
                    return meta._meta_table['DciFabricInterconnect.DciVrfs.DciVrf.V6ImportRt']['meta_info']


            class V6ExportRt(_Entity_):
                """
                V6 Export Route Targets
                
                .. attribute:: rt_value
                
                	RT Value
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: rt_flags
                
                	RT Flags
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-fti-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DciFabricInterconnect.DciVrfs.DciVrf.V6ExportRt, self).__init__()

                    self.yang_name = "v6-export-rt"
                    self.yang_parent_name = "dci-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rt_value', (YLeaf(YType.str, 'rt-value'), ['str'])),
                        ('rt_flags', (YLeaf(YType.str, 'rt-flags'), ['str'])),
                    ])
                    self.rt_value = None
                    self.rt_flags = None
                    self._segment_path = lambda: "v6-export-rt"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DciFabricInterconnect.DciVrfs.DciVrf.V6ExportRt, ['rt_value', 'rt_flags'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
                    return meta._meta_table['DciFabricInterconnect.DciVrfs.DciVrf.V6ExportRt']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
                return meta._meta_table['DciFabricInterconnect.DciVrfs.DciVrf']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
            return meta._meta_table['DciFabricInterconnect.DciVrfs']['meta_info']


    class Acp(_Entity_):
        """
        Auto Config Pool Info
        
        .. attribute:: vni_min
        
        	VNI MIN VALUE
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: vni_max
        
        	VNI MAX VALUE
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: vni_bits
        
        	Num of VNI used bits
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: bvi_min
        
        	BVI MIN VALUE
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: bvi_max
        
        	BVI MAX VALUE
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: bvi_bits
        
        	Num of BVI used bits
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: bd_min
        
        	BD MIN VALUE
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: bd_max
        
        	BD MAX VALUE
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: bd_bits
        
        	Num of BD used bits
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: vniused_range
        
        	Used VNI Range
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: bviused_range
        
        	Used BVI Range
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: bdused_range
        
        	Used BD Range
        	**type**\: str
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-fti-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(DciFabricInterconnect.Acp, self).__init__()

            self.yang_name = "acp"
            self.yang_parent_name = "dci-fabric-interconnect"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('vni_min', (YLeaf(YType.uint32, 'vni-min'), ['int'])),
                ('vni_max', (YLeaf(YType.uint32, 'vni-max'), ['int'])),
                ('vni_bits', (YLeaf(YType.uint32, 'vni-bits'), ['int'])),
                ('bvi_min', (YLeaf(YType.uint32, 'bvi-min'), ['int'])),
                ('bvi_max', (YLeaf(YType.uint32, 'bvi-max'), ['int'])),
                ('bvi_bits', (YLeaf(YType.uint32, 'bvi-bits'), ['int'])),
                ('bd_min', (YLeaf(YType.uint32, 'bd-min'), ['int'])),
                ('bd_max', (YLeaf(YType.uint32, 'bd-max'), ['int'])),
                ('bd_bits', (YLeaf(YType.uint32, 'bd-bits'), ['int'])),
                ('vniused_range', (YLeaf(YType.str, 'vniused-range'), ['str'])),
                ('bviused_range', (YLeaf(YType.str, 'bviused-range'), ['str'])),
                ('bdused_range', (YLeaf(YType.str, 'bdused-range'), ['str'])),
            ])
            self.vni_min = None
            self.vni_max = None
            self.vni_bits = None
            self.bvi_min = None
            self.bvi_max = None
            self.bvi_bits = None
            self.bd_min = None
            self.bd_max = None
            self.bd_bits = None
            self.vniused_range = None
            self.bviused_range = None
            self.bdused_range = None
            self._segment_path = lambda: "acp"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-fti-oper:dci-fabric-interconnect/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DciFabricInterconnect.Acp, ['vni_min', 'vni_max', 'vni_bits', 'bvi_min', 'bvi_max', 'bvi_bits', 'bd_min', 'bd_max', 'bd_bits', 'vniused_range', 'bviused_range', 'bdused_range'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
            return meta._meta_table['DciFabricInterconnect.Acp']['meta_info']

    def clone_ptr(self):
        self._top_entity = DciFabricInterconnect()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_fti_oper as meta
        return meta._meta_table['DciFabricInterconnect']['meta_info']



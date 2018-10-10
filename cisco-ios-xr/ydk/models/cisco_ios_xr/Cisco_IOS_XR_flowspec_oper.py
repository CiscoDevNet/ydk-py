""" Cisco_IOS_XR_flowspec_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR flowspec package operational data.

This module contains definitions
for the following management objects\:
  flow\-spec\: FlowSpec information

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FsClient(Enum):
    """
    FsClient (Enum Class)

    Fs client

    .. data:: bgp = 0

    	FlowSpec BGP Client

    .. data:: one_pk = 1

    	FlowSpec OneP Client

    .. data:: policy = 2

    	FlowSpec Policy Client

    .. data:: ha = 3

    	FlowSpec HA Client

    .. data:: test = 4

    	FlowSpec Test Client

    """

    bgp = Enum.YLeaf(0, "bgp")

    one_pk = Enum.YLeaf(1, "one-pk")

    policy = Enum.YLeaf(2, "policy")

    ha = Enum.YLeaf(3, "ha")

    test = Enum.YLeaf(4, "test")


class FsMgrClientState(Enum):
    """
    FsMgrClientState (Enum Class)

    FlowSpec manager client state

    .. data:: dormant = 0

    	Dormant

    .. data:: connected = 1

    	Connected

    .. data:: replay = 2

    	Replay

    .. data:: unconfigured = 3

    	Unconfigured

    """

    dormant = Enum.YLeaf(0, "dormant")

    connected = Enum.YLeaf(1, "connected")

    replay = Enum.YLeaf(2, "replay")

    unconfigured = Enum.YLeaf(3, "unconfigured")



class FlowSpec(Entity):
    """
    FlowSpec information
    
    .. attribute:: clients
    
    	Table of Client
    	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Clients>`
    
    .. attribute:: summary
    
    	FlowSpec summary
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Summary>`
    
    .. attribute:: vrfs
    
    	Table of VRF
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Vrfs>`
    
    

    """

    _prefix = 'flowspec-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(FlowSpec, self).__init__()
        self._top_entity = None

        self.yang_name = "flow-spec"
        self.yang_parent_name = "Cisco-IOS-XR-flowspec-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("clients", ("clients", FlowSpec.Clients)), ("summary", ("summary", FlowSpec.Summary)), ("vrfs", ("vrfs", FlowSpec.Vrfs))])
        self._leafs = OrderedDict()

        self.clients = FlowSpec.Clients()
        self.clients.parent = self
        self._children_name_map["clients"] = "clients"

        self.summary = FlowSpec.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"

        self.vrfs = FlowSpec.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._segment_path = lambda: "Cisco-IOS-XR-flowspec-oper:flow-spec"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(FlowSpec, [], name, value)


    class Clients(Entity):
        """
        Table of Client
        
        .. attribute:: client
        
        	FlowSpec client information
        	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Clients.Client>`
        
        

        """

        _prefix = 'flowspec-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(FlowSpec.Clients, self).__init__()

            self.yang_name = "clients"
            self.yang_parent_name = "flow-spec"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("client", ("client", FlowSpec.Clients.Client))])
            self._leafs = OrderedDict()

            self.client = YList(self)
            self._segment_path = lambda: "clients"
            self._absolute_path = lambda: "Cisco-IOS-XR-flowspec-oper:flow-spec/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FlowSpec.Clients, [], name, value)


        class Client(Entity):
            """
            FlowSpec client information
            
            .. attribute:: client_type
            
            	FlowSpec Client Type
            	**type**\:  :py:class:`FsClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FsClient>`
            
            .. attribute:: client_id
            
            	FlowSpec client ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: client_state
            
            	State of FS client
            	**type**\:  :py:class:`FsMgrClientState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FsMgrClientState>`
            
            .. attribute:: client_flows
            
            	Number of client flows
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'flowspec-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(FlowSpec.Clients.Client, self).__init__()

                self.yang_name = "client"
                self.yang_parent_name = "clients"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('client_type', (YLeaf(YType.enumeration, 'client-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper', 'FsClient', '')])),
                    ('client_id', (YLeaf(YType.uint32, 'client-id'), ['int'])),
                    ('client_state', (YLeaf(YType.enumeration, 'client-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper', 'FsMgrClientState', '')])),
                    ('client_flows', (YLeaf(YType.uint32, 'client-flows'), ['int'])),
                ])
                self.client_type = None
                self.client_id = None
                self.client_state = None
                self.client_flows = None
                self._segment_path = lambda: "client"
                self._absolute_path = lambda: "Cisco-IOS-XR-flowspec-oper:flow-spec/clients/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FlowSpec.Clients.Client, ['client_type', 'client_id', 'client_state', 'client_flows'], name, value)


    class Summary(Entity):
        """
        FlowSpec summary
        
        .. attribute:: vrfafi_tables
        
        	Total VRF+AFI tables
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: flows
        
        	Total flows
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'flowspec-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(FlowSpec.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "flow-spec"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('vrfafi_tables', (YLeaf(YType.uint32, 'vrfafi-tables'), ['int'])),
                ('flows', (YLeaf(YType.uint32, 'flows'), ['int'])),
            ])
            self.vrfafi_tables = None
            self.flows = None
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-flowspec-oper:flow-spec/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FlowSpec.Summary, ['vrfafi_tables', 'flows'], name, value)


    class Vrfs(Entity):
        """
        Table of VRF
        
        .. attribute:: vrf
        
        	VRF information
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Vrfs.Vrf>`
        
        

        """

        _prefix = 'flowspec-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(FlowSpec.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "flow-spec"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", FlowSpec.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-flowspec-oper:flow-spec/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FlowSpec.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            VRF information
            
            .. attribute:: vrf_name  (key)
            
            	VRF Name
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: afs
            
            	Table of AF
            	**type**\:  :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Vrfs.Vrf.Afs>`
            
            

            """

            _prefix = 'flowspec-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(FlowSpec.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("afs", ("afs", FlowSpec.Vrfs.Vrf.Afs))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None

                self.afs = FlowSpec.Vrfs.Vrf.Afs()
                self.afs.parent = self
                self._children_name_map["afs"] = "afs"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-flowspec-oper:flow-spec/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FlowSpec.Vrfs.Vrf, ['vrf_name'], name, value)


            class Afs(Entity):
                """
                Table of AF
                
                .. attribute:: af
                
                	AFI Type (IPv4/IPv6)
                	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Vrfs.Vrf.Afs.Af>`
                
                

                """

                _prefix = 'flowspec-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FlowSpec.Vrfs.Vrf.Afs, self).__init__()

                    self.yang_name = "afs"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("af", ("af", FlowSpec.Vrfs.Vrf.Afs.Af))])
                    self._leafs = OrderedDict()

                    self.af = YList(self)
                    self._segment_path = lambda: "afs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs, [], name, value)


                class Af(Entity):
                    """
                    AFI Type (IPv4/IPv6)
                    
                    .. attribute:: af_name  (key)
                    
                    	Set string
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: table_summary
                    
                    	FlowSpec summary for VRF+AFI tables
                    	**type**\:  :py:class:`TableSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Vrfs.Vrf.Afs.Af.TableSummary>`
                    
                    .. attribute:: nlris
                    
                    	Table of NLRI
                    	**type**\:  :py:class:`Nlris <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Vrfs.Vrf.Afs.Af.Nlris>`
                    
                    .. attribute:: flows
                    
                    	Table of Flow
                    	**type**\:  :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Vrfs.Vrf.Afs.Af.Flows>`
                    
                    

                    """

                    _prefix = 'flowspec-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FlowSpec.Vrfs.Vrf.Afs.Af, self).__init__()

                        self.yang_name = "af"
                        self.yang_parent_name = "afs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['af_name']
                        self._child_classes = OrderedDict([("table-summary", ("table_summary", FlowSpec.Vrfs.Vrf.Afs.Af.TableSummary)), ("nlris", ("nlris", FlowSpec.Vrfs.Vrf.Afs.Af.Nlris)), ("flows", ("flows", FlowSpec.Vrfs.Vrf.Afs.Af.Flows))])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.str, 'af-name'), ['str'])),
                        ])
                        self.af_name = None

                        self.table_summary = FlowSpec.Vrfs.Vrf.Afs.Af.TableSummary()
                        self.table_summary.parent = self
                        self._children_name_map["table_summary"] = "table-summary"

                        self.nlris = FlowSpec.Vrfs.Vrf.Afs.Af.Nlris()
                        self.nlris.parent = self
                        self._children_name_map["nlris"] = "nlris"

                        self.flows = FlowSpec.Vrfs.Vrf.Afs.Af.Flows()
                        self.flows.parent = self
                        self._children_name_map["flows"] = "flows"
                        self._segment_path = lambda: "af" + "[af-name='" + str(self.af_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af, ['af_name'], name, value)


                    class TableSummary(Entity):
                        """
                        FlowSpec summary for VRF+AFI tables
                        
                        .. attribute:: total_flows
                        
                        	Total number of flows
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_policies
                        
                        	Total number of attached service policies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_install_enabled
                        
                        	Local installation of flowspec rules
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'flowspec-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FlowSpec.Vrfs.Vrf.Afs.Af.TableSummary, self).__init__()

                            self.yang_name = "table-summary"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('total_flows', (YLeaf(YType.uint32, 'total-flows'), ['int'])),
                                ('service_policies', (YLeaf(YType.uint32, 'service-policies'), ['int'])),
                                ('local_install_enabled', (YLeaf(YType.boolean, 'local-install-enabled'), ['bool'])),
                            ])
                            self.total_flows = None
                            self.service_policies = None
                            self.local_install_enabled = None
                            self._segment_path = lambda: "table-summary"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af.TableSummary, ['total_flows', 'service_policies', 'local_install_enabled'], name, value)


                    class Nlris(Entity):
                        """
                        Table of NLRI
                        
                        .. attribute:: nlri
                        
                        	NLRI information (hexdump)
                        	**type**\: list of  		 :py:class:`Nlri <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri>`
                        
                        

                        """

                        _prefix = 'flowspec-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FlowSpec.Vrfs.Vrf.Afs.Af.Nlris, self).__init__()

                            self.yang_name = "nlris"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("nlri", ("nlri", FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri))])
                            self._leafs = OrderedDict()

                            self.nlri = YList(self)
                            self._segment_path = lambda: "nlris"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af.Nlris, [], name, value)


                        class Nlri(Entity):
                            """
                            NLRI information (hexdump)
                            
                            .. attribute:: nlri_bytes  (key)
                            
                            	Enter NLRI hex string
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: flow_statistics
                            
                            	Flow statistics
                            	**type**\:  :py:class:`FlowStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri.FlowStatistics>`
                            
                            

                            """

                            _prefix = 'flowspec-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri, self).__init__()

                                self.yang_name = "nlri"
                                self.yang_parent_name = "nlris"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['nlri_bytes']
                                self._child_classes = OrderedDict([("flow-statistics", ("flow_statistics", FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri.FlowStatistics))])
                                self._leafs = OrderedDict([
                                    ('nlri_bytes', (YLeaf(YType.str, 'nlri-bytes'), ['str'])),
                                ])
                                self.nlri_bytes = None

                                self.flow_statistics = FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri.FlowStatistics()
                                self.flow_statistics.parent = self
                                self._children_name_map["flow_statistics"] = "flow-statistics"
                                self._segment_path = lambda: "nlri" + "[nlri-bytes='" + str(self.nlri_bytes) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri, ['nlri_bytes'], name, value)


                            class FlowStatistics(Entity):
                                """
                                Flow statistics
                                
                                .. attribute:: classified
                                
                                	Classified statistics
                                	**type**\:  :py:class:`Classified <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri.FlowStatistics.Classified>`
                                
                                .. attribute:: dropped
                                
                                	Drop statistics
                                	**type**\:  :py:class:`Dropped <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri.FlowStatistics.Dropped>`
                                
                                

                                """

                                _prefix = 'flowspec-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri.FlowStatistics, self).__init__()

                                    self.yang_name = "flow-statistics"
                                    self.yang_parent_name = "nlri"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("classified", ("classified", FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri.FlowStatistics.Classified)), ("dropped", ("dropped", FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri.FlowStatistics.Dropped))])
                                    self._leafs = OrderedDict()

                                    self.classified = FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri.FlowStatistics.Classified()
                                    self.classified.parent = self
                                    self._children_name_map["classified"] = "classified"

                                    self.dropped = FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri.FlowStatistics.Dropped()
                                    self.dropped.parent = self
                                    self._children_name_map["dropped"] = "dropped"
                                    self._segment_path = lambda: "flow-statistics"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri.FlowStatistics, [], name, value)


                                class Classified(Entity):
                                    """
                                    Classified statistics
                                    
                                    .. attribute:: packets
                                    
                                    	Number of packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: bytes
                                    
                                    	Number of bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'flowspec-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri.FlowStatistics.Classified, self).__init__()

                                        self.yang_name = "classified"
                                        self.yang_parent_name = "flow-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                            ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                        ])
                                        self.packets = None
                                        self.bytes = None
                                        self._segment_path = lambda: "classified"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri.FlowStatistics.Classified, ['packets', 'bytes'], name, value)


                                class Dropped(Entity):
                                    """
                                    Drop statistics
                                    
                                    .. attribute:: packets
                                    
                                    	Number of packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: bytes
                                    
                                    	Number of bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'flowspec-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri.FlowStatistics.Dropped, self).__init__()

                                        self.yang_name = "dropped"
                                        self.yang_parent_name = "flow-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                            ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                        ])
                                        self.packets = None
                                        self.bytes = None
                                        self._segment_path = lambda: "dropped"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af.Nlris.Nlri.FlowStatistics.Dropped, ['packets', 'bytes'], name, value)


                    class Flows(Entity):
                        """
                        Table of Flow
                        
                        .. attribute:: flow
                        
                        	Flow notation string
                        	**type**\: list of  		 :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow>`
                        
                        

                        """

                        _prefix = 'flowspec-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FlowSpec.Vrfs.Vrf.Afs.Af.Flows, self).__init__()

                            self.yang_name = "flows"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("flow", ("flow", FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow))])
                            self._leafs = OrderedDict()

                            self.flow = YList(self)
                            self._segment_path = lambda: "flows"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af.Flows, [], name, value)


                        class Flow(Entity):
                            """
                            Flow notation string
                            
                            .. attribute:: flow_notation  (key)
                            
                            	Enter the Flow notation string
                            	**type**\: str
                            
                            .. attribute:: flow_statistics
                            
                            	Flow statistics
                            	**type**\:  :py:class:`FlowStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow.FlowStatistics>`
                            
                            

                            """

                            _prefix = 'flowspec-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow, self).__init__()

                                self.yang_name = "flow"
                                self.yang_parent_name = "flows"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['flow_notation']
                                self._child_classes = OrderedDict([("flow-statistics", ("flow_statistics", FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow.FlowStatistics))])
                                self._leafs = OrderedDict([
                                    ('flow_notation', (YLeaf(YType.str, 'flow-notation'), ['str'])),
                                ])
                                self.flow_notation = None

                                self.flow_statistics = FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow.FlowStatistics()
                                self.flow_statistics.parent = self
                                self._children_name_map["flow_statistics"] = "flow-statistics"
                                self._segment_path = lambda: "flow" + "[flow-notation='" + str(self.flow_notation) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow, ['flow_notation'], name, value)


                            class FlowStatistics(Entity):
                                """
                                Flow statistics
                                
                                .. attribute:: classified
                                
                                	Classified statistics
                                	**type**\:  :py:class:`Classified <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow.FlowStatistics.Classified>`
                                
                                .. attribute:: dropped
                                
                                	Drop statistics
                                	**type**\:  :py:class:`Dropped <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_oper.FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow.FlowStatistics.Dropped>`
                                
                                

                                """

                                _prefix = 'flowspec-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow.FlowStatistics, self).__init__()

                                    self.yang_name = "flow-statistics"
                                    self.yang_parent_name = "flow"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("classified", ("classified", FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow.FlowStatistics.Classified)), ("dropped", ("dropped", FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow.FlowStatistics.Dropped))])
                                    self._leafs = OrderedDict()

                                    self.classified = FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow.FlowStatistics.Classified()
                                    self.classified.parent = self
                                    self._children_name_map["classified"] = "classified"

                                    self.dropped = FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow.FlowStatistics.Dropped()
                                    self.dropped.parent = self
                                    self._children_name_map["dropped"] = "dropped"
                                    self._segment_path = lambda: "flow-statistics"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow.FlowStatistics, [], name, value)


                                class Classified(Entity):
                                    """
                                    Classified statistics
                                    
                                    .. attribute:: packets
                                    
                                    	Number of packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: bytes
                                    
                                    	Number of bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'flowspec-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow.FlowStatistics.Classified, self).__init__()

                                        self.yang_name = "classified"
                                        self.yang_parent_name = "flow-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                            ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                        ])
                                        self.packets = None
                                        self.bytes = None
                                        self._segment_path = lambda: "classified"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow.FlowStatistics.Classified, ['packets', 'bytes'], name, value)


                                class Dropped(Entity):
                                    """
                                    Drop statistics
                                    
                                    .. attribute:: packets
                                    
                                    	Number of packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: bytes
                                    
                                    	Number of bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'flowspec-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow.FlowStatistics.Dropped, self).__init__()

                                        self.yang_name = "dropped"
                                        self.yang_parent_name = "flow-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                            ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                        ])
                                        self.packets = None
                                        self.bytes = None
                                        self._segment_path = lambda: "dropped"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af.Flows.Flow.FlowStatistics.Dropped, ['packets', 'bytes'], name, value)

    def clone_ptr(self):
        self._top_entity = FlowSpec()
        return self._top_entity


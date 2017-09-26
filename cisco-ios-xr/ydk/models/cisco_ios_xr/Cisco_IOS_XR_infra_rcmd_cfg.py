""" Cisco_IOS_XR_infra_rcmd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rcmd package configuration.

This module contains definitions
for the following management objects\:
  router\-convergence\: Configure Router Convergence Monitoring

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ProtocolName(Enum):
    """
    ProtocolName

    Protocol name

    .. data:: ospf = 0

    	Configure parameters related to OSPF

    .. data:: isis = 1

    	Configure parameters related to ISIS

    """

    ospf = Enum.YLeaf(0, "ospf")

    isis = Enum.YLeaf(1, "isis")


class RcmdPriority(Enum):
    """
    RcmdPriority

    Rcmd priority

    .. data:: critical = 0

    	Critical routes

    .. data:: high = 1

    	High priority routes

    .. data:: medium = 2

    	Medium priority routes

    .. data:: low = 3

    	Low priority routes

    """

    critical = Enum.YLeaf(0, "critical")

    high = Enum.YLeaf(1, "high")

    medium = Enum.YLeaf(2, "medium")

    low = Enum.YLeaf(3, "low")



class RouterConvergence(Entity):
    """
    Configure Router Convergence Monitoring
    
    .. attribute:: collect_diagnostics
    
    	Table of CollectDiagnostics
    	**type**\:   :py:class:`CollectDiagnostics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.CollectDiagnostics>`
    
    .. attribute:: disable
    
    	Disable the monitoring of route convergence on the entire router
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: enable
    
    	Enable Configure Router Convergence Monitoring. Deletion of this object also causes deletion of all associated objects under RouterConvergence
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: event_buffer_size
    
    	Event buffer size for storing event traces (as number of events)
    	**type**\:  int
    
    	**range:** 100..500
    
    .. attribute:: max_events_stored
    
    	Maximum number of events stored in the server
    	**type**\:  int
    
    	**range:** 10..500
    
    .. attribute:: monitoring_interval
    
    	Interval in which to collect logs (in mins)
    	**type**\:  int
    
    	**range:** 5..120
    
    	**units**\: minute
    
    .. attribute:: mpls_ldp
    
    	RCMD related configuration for MPLS\-LDP
    	**type**\:   :py:class:`MplsLdp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.MplsLdp>`
    
    	**presence node**\: True
    
    .. attribute:: nodes
    
    	Table of Node
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Nodes>`
    
    .. attribute:: prefix_monitor_limit
    
    	Limits Individual Prefix Monitoring
    	**type**\:  int
    
    	**range:** 0..100
    
    .. attribute:: protocols
    
    	Table of Protocol
    	**type**\:   :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Protocols>`
    
    .. attribute:: storage_location
    
    	Absolute directory path for saving the archive files. Example /disk0\:/rcmd/ or <tftp\-location>/rcmd/
    	**type**\:   :py:class:`StorageLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.StorageLocation>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'infra-rcmd-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(RouterConvergence, self).__init__()
        self._top_entity = None

        self.yang_name = "router-convergence"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rcmd-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"collect-diagnostics" : ("collect_diagnostics", RouterConvergence.CollectDiagnostics), "mpls-ldp" : ("mpls_ldp", RouterConvergence.MplsLdp), "nodes" : ("nodes", RouterConvergence.Nodes), "protocols" : ("protocols", RouterConvergence.Protocols), "storage-location" : ("storage_location", RouterConvergence.StorageLocation)}
        self._child_list_classes = {}

        self.disable = YLeaf(YType.empty, "disable")

        self.enable = YLeaf(YType.empty, "enable")

        self.event_buffer_size = YLeaf(YType.uint32, "event-buffer-size")

        self.max_events_stored = YLeaf(YType.uint32, "max-events-stored")

        self.monitoring_interval = YLeaf(YType.uint32, "monitoring-interval")

        self.prefix_monitor_limit = YLeaf(YType.uint32, "prefix-monitor-limit")

        self.collect_diagnostics = RouterConvergence.CollectDiagnostics()
        self.collect_diagnostics.parent = self
        self._children_name_map["collect_diagnostics"] = "collect-diagnostics"
        self._children_yang_names.add("collect-diagnostics")

        self.mpls_ldp = None
        self._children_name_map["mpls_ldp"] = "mpls-ldp"
        self._children_yang_names.add("mpls-ldp")

        self.nodes = RouterConvergence.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")

        self.protocols = RouterConvergence.Protocols()
        self.protocols.parent = self
        self._children_name_map["protocols"] = "protocols"
        self._children_yang_names.add("protocols")

        self.storage_location = None
        self._children_name_map["storage_location"] = "storage-location"
        self._children_yang_names.add("storage-location")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence"

    def __setattr__(self, name, value):
        self._perform_setattr(RouterConvergence, ['disable', 'enable', 'event_buffer_size', 'max_events_stored', 'monitoring_interval', 'prefix_monitor_limit'], name, value)


    class CollectDiagnostics(Entity):
        """
        Table of CollectDiagnostics
        
        .. attribute:: collect_diagnostic
        
        	Collect diagnostics on specified node
        	**type**\: list of    :py:class:`CollectDiagnostic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.CollectDiagnostics.CollectDiagnostic>`
        
        

        """

        _prefix = 'infra-rcmd-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(RouterConvergence.CollectDiagnostics, self).__init__()

            self.yang_name = "collect-diagnostics"
            self.yang_parent_name = "router-convergence"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"collect-diagnostic" : ("collect_diagnostic", RouterConvergence.CollectDiagnostics.CollectDiagnostic)}

            self.collect_diagnostic = YList(self)
            self._segment_path = lambda: "collect-diagnostics"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RouterConvergence.CollectDiagnostics, [], name, value)


        class CollectDiagnostic(Entity):
            """
            Collect diagnostics on specified node
            
            .. attribute:: node_name  <key>
            
            	Specified location
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: enable
            
            	Enables collection of diagnostics on the specified location
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rcmd-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RouterConvergence.CollectDiagnostics.CollectDiagnostic, self).__init__()

                self.yang_name = "collect-diagnostic"
                self.yang_parent_name = "collect-diagnostics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "collect-diagnostic" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/collect-diagnostics/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RouterConvergence.CollectDiagnostics.CollectDiagnostic, ['node_name', 'enable'], name, value)


    class MplsLdp(Entity):
        """
        RCMD related configuration for MPLS\-LDP
        
        .. attribute:: remote_lfa
        
        	Monitoring configuration for Remote LFA
        	**type**\:   :py:class:`RemoteLfa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.MplsLdp.RemoteLfa>`
        
        	**presence node**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-rcmd-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(RouterConvergence.MplsLdp, self).__init__()

            self.yang_name = "mpls-ldp"
            self.yang_parent_name = "router-convergence"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"remote-lfa" : ("remote_lfa", RouterConvergence.MplsLdp.RemoteLfa)}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.remote_lfa = None
            self._children_name_map["remote_lfa"] = "remote-lfa"
            self._children_yang_names.add("remote-lfa")
            self._segment_path = lambda: "mpls-ldp"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/%s" % self._segment_path()


        class RemoteLfa(Entity):
            """
            Monitoring configuration for Remote LFA
            
            .. attribute:: threshold
            
            	Threshold value for label coverage (in percentage)
            	**type**\:  int
            
            	**range:** 1..100
            
            	**units**\: percentage
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-rcmd-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RouterConvergence.MplsLdp.RemoteLfa, self).__init__()

                self.yang_name = "remote-lfa"
                self.yang_parent_name = "mpls-ldp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}
                self.is_presence_container = True

                self.threshold = YLeaf(YType.uint32, "threshold")
                self._segment_path = lambda: "remote-lfa"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/mpls-ldp/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RouterConvergence.MplsLdp.RemoteLfa, ['threshold'], name, value)


    class Nodes(Entity):
        """
        Table of Node
        
        .. attribute:: node
        
        	Configure parameters for the specified node (Partially qualified location allowed)
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Nodes.Node>`
        
        

        """

        _prefix = 'infra-rcmd-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(RouterConvergence.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "router-convergence"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", RouterConvergence.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RouterConvergence.Nodes, [], name, value)


        class Node(Entity):
            """
            Configure parameters for the specified node
            (Partially qualified location allowed)
            
            .. attribute:: node_name  <key>
            
            	Wildcard expression(eg. \*/\*/\*, R/\*/\*, R/S/\*, R/S/I)
            	**type**\:  str
            
            	**pattern:** ((([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))/){2}(([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))
            
            .. attribute:: disable
            
            	Disables the monitoring of route convergence on specified location
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable Configure parameters for the specified node (Partially qualified location allowed). Deletion of this object also causes deletion of all associated objects under Node
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rcmd-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RouterConvergence.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.disable = YLeaf(YType.empty, "disable")

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RouterConvergence.Nodes.Node, ['node_name', 'disable', 'enable'], name, value)


    class Protocols(Entity):
        """
        Table of Protocol
        
        .. attribute:: protocol
        
        	Protocol for which to configure RCMD parameters
        	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Protocols.Protocol>`
        
        

        """

        _prefix = 'infra-rcmd-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(RouterConvergence.Protocols, self).__init__()

            self.yang_name = "protocols"
            self.yang_parent_name = "router-convergence"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"protocol" : ("protocol", RouterConvergence.Protocols.Protocol)}

            self.protocol = YList(self)
            self._segment_path = lambda: "protocols"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RouterConvergence.Protocols, [], name, value)


        class Protocol(Entity):
            """
            Protocol for which to configure RCMD parameters
            
            .. attribute:: protocol_name  <key>
            
            	Specify the protocol
            	**type**\:   :py:class:`ProtocolName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.ProtocolName>`
            
            .. attribute:: enable
            
            	Enable Protocol for which to configure RCMD parameters. Deletion of this object also causes deletion of all associated objects under Protocol
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: priorities
            
            	Table of Priority
            	**type**\:   :py:class:`Priorities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Protocols.Protocol.Priorities>`
            
            

            """

            _prefix = 'infra-rcmd-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RouterConvergence.Protocols.Protocol, self).__init__()

                self.yang_name = "protocol"
                self.yang_parent_name = "protocols"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"priorities" : ("priorities", RouterConvergence.Protocols.Protocol.Priorities)}
                self._child_list_classes = {}

                self.protocol_name = YLeaf(YType.enumeration, "protocol-name")

                self.enable = YLeaf(YType.empty, "enable")

                self.priorities = RouterConvergence.Protocols.Protocol.Priorities()
                self.priorities.parent = self
                self._children_name_map["priorities"] = "priorities"
                self._children_yang_names.add("priorities")
                self._segment_path = lambda: "protocol" + "[protocol-name='" + self.protocol_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/protocols/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RouterConvergence.Protocols.Protocol, ['protocol_name', 'enable'], name, value)


            class Priorities(Entity):
                """
                Table of Priority
                
                .. attribute:: priority
                
                	Priority
                	**type**\: list of    :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Protocols.Protocol.Priorities.Priority>`
                
                

                """

                _prefix = 'infra-rcmd-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RouterConvergence.Protocols.Protocol.Priorities, self).__init__()

                    self.yang_name = "priorities"
                    self.yang_parent_name = "protocol"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"priority" : ("priority", RouterConvergence.Protocols.Protocol.Priorities.Priority)}

                    self.priority = YList(self)
                    self._segment_path = lambda: "priorities"

                def __setattr__(self, name, value):
                    self._perform_setattr(RouterConvergence.Protocols.Protocol.Priorities, [], name, value)


                class Priority(Entity):
                    """
                    Priority
                    
                    .. attribute:: rcmd_priority  <key>
                    
                    	Specify the priority
                    	**type**\:   :py:class:`RcmdPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RcmdPriority>`
                    
                    .. attribute:: disable
                    
                    	Disables the monitoring of route convergence for specified priority
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: enable
                    
                    	Enable Priority. Deletion of this object also causes deletion of all associated objects under Priority
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: frr_threshold
                    
                    	Threshold value for Fast ReRoute Coverage (in percentage)
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**units**\: percentage
                    
                    .. attribute:: leaf_networks
                    
                    	Specify the maximum number of leaf networks monitored
                    	**type**\:  int
                    
                    	**range:** 10..100
                    
                    .. attribute:: threshold
                    
                    	Threshold value for convergence (in msec)
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'infra-rcmd-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RouterConvergence.Protocols.Protocol.Priorities.Priority, self).__init__()

                        self.yang_name = "priority"
                        self.yang_parent_name = "priorities"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.rcmd_priority = YLeaf(YType.enumeration, "rcmd-priority")

                        self.disable = YLeaf(YType.empty, "disable")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.frr_threshold = YLeaf(YType.uint32, "frr-threshold")

                        self.leaf_networks = YLeaf(YType.uint32, "leaf-networks")

                        self.threshold = YLeaf(YType.int32, "threshold")
                        self._segment_path = lambda: "priority" + "[rcmd-priority='" + self.rcmd_priority.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(RouterConvergence.Protocols.Protocol.Priorities.Priority, ['rcmd_priority', 'disable', 'enable', 'frr_threshold', 'leaf_networks', 'threshold'], name, value)


    class StorageLocation(Entity):
        """
        Absolute directory path for saving the archive
        files. Example /disk0\:/rcmd/ or
        <tftp\-location>/rcmd/
        
        .. attribute:: diagnostics
        
        	Absolute directory path for storing diagnostic reports. Example /disk0\:/rcmd/ or <tftp\-location>/rcmd/
        	**type**\:  str
        
        .. attribute:: diagnostics_size
        
        	Maximum size of diagnostics dir (5% \- 80%) for local storage
        	**type**\:  int
        
        	**range:** 5..80
        
        .. attribute:: reports
        
        	Absolute directory path for storing reports. Example /disk0\:/rcmd/ or <tftp\-location>/rcmd/
        	**type**\:  str
        
        .. attribute:: reports_size
        
        	Maximum size of reports dir (5% \- 80%) for local storage
        	**type**\:  int
        
        	**range:** 5..80
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-rcmd-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(RouterConvergence.StorageLocation, self).__init__()

            self.yang_name = "storage-location"
            self.yang_parent_name = "router-convergence"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.diagnostics = YLeaf(YType.str, "diagnostics")

            self.diagnostics_size = YLeaf(YType.uint32, "diagnostics-size")

            self.reports = YLeaf(YType.str, "reports")

            self.reports_size = YLeaf(YType.uint32, "reports-size")
            self._segment_path = lambda: "storage-location"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RouterConvergence.StorageLocation, ['diagnostics', 'diagnostics_size', 'reports', 'reports_size'], name, value)

    def clone_ptr(self):
        self._top_entity = RouterConvergence()
        return self._top_entity


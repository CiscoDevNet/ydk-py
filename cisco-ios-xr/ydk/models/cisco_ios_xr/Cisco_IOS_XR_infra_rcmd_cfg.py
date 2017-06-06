""" Cisco_IOS_XR_infra_rcmd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rcmd package configuration.

This module contains definitions
for the following management objects\:
  router\-convergence\: Configure Router Convergence Monitoring

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class ProtocolNameEnum(Enum):
    """
    ProtocolNameEnum

    Protocol name

    .. data:: ospf = 0

    	Configure parameters related to OSPF

    .. data:: isis = 1

    	Configure parameters related to ISIS

    """

    ospf = 0

    isis = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rcmd_cfg as meta
        return meta._meta_table['ProtocolNameEnum']


class RcmdPriorityEnum(Enum):
    """
    RcmdPriorityEnum

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

    critical = 0

    high = 1

    medium = 2

    low = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rcmd_cfg as meta
        return meta._meta_table['RcmdPriorityEnum']



class RouterConvergence(object):
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
    _revision = '2015-11-09'

    def __init__(self):
        self.collect_diagnostics = RouterConvergence.CollectDiagnostics()
        self.collect_diagnostics.parent = self
        self.disable = None
        self.enable = None
        self.event_buffer_size = None
        self.max_events_stored = None
        self.monitoring_interval = None
        self.mpls_ldp = None
        self.nodes = RouterConvergence.Nodes()
        self.nodes.parent = self
        self.prefix_monitor_limit = None
        self.protocols = RouterConvergence.Protocols()
        self.protocols.parent = self
        self.storage_location = None


    class Protocols(object):
        """
        Table of Protocol
        
        .. attribute:: protocol
        
        	Protocol for which to configure RCMD parameters
        	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Protocols.Protocol>`
        
        

        """

        _prefix = 'infra-rcmd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.protocol = YList()
            self.protocol.parent = self
            self.protocol.name = 'protocol'


        class Protocol(object):
            """
            Protocol for which to configure RCMD parameters
            
            .. attribute:: protocol_name  <key>
            
            	Specify the protocol
            	**type**\:   :py:class:`ProtocolNameEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.ProtocolNameEnum>`
            
            .. attribute:: enable
            
            	Enable Protocol for which to configure RCMD parameters. Deletion of this object also causes deletion of all associated objects under Protocol
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: priorities
            
            	Table of Priority
            	**type**\:   :py:class:`Priorities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Protocols.Protocol.Priorities>`
            
            

            """

            _prefix = 'infra-rcmd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.protocol_name = None
                self.enable = None
                self.priorities = RouterConvergence.Protocols.Protocol.Priorities()
                self.priorities.parent = self


            class Priorities(object):
                """
                Table of Priority
                
                .. attribute:: priority
                
                	Priority
                	**type**\: list of    :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Protocols.Protocol.Priorities.Priority>`
                
                

                """

                _prefix = 'infra-rcmd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.priority = YList()
                    self.priority.parent = self
                    self.priority.name = 'priority'


                class Priority(object):
                    """
                    Priority
                    
                    .. attribute:: rcmd_priority  <key>
                    
                    	Specify the priority
                    	**type**\:   :py:class:`RcmdPriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RcmdPriorityEnum>`
                    
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
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.rcmd_priority = None
                        self.disable = None
                        self.enable = None
                        self.frr_threshold = None
                        self.leaf_networks = None
                        self.threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.rcmd_priority is None:
                            raise YPYModelError('Key property rcmd_priority is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-rcmd-cfg:priority[Cisco-IOS-XR-infra-rcmd-cfg:rcmd-priority = ' + str(self.rcmd_priority) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.rcmd_priority is not None:
                            return True

                        if self.disable is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.frr_threshold is not None:
                            return True

                        if self.leaf_networks is not None:
                            return True

                        if self.threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rcmd_cfg as meta
                        return meta._meta_table['RouterConvergence.Protocols.Protocol.Priorities.Priority']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rcmd-cfg:priorities'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.priority is not None:
                        for child_ref in self.priority:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rcmd_cfg as meta
                    return meta._meta_table['RouterConvergence.Protocols.Protocol.Priorities']['meta_info']

            @property
            def _common_path(self):
                if self.protocol_name is None:
                    raise YPYModelError('Key property protocol_name is None')

                return '/Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/Cisco-IOS-XR-infra-rcmd-cfg:protocols/Cisco-IOS-XR-infra-rcmd-cfg:protocol[Cisco-IOS-XR-infra-rcmd-cfg:protocol-name = ' + str(self.protocol_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.protocol_name is not None:
                    return True

                if self.enable is not None:
                    return True

                if self.priorities is not None and self.priorities._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rcmd_cfg as meta
                return meta._meta_table['RouterConvergence.Protocols.Protocol']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/Cisco-IOS-XR-infra-rcmd-cfg:protocols'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.protocol is not None:
                for child_ref in self.protocol:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rcmd_cfg as meta
            return meta._meta_table['RouterConvergence.Protocols']['meta_info']


    class StorageLocation(object):
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
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-rcmd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.diagnostics = None
            self.diagnostics_size = None
            self.reports = None
            self.reports_size = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/Cisco-IOS-XR-infra-rcmd-cfg:storage-location'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.diagnostics is not None:
                return True

            if self.diagnostics_size is not None:
                return True

            if self.reports is not None:
                return True

            if self.reports_size is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rcmd_cfg as meta
            return meta._meta_table['RouterConvergence.StorageLocation']['meta_info']


    class MplsLdp(object):
        """
        RCMD related configuration for MPLS\-LDP
        
        .. attribute:: remote_lfa
        
        	Monitoring configuration for Remote LFA
        	**type**\:   :py:class:`RemoteLfa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.MplsLdp.RemoteLfa>`
        
        	**presence node**\: True
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-rcmd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.remote_lfa = None


        class RemoteLfa(object):
            """
            Monitoring configuration for Remote LFA
            
            .. attribute:: threshold
            
            	Threshold value for label coverage (in percentage)
            	**type**\:  int
            
            	**range:** 1..100
            
            	**units**\: percentage
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-rcmd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self._is_presence = True
                self.threshold = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/Cisco-IOS-XR-infra-rcmd-cfg:mpls-ldp/Cisco-IOS-XR-infra-rcmd-cfg:remote-lfa'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self._is_presence:
                    return True
                if self.threshold is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rcmd_cfg as meta
                return meta._meta_table['RouterConvergence.MplsLdp.RemoteLfa']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/Cisco-IOS-XR-infra-rcmd-cfg:mpls-ldp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.remote_lfa is not None and self.remote_lfa._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rcmd_cfg as meta
            return meta._meta_table['RouterConvergence.MplsLdp']['meta_info']


    class CollectDiagnostics(object):
        """
        Table of CollectDiagnostics
        
        .. attribute:: collect_diagnostic
        
        	Collect diagnostics on specified node
        	**type**\: list of    :py:class:`CollectDiagnostic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.CollectDiagnostics.CollectDiagnostic>`
        
        

        """

        _prefix = 'infra-rcmd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.collect_diagnostic = YList()
            self.collect_diagnostic.parent = self
            self.collect_diagnostic.name = 'collect_diagnostic'


        class CollectDiagnostic(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.enable = None

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/Cisco-IOS-XR-infra-rcmd-cfg:collect-diagnostics/Cisco-IOS-XR-infra-rcmd-cfg:collect-diagnostic[Cisco-IOS-XR-infra-rcmd-cfg:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rcmd_cfg as meta
                return meta._meta_table['RouterConvergence.CollectDiagnostics.CollectDiagnostic']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/Cisco-IOS-XR-infra-rcmd-cfg:collect-diagnostics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.collect_diagnostic is not None:
                for child_ref in self.collect_diagnostic:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rcmd_cfg as meta
            return meta._meta_table['RouterConvergence.CollectDiagnostics']['meta_info']


    class Nodes(object):
        """
        Table of Node
        
        .. attribute:: node
        
        	Configure parameters for the specified node (Partially qualified location allowed)
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Nodes.Node>`
        
        

        """

        _prefix = 'infra-rcmd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.disable = None
                self.enable = None

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/Cisco-IOS-XR-infra-rcmd-cfg:nodes/Cisco-IOS-XR-infra-rcmd-cfg:node[Cisco-IOS-XR-infra-rcmd-cfg:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.disable is not None:
                    return True

                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rcmd_cfg as meta
                return meta._meta_table['RouterConvergence.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/Cisco-IOS-XR-infra-rcmd-cfg:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rcmd_cfg as meta
            return meta._meta_table['RouterConvergence.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-rcmd-cfg:router-convergence'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.collect_diagnostics is not None and self.collect_diagnostics._has_data():
            return True

        if self.disable is not None:
            return True

        if self.enable is not None:
            return True

        if self.event_buffer_size is not None:
            return True

        if self.max_events_stored is not None:
            return True

        if self.monitoring_interval is not None:
            return True

        if self.mpls_ldp is not None and self.mpls_ldp._has_data():
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        if self.prefix_monitor_limit is not None:
            return True

        if self.protocols is not None and self.protocols._has_data():
            return True

        if self.storage_location is not None and self.storage_location._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rcmd_cfg as meta
        return meta._meta_table['RouterConvergence']['meta_info']



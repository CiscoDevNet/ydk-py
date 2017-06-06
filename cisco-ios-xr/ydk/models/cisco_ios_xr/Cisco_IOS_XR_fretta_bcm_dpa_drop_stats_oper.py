""" Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fretta\-bcm\-dpa\-drop\-stats package operational data.

This module contains definitions
for the following management objects\:
  drop\: Drop stats data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Drop(object):
    """
    Drop stats data
    
    .. attribute:: nodes
    
    	Drop data per node
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper.Drop.Nodes>`
    
    

    """

    _prefix = 'fretta-bcm-dpa-drop-stats-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Drop.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Drop data per node
        
        .. attribute:: node
        
        	Drop stats data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper.Drop.Nodes.Node>`
        
        

        """

        _prefix = 'fretta-bcm-dpa-drop-stats-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Drop stats data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: npu_number_for_drop_stats
            
            	NPU drop stats
            	**type**\:   :py:class:`NpuNumberForDropStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper.Drop.Nodes.Node.NpuNumberForDropStats>`
            
            

            """

            _prefix = 'fretta-bcm-dpa-drop-stats-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.npu_number_for_drop_stats = Drop.Nodes.Node.NpuNumberForDropStats()
                self.npu_number_for_drop_stats.parent = self


            class NpuNumberForDropStats(object):
                """
                NPU drop stats
                
                .. attribute:: npu_number_for_drop_stat
                
                	All drop stats for a particular NPU
                	**type**\: list of    :py:class:`NpuNumberForDropStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper.Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat>`
                
                

                """

                _prefix = 'fretta-bcm-dpa-drop-stats-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.npu_number_for_drop_stat = YList()
                    self.npu_number_for_drop_stat.parent = self
                    self.npu_number_for_drop_stat.name = 'npu_number_for_drop_stat'


                class NpuNumberForDropStat(object):
                    """
                    All drop stats for a particular NPU
                    
                    .. attribute:: npu_id  <key>
                    
                    	NPU number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: drop_specific_stats_data
                    
                    	Second argument to the module
                    	**type**\: list of    :py:class:`DropSpecificStatsData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper.Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat.DropSpecificStatsData>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-drop-stats-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.npu_id = None
                        self.drop_specific_stats_data = YList()
                        self.drop_specific_stats_data.parent = self
                        self.drop_specific_stats_data.name = 'drop_specific_stats_data'


                    class DropSpecificStatsData(object):
                        """
                        Second argument to the module
                        
                        .. attribute:: drop_data  <key>
                        
                        	Drop ID
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: count
                        
                        	count
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: id
                        
                        	id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-drop-stats-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.drop_data = None
                            self.count = None
                            self.id = None
                            self.name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.drop_data is None:
                                raise YPYModelError('Key property drop_data is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:drop-specific-stats-data[Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:drop-data = ' + str(self.drop_data) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.drop_data is not None:
                                return True

                            if self.count is not None:
                                return True

                            if self.id is not None:
                                return True

                            if self.name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper as meta
                            return meta._meta_table['Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat.DropSpecificStatsData']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.npu_id is None:
                            raise YPYModelError('Key property npu_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:npu-number-for-drop-stat[Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:npu-id = ' + str(self.npu_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.npu_id is not None:
                            return True

                        if self.drop_specific_stats_data is not None:
                            for child_ref in self.drop_specific_stats_data:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper as meta
                        return meta._meta_table['Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:npu-number-for-drop-stats'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.npu_number_for_drop_stat is not None:
                        for child_ref in self.npu_number_for_drop_stat:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper as meta
                    return meta._meta_table['Drop.Nodes.Node.NpuNumberForDropStats']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:drop/Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:nodes/Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:node[Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.npu_number_for_drop_stats is not None and self.npu_number_for_drop_stats._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper as meta
                return meta._meta_table['Drop.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:drop/Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper as meta
            return meta._meta_table['Drop.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:drop'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper as meta
        return meta._meta_table['Drop']['meta_info']



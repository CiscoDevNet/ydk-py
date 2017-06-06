""" Cisco_IOS_XR_asr9k_fsi_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-fsi package operational data.

This module contains definitions
for the following management objects\:
  fabric\-stats\: Fabric stats operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class FabricStats(object):
    """
    Fabric stats operational data
    
    .. attribute:: nodes
    
    	Table of Nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes>`
    
    

    """

    _prefix = 'asr9k-fsi-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = FabricStats.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Table of Nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-fsi-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Information about a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: statses
            
            	Table of stats information
            	**type**\:   :py:class:`Statses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes.Node.Statses>`
            
            

            """

            _prefix = 'asr9k-fsi-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.statses = FabricStats.Nodes.Node.Statses()
                self.statses.parent = self


            class Statses(object):
                """
                Table of stats information
                
                .. attribute:: stats
                
                	Stats information for a particular type
                	**type**\: list of    :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes.Node.Statses.Stats>`
                
                

                """

                _prefix = 'asr9k-fsi-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.stats = YList()
                    self.stats.parent = self
                    self.stats.name = 'stats'


                class Stats(object):
                    """
                    Stats information for a particular type
                    
                    .. attribute:: type  <key>
                    
                    	Fabric asic type
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: stat_table_name
                    
                    	Stat Table Name
                    	**type**\:  str
                    
                    .. attribute:: stats_table
                    
                    	Array of counters 
                    	**type**\: list of    :py:class:`StatsTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes.Node.Statses.Stats.StatsTable>`
                    
                    

                    """

                    _prefix = 'asr9k-fsi-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.type = None
                        self.stat_table_name = None
                        self.stats_table = YList()
                        self.stats_table.parent = self
                        self.stats_table.name = 'stats_table'


                    class StatsTable(object):
                        """
                        Array of counters 
                        
                        .. attribute:: fsi_stat
                        
                        	Stats Table
                        	**type**\: list of    :py:class:`FsiStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat>`
                        
                        

                        """

                        _prefix = 'asr9k-fsi-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.fsi_stat = YList()
                            self.fsi_stat.parent = self
                            self.fsi_stat.name = 'fsi_stat'


                        class FsiStat(object):
                            """
                            Stats Table
                            
                            .. attribute:: count
                            
                            	Counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: counter_name
                            
                            	Counter Name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'asr9k-fsi-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.count = None
                                self.counter_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-fsi-oper:fsi-stat'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.count is not None:
                                    return True

                                if self.counter_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_fsi_oper as meta
                                return meta._meta_table['FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-fsi-oper:stats-table'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.fsi_stat is not None:
                                for child_ref in self.fsi_stat:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_fsi_oper as meta
                            return meta._meta_table['FabricStats.Nodes.Node.Statses.Stats.StatsTable']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.type is None:
                            raise YPYModelError('Key property type is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-fsi-oper:stats[Cisco-IOS-XR-asr9k-fsi-oper:type = ' + str(self.type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.type is not None:
                            return True

                        if self.stat_table_name is not None:
                            return True

                        if self.stats_table is not None:
                            for child_ref in self.stats_table:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_fsi_oper as meta
                        return meta._meta_table['FabricStats.Nodes.Node.Statses.Stats']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-fsi-oper:statses'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.stats is not None:
                        for child_ref in self.stats:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_fsi_oper as meta
                    return meta._meta_table['FabricStats.Nodes.Node.Statses']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-asr9k-fsi-oper:fabric-stats/Cisco-IOS-XR-asr9k-fsi-oper:nodes/Cisco-IOS-XR-asr9k-fsi-oper:node[Cisco-IOS-XR-asr9k-fsi-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.statses is not None and self.statses._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_fsi_oper as meta
                return meta._meta_table['FabricStats.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-fsi-oper:fabric-stats/Cisco-IOS-XR-asr9k-fsi-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_fsi_oper as meta
            return meta._meta_table['FabricStats.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-fsi-oper:fabric-stats'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_fsi_oper as meta
        return meta._meta_table['FabricStats']['meta_info']



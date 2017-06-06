""" Cisco_IOS_XR_asr9k_asic_errors_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-asic\-errors package operational data.

This module contains definitions
for the following management objects\:
  asic\-error\-stats\: Asic error stats operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class AsicErrorStats(object):
    """
    Asic error stats operational data
    
    .. attribute:: nodes
    
    	Table of Nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Nodes>`
    
    

    """

    _prefix = 'asr9k-asic-errors-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = AsicErrorStats.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Table of Nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-asic-errors-oper'
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
            
            .. attribute:: counts
            
            	Table of all Asic Types information on a node
            	**type**\:   :py:class:`Counts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Nodes.Node.Counts>`
            
            

            """

            _prefix = 'asr9k-asic-errors-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.counts = AsicErrorStats.Nodes.Node.Counts()
                self.counts.parent = self


            class Counts(object):
                """
                Table of all Asic Types information on a node
                
                .. attribute:: count
                
                	Summary Asic error counts for a Asic Type
                	**type**\: list of    :py:class:`Count <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Nodes.Node.Counts.Count>`
                
                

                """

                _prefix = 'asr9k-asic-errors-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.count = YList()
                    self.count.parent = self
                    self.count.name = 'count'


                class Count(object):
                    """
                    Summary Asic error counts for a Asic Type
                    
                    .. attribute:: type  <key>
                    
                    	Asic Type
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: sum_data
                    
                    	sum data
                    	**type**\: list of    :py:class:`SumData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Nodes.Node.Counts.Count.SumData>`
                    
                    

                    """

                    _prefix = 'asr9k-asic-errors-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.type = None
                        self.sum_data = YList()
                        self.sum_data.parent = self
                        self.sum_data.name = 'sum_data'


                    class SumData(object):
                        """
                        sum data
                        
                        .. attribute:: crc_err_count
                        
                        	crc err count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: gen_err_count
                        
                        	gen err count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: instance
                        
                        	instance
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mbe_err_count
                        
                        	mbe err count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: node_key
                        
                        	node key
                        	**type**\:  list of int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: num_nodes
                        
                        	num nodes
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: par_err_count
                        
                        	par err count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reset_err_count
                        
                        	reset err count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sbe_err_count
                        
                        	sbe err count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'asr9k-asic-errors-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.crc_err_count = None
                            self.gen_err_count = None
                            self.instance = None
                            self.mbe_err_count = None
                            self.node_key = YLeafList()
                            self.node_key.parent = self
                            self.node_key.name = 'node_key'
                            self.num_nodes = None
                            self.par_err_count = None
                            self.reset_err_count = None
                            self.sbe_err_count = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-asic-errors-oper:sum-data'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.crc_err_count is not None:
                                return True

                            if self.gen_err_count is not None:
                                return True

                            if self.instance is not None:
                                return True

                            if self.mbe_err_count is not None:
                                return True

                            if self.node_key is not None:
                                for child in self.node_key:
                                    if child is not None:
                                        return True

                            if self.num_nodes is not None:
                                return True

                            if self.par_err_count is not None:
                                return True

                            if self.reset_err_count is not None:
                                return True

                            if self.sbe_err_count is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_asic_errors_oper as meta
                            return meta._meta_table['AsicErrorStats.Nodes.Node.Counts.Count.SumData']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.type is None:
                            raise YPYModelError('Key property type is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-asic-errors-oper:count[Cisco-IOS-XR-asr9k-asic-errors-oper:type = ' + str(self.type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.type is not None:
                            return True

                        if self.sum_data is not None:
                            for child_ref in self.sum_data:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_asic_errors_oper as meta
                        return meta._meta_table['AsicErrorStats.Nodes.Node.Counts.Count']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-asic-errors-oper:counts'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.count is not None:
                        for child_ref in self.count:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_asic_errors_oper as meta
                    return meta._meta_table['AsicErrorStats.Nodes.Node.Counts']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-asr9k-asic-errors-oper:asic-error-stats/Cisco-IOS-XR-asr9k-asic-errors-oper:nodes/Cisco-IOS-XR-asr9k-asic-errors-oper:node[Cisco-IOS-XR-asr9k-asic-errors-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.counts is not None and self.counts._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_asic_errors_oper as meta
                return meta._meta_table['AsicErrorStats.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-asic-errors-oper:asic-error-stats/Cisco-IOS-XR-asr9k-asic-errors-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_asic_errors_oper as meta
            return meta._meta_table['AsicErrorStats.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-asic-errors-oper:asic-error-stats'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_asic_errors_oper as meta
        return meta._meta_table['AsicErrorStats']['meta_info']



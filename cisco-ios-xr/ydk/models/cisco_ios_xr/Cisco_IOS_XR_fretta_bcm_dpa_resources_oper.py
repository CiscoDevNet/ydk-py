""" Cisco_IOS_XR_fretta_bcm_dpa_resources_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fretta\-bcm\-dpa\-resources package operational data.

This module contains definitions
for the following management objects\:
  dpa\: DPA operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Dpa(object):
    """
    DPA operational data
    
    .. attribute:: resources
    
    	DPA Resources Data
    	**type**\:   :py:class:`Resources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources>`
    
    .. attribute:: stats
    
    	DPA voq data
    	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats>`
    
    

    """

    _prefix = 'fretta-bcm-dpa-resources-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.resources = Dpa.Resources()
        self.resources.parent = self
        self.stats = Dpa.Stats()
        self.stats.parent = self


    class Resources(object):
        """
        DPA Resources Data
        
        .. attribute:: nodes
        
        	DPA data for available nodes
        	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes>`
        
        

        """

        _prefix = 'fretta-bcm-dpa-resources-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.nodes = Dpa.Resources.Nodes()
            self.nodes.parent = self


        class Nodes(object):
            """
            DPA data for available nodes
            
            .. attribute:: node
            
            	DPA operational data for a particular node
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node>`
            
            

            """

            _prefix = 'fretta-bcm-dpa-resources-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node = YList()
                self.node.parent = self
                self.node.name = 'node'


            class Node(object):
                """
                DPA operational data for a particular node
                
                .. attribute:: node_name  <key>
                
                	Node ID
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: table_datas
                
                	DPA Resources table
                	**type**\:   :py:class:`TableDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node.TableDatas>`
                
                

                """

                _prefix = 'fretta-bcm-dpa-resources-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node_name = None
                    self.table_datas = Dpa.Resources.Nodes.Node.TableDatas()
                    self.table_datas.parent = self


                class TableDatas(object):
                    """
                    DPA Resources table
                    
                    .. attribute:: table_data
                    
                    	Resources table
                    	**type**\: list of    :py:class:`TableData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node.TableDatas.TableData>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.table_data = YList()
                        self.table_data.parent = self
                        self.table_data.name = 'table_data'


                    class TableData(object):
                        """
                        Resources table
                        
                        .. attribute:: resource  <key>
                        
                        	Resource type
                        	**type**\:  int
                        
                        	**range:** 0..106
                        
                        .. attribute:: is_global
                        
                        	is global
                        	**type**\:  bool
                        
                        .. attribute:: name
                        
                        	name
                        	**type**\:  str
                        
                        	**length:** 0..64
                        
                        .. attribute:: npu_tblr
                        
                        	npu tblr
                        	**type**\: list of    :py:class:`NpuTblr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr>`
                        
                        .. attribute:: num_npus
                        
                        	num npus
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: table_id
                        
                        	table id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: table_specific_list
                        
                        	table specific list
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.resource = None
                            self.is_global = None
                            self.name = None
                            self.npu_tblr = YList()
                            self.npu_tblr.parent = self
                            self.npu_tblr.name = 'npu_tblr'
                            self.num_npus = None
                            self.table_id = None
                            self.table_specific_list = None


                        class NpuTblr(object):
                            """
                            npu tblr
                            
                            .. attribute:: create_ok
                            
                            	create ok
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: create_req
                            
                            	create req
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: delete_ok
                            
                            	delete ok
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: delete_req
                            
                            	delete req
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: eod_ok
                            
                            	eod ok
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: eod_req
                            
                            	eod req
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_db_exists
                            
                            	err db exists
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_db_nomem
                            
                            	err db nomem
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_db_notfound
                            
                            	err db notfound
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_hw_fail
                            
                            	err hw fail
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_ref_resolve
                            
                            	err ref resolve
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: npu_id
                            
                            	npu id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: num_objs
                            
                            	num objs
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: update_ok
                            
                            	update ok
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: update_req
                            
                            	update req
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.create_ok = None
                                self.create_req = None
                                self.delete_ok = None
                                self.delete_req = None
                                self.eod_ok = None
                                self.eod_req = None
                                self.err_db_exists = None
                                self.err_db_nomem = None
                                self.err_db_notfound = None
                                self.err_hw_fail = None
                                self.err_ref_resolve = None
                                self.npu_id = None
                                self.num_objs = None
                                self.update_ok = None
                                self.update_req = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:npu-tblr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.create_ok is not None:
                                    return True

                                if self.create_req is not None:
                                    return True

                                if self.delete_ok is not None:
                                    return True

                                if self.delete_req is not None:
                                    return True

                                if self.eod_ok is not None:
                                    return True

                                if self.eod_req is not None:
                                    return True

                                if self.err_db_exists is not None:
                                    return True

                                if self.err_db_nomem is not None:
                                    return True

                                if self.err_db_notfound is not None:
                                    return True

                                if self.err_hw_fail is not None:
                                    return True

                                if self.err_ref_resolve is not None:
                                    return True

                                if self.npu_id is not None:
                                    return True

                                if self.num_objs is not None:
                                    return True

                                if self.update_ok is not None:
                                    return True

                                if self.update_req is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                                return meta._meta_table['Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.resource is None:
                                raise YPYModelError('Key property resource is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:table-data[Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:resource = ' + str(self.resource) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.resource is not None:
                                return True

                            if self.is_global is not None:
                                return True

                            if self.name is not None:
                                return True

                            if self.npu_tblr is not None:
                                for child_ref in self.npu_tblr:
                                    if child_ref._has_data():
                                        return True

                            if self.num_npus is not None:
                                return True

                            if self.table_id is not None:
                                return True

                            if self.table_specific_list is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                            return meta._meta_table['Dpa.Resources.Nodes.Node.TableDatas.TableData']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:table-datas'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.table_data is not None:
                            for child_ref in self.table_data:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                        return meta._meta_table['Dpa.Resources.Nodes.Node.TableDatas']['meta_info']

                @property
                def _common_path(self):
                    if self.node_name is None:
                        raise YPYModelError('Key property node_name is None')

                    return '/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:resources/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:nodes/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:node[Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:node-name = ' + str(self.node_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.node_name is not None:
                        return True

                    if self.table_datas is not None and self.table_datas._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                    return meta._meta_table['Dpa.Resources.Nodes.Node']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:resources/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:nodes'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                return meta._meta_table['Dpa.Resources.Nodes']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:resources'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.nodes is not None and self.nodes._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
            return meta._meta_table['Dpa.Resources']['meta_info']


    class Stats(object):
        """
        DPA voq data
        
        .. attribute:: nodes
        
        	DPA data for available nodes
        	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes>`
        
        

        """

        _prefix = 'fretta-bcm-dpa-resources-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.nodes = Dpa.Stats.Nodes()
            self.nodes.parent = self


        class Nodes(object):
            """
            DPA data for available nodes
            
            .. attribute:: node
            
            	DPA operational data for a particular node
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node>`
            
            

            """

            _prefix = 'fretta-bcm-dpa-resources-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node = YList()
                self.node.parent = self
                self.node.name = 'node'


            class Node(object):
                """
                DPA operational data for a particular node
                
                .. attribute:: node_name  <key>
                
                	Node ID
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: clear_voq_data_for_npu_numbers
                
                	Clear voq ingress stats for all interfaces on particular npu
                	**type**\:   :py:class:`ClearVoqDataForNpuNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers>`
                
                .. attribute:: npu_number_for_trap_data_clears
                
                	Trap stats for all traps
                	**type**\:   :py:class:`NpuNumberForTrapDataClears <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears>`
                
                .. attribute:: npu_number_for_trap_datas
                
                	Trap stats for all traps
                	**type**\:   :py:class:`NpuNumberForTrapDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas>`
                
                .. attribute:: npu_number_for_voq_datas
                
                	DPA voq ingress stats for all interfaces
                	**type**\:   :py:class:`NpuNumberForVoqDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas>`
                
                .. attribute:: voq_base_number_stats_clears
                
                	Clear DPA voq base stats 
                	**type**\:   :py:class:`VoqBaseNumberStatsClears <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears>`
                
                .. attribute:: voq_base_numbers
                
                	DPA voq base stats 
                	**type**\:   :py:class:`VoqBaseNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.VoqBaseNumbers>`
                
                

                """

                _prefix = 'fretta-bcm-dpa-resources-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node_name = None
                    self.clear_voq_data_for_npu_numbers = Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers()
                    self.clear_voq_data_for_npu_numbers.parent = self
                    self.npu_number_for_trap_data_clears = Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears()
                    self.npu_number_for_trap_data_clears.parent = self
                    self.npu_number_for_trap_datas = Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas()
                    self.npu_number_for_trap_datas.parent = self
                    self.npu_number_for_voq_datas = Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas()
                    self.npu_number_for_voq_datas.parent = self
                    self.voq_base_number_stats_clears = Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears()
                    self.voq_base_number_stats_clears.parent = self
                    self.voq_base_numbers = Dpa.Stats.Nodes.Node.VoqBaseNumbers()
                    self.voq_base_numbers.parent = self


                class VoqBaseNumberStatsClears(object):
                    """
                    Clear DPA voq base stats 
                    
                    .. attribute:: voq_base_number_stats_clear
                    
                    	Filter by npu number
                    	**type**\: list of    :py:class:`VoqBaseNumberStatsClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears.VoqBaseNumberStatsClear>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.voq_base_number_stats_clear = YList()
                        self.voq_base_number_stats_clear.parent = self
                        self.voq_base_number_stats_clear.name = 'voq_base_number_stats_clear'


                    class VoqBaseNumberStatsClear(object):
                        """
                        Filter by npu number
                        
                        .. attribute:: npu_number  <key>
                        
                        	Npu Number
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: voq_base_stats_clear_data
                        
                        	Clear stats  for a particular voq base number
                        	**type**\: list of    :py:class:`VoqBaseStatsClearData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears.VoqBaseNumberStatsClear.VoqBaseStatsClearData>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.npu_number = None
                            self.voq_base_stats_clear_data = YList()
                            self.voq_base_stats_clear_data.parent = self
                            self.voq_base_stats_clear_data.name = 'voq_base_stats_clear_data'


                        class VoqBaseStatsClearData(object):
                            """
                            Clear stats  for a particular voq base
                            number
                            
                            .. attribute:: base_number  <key>
                            
                            	Interface handle
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clear_status
                            
                            	clear status
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.base_number = None
                                self.clear_status = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.base_number is None:
                                    raise YPYModelError('Key property base_number is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:voq-base-stats-clear-data[Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:base-number = ' + str(self.base_number) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.base_number is not None:
                                    return True

                                if self.clear_status is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                                return meta._meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears.VoqBaseNumberStatsClear.VoqBaseStatsClearData']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.npu_number is None:
                                raise YPYModelError('Key property npu_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:voq-base-number-stats-clear[Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:npu-number = ' + str(self.npu_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.npu_number is not None:
                                return True

                            if self.voq_base_stats_clear_data is not None:
                                for child_ref in self.voq_base_stats_clear_data:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                            return meta._meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears.VoqBaseNumberStatsClear']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:voq-base-number-stats-clears'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.voq_base_number_stats_clear is not None:
                            for child_ref in self.voq_base_number_stats_clear:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                        return meta._meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears']['meta_info']


                class NpuNumberForTrapDatas(object):
                    """
                    Trap stats for all traps
                    
                    .. attribute:: npu_number_for_trap_data
                    
                    	All trap stats for a particular npu
                    	**type**\: list of    :py:class:`NpuNumberForTrapData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas.NpuNumberForTrapData>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.npu_number_for_trap_data = YList()
                        self.npu_number_for_trap_data.parent = self
                        self.npu_number_for_trap_data.name = 'npu_number_for_trap_data'


                    class NpuNumberForTrapData(object):
                        """
                        All trap stats for a particular npu
                        
                        .. attribute:: npu_id  <key>
                        
                        	NPU number
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: trap_specific_stats_data
                        
                        	Filter by specific trap id
                        	**type**\: list of    :py:class:`TrapSpecificStatsData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas.NpuNumberForTrapData.TrapSpecificStatsData>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.npu_id = None
                            self.trap_specific_stats_data = YList()
                            self.trap_specific_stats_data.parent = self
                            self.trap_specific_stats_data.name = 'trap_specific_stats_data'


                        class TrapSpecificStatsData(object):
                            """
                            Filter by specific trap id
                            
                            .. attribute:: trap_data  <key>
                            
                            	Trap Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: encap_id
                            
                            	encap id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fec_id
                            
                            	fec id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: gport
                            
                            	gport
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: id
                            
                            	id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mc_group
                            
                            	mc group
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: npu_id
                            
                            	npu id
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: offset
                            
                            	offset
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: packet_accepted
                            
                            	packet accepted
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: packet_dropped
                            
                            	packet dropped
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: policer_id
                            
                            	policer id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: priority
                            
                            	priority
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stats_id
                            
                            	stats id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: trap_id
                            
                            	trap id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: trap_strength
                            
                            	trap strength
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: trap_string
                            
                            	trap string
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.trap_data = None
                                self.encap_id = None
                                self.fec_id = None
                                self.gport = None
                                self.id = None
                                self.mc_group = None
                                self.npu_id = None
                                self.offset = None
                                self.packet_accepted = None
                                self.packet_dropped = None
                                self.policer_id = None
                                self.priority = None
                                self.stats_id = None
                                self.trap_id = None
                                self.trap_strength = None
                                self.trap_string = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.trap_data is None:
                                    raise YPYModelError('Key property trap_data is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:trap-specific-stats-data[Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:trap-data = ' + str(self.trap_data) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.trap_data is not None:
                                    return True

                                if self.encap_id is not None:
                                    return True

                                if self.fec_id is not None:
                                    return True

                                if self.gport is not None:
                                    return True

                                if self.id is not None:
                                    return True

                                if self.mc_group is not None:
                                    return True

                                if self.npu_id is not None:
                                    return True

                                if self.offset is not None:
                                    return True

                                if self.packet_accepted is not None:
                                    return True

                                if self.packet_dropped is not None:
                                    return True

                                if self.policer_id is not None:
                                    return True

                                if self.priority is not None:
                                    return True

                                if self.stats_id is not None:
                                    return True

                                if self.trap_id is not None:
                                    return True

                                if self.trap_strength is not None:
                                    return True

                                if self.trap_string is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                                return meta._meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas.NpuNumberForTrapData.TrapSpecificStatsData']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.npu_id is None:
                                raise YPYModelError('Key property npu_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:npu-number-for-trap-data[Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:npu-id = ' + str(self.npu_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.npu_id is not None:
                                return True

                            if self.trap_specific_stats_data is not None:
                                for child_ref in self.trap_specific_stats_data:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                            return meta._meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas.NpuNumberForTrapData']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:npu-number-for-trap-datas'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.npu_number_for_trap_data is not None:
                            for child_ref in self.npu_number_for_trap_data:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                        return meta._meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas']['meta_info']


                class VoqBaseNumbers(object):
                    """
                    DPA voq base stats 
                    
                    .. attribute:: voq_base_number
                    
                    	Filter by npu number
                    	**type**\: list of    :py:class:`VoqBaseNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.voq_base_number = YList()
                        self.voq_base_number.parent = self
                        self.voq_base_number.name = 'voq_base_number'


                    class VoqBaseNumber(object):
                        """
                        Filter by npu number
                        
                        .. attribute:: npu_number  <key>
                        
                        	Npu Number
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: voq_base_stats_data
                        
                        	Voq Base Number for a particular voq
                        	**type**\: list of    :py:class:`VoqBaseStatsData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseStatsData>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.npu_number = None
                            self.voq_base_stats_data = YList()
                            self.voq_base_stats_data.parent = self
                            self.voq_base_stats_data.name = 'voq_base_stats_data'


                        class VoqBaseStatsData(object):
                            """
                            Voq Base Number for a particular voq
                            
                            .. attribute:: base_number  <key>
                            
                            	Interface handle
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connector_id
                            
                            	connector id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ifhandle
                            
                            	ifhandle
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_inuse
                            
                            	is inuse
                            	**type**\:  bool
                            
                            .. attribute:: is_local_port
                            
                            	is local port
                            	**type**\:  bool
                            
                            .. attribute:: npu_core
                            
                            	npu core
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: npu_num
                            
                            	npu num
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_num
                            
                            	port num
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_speed
                            
                            	port speed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pp_port
                            
                            	pp port
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rack_num
                            
                            	rack num
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: slot_num
                            
                            	slot num
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: sysport
                            
                            	sysport
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: voq_base
                            
                            	voq base
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: voq_stat
                            
                            	voq stat
                            	**type**\: list of    :py:class:`VoqStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseStatsData.VoqStat>`
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.base_number = None
                                self.connector_id = None
                                self.ifhandle = None
                                self.is_inuse = None
                                self.is_local_port = None
                                self.npu_core = None
                                self.npu_num = None
                                self.port_num = None
                                self.port_speed = None
                                self.pp_port = None
                                self.rack_num = None
                                self.slot_num = None
                                self.sysport = None
                                self.voq_base = None
                                self.voq_stat = YList()
                                self.voq_stat.parent = self
                                self.voq_stat.name = 'voq_stat'


                            class VoqStat(object):
                                """
                                voq stat
                                
                                .. attribute:: gport_dropped_bytes
                                
                                	GportDroppedBytes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: gport_dropped_pkts
                                
                                	GportDroppedPkts
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: gport_received_bytes
                                
                                	GportReceivedBytes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: gport_received_pkts
                                
                                	GportReceivedPkts
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.gport_dropped_bytes = None
                                    self.gport_dropped_pkts = None
                                    self.gport_received_bytes = None
                                    self.gport_received_pkts = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:voq-stat'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.gport_dropped_bytes is not None:
                                        return True

                                    if self.gport_dropped_pkts is not None:
                                        return True

                                    if self.gport_received_bytes is not None:
                                        return True

                                    if self.gport_received_pkts is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                                    return meta._meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseStatsData.VoqStat']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.base_number is None:
                                    raise YPYModelError('Key property base_number is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:voq-base-stats-data[Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:base-number = ' + str(self.base_number) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.base_number is not None:
                                    return True

                                if self.connector_id is not None:
                                    return True

                                if self.ifhandle is not None:
                                    return True

                                if self.is_inuse is not None:
                                    return True

                                if self.is_local_port is not None:
                                    return True

                                if self.npu_core is not None:
                                    return True

                                if self.npu_num is not None:
                                    return True

                                if self.port_num is not None:
                                    return True

                                if self.port_speed is not None:
                                    return True

                                if self.pp_port is not None:
                                    return True

                                if self.rack_num is not None:
                                    return True

                                if self.slot_num is not None:
                                    return True

                                if self.sysport is not None:
                                    return True

                                if self.voq_base is not None:
                                    return True

                                if self.voq_stat is not None:
                                    for child_ref in self.voq_stat:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                                return meta._meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseStatsData']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.npu_number is None:
                                raise YPYModelError('Key property npu_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:voq-base-number[Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:npu-number = ' + str(self.npu_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.npu_number is not None:
                                return True

                            if self.voq_base_stats_data is not None:
                                for child_ref in self.voq_base_stats_data:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                            return meta._meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:voq-base-numbers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.voq_base_number is not None:
                            for child_ref in self.voq_base_number:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                        return meta._meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers']['meta_info']


                class NpuNumberForVoqDatas(object):
                    """
                    DPA voq ingress stats for all interfaces
                    
                    .. attribute:: npu_number_for_voq_data
                    
                    	All voq stats for a particular npu
                    	**type**\: list of    :py:class:`NpuNumberForVoqData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.npu_number_for_voq_data = YList()
                        self.npu_number_for_voq_data.parent = self
                        self.npu_number_for_voq_data.name = 'npu_number_for_voq_data'


                    class NpuNumberForVoqData(object):
                        """
                        All voq stats for a particular npu
                        
                        .. attribute:: npu_id  <key>
                        
                        	Npu number
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: voq_specific_stats_data
                        
                        	Filter data by interface handle
                        	**type**\: list of    :py:class:`VoqSpecificStatsData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData.VoqSpecificStatsData>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.npu_id = None
                            self.voq_specific_stats_data = YList()
                            self.voq_specific_stats_data.parent = self
                            self.voq_specific_stats_data.name = 'voq_specific_stats_data'


                        class VoqSpecificStatsData(object):
                            """
                            Filter data by interface handle
                            
                            .. attribute:: voq_data  <key>
                            
                            	Interface Handle
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: connector_id
                            
                            	connector id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ifhandle
                            
                            	ifhandle
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_inuse
                            
                            	is inuse
                            	**type**\:  bool
                            
                            .. attribute:: is_local_port
                            
                            	is local port
                            	**type**\:  bool
                            
                            .. attribute:: npu_core
                            
                            	npu core
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: npu_num
                            
                            	npu num
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_num
                            
                            	port num
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_speed
                            
                            	port speed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pp_port
                            
                            	pp port
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rack_num
                            
                            	rack num
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: slot_num
                            
                            	slot num
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: sysport
                            
                            	sysport
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: voq_base
                            
                            	voq base
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: voq_stat
                            
                            	voq stat
                            	**type**\: list of    :py:class:`VoqStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData.VoqSpecificStatsData.VoqStat>`
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.voq_data = None
                                self.connector_id = None
                                self.ifhandle = None
                                self.is_inuse = None
                                self.is_local_port = None
                                self.npu_core = None
                                self.npu_num = None
                                self.port_num = None
                                self.port_speed = None
                                self.pp_port = None
                                self.rack_num = None
                                self.slot_num = None
                                self.sysport = None
                                self.voq_base = None
                                self.voq_stat = YList()
                                self.voq_stat.parent = self
                                self.voq_stat.name = 'voq_stat'


                            class VoqStat(object):
                                """
                                voq stat
                                
                                .. attribute:: gport_dropped_bytes
                                
                                	GportDroppedBytes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: gport_dropped_pkts
                                
                                	GportDroppedPkts
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: gport_received_bytes
                                
                                	GportReceivedBytes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: gport_received_pkts
                                
                                	GportReceivedPkts
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.gport_dropped_bytes = None
                                    self.gport_dropped_pkts = None
                                    self.gport_received_bytes = None
                                    self.gport_received_pkts = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:voq-stat'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.gport_dropped_bytes is not None:
                                        return True

                                    if self.gport_dropped_pkts is not None:
                                        return True

                                    if self.gport_received_bytes is not None:
                                        return True

                                    if self.gport_received_pkts is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                                    return meta._meta_table['Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData.VoqSpecificStatsData.VoqStat']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.voq_data is None:
                                    raise YPYModelError('Key property voq_data is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:voq-specific-stats-data[Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:voq-data = ' + str(self.voq_data) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.voq_data is not None:
                                    return True

                                if self.connector_id is not None:
                                    return True

                                if self.ifhandle is not None:
                                    return True

                                if self.is_inuse is not None:
                                    return True

                                if self.is_local_port is not None:
                                    return True

                                if self.npu_core is not None:
                                    return True

                                if self.npu_num is not None:
                                    return True

                                if self.port_num is not None:
                                    return True

                                if self.port_speed is not None:
                                    return True

                                if self.pp_port is not None:
                                    return True

                                if self.rack_num is not None:
                                    return True

                                if self.slot_num is not None:
                                    return True

                                if self.sysport is not None:
                                    return True

                                if self.voq_base is not None:
                                    return True

                                if self.voq_stat is not None:
                                    for child_ref in self.voq_stat:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                                return meta._meta_table['Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData.VoqSpecificStatsData']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.npu_id is None:
                                raise YPYModelError('Key property npu_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:npu-number-for-voq-data[Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:npu-id = ' + str(self.npu_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.npu_id is not None:
                                return True

                            if self.voq_specific_stats_data is not None:
                                for child_ref in self.voq_specific_stats_data:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                            return meta._meta_table['Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:npu-number-for-voq-datas'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.npu_number_for_voq_data is not None:
                            for child_ref in self.npu_number_for_voq_data:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                        return meta._meta_table['Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas']['meta_info']


                class ClearVoqDataForNpuNumbers(object):
                    """
                    Clear voq ingress stats for all interfaces on
                    particular npu
                    
                    .. attribute:: clear_voq_data_for_npu_number
                    
                    	Npu id on which stats will be cleared
                    	**type**\: list of    :py:class:`ClearVoqDataForNpuNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers.ClearVoqDataForNpuNumber>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.clear_voq_data_for_npu_number = YList()
                        self.clear_voq_data_for_npu_number.parent = self
                        self.clear_voq_data_for_npu_number.name = 'clear_voq_data_for_npu_number'


                    class ClearVoqDataForNpuNumber(object):
                        """
                        Npu id on which stats will be cleared
                        
                        .. attribute:: npu_id  <key>
                        
                        	Npu number
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: voq_specific_stats_data_clear
                        
                        	Filter data by interface handle
                        	**type**\: list of    :py:class:`VoqSpecificStatsDataClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers.ClearVoqDataForNpuNumber.VoqSpecificStatsDataClear>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.npu_id = None
                            self.voq_specific_stats_data_clear = YList()
                            self.voq_specific_stats_data_clear.parent = self
                            self.voq_specific_stats_data_clear.name = 'voq_specific_stats_data_clear'


                        class VoqSpecificStatsDataClear(object):
                            """
                            Filter data by interface handle
                            
                            .. attribute:: voq_data  <key>
                            
                            	Interface Handle
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: clear_status
                            
                            	clear status
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.voq_data = None
                                self.clear_status = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.voq_data is None:
                                    raise YPYModelError('Key property voq_data is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:voq-specific-stats-data-clear[Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:voq-data = ' + str(self.voq_data) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.voq_data is not None:
                                    return True

                                if self.clear_status is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                                return meta._meta_table['Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers.ClearVoqDataForNpuNumber.VoqSpecificStatsDataClear']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.npu_id is None:
                                raise YPYModelError('Key property npu_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:clear-voq-data-for-npu-number[Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:npu-id = ' + str(self.npu_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.npu_id is not None:
                                return True

                            if self.voq_specific_stats_data_clear is not None:
                                for child_ref in self.voq_specific_stats_data_clear:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                            return meta._meta_table['Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers.ClearVoqDataForNpuNumber']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:clear-voq-data-for-npu-numbers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.clear_voq_data_for_npu_number is not None:
                            for child_ref in self.clear_voq_data_for_npu_number:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                        return meta._meta_table['Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers']['meta_info']


                class NpuNumberForTrapDataClears(object):
                    """
                    Trap stats for all traps
                    
                    .. attribute:: npu_number_for_trap_data_clear
                    
                    	All trap stats for a particular npu
                    	**type**\: list of    :py:class:`NpuNumberForTrapDataClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears.NpuNumberForTrapDataClear>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.npu_number_for_trap_data_clear = YList()
                        self.npu_number_for_trap_data_clear.parent = self
                        self.npu_number_for_trap_data_clear.name = 'npu_number_for_trap_data_clear'


                    class NpuNumberForTrapDataClear(object):
                        """
                        All trap stats for a particular npu
                        
                        .. attribute:: npu_id  <key>
                        
                        	NPU number
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: trap_specific_stats_data
                        
                        	Filter by specific trap id
                        	**type**\: list of    :py:class:`TrapSpecificStatsData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears.NpuNumberForTrapDataClear.TrapSpecificStatsData>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.npu_id = None
                            self.trap_specific_stats_data = YList()
                            self.trap_specific_stats_data.parent = self
                            self.trap_specific_stats_data.name = 'trap_specific_stats_data'


                        class TrapSpecificStatsData(object):
                            """
                            Filter by specific trap id
                            
                            .. attribute:: trap_data  <key>
                            
                            	Trap Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clear_status
                            
                            	clear status
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.trap_data = None
                                self.clear_status = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.trap_data is None:
                                    raise YPYModelError('Key property trap_data is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:trap-specific-stats-data[Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:trap-data = ' + str(self.trap_data) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.trap_data is not None:
                                    return True

                                if self.clear_status is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                                return meta._meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears.NpuNumberForTrapDataClear.TrapSpecificStatsData']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.npu_id is None:
                                raise YPYModelError('Key property npu_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:npu-number-for-trap-data-clear[Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:npu-id = ' + str(self.npu_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.npu_id is not None:
                                return True

                            if self.trap_specific_stats_data is not None:
                                for child_ref in self.trap_specific_stats_data:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                            return meta._meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears.NpuNumberForTrapDataClear']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:npu-number-for-trap-data-clears'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.npu_number_for_trap_data_clear is not None:
                            for child_ref in self.npu_number_for_trap_data_clear:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                        return meta._meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears']['meta_info']

                @property
                def _common_path(self):
                    if self.node_name is None:
                        raise YPYModelError('Key property node_name is None')

                    return '/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:stats/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:nodes/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:node[Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:node-name = ' + str(self.node_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.node_name is not None:
                        return True

                    if self.clear_voq_data_for_npu_numbers is not None and self.clear_voq_data_for_npu_numbers._has_data():
                        return True

                    if self.npu_number_for_trap_data_clears is not None and self.npu_number_for_trap_data_clears._has_data():
                        return True

                    if self.npu_number_for_trap_datas is not None and self.npu_number_for_trap_datas._has_data():
                        return True

                    if self.npu_number_for_voq_datas is not None and self.npu_number_for_voq_datas._has_data():
                        return True

                    if self.voq_base_number_stats_clears is not None and self.voq_base_number_stats_clears._has_data():
                        return True

                    if self.voq_base_numbers is not None and self.voq_base_numbers._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                    return meta._meta_table['Dpa.Stats.Nodes.Node']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:stats/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:nodes'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
                return meta._meta_table['Dpa.Stats.Nodes']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:stats'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.nodes is not None and self.nodes._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
            return meta._meta_table['Dpa.Stats']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.resources is not None and self.resources._has_data():
            return True

        if self.stats is not None and self.stats._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_bcm_dpa_resources_oper as meta
        return meta._meta_table['Dpa']['meta_info']



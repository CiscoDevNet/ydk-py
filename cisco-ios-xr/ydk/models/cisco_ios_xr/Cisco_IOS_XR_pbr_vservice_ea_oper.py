""" Cisco_IOS_XR_pbr_vservice_ea_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pbr\-vservice\-ea package operational data.

This module contains definitions
for the following management objects\:
  service\-function\-chaining\: NSH Service Function Chaining
    operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class VsNshStatsEnum(Enum):
    """
    VsNshStatsEnum

    Vs nsh stats

    .. data:: vs_nsh_stats_spi_si = 0

    	vs nsh stats spi si

    .. data:: vs_nsh_stats_ter_min_ate = 1

    	vs nsh stats ter min ate

    .. data:: vs_nsh_stats_sf = 2

    	vs nsh stats sf

    .. data:: vs_nsh_stats_sff = 3

    	vs nsh stats sff

    .. data:: vs_nsh_stats_sff_local = 4

    	vs nsh stats sff local

    .. data:: vs_nsh_stats_sfp = 5

    	vs nsh stats sfp

    .. data:: vs_nsh_stats_sfp_detail = 6

    	vs nsh stats sfp detail

    .. data:: vs_nsh_stats_max = 7

    	vs nsh stats max

    """

    vs_nsh_stats_spi_si = 0

    vs_nsh_stats_ter_min_ate = 1

    vs_nsh_stats_sf = 2

    vs_nsh_stats_sff = 3

    vs_nsh_stats_sff_local = 4

    vs_nsh_stats_sfp = 5

    vs_nsh_stats_sfp_detail = 6

    vs_nsh_stats_max = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
        return meta._meta_table['VsNshStatsEnum']



class ServiceFunctionChaining(object):
    """
    NSH Service Function Chaining operational data
    
    .. attribute:: nodes
    
    	Node\-specific NSH Service Function Chaining operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes>`
    
    

    """

    _prefix = 'pbr-vservice-ea-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = ServiceFunctionChaining.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Node\-specific NSH Service Function Chaining
        operational data
        
        .. attribute:: node
        
        	NSH operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node>`
        
        

        """

        _prefix = 'pbr-vservice-ea-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            NSH operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node to collect statistics from
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: process
            
            	Client Process
            	**type**\:   :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process>`
            
            

            """

            _prefix = 'pbr-vservice-ea-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.process = ServiceFunctionChaining.Nodes.Node.Process()
                self.process.parent = self


            class Process(object):
                """
                Client Process
                
                .. attribute:: service_function
                
                	Service Function operational data
                	**type**\:   :py:class:`ServiceFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction>`
                
                .. attribute:: service_function_forwarder
                
                	Service Function Forwarder operational data
                	**type**\:   :py:class:`ServiceFunctionForwarder <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder>`
                
                .. attribute:: service_function_path
                
                	Service Function Path operational data
                	**type**\:   :py:class:`ServiceFunctionPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath>`
                
                

                """

                _prefix = 'pbr-vservice-ea-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.service_function = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction()
                    self.service_function.parent = self
                    self.service_function_forwarder = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder()
                    self.service_function_forwarder.parent = self
                    self.service_function_path = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath()
                    self.service_function_path.parent = self


                class ServiceFunctionPath(object):
                    """
                    Service Function Path operational data
                    
                    .. attribute:: path_ids
                    
                    	Service Function Path Id 
                    	**type**\:   :py:class:`PathIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds>`
                    
                    

                    """

                    _prefix = 'pbr-vservice-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.path_ids = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds()
                        self.path_ids.parent = self


                    class PathIds(object):
                        """
                        Service Function Path Id 
                        
                        .. attribute:: path_id
                        
                        	Specific Service\-Function\-Path identifier 
                        	**type**\: list of    :py:class:`PathId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId>`
                        
                        

                        """

                        _prefix = 'pbr-vservice-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.path_id = YList()
                            self.path_id.parent = self
                            self.path_id.name = 'path_id'


                        class PathId(object):
                            """
                            Specific Service\-Function\-Path identifier 
                            
                            .. attribute:: id  <key>
                            
                            	Specific Service\-Function\-Path identifier
                            	**type**\:  int
                            
                            	**range:** 1..16777215
                            
                            .. attribute:: service_indexes
                            
                            	Service Index Belonging to Path
                            	**type**\:   :py:class:`ServiceIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes>`
                            
                            .. attribute:: stats
                            
                            	SFP Statistics
                            	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats>`
                            
                            

                            """

                            _prefix = 'pbr-vservice-ea-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.id = None
                                self.service_indexes = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes()
                                self.service_indexes.parent = self
                                self.stats = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats()
                                self.stats.parent = self


                            class ServiceIndexes(object):
                                """
                                Service Index Belonging to Path
                                
                                .. attribute:: service_index
                                
                                	Service index operational data belonging to this path
                                	**type**\: list of    :py:class:`ServiceIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex>`
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.service_index = YList()
                                    self.service_index.parent = self
                                    self.service_index.name = 'service_index'


                                class ServiceIndex(object):
                                    """
                                    Service index operational data belonging
                                    to this path
                                    
                                    .. attribute:: index  <key>
                                    
                                    	Service Index
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    .. attribute:: data
                                    
                                    	Statistics data
                                    	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data>`
                                    
                                    .. attribute:: si_arr
                                    
                                    	SI array in case of detail stats
                                    	**type**\: list of    :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.index = None
                                        self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data()
                                        self.data.parent = self
                                        self.si_arr = YList()
                                        self.si_arr.parent = self
                                        self.si_arr.name = 'si_arr'


                                    class Data(object):
                                        """
                                        Statistics data
                                        
                                        .. attribute:: sf
                                        
                                        	Service function stats
                                        	**type**\:   :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf>`
                                        
                                        .. attribute:: sff
                                        
                                        	Service function forwarder stats
                                        	**type**\:   :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff>`
                                        
                                        .. attribute:: sff_local
                                        
                                        	Local service function forwarder stats
                                        	**type**\:   :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal>`
                                        
                                        .. attribute:: sfp
                                        
                                        	SFP stats
                                        	**type**\:   :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp>`
                                        
                                        .. attribute:: spi_si
                                        
                                        	SPI SI stats
                                        	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi>`
                                        
                                        .. attribute:: term
                                        
                                        	Terminate stats
                                        	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term>`
                                        
                                        .. attribute:: type
                                        
                                        	type
                                        	**type**\:   :py:class:`VsNshStatsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStatsEnum>`
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf()
                                            self.sf.parent = self
                                            self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff()
                                            self.sff.parent = self
                                            self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal()
                                            self.sff_local.parent = self
                                            self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp()
                                            self.sfp.parent = self
                                            self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi()
                                            self.spi_si.parent = self
                                            self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term()
                                            self.term.parent = self
                                            self.type = None


                                        class Sfp(object):
                                            """
                                            SFP stats
                                            
                                            .. attribute:: spi_si
                                            
                                            	Service index counters
                                            	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate counters
                                            	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi()
                                                self.spi_si.parent = self
                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term()
                                                self.term.parent = self


                                            class SpiSi(object):
                                                """
                                                Service index counters
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.processed_bytes = None
                                                    self.processed_pkts = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.processed_bytes is not None:
                                                        return True

                                                    if self.processed_pkts is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi']['meta_info']


                                            class Term(object):
                                                """
                                                Terminate counters
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.terminated_bytes = None
                                                    self.terminated_pkts = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.terminated_bytes is not None:
                                                        return True

                                                    if self.terminated_pkts is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sfp'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.spi_si is not None and self.spi_si._has_data():
                                                    return True

                                                if self.term is not None and self.term._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp']['meta_info']


                                        class SpiSi(object):
                                            """
                                            SPI SI stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.processed_bytes = None
                                                self.processed_pkts = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.processed_bytes is not None:
                                                    return True

                                                if self.processed_pkts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi']['meta_info']


                                        class Term(object):
                                            """
                                            Terminate stats
                                            
                                            .. attribute:: terminated_bytes
                                            
                                            	Total bytes terminated
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: terminated_pkts
                                            
                                            	Number of terminated packets
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.terminated_bytes = None
                                                self.terminated_pkts = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.terminated_bytes is not None:
                                                    return True

                                                if self.terminated_pkts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term']['meta_info']


                                        class Sf(object):
                                            """
                                            Service function stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.processed_bytes = None
                                                self.processed_pkts = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sf'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.processed_bytes is not None:
                                                    return True

                                                if self.processed_pkts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf']['meta_info']


                                        class Sff(object):
                                            """
                                            Service function forwarder stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.processed_bytes = None
                                                self.processed_pkts = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sff'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.processed_bytes is not None:
                                                    return True

                                                if self.processed_pkts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff']['meta_info']


                                        class SffLocal(object):
                                            """
                                            Local service function forwarder stats
                                            
                                            .. attribute:: lookup_err_bytes
                                            
                                            	Total bytes with unknown spi\-si
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: lookup_err_pkts
                                            
                                            	Number of packets with unknown spi\-si
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: malformed_err_bytes
                                            
                                            	Total bytes with invalid NSH header
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: malformed_err_pkts
                                            
                                            	Number of packets with invalid NSH header
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.lookup_err_bytes = None
                                                self.lookup_err_pkts = None
                                                self.malformed_err_bytes = None
                                                self.malformed_err_pkts = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sff-local'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.lookup_err_bytes is not None:
                                                    return True

                                                if self.lookup_err_pkts is not None:
                                                    return True

                                                if self.malformed_err_bytes is not None:
                                                    return True

                                                if self.malformed_err_pkts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:data'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.sf is not None and self.sf._has_data():
                                                return True

                                            if self.sff is not None and self.sff._has_data():
                                                return True

                                            if self.sff_local is not None and self.sff_local._has_data():
                                                return True

                                            if self.sfp is not None and self.sfp._has_data():
                                                return True

                                            if self.spi_si is not None and self.spi_si._has_data():
                                                return True

                                            if self.term is not None and self.term._has_data():
                                                return True

                                            if self.type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data']['meta_info']


                                    class SiArr(object):
                                        """
                                        SI array in case of detail stats
                                        
                                        .. attribute:: data
                                        
                                        	Stats counter for this index
                                        	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data>`
                                        
                                        .. attribute:: si
                                        
                                        	Service index
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data()
                                            self.data.parent = self
                                            self.si = None


                                        class Data(object):
                                            """
                                            Stats counter for this index
                                            
                                            .. attribute:: spi_si
                                            
                                            	SF/SFF stats
                                            	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate stats
                                            	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term>`
                                            
                                            .. attribute:: type
                                            
                                            	type
                                            	**type**\:   :py:class:`VsNshStatsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStatsEnum>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi()
                                                self.spi_si.parent = self
                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term()
                                                self.term.parent = self
                                                self.type = None


                                            class SpiSi(object):
                                                """
                                                SF/SFF stats
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.processed_bytes = None
                                                    self.processed_pkts = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.processed_bytes is not None:
                                                        return True

                                                    if self.processed_pkts is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi']['meta_info']


                                            class Term(object):
                                                """
                                                Terminate stats
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.terminated_bytes = None
                                                    self.terminated_pkts = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.terminated_bytes is not None:
                                                        return True

                                                    if self.terminated_pkts is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:data'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.spi_si is not None and self.spi_si._has_data():
                                                    return True

                                                if self.term is not None and self.term._has_data():
                                                    return True

                                                if self.type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:si-arr'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.data is not None and self.data._has_data():
                                                return True

                                            if self.si is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.index is None:
                                            raise YPYModelError('Key property index is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:service-index[Cisco-IOS-XR-pbr-vservice-ea-oper:index = ' + str(self.index) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.index is not None:
                                            return True

                                        if self.data is not None and self.data._has_data():
                                            return True

                                        if self.si_arr is not None:
                                            for child_ref in self.si_arr:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:service-indexes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.service_index is not None:
                                        for child_ref in self.service_index:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes']['meta_info']


                            class Stats(object):
                                """
                                SFP Statistics
                                
                                .. attribute:: detail
                                
                                	Detail statistics per service index 
                                	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail>`
                                
                                .. attribute:: summarized
                                
                                	Combined statistics of all service index in service functionpath
                                	**type**\:   :py:class:`Summarized <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized>`
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.detail = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail()
                                    self.detail.parent = self
                                    self.summarized = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized()
                                    self.summarized.parent = self


                                class Detail(object):
                                    """
                                    Detail statistics per service index 
                                    
                                    .. attribute:: data
                                    
                                    	Statistics data
                                    	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data>`
                                    
                                    .. attribute:: si_arr
                                    
                                    	SI array in case of detail stats
                                    	**type**\: list of    :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data()
                                        self.data.parent = self
                                        self.si_arr = YList()
                                        self.si_arr.parent = self
                                        self.si_arr.name = 'si_arr'


                                    class Data(object):
                                        """
                                        Statistics data
                                        
                                        .. attribute:: sf
                                        
                                        	Service function stats
                                        	**type**\:   :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf>`
                                        
                                        .. attribute:: sff
                                        
                                        	Service function forwarder stats
                                        	**type**\:   :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff>`
                                        
                                        .. attribute:: sff_local
                                        
                                        	Local service function forwarder stats
                                        	**type**\:   :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal>`
                                        
                                        .. attribute:: sfp
                                        
                                        	SFP stats
                                        	**type**\:   :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp>`
                                        
                                        .. attribute:: spi_si
                                        
                                        	SPI SI stats
                                        	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi>`
                                        
                                        .. attribute:: term
                                        
                                        	Terminate stats
                                        	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term>`
                                        
                                        .. attribute:: type
                                        
                                        	type
                                        	**type**\:   :py:class:`VsNshStatsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStatsEnum>`
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf()
                                            self.sf.parent = self
                                            self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff()
                                            self.sff.parent = self
                                            self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal()
                                            self.sff_local.parent = self
                                            self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp()
                                            self.sfp.parent = self
                                            self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi()
                                            self.spi_si.parent = self
                                            self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term()
                                            self.term.parent = self
                                            self.type = None


                                        class Sfp(object):
                                            """
                                            SFP stats
                                            
                                            .. attribute:: spi_si
                                            
                                            	Service index counters
                                            	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate counters
                                            	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi()
                                                self.spi_si.parent = self
                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term()
                                                self.term.parent = self


                                            class SpiSi(object):
                                                """
                                                Service index counters
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.processed_bytes = None
                                                    self.processed_pkts = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.processed_bytes is not None:
                                                        return True

                                                    if self.processed_pkts is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi']['meta_info']


                                            class Term(object):
                                                """
                                                Terminate counters
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.terminated_bytes = None
                                                    self.terminated_pkts = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.terminated_bytes is not None:
                                                        return True

                                                    if self.terminated_pkts is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sfp'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.spi_si is not None and self.spi_si._has_data():
                                                    return True

                                                if self.term is not None and self.term._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp']['meta_info']


                                        class SpiSi(object):
                                            """
                                            SPI SI stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.processed_bytes = None
                                                self.processed_pkts = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.processed_bytes is not None:
                                                    return True

                                                if self.processed_pkts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi']['meta_info']


                                        class Term(object):
                                            """
                                            Terminate stats
                                            
                                            .. attribute:: terminated_bytes
                                            
                                            	Total bytes terminated
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: terminated_pkts
                                            
                                            	Number of terminated packets
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.terminated_bytes = None
                                                self.terminated_pkts = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.terminated_bytes is not None:
                                                    return True

                                                if self.terminated_pkts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term']['meta_info']


                                        class Sf(object):
                                            """
                                            Service function stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.processed_bytes = None
                                                self.processed_pkts = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sf'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.processed_bytes is not None:
                                                    return True

                                                if self.processed_pkts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf']['meta_info']


                                        class Sff(object):
                                            """
                                            Service function forwarder stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.processed_bytes = None
                                                self.processed_pkts = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sff'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.processed_bytes is not None:
                                                    return True

                                                if self.processed_pkts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff']['meta_info']


                                        class SffLocal(object):
                                            """
                                            Local service function forwarder stats
                                            
                                            .. attribute:: lookup_err_bytes
                                            
                                            	Total bytes with unknown spi\-si
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: lookup_err_pkts
                                            
                                            	Number of packets with unknown spi\-si
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: malformed_err_bytes
                                            
                                            	Total bytes with invalid NSH header
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: malformed_err_pkts
                                            
                                            	Number of packets with invalid NSH header
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.lookup_err_bytes = None
                                                self.lookup_err_pkts = None
                                                self.malformed_err_bytes = None
                                                self.malformed_err_pkts = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sff-local'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.lookup_err_bytes is not None:
                                                    return True

                                                if self.lookup_err_pkts is not None:
                                                    return True

                                                if self.malformed_err_bytes is not None:
                                                    return True

                                                if self.malformed_err_pkts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:data'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.sf is not None and self.sf._has_data():
                                                return True

                                            if self.sff is not None and self.sff._has_data():
                                                return True

                                            if self.sff_local is not None and self.sff_local._has_data():
                                                return True

                                            if self.sfp is not None and self.sfp._has_data():
                                                return True

                                            if self.spi_si is not None and self.spi_si._has_data():
                                                return True

                                            if self.term is not None and self.term._has_data():
                                                return True

                                            if self.type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data']['meta_info']


                                    class SiArr(object):
                                        """
                                        SI array in case of detail stats
                                        
                                        .. attribute:: data
                                        
                                        	Stats counter for this index
                                        	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data>`
                                        
                                        .. attribute:: si
                                        
                                        	Service index
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data()
                                            self.data.parent = self
                                            self.si = None


                                        class Data(object):
                                            """
                                            Stats counter for this index
                                            
                                            .. attribute:: spi_si
                                            
                                            	SF/SFF stats
                                            	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate stats
                                            	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term>`
                                            
                                            .. attribute:: type
                                            
                                            	type
                                            	**type**\:   :py:class:`VsNshStatsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStatsEnum>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi()
                                                self.spi_si.parent = self
                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term()
                                                self.term.parent = self
                                                self.type = None


                                            class SpiSi(object):
                                                """
                                                SF/SFF stats
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.processed_bytes = None
                                                    self.processed_pkts = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.processed_bytes is not None:
                                                        return True

                                                    if self.processed_pkts is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi']['meta_info']


                                            class Term(object):
                                                """
                                                Terminate stats
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.terminated_bytes = None
                                                    self.terminated_pkts = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.terminated_bytes is not None:
                                                        return True

                                                    if self.terminated_pkts is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:data'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.spi_si is not None and self.spi_si._has_data():
                                                    return True

                                                if self.term is not None and self.term._has_data():
                                                    return True

                                                if self.type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:si-arr'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.data is not None and self.data._has_data():
                                                return True

                                            if self.si is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:detail'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.data is not None and self.data._has_data():
                                            return True

                                        if self.si_arr is not None:
                                            for child_ref in self.si_arr:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail']['meta_info']


                                class Summarized(object):
                                    """
                                    Combined statistics of all service index
                                    in service functionpath
                                    
                                    .. attribute:: data
                                    
                                    	Statistics data
                                    	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data>`
                                    
                                    .. attribute:: si_arr
                                    
                                    	SI array in case of detail stats
                                    	**type**\: list of    :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data()
                                        self.data.parent = self
                                        self.si_arr = YList()
                                        self.si_arr.parent = self
                                        self.si_arr.name = 'si_arr'


                                    class Data(object):
                                        """
                                        Statistics data
                                        
                                        .. attribute:: sf
                                        
                                        	Service function stats
                                        	**type**\:   :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf>`
                                        
                                        .. attribute:: sff
                                        
                                        	Service function forwarder stats
                                        	**type**\:   :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff>`
                                        
                                        .. attribute:: sff_local
                                        
                                        	Local service function forwarder stats
                                        	**type**\:   :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal>`
                                        
                                        .. attribute:: sfp
                                        
                                        	SFP stats
                                        	**type**\:   :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp>`
                                        
                                        .. attribute:: spi_si
                                        
                                        	SPI SI stats
                                        	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi>`
                                        
                                        .. attribute:: term
                                        
                                        	Terminate stats
                                        	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term>`
                                        
                                        .. attribute:: type
                                        
                                        	type
                                        	**type**\:   :py:class:`VsNshStatsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStatsEnum>`
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf()
                                            self.sf.parent = self
                                            self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff()
                                            self.sff.parent = self
                                            self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal()
                                            self.sff_local.parent = self
                                            self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp()
                                            self.sfp.parent = self
                                            self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi()
                                            self.spi_si.parent = self
                                            self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term()
                                            self.term.parent = self
                                            self.type = None


                                        class Sfp(object):
                                            """
                                            SFP stats
                                            
                                            .. attribute:: spi_si
                                            
                                            	Service index counters
                                            	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate counters
                                            	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi()
                                                self.spi_si.parent = self
                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term()
                                                self.term.parent = self


                                            class SpiSi(object):
                                                """
                                                Service index counters
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.processed_bytes = None
                                                    self.processed_pkts = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.processed_bytes is not None:
                                                        return True

                                                    if self.processed_pkts is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi']['meta_info']


                                            class Term(object):
                                                """
                                                Terminate counters
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.terminated_bytes = None
                                                    self.terminated_pkts = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.terminated_bytes is not None:
                                                        return True

                                                    if self.terminated_pkts is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sfp'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.spi_si is not None and self.spi_si._has_data():
                                                    return True

                                                if self.term is not None and self.term._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp']['meta_info']


                                        class SpiSi(object):
                                            """
                                            SPI SI stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.processed_bytes = None
                                                self.processed_pkts = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.processed_bytes is not None:
                                                    return True

                                                if self.processed_pkts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi']['meta_info']


                                        class Term(object):
                                            """
                                            Terminate stats
                                            
                                            .. attribute:: terminated_bytes
                                            
                                            	Total bytes terminated
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: terminated_pkts
                                            
                                            	Number of terminated packets
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.terminated_bytes = None
                                                self.terminated_pkts = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.terminated_bytes is not None:
                                                    return True

                                                if self.terminated_pkts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term']['meta_info']


                                        class Sf(object):
                                            """
                                            Service function stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.processed_bytes = None
                                                self.processed_pkts = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sf'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.processed_bytes is not None:
                                                    return True

                                                if self.processed_pkts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf']['meta_info']


                                        class Sff(object):
                                            """
                                            Service function forwarder stats
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.processed_bytes = None
                                                self.processed_pkts = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sff'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.processed_bytes is not None:
                                                    return True

                                                if self.processed_pkts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff']['meta_info']


                                        class SffLocal(object):
                                            """
                                            Local service function forwarder stats
                                            
                                            .. attribute:: lookup_err_bytes
                                            
                                            	Total bytes with unknown spi\-si
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: lookup_err_pkts
                                            
                                            	Number of packets with unknown spi\-si
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: malformed_err_bytes
                                            
                                            	Total bytes with invalid NSH header
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: malformed_err_pkts
                                            
                                            	Number of packets with invalid NSH header
                                            	**type**\:  int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.lookup_err_bytes = None
                                                self.lookup_err_pkts = None
                                                self.malformed_err_bytes = None
                                                self.malformed_err_pkts = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sff-local'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.lookup_err_bytes is not None:
                                                    return True

                                                if self.lookup_err_pkts is not None:
                                                    return True

                                                if self.malformed_err_bytes is not None:
                                                    return True

                                                if self.malformed_err_pkts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:data'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.sf is not None and self.sf._has_data():
                                                return True

                                            if self.sff is not None and self.sff._has_data():
                                                return True

                                            if self.sff_local is not None and self.sff_local._has_data():
                                                return True

                                            if self.sfp is not None and self.sfp._has_data():
                                                return True

                                            if self.spi_si is not None and self.spi_si._has_data():
                                                return True

                                            if self.term is not None and self.term._has_data():
                                                return True

                                            if self.type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data']['meta_info']


                                    class SiArr(object):
                                        """
                                        SI array in case of detail stats
                                        
                                        .. attribute:: data
                                        
                                        	Stats counter for this index
                                        	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data>`
                                        
                                        .. attribute:: si
                                        
                                        	Service index
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data()
                                            self.data.parent = self
                                            self.si = None


                                        class Data(object):
                                            """
                                            Stats counter for this index
                                            
                                            .. attribute:: spi_si
                                            
                                            	SF/SFF stats
                                            	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate stats
                                            	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term>`
                                            
                                            .. attribute:: type
                                            
                                            	type
                                            	**type**\:   :py:class:`VsNshStatsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStatsEnum>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi()
                                                self.spi_si.parent = self
                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term()
                                                self.term.parent = self
                                                self.type = None


                                            class SpiSi(object):
                                                """
                                                SF/SFF stats
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.processed_bytes = None
                                                    self.processed_pkts = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.processed_bytes is not None:
                                                        return True

                                                    if self.processed_pkts is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi']['meta_info']


                                            class Term(object):
                                                """
                                                Terminate stats
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\:  int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.terminated_bytes = None
                                                    self.terminated_pkts = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.terminated_bytes is not None:
                                                        return True

                                                    if self.terminated_pkts is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:data'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.spi_si is not None and self.spi_si._has_data():
                                                    return True

                                                if self.term is not None and self.term._has_data():
                                                    return True

                                                if self.type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:si-arr'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.data is not None and self.data._has_data():
                                                return True

                                            if self.si is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:summarized'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.data is not None and self.data._has_data():
                                            return True

                                        if self.si_arr is not None:
                                            for child_ref in self.si_arr:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.detail is not None and self.detail._has_data():
                                        return True

                                    if self.summarized is not None and self.summarized._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.id is None:
                                    raise YPYModelError('Key property id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:path-id[Cisco-IOS-XR-pbr-vservice-ea-oper:id = ' + str(self.id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.id is not None:
                                    return True

                                if self.service_indexes is not None and self.service_indexes._has_data():
                                    return True

                                if self.stats is not None and self.stats._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:path-ids'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.path_id is not None:
                                for child_ref in self.path_id:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:service-function-path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.path_ids is not None and self.path_ids._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath']['meta_info']


                class ServiceFunction(object):
                    """
                    Service Function operational data
                    
                    .. attribute:: sf_names
                    
                    	List of Service Function Names
                    	**type**\:   :py:class:`SfNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames>`
                    
                    

                    """

                    _prefix = 'pbr-vservice-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.sf_names = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames()
                        self.sf_names.parent = self


                    class SfNames(object):
                        """
                        List of Service Function Names
                        
                        .. attribute:: sf_name
                        
                        	Name of Service Function
                        	**type**\: list of    :py:class:`SfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName>`
                        
                        

                        """

                        _prefix = 'pbr-vservice-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sf_name = YList()
                            self.sf_name.parent = self
                            self.sf_name.name = 'sf_name'


                        class SfName(object):
                            """
                            Name of Service Function
                            
                            .. attribute:: name  <key>
                            
                            	Name
                            	**type**\:  str
                            
                            	**length:** 1..32
                            
                            .. attribute:: data
                            
                            	Statistics data
                            	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data>`
                            
                            .. attribute:: si_arr
                            
                            	SI array in case of detail stats
                            	**type**\: list of    :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr>`
                            
                            

                            """

                            _prefix = 'pbr-vservice-ea-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.name = None
                                self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data()
                                self.data.parent = self
                                self.si_arr = YList()
                                self.si_arr.parent = self
                                self.si_arr.name = 'si_arr'


                            class Data(object):
                                """
                                Statistics data
                                
                                .. attribute:: sf
                                
                                	Service function stats
                                	**type**\:   :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sf>`
                                
                                .. attribute:: sff
                                
                                	Service function forwarder stats
                                	**type**\:   :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sff>`
                                
                                .. attribute:: sff_local
                                
                                	Local service function forwarder stats
                                	**type**\:   :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SffLocal>`
                                
                                .. attribute:: sfp
                                
                                	SFP stats
                                	**type**\:   :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp>`
                                
                                .. attribute:: spi_si
                                
                                	SPI SI stats
                                	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SpiSi>`
                                
                                .. attribute:: term
                                
                                	Terminate stats
                                	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Term>`
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:   :py:class:`VsNshStatsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStatsEnum>`
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sf()
                                    self.sf.parent = self
                                    self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sff()
                                    self.sff.parent = self
                                    self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SffLocal()
                                    self.sff_local.parent = self
                                    self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp()
                                    self.sfp.parent = self
                                    self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SpiSi()
                                    self.spi_si.parent = self
                                    self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Term()
                                    self.term.parent = self
                                    self.type = None


                                class Sfp(object):
                                    """
                                    SFP stats
                                    
                                    .. attribute:: spi_si
                                    
                                    	Service index counters
                                    	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate counters
                                    	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.Term>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi()
                                        self.spi_si.parent = self
                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.Term()
                                        self.term.parent = self


                                    class SpiSi(object):
                                        """
                                        Service index counters
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.processed_bytes = None
                                            self.processed_pkts = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.processed_bytes is not None:
                                                return True

                                            if self.processed_pkts is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi']['meta_info']


                                    class Term(object):
                                        """
                                        Terminate counters
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.terminated_bytes = None
                                            self.terminated_pkts = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.terminated_bytes is not None:
                                                return True

                                            if self.terminated_pkts is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.Term']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sfp'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.spi_si is not None and self.spi_si._has_data():
                                            return True

                                        if self.term is not None and self.term._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp']['meta_info']


                                class SpiSi(object):
                                    """
                                    SPI SI stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.processed_bytes = None
                                        self.processed_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.processed_bytes is not None:
                                            return True

                                        if self.processed_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SpiSi']['meta_info']


                                class Term(object):
                                    """
                                    Terminate stats
                                    
                                    .. attribute:: terminated_bytes
                                    
                                    	Total bytes terminated
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: terminated_pkts
                                    
                                    	Number of terminated packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.terminated_bytes = None
                                        self.terminated_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.terminated_bytes is not None:
                                            return True

                                        if self.terminated_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Term']['meta_info']


                                class Sf(object):
                                    """
                                    Service function stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.processed_bytes = None
                                        self.processed_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sf'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.processed_bytes is not None:
                                            return True

                                        if self.processed_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sf']['meta_info']


                                class Sff(object):
                                    """
                                    Service function forwarder stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.processed_bytes = None
                                        self.processed_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sff'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.processed_bytes is not None:
                                            return True

                                        if self.processed_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sff']['meta_info']


                                class SffLocal(object):
                                    """
                                    Local service function forwarder stats
                                    
                                    .. attribute:: lookup_err_bytes
                                    
                                    	Total bytes with unknown spi\-si
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: lookup_err_pkts
                                    
                                    	Number of packets with unknown spi\-si
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: malformed_err_bytes
                                    
                                    	Total bytes with invalid NSH header
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: malformed_err_pkts
                                    
                                    	Number of packets with invalid NSH header
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.lookup_err_bytes = None
                                        self.lookup_err_pkts = None
                                        self.malformed_err_bytes = None
                                        self.malformed_err_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sff-local'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.lookup_err_bytes is not None:
                                            return True

                                        if self.lookup_err_pkts is not None:
                                            return True

                                        if self.malformed_err_bytes is not None:
                                            return True

                                        if self.malformed_err_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SffLocal']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:data'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.sf is not None and self.sf._has_data():
                                        return True

                                    if self.sff is not None and self.sff._has_data():
                                        return True

                                    if self.sff_local is not None and self.sff_local._has_data():
                                        return True

                                    if self.sfp is not None and self.sfp._has_data():
                                        return True

                                    if self.spi_si is not None and self.spi_si._has_data():
                                        return True

                                    if self.term is not None and self.term._has_data():
                                        return True

                                    if self.type is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data']['meta_info']


                            class SiArr(object):
                                """
                                SI array in case of detail stats
                                
                                .. attribute:: data
                                
                                	Stats counter for this index
                                	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data>`
                                
                                .. attribute:: si
                                
                                	Service index
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data()
                                    self.data.parent = self
                                    self.si = None


                                class Data(object):
                                    """
                                    Stats counter for this index
                                    
                                    .. attribute:: spi_si
                                    
                                    	SF/SFF stats
                                    	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate stats
                                    	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.Term>`
                                    
                                    .. attribute:: type
                                    
                                    	type
                                    	**type**\:   :py:class:`VsNshStatsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStatsEnum>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi()
                                        self.spi_si.parent = self
                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.Term()
                                        self.term.parent = self
                                        self.type = None


                                    class SpiSi(object):
                                        """
                                        SF/SFF stats
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.processed_bytes = None
                                            self.processed_pkts = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.processed_bytes is not None:
                                                return True

                                            if self.processed_pkts is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi']['meta_info']


                                    class Term(object):
                                        """
                                        Terminate stats
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.terminated_bytes = None
                                            self.terminated_pkts = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.terminated_bytes is not None:
                                                return True

                                            if self.terminated_pkts is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.Term']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:data'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.spi_si is not None and self.spi_si._has_data():
                                            return True

                                        if self.term is not None and self.term._has_data():
                                            return True

                                        if self.type is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:si-arr'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.data is not None and self.data._has_data():
                                        return True

                                    if self.si is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.name is None:
                                    raise YPYModelError('Key property name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sf-name[Cisco-IOS-XR-pbr-vservice-ea-oper:name = ' + str(self.name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.name is not None:
                                    return True

                                if self.data is not None and self.data._has_data():
                                    return True

                                if self.si_arr is not None:
                                    for child_ref in self.si_arr:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sf-names'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sf_name is not None:
                                for child_ref in self.sf_name:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:service-function'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.sf_names is not None and self.sf_names._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction']['meta_info']


                class ServiceFunctionForwarder(object):
                    """
                    Service Function Forwarder operational data
                    
                    .. attribute:: local
                    
                    	Local Service Function Forwarder operational data
                    	**type**\:   :py:class:`Local <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local>`
                    
                    .. attribute:: sff_names
                    
                    	List of Service Function Forwarder Names
                    	**type**\:   :py:class:`SffNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames>`
                    
                    

                    """

                    _prefix = 'pbr-vservice-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local()
                        self.local.parent = self
                        self.sff_names = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames()
                        self.sff_names.parent = self


                    class Local(object):
                        """
                        Local Service Function Forwarder operational
                        data
                        
                        .. attribute:: error
                        
                        	Error Statistics for local service function forwarder
                        	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error>`
                        
                        

                        """

                        _prefix = 'pbr-vservice-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.error = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error()
                            self.error.parent = self


                        class Error(object):
                            """
                            Error Statistics for local service function
                            forwarder
                            
                            .. attribute:: data
                            
                            	Statistics data
                            	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data>`
                            
                            .. attribute:: si_arr
                            
                            	SI array in case of detail stats
                            	**type**\: list of    :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr>`
                            
                            

                            """

                            _prefix = 'pbr-vservice-ea-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data()
                                self.data.parent = self
                                self.si_arr = YList()
                                self.si_arr.parent = self
                                self.si_arr.name = 'si_arr'


                            class Data(object):
                                """
                                Statistics data
                                
                                .. attribute:: sf
                                
                                	Service function stats
                                	**type**\:   :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sf>`
                                
                                .. attribute:: sff
                                
                                	Service function forwarder stats
                                	**type**\:   :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sff>`
                                
                                .. attribute:: sff_local
                                
                                	Local service function forwarder stats
                                	**type**\:   :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SffLocal>`
                                
                                .. attribute:: sfp
                                
                                	SFP stats
                                	**type**\:   :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp>`
                                
                                .. attribute:: spi_si
                                
                                	SPI SI stats
                                	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SpiSi>`
                                
                                .. attribute:: term
                                
                                	Terminate stats
                                	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Term>`
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:   :py:class:`VsNshStatsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStatsEnum>`
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sf()
                                    self.sf.parent = self
                                    self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sff()
                                    self.sff.parent = self
                                    self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SffLocal()
                                    self.sff_local.parent = self
                                    self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp()
                                    self.sfp.parent = self
                                    self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SpiSi()
                                    self.spi_si.parent = self
                                    self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Term()
                                    self.term.parent = self
                                    self.type = None


                                class Sfp(object):
                                    """
                                    SFP stats
                                    
                                    .. attribute:: spi_si
                                    
                                    	Service index counters
                                    	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate counters
                                    	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi()
                                        self.spi_si.parent = self
                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term()
                                        self.term.parent = self


                                    class SpiSi(object):
                                        """
                                        Service index counters
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.processed_bytes = None
                                            self.processed_pkts = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.processed_bytes is not None:
                                                return True

                                            if self.processed_pkts is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi']['meta_info']


                                    class Term(object):
                                        """
                                        Terminate counters
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.terminated_bytes = None
                                            self.terminated_pkts = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.terminated_bytes is not None:
                                                return True

                                            if self.terminated_pkts is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sfp'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.spi_si is not None and self.spi_si._has_data():
                                            return True

                                        if self.term is not None and self.term._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp']['meta_info']


                                class SpiSi(object):
                                    """
                                    SPI SI stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.processed_bytes = None
                                        self.processed_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.processed_bytes is not None:
                                            return True

                                        if self.processed_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SpiSi']['meta_info']


                                class Term(object):
                                    """
                                    Terminate stats
                                    
                                    .. attribute:: terminated_bytes
                                    
                                    	Total bytes terminated
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: terminated_pkts
                                    
                                    	Number of terminated packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.terminated_bytes = None
                                        self.terminated_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.terminated_bytes is not None:
                                            return True

                                        if self.terminated_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Term']['meta_info']


                                class Sf(object):
                                    """
                                    Service function stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.processed_bytes = None
                                        self.processed_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sf'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.processed_bytes is not None:
                                            return True

                                        if self.processed_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sf']['meta_info']


                                class Sff(object):
                                    """
                                    Service function forwarder stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.processed_bytes = None
                                        self.processed_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sff'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.processed_bytes is not None:
                                            return True

                                        if self.processed_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sff']['meta_info']


                                class SffLocal(object):
                                    """
                                    Local service function forwarder stats
                                    
                                    .. attribute:: lookup_err_bytes
                                    
                                    	Total bytes with unknown spi\-si
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: lookup_err_pkts
                                    
                                    	Number of packets with unknown spi\-si
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: malformed_err_bytes
                                    
                                    	Total bytes with invalid NSH header
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: malformed_err_pkts
                                    
                                    	Number of packets with invalid NSH header
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.lookup_err_bytes = None
                                        self.lookup_err_pkts = None
                                        self.malformed_err_bytes = None
                                        self.malformed_err_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sff-local'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.lookup_err_bytes is not None:
                                            return True

                                        if self.lookup_err_pkts is not None:
                                            return True

                                        if self.malformed_err_bytes is not None:
                                            return True

                                        if self.malformed_err_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SffLocal']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:data'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.sf is not None and self.sf._has_data():
                                        return True

                                    if self.sff is not None and self.sff._has_data():
                                        return True

                                    if self.sff_local is not None and self.sff_local._has_data():
                                        return True

                                    if self.sfp is not None and self.sfp._has_data():
                                        return True

                                    if self.spi_si is not None and self.spi_si._has_data():
                                        return True

                                    if self.term is not None and self.term._has_data():
                                        return True

                                    if self.type is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data']['meta_info']


                            class SiArr(object):
                                """
                                SI array in case of detail stats
                                
                                .. attribute:: data
                                
                                	Stats counter for this index
                                	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data>`
                                
                                .. attribute:: si
                                
                                	Service index
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data()
                                    self.data.parent = self
                                    self.si = None


                                class Data(object):
                                    """
                                    Stats counter for this index
                                    
                                    .. attribute:: spi_si
                                    
                                    	SF/SFF stats
                                    	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate stats
                                    	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term>`
                                    
                                    .. attribute:: type
                                    
                                    	type
                                    	**type**\:   :py:class:`VsNshStatsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStatsEnum>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi()
                                        self.spi_si.parent = self
                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term()
                                        self.term.parent = self
                                        self.type = None


                                    class SpiSi(object):
                                        """
                                        SF/SFF stats
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.processed_bytes = None
                                            self.processed_pkts = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.processed_bytes is not None:
                                                return True

                                            if self.processed_pkts is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi']['meta_info']


                                    class Term(object):
                                        """
                                        Terminate stats
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.terminated_bytes = None
                                            self.terminated_pkts = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.terminated_bytes is not None:
                                                return True

                                            if self.terminated_pkts is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:data'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.spi_si is not None and self.spi_si._has_data():
                                            return True

                                        if self.term is not None and self.term._has_data():
                                            return True

                                        if self.type is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:si-arr'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.data is not None and self.data._has_data():
                                        return True

                                    if self.si is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:error'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.data is not None and self.data._has_data():
                                    return True

                                if self.si_arr is not None:
                                    for child_ref in self.si_arr:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:local'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.error is not None and self.error._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local']['meta_info']


                    class SffNames(object):
                        """
                        List of Service Function Forwarder Names
                        
                        .. attribute:: sff_name
                        
                        	Name of Service Function Forwarder
                        	**type**\: list of    :py:class:`SffName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName>`
                        
                        

                        """

                        _prefix = 'pbr-vservice-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sff_name = YList()
                            self.sff_name.parent = self
                            self.sff_name.name = 'sff_name'


                        class SffName(object):
                            """
                            Name of Service Function Forwarder
                            
                            .. attribute:: name  <key>
                            
                            	Name
                            	**type**\:  str
                            
                            	**length:** 1..32
                            
                            .. attribute:: data
                            
                            	Statistics data
                            	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data>`
                            
                            .. attribute:: si_arr
                            
                            	SI array in case of detail stats
                            	**type**\: list of    :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr>`
                            
                            

                            """

                            _prefix = 'pbr-vservice-ea-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.name = None
                                self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data()
                                self.data.parent = self
                                self.si_arr = YList()
                                self.si_arr.parent = self
                                self.si_arr.name = 'si_arr'


                            class Data(object):
                                """
                                Statistics data
                                
                                .. attribute:: sf
                                
                                	Service function stats
                                	**type**\:   :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sf>`
                                
                                .. attribute:: sff
                                
                                	Service function forwarder stats
                                	**type**\:   :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sff>`
                                
                                .. attribute:: sff_local
                                
                                	Local service function forwarder stats
                                	**type**\:   :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal>`
                                
                                .. attribute:: sfp
                                
                                	SFP stats
                                	**type**\:   :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp>`
                                
                                .. attribute:: spi_si
                                
                                	SPI SI stats
                                	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi>`
                                
                                .. attribute:: term
                                
                                	Terminate stats
                                	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Term>`
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:   :py:class:`VsNshStatsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStatsEnum>`
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sf()
                                    self.sf.parent = self
                                    self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sff()
                                    self.sff.parent = self
                                    self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal()
                                    self.sff_local.parent = self
                                    self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp()
                                    self.sfp.parent = self
                                    self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi()
                                    self.spi_si.parent = self
                                    self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Term()
                                    self.term.parent = self
                                    self.type = None


                                class Sfp(object):
                                    """
                                    SFP stats
                                    
                                    .. attribute:: spi_si
                                    
                                    	Service index counters
                                    	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate counters
                                    	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi()
                                        self.spi_si.parent = self
                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term()
                                        self.term.parent = self


                                    class SpiSi(object):
                                        """
                                        Service index counters
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.processed_bytes = None
                                            self.processed_pkts = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.processed_bytes is not None:
                                                return True

                                            if self.processed_pkts is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi']['meta_info']


                                    class Term(object):
                                        """
                                        Terminate counters
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.terminated_bytes = None
                                            self.terminated_pkts = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.terminated_bytes is not None:
                                                return True

                                            if self.terminated_pkts is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sfp'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.spi_si is not None and self.spi_si._has_data():
                                            return True

                                        if self.term is not None and self.term._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp']['meta_info']


                                class SpiSi(object):
                                    """
                                    SPI SI stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.processed_bytes = None
                                        self.processed_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.processed_bytes is not None:
                                            return True

                                        if self.processed_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi']['meta_info']


                                class Term(object):
                                    """
                                    Terminate stats
                                    
                                    .. attribute:: terminated_bytes
                                    
                                    	Total bytes terminated
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: terminated_pkts
                                    
                                    	Number of terminated packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.terminated_bytes = None
                                        self.terminated_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.terminated_bytes is not None:
                                            return True

                                        if self.terminated_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Term']['meta_info']


                                class Sf(object):
                                    """
                                    Service function stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.processed_bytes = None
                                        self.processed_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sf'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.processed_bytes is not None:
                                            return True

                                        if self.processed_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sf']['meta_info']


                                class Sff(object):
                                    """
                                    Service function forwarder stats
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.processed_bytes = None
                                        self.processed_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sff'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.processed_bytes is not None:
                                            return True

                                        if self.processed_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sff']['meta_info']


                                class SffLocal(object):
                                    """
                                    Local service function forwarder stats
                                    
                                    .. attribute:: lookup_err_bytes
                                    
                                    	Total bytes with unknown spi\-si
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: lookup_err_pkts
                                    
                                    	Number of packets with unknown spi\-si
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: malformed_err_bytes
                                    
                                    	Total bytes with invalid NSH header
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: malformed_err_pkts
                                    
                                    	Number of packets with invalid NSH header
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.lookup_err_bytes = None
                                        self.lookup_err_pkts = None
                                        self.malformed_err_bytes = None
                                        self.malformed_err_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sff-local'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.lookup_err_bytes is not None:
                                            return True

                                        if self.lookup_err_pkts is not None:
                                            return True

                                        if self.malformed_err_bytes is not None:
                                            return True

                                        if self.malformed_err_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:data'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.sf is not None and self.sf._has_data():
                                        return True

                                    if self.sff is not None and self.sff._has_data():
                                        return True

                                    if self.sff_local is not None and self.sff_local._has_data():
                                        return True

                                    if self.sfp is not None and self.sfp._has_data():
                                        return True

                                    if self.spi_si is not None and self.spi_si._has_data():
                                        return True

                                    if self.term is not None and self.term._has_data():
                                        return True

                                    if self.type is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data']['meta_info']


                            class SiArr(object):
                                """
                                SI array in case of detail stats
                                
                                .. attribute:: data
                                
                                	Stats counter for this index
                                	**type**\:   :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data>`
                                
                                .. attribute:: si
                                
                                	Service index
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data()
                                    self.data.parent = self
                                    self.si = None


                                class Data(object):
                                    """
                                    Stats counter for this index
                                    
                                    .. attribute:: spi_si
                                    
                                    	SF/SFF stats
                                    	**type**\:   :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate stats
                                    	**type**\:   :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term>`
                                    
                                    .. attribute:: type
                                    
                                    	type
                                    	**type**\:   :py:class:`VsNshStatsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStatsEnum>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi()
                                        self.spi_si.parent = self
                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term()
                                        self.term.parent = self
                                        self.type = None


                                    class SpiSi(object):
                                        """
                                        SF/SFF stats
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.processed_bytes = None
                                            self.processed_pkts = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:spi-si'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.processed_bytes is not None:
                                                return True

                                            if self.processed_pkts is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi']['meta_info']


                                    class Term(object):
                                        """
                                        Terminate stats
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.terminated_bytes = None
                                            self.terminated_pkts = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:term'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.terminated_bytes is not None:
                                                return True

                                            if self.terminated_pkts is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:data'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.spi_si is not None and self.spi_si._has_data():
                                            return True

                                        if self.term is not None and self.term._has_data():
                                            return True

                                        if self.type is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:si-arr'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.data is not None and self.data._has_data():
                                        return True

                                    if self.si is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.name is None:
                                    raise YPYModelError('Key property name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sff-name[Cisco-IOS-XR-pbr-vservice-ea-oper:name = ' + str(self.name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.name is not None:
                                    return True

                                if self.data is not None and self.data._has_data():
                                    return True

                                if self.si_arr is not None:
                                    for child_ref in self.si_arr:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                                return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:sff-names'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sff_name is not None:
                                for child_ref in self.sff_name:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                            return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:service-function-forwarder'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.local is not None and self.local._has_data():
                            return True

                        if self.sff_names is not None and self.sff_names._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                        return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-vservice-ea-oper:process'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.service_function is not None and self.service_function._has_data():
                        return True

                    if self.service_function_forwarder is not None and self.service_function_forwarder._has_data():
                        return True

                    if self.service_function_path is not None and self.service_function_path._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                    return meta._meta_table['ServiceFunctionChaining.Nodes.Node.Process']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-pbr-vservice-ea-oper:service-function-chaining/Cisco-IOS-XR-pbr-vservice-ea-oper:nodes/Cisco-IOS-XR-pbr-vservice-ea-oper:node[Cisco-IOS-XR-pbr-vservice-ea-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.process is not None and self.process._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
                return meta._meta_table['ServiceFunctionChaining.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-pbr-vservice-ea-oper:service-function-chaining/Cisco-IOS-XR-pbr-vservice-ea-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
            return meta._meta_table['ServiceFunctionChaining.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-pbr-vservice-ea-oper:service-function-chaining'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_ea_oper as meta
        return meta._meta_table['ServiceFunctionChaining']['meta_info']



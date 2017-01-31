""" Cisco_IOS_XR_ncs5500_coherent_node_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5500\-coherent\-node package operational data.

This module contains definitions
for the following management objects\:
  coherent\: Coherent node  operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Coherent(object):
    """
    Coherent node  operational data
    
    .. attribute:: nodes
    
    	Coherent list of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes>`
    
    

    """

    _prefix = 'ncs5500-coherent-node-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Coherent.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Coherent list of nodes
        
        .. attribute:: node
        
        	Coherent discovery operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node>`
        
        

        """

        _prefix = 'ncs5500-coherent-node-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Coherent discovery operational data for a
            particular node
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: coherent_time_stats
            
            	Coherent driver performace information
            	**type**\:   :py:class:`CoherentTimeStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats>`
            
            .. attribute:: coherenthealth
            
            	Coherent node data for driver health
            	**type**\:   :py:class:`Coherenthealth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth>`
            
            .. attribute:: devicemapping
            
            	Coherent node data for device \_mapping
            	**type**\:   :py:class:`Devicemapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Devicemapping>`
            
            .. attribute:: port_mode_all_info
            
            	PortMode all operational data
            	**type**\:   :py:class:`PortModeAllInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.PortModeAllInfo>`
            
            

            """

            _prefix = 'ncs5500-coherent-node-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.coherent_time_stats = Coherent.Nodes.Node.CoherentTimeStats()
                self.coherent_time_stats.parent = self
                self.coherenthealth = Coherent.Nodes.Node.Coherenthealth()
                self.coherenthealth.parent = self
                self.devicemapping = Coherent.Nodes.Node.Devicemapping()
                self.devicemapping.parent = self
                self.port_mode_all_info = Coherent.Nodes.Node.PortModeAllInfo()
                self.port_mode_all_info.parent = self


            class CoherentTimeStats(object):
                """
                Coherent driver performace information
                
                .. attribute:: device_created
                
                	device created
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: driver_init
                
                	driver init
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: driver_operational
                
                	driver operational
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dsp_controllers_created
                
                	dsp controllers created
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dsp_ea_bulk_create
                
                	dsp ea bulk create
                	**type**\:   :py:class:`DspEaBulkCreate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate>`
                
                .. attribute:: dsp_ea_bulk_update
                
                	dsp ea bulk update
                	**type**\:   :py:class:`DspEaBulkUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate>`
                
                .. attribute:: eth_intf_created
                
                	eth intf created
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: optics_controllers_created
                
                	optics controllers created
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: opts_ea_bulk_create
                
                	opts ea bulk create
                	**type**\:   :py:class:`OptsEaBulkCreate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate>`
                
                .. attribute:: opts_ea_bulk_update
                
                	opts ea bulk update
                	**type**\:   :py:class:`OptsEaBulkUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate>`
                
                .. attribute:: port_stat
                
                	port stat
                	**type**\: list of    :py:class:`PortStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat>`
                
                

                """

                _prefix = 'ncs5500-coherent-node-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.device_created = None
                    self.driver_init = None
                    self.driver_operational = None
                    self.dsp_controllers_created = None
                    self.dsp_ea_bulk_create = Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate()
                    self.dsp_ea_bulk_create.parent = self
                    self.dsp_ea_bulk_update = Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate()
                    self.dsp_ea_bulk_update.parent = self
                    self.eth_intf_created = None
                    self.optics_controllers_created = None
                    self.opts_ea_bulk_create = Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate()
                    self.opts_ea_bulk_create.parent = self
                    self.opts_ea_bulk_update = Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate()
                    self.opts_ea_bulk_update.parent = self
                    self.port_stat = YList()
                    self.port_stat.parent = self
                    self.port_stat.name = 'port_stat'


                class OptsEaBulkCreate(object):
                    """
                    opts ea bulk create
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.end = None
                        self.start = None
                        self.time_taken = None
                        self.worst_time = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:opts-ea-bulk-create'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.end is not None:
                            return True

                        if self.start is not None:
                            return True

                        if self.time_taken is not None:
                            return True

                        if self.worst_time is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                        return meta._meta_table['Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate']['meta_info']


                class OptsEaBulkUpdate(object):
                    """
                    opts ea bulk update
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.end = None
                        self.start = None
                        self.time_taken = None
                        self.worst_time = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:opts-ea-bulk-update'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.end is not None:
                            return True

                        if self.start is not None:
                            return True

                        if self.time_taken is not None:
                            return True

                        if self.worst_time is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                        return meta._meta_table['Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate']['meta_info']


                class DspEaBulkCreate(object):
                    """
                    dsp ea bulk create
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.end = None
                        self.start = None
                        self.time_taken = None
                        self.worst_time = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:dsp-ea-bulk-create'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.end is not None:
                            return True

                        if self.start is not None:
                            return True

                        if self.time_taken is not None:
                            return True

                        if self.worst_time is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                        return meta._meta_table['Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate']['meta_info']


                class DspEaBulkUpdate(object):
                    """
                    dsp ea bulk update
                    
                    .. attribute:: end
                    
                    	end
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: start
                    
                    	start
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: time_taken
                    
                    	time taken
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: worst_time
                    
                    	worst time
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.end = None
                        self.start = None
                        self.time_taken = None
                        self.worst_time = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:dsp-ea-bulk-update'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.end is not None:
                            return True

                        if self.start is not None:
                            return True

                        if self.time_taken is not None:
                            return True

                        if self.worst_time is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                        return meta._meta_table['Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate']['meta_info']


                class PortStat(object):
                    """
                    port stat
                    
                    .. attribute:: cd_max
                    
                    	cd max
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cd_min
                    
                    	cd min
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cdmax_op_stats
                    
                    	cdmax op stats
                    	**type**\:   :py:class:`CdmaxOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats>`
                    
                    .. attribute:: cdmin_op_stats
                    
                    	cdmin op stats
                    	**type**\:   :py:class:`CdminOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats>`
                    
                    .. attribute:: laser_off_stats
                    
                    	laser off stats
                    	**type**\:   :py:class:`LaserOffStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats>`
                    
                    .. attribute:: laser_on_stats
                    
                    	laser on stats
                    	**type**\:   :py:class:`LaserOnStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats>`
                    
                    .. attribute:: laser_state
                    
                    	laser state
                    	**type**\:  bool
                    
                    .. attribute:: traffic_type
                    
                    	traffic type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: traffictype_op_stats
                    
                    	traffictype op stats
                    	**type**\:   :py:class:`TraffictypeOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats>`
                    
                    .. attribute:: tx_power
                    
                    	tx power
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: txpwr_op_stats
                    
                    	txpwr op stats
                    	**type**\:   :py:class:`TxpwrOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats>`
                    
                    .. attribute:: wavelength
                    
                    	wavelength
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wl_op_stats
                    
                    	wl op stats
                    	**type**\:   :py:class:`WlOpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats>`
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.cd_max = None
                        self.cd_min = None
                        self.cdmax_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats()
                        self.cdmax_op_stats.parent = self
                        self.cdmin_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats()
                        self.cdmin_op_stats.parent = self
                        self.laser_off_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats()
                        self.laser_off_stats.parent = self
                        self.laser_on_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats()
                        self.laser_on_stats.parent = self
                        self.laser_state = None
                        self.traffic_type = None
                        self.traffictype_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats()
                        self.traffictype_op_stats.parent = self
                        self.tx_power = None
                        self.txpwr_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats()
                        self.txpwr_op_stats.parent = self
                        self.wavelength = None
                        self.wl_op_stats = Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats()
                        self.wl_op_stats.parent = self


                    class LaserOnStats(object):
                        """
                        laser on stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.end = None
                            self.start = None
                            self.time_taken = None
                            self.worst_time = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:laser-on-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.end is not None:
                                return True

                            if self.start is not None:
                                return True

                            if self.time_taken is not None:
                                return True

                            if self.worst_time is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                            return meta._meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats']['meta_info']


                    class LaserOffStats(object):
                        """
                        laser off stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.end = None
                            self.start = None
                            self.time_taken = None
                            self.worst_time = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:laser-off-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.end is not None:
                                return True

                            if self.start is not None:
                                return True

                            if self.time_taken is not None:
                                return True

                            if self.worst_time is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                            return meta._meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats']['meta_info']


                    class WlOpStats(object):
                        """
                        wl op stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.end = None
                            self.start = None
                            self.time_taken = None
                            self.worst_time = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:wl-op-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.end is not None:
                                return True

                            if self.start is not None:
                                return True

                            if self.time_taken is not None:
                                return True

                            if self.worst_time is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                            return meta._meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats']['meta_info']


                    class TxpwrOpStats(object):
                        """
                        txpwr op stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.end = None
                            self.start = None
                            self.time_taken = None
                            self.worst_time = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:txpwr-op-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.end is not None:
                                return True

                            if self.start is not None:
                                return True

                            if self.time_taken is not None:
                                return True

                            if self.worst_time is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                            return meta._meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats']['meta_info']


                    class CdminOpStats(object):
                        """
                        cdmin op stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.end = None
                            self.start = None
                            self.time_taken = None
                            self.worst_time = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:cdmin-op-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.end is not None:
                                return True

                            if self.start is not None:
                                return True

                            if self.time_taken is not None:
                                return True

                            if self.worst_time is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                            return meta._meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats']['meta_info']


                    class CdmaxOpStats(object):
                        """
                        cdmax op stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.end = None
                            self.start = None
                            self.time_taken = None
                            self.worst_time = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:cdmax-op-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.end is not None:
                                return True

                            if self.start is not None:
                                return True

                            if self.time_taken is not None:
                                return True

                            if self.worst_time is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                            return meta._meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats']['meta_info']


                    class TraffictypeOpStats(object):
                        """
                        traffictype op stats
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: time_taken
                        
                        	time taken
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        .. attribute:: worst_time
                        
                        	worst time
                        	**type**\:  str
                        
                        	**length:** 0..255
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.end = None
                            self.start = None
                            self.time_taken = None
                            self.worst_time = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:traffictype-op-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.end is not None:
                                return True

                            if self.start is not None:
                                return True

                            if self.time_taken is not None:
                                return True

                            if self.worst_time is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                            return meta._meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:port-stat'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.cd_max is not None:
                            return True

                        if self.cd_min is not None:
                            return True

                        if self.cdmax_op_stats is not None and self.cdmax_op_stats._has_data():
                            return True

                        if self.cdmin_op_stats is not None and self.cdmin_op_stats._has_data():
                            return True

                        if self.laser_off_stats is not None and self.laser_off_stats._has_data():
                            return True

                        if self.laser_on_stats is not None and self.laser_on_stats._has_data():
                            return True

                        if self.laser_state is not None:
                            return True

                        if self.traffic_type is not None:
                            return True

                        if self.traffictype_op_stats is not None and self.traffictype_op_stats._has_data():
                            return True

                        if self.tx_power is not None:
                            return True

                        if self.txpwr_op_stats is not None and self.txpwr_op_stats._has_data():
                            return True

                        if self.wavelength is not None:
                            return True

                        if self.wl_op_stats is not None and self.wl_op_stats._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                        return meta._meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:coherent-time-stats'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.device_created is not None:
                        return True

                    if self.driver_init is not None:
                        return True

                    if self.driver_operational is not None:
                        return True

                    if self.dsp_controllers_created is not None:
                        return True

                    if self.dsp_ea_bulk_create is not None and self.dsp_ea_bulk_create._has_data():
                        return True

                    if self.dsp_ea_bulk_update is not None and self.dsp_ea_bulk_update._has_data():
                        return True

                    if self.eth_intf_created is not None:
                        return True

                    if self.optics_controllers_created is not None:
                        return True

                    if self.opts_ea_bulk_create is not None and self.opts_ea_bulk_create._has_data():
                        return True

                    if self.opts_ea_bulk_update is not None and self.opts_ea_bulk_update._has_data():
                        return True

                    if self.port_stat is not None:
                        for child_ref in self.port_stat:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                    return meta._meta_table['Coherent.Nodes.Node.CoherentTimeStats']['meta_info']


            class Devicemapping(object):
                """
                Coherent node data for device \_mapping
                
                .. attribute:: dev_map
                
                	dev map
                	**type**\: list of    :py:class:`DevMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Devicemapping.DevMap>`
                
                .. attribute:: num_entries
                
                	Number of dev map entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ncs5500-coherent-node-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.dev_map = YList()
                    self.dev_map.parent = self
                    self.dev_map.name = 'dev_map'
                    self.num_entries = None


                class DevMap(object):
                    """
                    dev map
                    
                    .. attribute:: device_address
                    
                    	Device address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ifhandle
                    
                    	Interface handle
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: intf_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.device_address = None
                        self.ifhandle = None
                        self.intf_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:dev-map'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.device_address is not None:
                            return True

                        if self.ifhandle is not None:
                            return True

                        if self.intf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                        return meta._meta_table['Coherent.Nodes.Node.Devicemapping.DevMap']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:devicemapping'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.dev_map is not None:
                        for child_ref in self.dev_map:
                            if child_ref._has_data():
                                return True

                    if self.num_entries is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                    return meta._meta_table['Coherent.Nodes.Node.Devicemapping']['meta_info']


            class Coherenthealth(object):
                """
                Coherent node data for driver health
                
                .. attribute:: aipc_srvr_state
                
                	aipc srvr state
                	**type**\:  bool
                
                .. attribute:: board_type
                
                	board type
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: denali_version
                
                	denali version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dsp_ea_conn
                
                	dsp ea conn
                	**type**\:  bool
                
                .. attribute:: im_state
                
                	im state
                	**type**\:  bool
                
                .. attribute:: jlink_op
                
                	jlink op
                	**type**\:  str
                
                	**length:** 0..1024
                
                .. attribute:: morgoth_alive
                
                	morgoth alive
                	**type**\:  bool
                
                .. attribute:: morgoth_downloaded_version
                
                	morgoth downloaded version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: morgoth_golden_version
                
                	morgoth golden version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: morgoth_running_version
                
                	morgoth running version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: optics_ea_conn
                
                	optics ea conn
                	**type**\:  bool
                
                .. attribute:: pm_state
                
                	pm state
                	**type**\:  bool
                
                .. attribute:: port_data
                
                	port data
                	**type**\: list of    :py:class:`PortData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData>`
                
                .. attribute:: prov_infra_state
                
                	prov infra state
                	**type**\:  bool
                
                .. attribute:: sdk_fpga_compatible
                
                	sdk fpga compatible
                	**type**\:  bool
                
                .. attribute:: sdk_version
                
                	sdk version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: sysdb_state
                
                	sysdb state
                	**type**\:  bool
                
                .. attribute:: vether_state
                
                	vether state
                	**type**\:  bool
                
                

                """

                _prefix = 'ncs5500-coherent-node-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.aipc_srvr_state = None
                    self.board_type = None
                    self.denali_version = None
                    self.dsp_ea_conn = None
                    self.im_state = None
                    self.jlink_op = None
                    self.morgoth_alive = None
                    self.morgoth_downloaded_version = None
                    self.morgoth_golden_version = None
                    self.morgoth_running_version = None
                    self.optics_ea_conn = None
                    self.pm_state = None
                    self.port_data = YList()
                    self.port_data.parent = self
                    self.port_data.name = 'port_data'
                    self.prov_infra_state = None
                    self.sdk_fpga_compatible = None
                    self.sdk_version = None
                    self.sysdb_state = None
                    self.vether_state = None


                class PortData(object):
                    """
                    port data
                    
                    .. attribute:: ctp_info
                    
                    	ctp info
                    	**type**\:   :py:class:`CtpInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo>`
                    
                    .. attribute:: dsp_admin_up
                    
                    	dsp admin up
                    	**type**\:  bool
                    
                    .. attribute:: dsp_ctrl_created
                    
                    	dsp ctrl created
                    	**type**\:  bool
                    
                    .. attribute:: fp_port_idx
                    
                    	fp port idx
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: has_pluggable
                    
                    	has pluggable
                    	**type**\:  bool
                    
                    .. attribute:: interface_info
                    
                    	interface info
                    	**type**\:   :py:class:`InterfaceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo>`
                    
                    .. attribute:: laser_op_rc
                    
                    	laser op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: laser_state
                    
                    	laser state
                    	**type**\:  bool
                    
                    .. attribute:: optics_admin_up
                    
                    	optics admin up
                    	**type**\:  bool
                    
                    .. attribute:: optics_ctrl_created
                    
                    	optics ctrl created
                    	**type**\:  bool
                    
                    .. attribute:: traffic_op_rc
                    
                    	traffic op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: traffic_type
                    
                    	traffic type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wavelength
                    
                    	wavelength
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wlen_op_rc
                    
                    	wlen op rc
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ctp_info = Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo()
                        self.ctp_info.parent = self
                        self.dsp_admin_up = None
                        self.dsp_ctrl_created = None
                        self.fp_port_idx = None
                        self.has_pluggable = None
                        self.interface_info = Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo()
                        self.interface_info.parent = self
                        self.laser_op_rc = None
                        self.laser_state = None
                        self.optics_admin_up = None
                        self.optics_ctrl_created = None
                        self.traffic_op_rc = None
                        self.traffic_type = None
                        self.wavelength = None
                        self.wlen_op_rc = None


                    class CtpInfo(object):
                        """
                        ctp info
                        
                        .. attribute:: clei_code_number
                        
                        	CLEI code number
                        	**type**\:  str
                        
                        	**length:** 0..10
                        
                        .. attribute:: ctp_type
                        
                        	ctp type
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: date_code_number
                        
                        	date code number
                        	**type**\:  str
                        
                        	**length:** 0..10
                        
                        .. attribute:: description
                        
                        	description
                        	**type**\:  str
                        
                        	**length:** 0..64
                        
                        .. attribute:: deviation
                        
                        	deviation
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        .. attribute:: module_firmware_committed_version_number
                        
                        	module firmware committed version number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: module_firmware_running_version_number
                        
                        	module firmware running version number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: module_hardware_version_number
                        
                        	module hardware version number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: part_number
                        
                        	part number
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        .. attribute:: pid
                        
                        	pid
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        .. attribute:: serial_number
                        
                        	serial number
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        .. attribute:: vendorname
                        
                        	vendorname
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        .. attribute:: vid
                        
                        	vid
                        	**type**\:  str
                        
                        	**length:** 0..16
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.clei_code_number = None
                            self.ctp_type = None
                            self.date_code_number = None
                            self.description = None
                            self.deviation = None
                            self.module_firmware_committed_version_number = None
                            self.module_firmware_running_version_number = None
                            self.module_hardware_version_number = None
                            self.part_number = None
                            self.pid = None
                            self.serial_number = None
                            self.vendorname = None
                            self.vid = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:ctp-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.clei_code_number is not None:
                                return True

                            if self.ctp_type is not None:
                                return True

                            if self.date_code_number is not None:
                                return True

                            if self.description is not None:
                                return True

                            if self.deviation is not None:
                                return True

                            if self.module_firmware_committed_version_number is not None:
                                return True

                            if self.module_firmware_running_version_number is not None:
                                return True

                            if self.module_hardware_version_number is not None:
                                return True

                            if self.part_number is not None:
                                return True

                            if self.pid is not None:
                                return True

                            if self.serial_number is not None:
                                return True

                            if self.vendorname is not None:
                                return True

                            if self.vid is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                            return meta._meta_table['Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo']['meta_info']


                    class InterfaceInfo(object):
                        """
                        interface info
                        
                        .. attribute:: eth_data
                        
                        	eth data
                        	**type**\: list of    :py:class:`EthData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData>`
                        
                        .. attribute:: intf_count
                        
                        	intf count
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'ncs5500-coherent-node-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.eth_data = YList()
                            self.eth_data.parent = self
                            self.eth_data.name = 'eth_data'
                            self.intf_count = None


                        class EthData(object):
                            """
                            eth data
                            
                            .. attribute:: admin_state
                            
                            	admin state
                            	**type**\:  bool
                            
                            .. attribute:: ifname
                            
                            	ifname
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: intf_handle
                            
                            	intf handle
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ncs5500-coherent-node-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.admin_state = None
                                self.ifname = None
                                self.intf_handle = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:eth-data'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.admin_state is not None:
                                    return True

                                if self.ifname is not None:
                                    return True

                                if self.intf_handle is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                                return meta._meta_table['Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:interface-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.eth_data is not None:
                                for child_ref in self.eth_data:
                                    if child_ref._has_data():
                                        return True

                            if self.intf_count is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                            return meta._meta_table['Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:port-data'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.ctp_info is not None and self.ctp_info._has_data():
                            return True

                        if self.dsp_admin_up is not None:
                            return True

                        if self.dsp_ctrl_created is not None:
                            return True

                        if self.fp_port_idx is not None:
                            return True

                        if self.has_pluggable is not None:
                            return True

                        if self.interface_info is not None and self.interface_info._has_data():
                            return True

                        if self.laser_op_rc is not None:
                            return True

                        if self.laser_state is not None:
                            return True

                        if self.optics_admin_up is not None:
                            return True

                        if self.optics_ctrl_created is not None:
                            return True

                        if self.traffic_op_rc is not None:
                            return True

                        if self.traffic_type is not None:
                            return True

                        if self.wavelength is not None:
                            return True

                        if self.wlen_op_rc is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                        return meta._meta_table['Coherent.Nodes.Node.Coherenthealth.PortData']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:coherenthealth'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.aipc_srvr_state is not None:
                        return True

                    if self.board_type is not None:
                        return True

                    if self.denali_version is not None:
                        return True

                    if self.dsp_ea_conn is not None:
                        return True

                    if self.im_state is not None:
                        return True

                    if self.jlink_op is not None:
                        return True

                    if self.morgoth_alive is not None:
                        return True

                    if self.morgoth_downloaded_version is not None:
                        return True

                    if self.morgoth_golden_version is not None:
                        return True

                    if self.morgoth_running_version is not None:
                        return True

                    if self.optics_ea_conn is not None:
                        return True

                    if self.pm_state is not None:
                        return True

                    if self.port_data is not None:
                        for child_ref in self.port_data:
                            if child_ref._has_data():
                                return True

                    if self.prov_infra_state is not None:
                        return True

                    if self.sdk_fpga_compatible is not None:
                        return True

                    if self.sdk_version is not None:
                        return True

                    if self.sysdb_state is not None:
                        return True

                    if self.vether_state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                    return meta._meta_table['Coherent.Nodes.Node.Coherenthealth']['meta_info']


            class PortModeAllInfo(object):
                """
                PortMode all operational data
                
                .. attribute:: num_entries
                
                	Number of dev map entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: portmode_entry
                
                	portmode entry
                	**type**\: list of    :py:class:`PortmodeEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper.Coherent.Nodes.Node.PortModeAllInfo.PortmodeEntry>`
                
                

                """

                _prefix = 'ncs5500-coherent-node-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.num_entries = None
                    self.portmode_entry = YList()
                    self.portmode_entry.parent = self
                    self.portmode_entry.name = 'portmode_entry'


                class PortmodeEntry(object):
                    """
                    portmode entry
                    
                    .. attribute:: diff
                    
                    	Optics diff
                    	**type**\:  str
                    
                    .. attribute:: fec
                    
                    	Optics fec
                    	**type**\:  str
                    
                    .. attribute:: intf_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    .. attribute:: modulation
                    
                    	Optics modulation
                    	**type**\:  str
                    
                    .. attribute:: speed
                    
                    	Optics speed
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ncs5500-coherent-node-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.diff = None
                        self.fec = None
                        self.intf_name = None
                        self.modulation = None
                        self.speed = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:portmode-entry'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.diff is not None:
                            return True

                        if self.fec is not None:
                            return True

                        if self.intf_name is not None:
                            return True

                        if self.modulation is not None:
                            return True

                        if self.speed is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                        return meta._meta_table['Coherent.Nodes.Node.PortModeAllInfo.PortmodeEntry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ncs5500-coherent-node-oper:port-mode-all-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.num_entries is not None:
                        return True

                    if self.portmode_entry is not None:
                        for child_ref in self.portmode_entry:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                    return meta._meta_table['Coherent.Nodes.Node.PortModeAllInfo']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ncs5500-coherent-node-oper:coherent/Cisco-IOS-XR-ncs5500-coherent-node-oper:nodes/Cisco-IOS-XR-ncs5500-coherent-node-oper:node[Cisco-IOS-XR-ncs5500-coherent-node-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.node_name is not None:
                    return True

                if self.coherent_time_stats is not None and self.coherent_time_stats._has_data():
                    return True

                if self.coherenthealth is not None and self.coherenthealth._has_data():
                    return True

                if self.devicemapping is not None and self.devicemapping._has_data():
                    return True

                if self.port_mode_all_info is not None and self.port_mode_all_info._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
                return meta._meta_table['Coherent.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ncs5500-coherent-node-oper:coherent/Cisco-IOS-XR-ncs5500-coherent-node-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
            return meta._meta_table['Coherent.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ncs5500-coherent-node-oper:coherent'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5500_coherent_node_oper as meta
        return meta._meta_table['Coherent']['meta_info']



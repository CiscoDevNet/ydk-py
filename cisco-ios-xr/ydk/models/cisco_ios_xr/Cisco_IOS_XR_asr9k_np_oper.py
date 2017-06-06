""" Cisco_IOS_XR_asr9k_np_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-np package operational data.

This module contains definitions
for the following management objects\:
  hardware\-module\-np\: Hardware NP Counters

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class HardwareModuleNp(object):
    """
    Hardware NP Counters
    
    .. attribute:: nodes
    
    	Table of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes>`
    
    

    """

    _prefix = 'asr9k-np-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = HardwareModuleNp.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Number
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-np-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Number
            
            .. attribute:: node_name  <key>
            
            	node number
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: nps
            
            	List of all NP
            	**type**\:   :py:class:`Nps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps>`
            
            

            """

            _prefix = 'asr9k-np-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.nps = HardwareModuleNp.Nodes.Node.Nps()
                self.nps.parent = self


            class Nps(object):
                """
                List of all NP
                
                .. attribute:: np
                
                	np0 to np7
                	**type**\: list of    :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np>`
                
                

                """

                _prefix = 'asr9k-np-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.np = YList()
                    self.np.parent = self
                    self.np.name = 'np'


                class Np(object):
                    """
                    np0 to np7
                    
                    .. attribute:: np_name  <key>
                    
                    	NP name
                    	**type**\:  str
                    
                    	**pattern:** (np0)\|(np1)\|(np2)\|(np3)\|(np4)\|(np5)\|(np6)\|(np7)
                    
                    .. attribute:: chn_load
                    
                    	prm channel load info
                    	**type**\:   :py:class:`ChnLoad <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad>`
                    
                    .. attribute:: counters
                    
                    	prm counters info
                    	**type**\:   :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.Counters>`
                    
                    .. attribute:: fast_drop
                    
                    	prm fast drop counters info
                    	**type**\:   :py:class:`FastDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop>`
                    
                    .. attribute:: tcam_summary
                    
                    	prm tcam summary info
                    	**type**\:   :py:class:`TcamSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary>`
                    
                    

                    """

                    _prefix = 'asr9k-np-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.np_name = None
                        self.chn_load = HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad()
                        self.chn_load.parent = self
                        self.counters = HardwareModuleNp.Nodes.Node.Nps.Np.Counters()
                        self.counters.parent = self
                        self.fast_drop = HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop()
                        self.fast_drop.parent = self
                        self.tcam_summary = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary()
                        self.tcam_summary.parent = self


                    class ChnLoad(object):
                        """
                        prm channel load info
                        
                        .. attribute:: np_chn_load
                        
                        	Array of NP Channel load counters
                        	**type**\: list of    :py:class:`NpChnLoad <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad>`
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.np_chn_load = YList()
                            self.np_chn_load.parent = self
                            self.np_chn_load.name = 'np_chn_load'


                        class NpChnLoad(object):
                            """
                            Array of NP Channel load counters
                            
                            .. attribute:: avg_guar_rfd_usage
                            
                            	Average of garanteed RFD usage
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: avg_rfd_usage
                            
                            	Average RFD Usage
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: flow_ctr_counter
                            
                            	Flow control counters
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interface_name
                            
                            	Inerface Name
                            	**type**\:  str
                            
                            .. attribute:: peak_guar_rfd_usage
                            
                            	Peak of garanteed RFD usage
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: peak_rfd_usage
                            
                            	Peak RFD Usage
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.avg_guar_rfd_usage = None
                                self.avg_rfd_usage = None
                                self.flow_ctr_counter = None
                                self.interface_name = None
                                self.peak_guar_rfd_usage = None
                                self.peak_rfd_usage = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:np-chn-load'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.avg_guar_rfd_usage is not None:
                                    return True

                                if self.avg_rfd_usage is not None:
                                    return True

                                if self.flow_ctr_counter is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.peak_guar_rfd_usage is not None:
                                    return True

                                if self.peak_rfd_usage is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:chn-load'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.np_chn_load is not None:
                                for child_ref in self.np_chn_load:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                            return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad']['meta_info']


                    class TcamSummary(object):
                        """
                        prm tcam summary info
                        
                        .. attribute:: internal_tcam_info
                        
                        	Internal tcam summary info
                        	**type**\:   :py:class:`InternalTcamInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo>`
                        
                        .. attribute:: tcam_info
                        
                        	External tcam summary info
                        	**type**\:   :py:class:`TcamInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo>`
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.internal_tcam_info = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo()
                            self.internal_tcam_info.parent = self
                            self.tcam_info = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo()
                            self.tcam_info.parent = self


                        class InternalTcamInfo(object):
                            """
                            Internal tcam summary info
                            
                            .. attribute:: tcam_lt_l2
                            
                            	Array of TCAM LT L2 partition summaries
                            	**type**\: list of    :py:class:`TcamLtL2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2>`
                            
                            .. attribute:: tcam_lt_ods2
                            
                            	TCAM LT ODS 2 summary
                            	**type**\:   :py:class:`TcamLtOds2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2>`
                            
                            .. attribute:: tcam_lt_ods8
                            
                            	TCAM LT\_ODS 8 summary
                            	**type**\:   :py:class:`TcamLtOds8 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8>`
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.tcam_lt_l2 = YList()
                                self.tcam_lt_l2.parent = self
                                self.tcam_lt_l2.name = 'tcam_lt_l2'
                                self.tcam_lt_ods2 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2()
                                self.tcam_lt_ods2.parent = self
                                self.tcam_lt_ods8 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8()
                                self.tcam_lt_ods8.parent = self


                            class TcamLtOds2(object):
                                """
                                TCAM LT ODS 2 summary
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:   :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl>`
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:   :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon>`
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:   :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib>`
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:   :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi>`
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:   :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr>`
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:   :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos>`
                                
                                .. attribute:: application_edpl_entry
                                
                                	app EDPL entry
                                	**type**\:   :py:class:`ApplicationEdplEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry>`
                                
                                .. attribute:: free_entries
                                
                                	free entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: max_entries
                                
                                	Max entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi()
                                    self.app_id_li.parent = self
                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self.application_edpl_entry = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry()
                                    self.application_edpl_entry.parent = self
                                    self.free_entries = None
                                    self.max_entries = None


                                class AppIdIfib(object):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_vmr_ids = None
                                        self.total_allocated_entries = None
                                        self.total_used_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-ifib'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_vmr_ids is not None:
                                            return True

                                        if self.total_allocated_entries is not None:
                                            return True

                                        if self.total_used_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib']['meta_info']


                                class AppIdQos(object):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_vmr_ids = None
                                        self.total_allocated_entries = None
                                        self.total_used_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-qos'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_vmr_ids is not None:
                                            return True

                                        if self.total_allocated_entries is not None:
                                            return True

                                        if self.total_used_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos']['meta_info']


                                class AppIdAcl(object):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_vmr_ids = None
                                        self.total_allocated_entries = None
                                        self.total_used_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-acl'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_vmr_ids is not None:
                                            return True

                                        if self.total_allocated_entries is not None:
                                            return True

                                        if self.total_used_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl']['meta_info']


                                class AppIdAfmon(object):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_vmr_ids = None
                                        self.total_allocated_entries = None
                                        self.total_used_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-afmon'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_vmr_ids is not None:
                                            return True

                                        if self.total_allocated_entries is not None:
                                            return True

                                        if self.total_used_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon']['meta_info']


                                class AppIdLi(object):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_vmr_ids = None
                                        self.total_allocated_entries = None
                                        self.total_used_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-li'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_vmr_ids is not None:
                                            return True

                                        if self.total_allocated_entries is not None:
                                            return True

                                        if self.total_used_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi']['meta_info']


                                class AppIdPbr(object):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_vmr_ids = None
                                        self.total_allocated_entries = None
                                        self.total_used_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-pbr'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_vmr_ids is not None:
                                            return True

                                        if self.total_allocated_entries is not None:
                                            return True

                                        if self.total_used_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr']['meta_info']


                                class ApplicationEdplEntry(object):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_vmr_ids = None
                                        self.total_allocated_entries = None
                                        self.total_used_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:application-edpl-entry'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_vmr_ids is not None:
                                            return True

                                        if self.total_allocated_entries is not None:
                                            return True

                                        if self.total_used_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:tcam-lt-ods2'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.app_id_acl is not None and self.app_id_acl._has_data():
                                        return True

                                    if self.app_id_afmon is not None and self.app_id_afmon._has_data():
                                        return True

                                    if self.app_id_ifib is not None and self.app_id_ifib._has_data():
                                        return True

                                    if self.app_id_li is not None and self.app_id_li._has_data():
                                        return True

                                    if self.app_id_pbr is not None and self.app_id_pbr._has_data():
                                        return True

                                    if self.app_id_qos is not None and self.app_id_qos._has_data():
                                        return True

                                    if self.application_edpl_entry is not None and self.application_edpl_entry._has_data():
                                        return True

                                    if self.free_entries is not None:
                                        return True

                                    if self.max_entries is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2']['meta_info']


                            class TcamLtOds8(object):
                                """
                                TCAM LT\_ODS 8 summary
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:   :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl>`
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:   :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon>`
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:   :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib>`
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:   :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi>`
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:   :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr>`
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:   :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos>`
                                
                                .. attribute:: application_edpl_entry
                                
                                	app EDPL entry
                                	**type**\:   :py:class:`ApplicationEdplEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry>`
                                
                                .. attribute:: free_entries
                                
                                	free entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: max_entries
                                
                                	Max entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi()
                                    self.app_id_li.parent = self
                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self.application_edpl_entry = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry()
                                    self.application_edpl_entry.parent = self
                                    self.free_entries = None
                                    self.max_entries = None


                                class AppIdIfib(object):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_vmr_ids = None
                                        self.total_allocated_entries = None
                                        self.total_used_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-ifib'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_vmr_ids is not None:
                                            return True

                                        if self.total_allocated_entries is not None:
                                            return True

                                        if self.total_used_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib']['meta_info']


                                class AppIdQos(object):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_vmr_ids = None
                                        self.total_allocated_entries = None
                                        self.total_used_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-qos'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_vmr_ids is not None:
                                            return True

                                        if self.total_allocated_entries is not None:
                                            return True

                                        if self.total_used_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos']['meta_info']


                                class AppIdAcl(object):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_vmr_ids = None
                                        self.total_allocated_entries = None
                                        self.total_used_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-acl'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_vmr_ids is not None:
                                            return True

                                        if self.total_allocated_entries is not None:
                                            return True

                                        if self.total_used_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl']['meta_info']


                                class AppIdAfmon(object):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_vmr_ids = None
                                        self.total_allocated_entries = None
                                        self.total_used_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-afmon'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_vmr_ids is not None:
                                            return True

                                        if self.total_allocated_entries is not None:
                                            return True

                                        if self.total_used_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon']['meta_info']


                                class AppIdLi(object):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_vmr_ids = None
                                        self.total_allocated_entries = None
                                        self.total_used_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-li'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_vmr_ids is not None:
                                            return True

                                        if self.total_allocated_entries is not None:
                                            return True

                                        if self.total_used_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi']['meta_info']


                                class AppIdPbr(object):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_vmr_ids = None
                                        self.total_allocated_entries = None
                                        self.total_used_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-pbr'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_vmr_ids is not None:
                                            return True

                                        if self.total_allocated_entries is not None:
                                            return True

                                        if self.total_used_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr']['meta_info']


                                class ApplicationEdplEntry(object):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_vmr_ids = None
                                        self.total_allocated_entries = None
                                        self.total_used_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:application-edpl-entry'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_vmr_ids is not None:
                                            return True

                                        if self.total_allocated_entries is not None:
                                            return True

                                        if self.total_used_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:tcam-lt-ods8'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.app_id_acl is not None and self.app_id_acl._has_data():
                                        return True

                                    if self.app_id_afmon is not None and self.app_id_afmon._has_data():
                                        return True

                                    if self.app_id_ifib is not None and self.app_id_ifib._has_data():
                                        return True

                                    if self.app_id_li is not None and self.app_id_li._has_data():
                                        return True

                                    if self.app_id_pbr is not None and self.app_id_pbr._has_data():
                                        return True

                                    if self.app_id_qos is not None and self.app_id_qos._has_data():
                                        return True

                                    if self.application_edpl_entry is not None and self.application_edpl_entry._has_data():
                                        return True

                                    if self.free_entries is not None:
                                        return True

                                    if self.max_entries is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8']['meta_info']


                            class TcamLtL2(object):
                                """
                                Array of TCAM LT L2 partition summaries
                                
                                .. attribute:: free_entries
                                
                                	Free Entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: partition_id
                                
                                	PartitionID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: valid_entries
                                
                                	Valid Entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.free_entries = None
                                    self.partition_id = None
                                    self.valid_entries = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:tcam-lt-l2'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.free_entries is not None:
                                        return True

                                    if self.partition_id is not None:
                                        return True

                                    if self.valid_entries is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:internal-tcam-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.tcam_lt_l2 is not None:
                                    for child_ref in self.tcam_lt_l2:
                                        if child_ref._has_data():
                                            return True

                                if self.tcam_lt_ods2 is not None and self.tcam_lt_ods2._has_data():
                                    return True

                                if self.tcam_lt_ods8 is not None and self.tcam_lt_ods8._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo']['meta_info']


                        class TcamInfo(object):
                            """
                            External tcam summary info
                            
                            .. attribute:: tcam_lt_l2
                            
                            	Array of TCAM L2 partition summaries
                            	**type**\: list of    :py:class:`TcamLtL2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2>`
                            
                            .. attribute:: tcam_lt_ods2
                            
                            	TCAM ODS2 partition summary
                            	**type**\:   :py:class:`TcamLtOds2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2>`
                            
                            .. attribute:: tcam_lt_ods8
                            
                            	TCAM ODS8 partition summary
                            	**type**\:   :py:class:`TcamLtOds8 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8>`
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.tcam_lt_l2 = YList()
                                self.tcam_lt_l2.parent = self
                                self.tcam_lt_l2.name = 'tcam_lt_l2'
                                self.tcam_lt_ods2 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2()
                                self.tcam_lt_ods2.parent = self
                                self.tcam_lt_ods8 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8()
                                self.tcam_lt_ods8.parent = self


                            class TcamLtOds2(object):
                                """
                                TCAM ODS2 partition summary
                                
                                .. attribute:: acl_common
                                
                                	ACL common region
                                	**type**\:   :py:class:`AclCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon>`
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:   :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl>`
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:   :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon>`
                                
                                .. attribute:: app_id_edpl
                                
                                	app EDPL entry
                                	**type**\:   :py:class:`AppIdEdpl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl>`
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:   :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib>`
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:   :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi>`
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:   :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr>`
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:   :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos>`
                                
                                .. attribute:: free_entries
                                
                                	Free entries in the table
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: reserved_entries
                                
                                	The number of active vmr entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acl_common = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon()
                                    self.acl_common.parent = self
                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self.app_id_edpl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl()
                                    self.app_id_edpl.parent = self
                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi()
                                    self.app_id_li.parent = self
                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self.free_entries = None
                                    self.reserved_entries = None


                                class AclCommon(object):
                                    """
                                    ACL common region
                                    
                                    .. attribute:: allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: free_entries
                                    
                                    	Free entries in the table
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.allocated_entries = None
                                        self.free_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:acl-common'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.allocated_entries is not None:
                                            return True

                                        if self.free_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon']['meta_info']


                                class AppIdIfib(object):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self.num_vmr_ids = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-ifib'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_active_entries is not None:
                                            return True

                                        if self.num_allocated_entries is not None:
                                            return True

                                        if self.num_vmr_ids is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib']['meta_info']


                                class AppIdQos(object):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self.num_vmr_ids = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-qos'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_active_entries is not None:
                                            return True

                                        if self.num_allocated_entries is not None:
                                            return True

                                        if self.num_vmr_ids is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos']['meta_info']


                                class AppIdAcl(object):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self.num_vmr_ids = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-acl'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_active_entries is not None:
                                            return True

                                        if self.num_allocated_entries is not None:
                                            return True

                                        if self.num_vmr_ids is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl']['meta_info']


                                class AppIdAfmon(object):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self.num_vmr_ids = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-afmon'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_active_entries is not None:
                                            return True

                                        if self.num_allocated_entries is not None:
                                            return True

                                        if self.num_vmr_ids is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon']['meta_info']


                                class AppIdLi(object):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self.num_vmr_ids = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-li'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_active_entries is not None:
                                            return True

                                        if self.num_allocated_entries is not None:
                                            return True

                                        if self.num_vmr_ids is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi']['meta_info']


                                class AppIdPbr(object):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self.num_vmr_ids = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-pbr'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_active_entries is not None:
                                            return True

                                        if self.num_allocated_entries is not None:
                                            return True

                                        if self.num_vmr_ids is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr']['meta_info']


                                class AppIdEdpl(object):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self.num_vmr_ids = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-edpl'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_active_entries is not None:
                                            return True

                                        if self.num_allocated_entries is not None:
                                            return True

                                        if self.num_vmr_ids is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:tcam-lt-ods2'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.acl_common is not None and self.acl_common._has_data():
                                        return True

                                    if self.app_id_acl is not None and self.app_id_acl._has_data():
                                        return True

                                    if self.app_id_afmon is not None and self.app_id_afmon._has_data():
                                        return True

                                    if self.app_id_edpl is not None and self.app_id_edpl._has_data():
                                        return True

                                    if self.app_id_ifib is not None and self.app_id_ifib._has_data():
                                        return True

                                    if self.app_id_li is not None and self.app_id_li._has_data():
                                        return True

                                    if self.app_id_pbr is not None and self.app_id_pbr._has_data():
                                        return True

                                    if self.app_id_qos is not None and self.app_id_qos._has_data():
                                        return True

                                    if self.free_entries is not None:
                                        return True

                                    if self.reserved_entries is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2']['meta_info']


                            class TcamLtOds8(object):
                                """
                                TCAM ODS8 partition summary
                                
                                .. attribute:: acl_common
                                
                                	ACL common region
                                	**type**\:   :py:class:`AclCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon>`
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:   :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl>`
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:   :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon>`
                                
                                .. attribute:: app_id_edpl
                                
                                	app EDPL entry
                                	**type**\:   :py:class:`AppIdEdpl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl>`
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:   :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib>`
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:   :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi>`
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:   :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr>`
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:   :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos>`
                                
                                .. attribute:: free_entries
                                
                                	Free entries in the table
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: reserved_entries
                                
                                	The number of active vmr entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acl_common = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon()
                                    self.acl_common.parent = self
                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self.app_id_edpl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl()
                                    self.app_id_edpl.parent = self
                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi()
                                    self.app_id_li.parent = self
                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self.free_entries = None
                                    self.reserved_entries = None


                                class AclCommon(object):
                                    """
                                    ACL common region
                                    
                                    .. attribute:: allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: free_entries
                                    
                                    	Free entries in the table
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.allocated_entries = None
                                        self.free_entries = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:acl-common'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.allocated_entries is not None:
                                            return True

                                        if self.free_entries is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon']['meta_info']


                                class AppIdIfib(object):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self.num_vmr_ids = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-ifib'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_active_entries is not None:
                                            return True

                                        if self.num_allocated_entries is not None:
                                            return True

                                        if self.num_vmr_ids is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib']['meta_info']


                                class AppIdQos(object):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self.num_vmr_ids = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-qos'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_active_entries is not None:
                                            return True

                                        if self.num_allocated_entries is not None:
                                            return True

                                        if self.num_vmr_ids is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos']['meta_info']


                                class AppIdAcl(object):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self.num_vmr_ids = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-acl'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_active_entries is not None:
                                            return True

                                        if self.num_allocated_entries is not None:
                                            return True

                                        if self.num_vmr_ids is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl']['meta_info']


                                class AppIdAfmon(object):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self.num_vmr_ids = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-afmon'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_active_entries is not None:
                                            return True

                                        if self.num_allocated_entries is not None:
                                            return True

                                        if self.num_vmr_ids is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon']['meta_info']


                                class AppIdLi(object):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self.num_vmr_ids = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-li'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_active_entries is not None:
                                            return True

                                        if self.num_allocated_entries is not None:
                                            return True

                                        if self.num_vmr_ids is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi']['meta_info']


                                class AppIdPbr(object):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self.num_vmr_ids = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-pbr'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_active_entries is not None:
                                            return True

                                        if self.num_allocated_entries is not None:
                                            return True

                                        if self.num_vmr_ids is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr']['meta_info']


                                class AppIdEdpl(object):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self.num_vmr_ids = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:app-id-edpl'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.num_active_entries is not None:
                                            return True

                                        if self.num_allocated_entries is not None:
                                            return True

                                        if self.num_vmr_ids is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:tcam-lt-ods8'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.acl_common is not None and self.acl_common._has_data():
                                        return True

                                    if self.app_id_acl is not None and self.app_id_acl._has_data():
                                        return True

                                    if self.app_id_afmon is not None and self.app_id_afmon._has_data():
                                        return True

                                    if self.app_id_edpl is not None and self.app_id_edpl._has_data():
                                        return True

                                    if self.app_id_ifib is not None and self.app_id_ifib._has_data():
                                        return True

                                    if self.app_id_li is not None and self.app_id_li._has_data():
                                        return True

                                    if self.app_id_pbr is not None and self.app_id_pbr._has_data():
                                        return True

                                    if self.app_id_qos is not None and self.app_id_qos._has_data():
                                        return True

                                    if self.free_entries is not None:
                                        return True

                                    if self.reserved_entries is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8']['meta_info']


                            class TcamLtL2(object):
                                """
                                Array of TCAM L2 partition summaries
                                
                                .. attribute:: free_entries
                                
                                	Free Entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: partition_id
                                
                                	PartitionID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: priority
                                
                                	Priority
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: valid_entries
                                
                                	Valid Entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.free_entries = None
                                    self.partition_id = None
                                    self.priority = None
                                    self.valid_entries = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:tcam-lt-l2'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.free_entries is not None:
                                        return True

                                    if self.partition_id is not None:
                                        return True

                                    if self.priority is not None:
                                        return True

                                    if self.valid_entries is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:tcam-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.tcam_lt_l2 is not None:
                                    for child_ref in self.tcam_lt_l2:
                                        if child_ref._has_data():
                                            return True

                                if self.tcam_lt_ods2 is not None and self.tcam_lt_ods2._has_data():
                                    return True

                                if self.tcam_lt_ods8 is not None and self.tcam_lt_ods8._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:tcam-summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.internal_tcam_info is not None and self.internal_tcam_info._has_data():
                                return True

                            if self.tcam_info is not None and self.tcam_info._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                            return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary']['meta_info']


                    class Counters(object):
                        """
                        prm counters info
                        
                        .. attribute:: np_counter
                        
                        	Array of NP Counters
                        	**type**\: list of    :py:class:`NpCounter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter>`
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.np_counter = YList()
                            self.np_counter.parent = self
                            self.np_counter.name = 'np_counter'


                        class NpCounter(object):
                            """
                            Array of NP Counters
                            
                            .. attribute:: counter_index
                            
                            	Counter Index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: counter_name
                            
                            	Counter name
                            	**type**\:  str
                            
                            .. attribute:: counter_type
                            
                            	Counter TypeDROP\: Drop counterPUNT\: Punt counterFWD\:  Forward or generic counterUNKNOWN\: Counter type unknown
                            	**type**\:  str
                            
                            .. attribute:: counter_value
                            
                            	The accurate value of the counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rate
                            
                            	Rate in Packets Per Second
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.counter_index = None
                                self.counter_name = None
                                self.counter_type = None
                                self.counter_value = None
                                self.rate = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:np-counter'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter_index is not None:
                                    return True

                                if self.counter_name is not None:
                                    return True

                                if self.counter_type is not None:
                                    return True

                                if self.counter_value is not None:
                                    return True

                                if self.rate is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:counters'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.np_counter is not None:
                                for child_ref in self.np_counter:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                            return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.Counters']['meta_info']


                    class FastDrop(object):
                        """
                        prm fast drop counters info
                        
                        .. attribute:: np_fast_drop
                        
                        	Array of NP Fast Drop Counters
                        	**type**\: list of    :py:class:`NpFastDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop>`
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.np_fast_drop = YList()
                            self.np_fast_drop.parent = self
                            self.np_fast_drop.name = 'np_fast_drop'


                        class NpFastDrop(object):
                            """
                            Array of NP Fast Drop Counters
                            
                            .. attribute:: counter_value
                            
                            	The Value of the counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.counter_value = None
                                self.interface_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:np-fast-drop'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.counter_value is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:fast-drop'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.np_fast_drop is not None:
                                for child_ref in self.np_fast_drop:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                            return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.np_name is None:
                            raise YPYModelError('Key property np_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:np[Cisco-IOS-XR-asr9k-np-oper:np-name = ' + str(self.np_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.np_name is not None:
                            return True

                        if self.chn_load is not None and self.chn_load._has_data():
                            return True

                        if self.counters is not None and self.counters._has_data():
                            return True

                        if self.fast_drop is not None and self.fast_drop._has_data():
                            return True

                        if self.tcam_summary is not None and self.tcam_summary._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-np-oper:nps'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.np is not None:
                        for child_ref in self.np:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-asr9k-np-oper:hardware-module-np/Cisco-IOS-XR-asr9k-np-oper:nodes/Cisco-IOS-XR-asr9k-np-oper:node[Cisco-IOS-XR-asr9k-np-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.nps is not None and self.nps._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                return meta._meta_table['HardwareModuleNp.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-np-oper:hardware-module-np/Cisco-IOS-XR-asr9k-np-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
            return meta._meta_table['HardwareModuleNp.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-np-oper:hardware-module-np'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
        return meta._meta_table['HardwareModuleNp']['meta_info']



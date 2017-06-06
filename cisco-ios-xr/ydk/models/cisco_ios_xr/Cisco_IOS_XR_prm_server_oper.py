""" Cisco_IOS_XR_prm_server_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR prm\-server package operational data.

This module contains definitions
for the following management objects\:
  hardware\-module\: PRM data
  prm\: prm

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class HardwareModule(object):
    """
    PRM data
    
    .. attribute:: nodes
    
    	List of PRM Nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes>`
    
    

    """

    _prefix = 'prm-server-oper'
    _revision = '2016-02-22'

    def __init__(self):
        self.nodes = HardwareModule.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        List of PRM Nodes
        
        .. attribute:: node
        
        	Node Information
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node>`
        
        

        """

        _prefix = 'prm-server-oper'
        _revision = '2016-02-22'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Node Information
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: np
            
            	Server specific
            	**type**\:   :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np>`
            
            

            """

            _prefix = 'prm-server-oper'
            _revision = '2016-02-22'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.np = HardwareModule.Nodes.Node.Np()
                self.np.parent = self


            class Np(object):
                """
                Server specific
                
                .. attribute:: cpu
                
                	Resource specific
                	**type**\:   :py:class:`Cpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.Cpu>`
                
                .. attribute:: platform_drop
                
                	Platform drops
                	**type**\:   :py:class:`PlatformDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.PlatformDrop>`
                
                

                """

                _prefix = 'prm-server-oper'
                _revision = '2016-02-22'

                def __init__(self):
                    self.parent = None
                    self.cpu = HardwareModule.Nodes.Node.Np.Cpu()
                    self.cpu.parent = self
                    self.platform_drop = HardwareModule.Nodes.Node.Np.PlatformDrop()
                    self.platform_drop.parent = self


                class Cpu(object):
                    """
                    Resource specific
                    
                    .. attribute:: indexes
                    
                    	Data for software resource
                    	**type**\:   :py:class:`Indexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.Cpu.Indexes>`
                    
                    

                    """

                    _prefix = 'prm-server-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        self.parent = None
                        self.indexes = HardwareModule.Nodes.Node.Np.Cpu.Indexes()
                        self.indexes.parent = self


                    class Indexes(object):
                        """
                        Data for software resource
                        
                        .. attribute:: index
                        
                        	Queue Stats
                        	**type**\: list of    :py:class:`Index <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.Cpu.Indexes.Index>`
                        
                        

                        """

                        _prefix = 'prm-server-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            self.parent = None
                            self.index = YList()
                            self.index.parent = self
                            self.index.name = 'index'


                        class Index(object):
                            """
                            Queue Stats
                            
                            .. attribute:: index  <key>
                            
                            	Index value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: accepted
                            
                            	Accepted
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: burst
                            
                            	Burst
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cos_q
                            
                            	CosQ No
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: cos_q_name
                            
                            	CosQ Name
                            	**type**\:  str
                            
                            	**length:** 0..1024
                            
                            .. attribute:: dropped
                            
                            	Dropped
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: flow_rate
                            
                            	Flow Rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_channel
                            
                            	Rx DMA Channel
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'prm-server-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                self.parent = None
                                self.index = None
                                self.accepted = None
                                self.burst = None
                                self.cos_q = None
                                self.cos_q_name = None
                                self.dropped = None
                                self.flow_rate = None
                                self.rx_channel = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.index is None:
                                    raise YPYModelError('Key property index is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-prm-server-oper:index[Cisco-IOS-XR-prm-server-oper:index = ' + str(self.index) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.index is not None:
                                    return True

                                if self.accepted is not None:
                                    return True

                                if self.burst is not None:
                                    return True

                                if self.cos_q is not None:
                                    return True

                                if self.cos_q_name is not None:
                                    return True

                                if self.dropped is not None:
                                    return True

                                if self.flow_rate is not None:
                                    return True

                                if self.rx_channel is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
                                return meta._meta_table['HardwareModule.Nodes.Node.Np.Cpu.Indexes.Index']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-prm-server-oper:indexes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.index is not None:
                                for child_ref in self.index:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
                            return meta._meta_table['HardwareModule.Nodes.Node.Np.Cpu.Indexes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-prm-server-oper:cpu'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.indexes is not None and self.indexes._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
                        return meta._meta_table['HardwareModule.Nodes.Node.Np.Cpu']['meta_info']


                class PlatformDrop(object):
                    """
                    Platform drops
                    
                    .. attribute:: idxes
                    
                    	Stats for Drop packets
                    	**type**\:   :py:class:`Idxes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes>`
                    
                    .. attribute:: indxes
                    
                    	Captured Packets
                    	**type**\:   :py:class:`Indxes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes>`
                    
                    

                    """

                    _prefix = 'prm-server-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        self.parent = None
                        self.idxes = HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes()
                        self.idxes.parent = self
                        self.indxes = HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes()
                        self.indxes.parent = self


                    class Indxes(object):
                        """
                        Captured Packets
                        
                        .. attribute:: indx
                        
                        	Captured packets
                        	**type**\: list of    :py:class:`Indx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes.Indx>`
                        
                        

                        """

                        _prefix = 'prm-server-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            self.parent = None
                            self.indx = YList()
                            self.indx.parent = self
                            self.indx.name = 'indx'


                        class Indx(object):
                            """
                            Captured packets
                            
                            .. attribute:: index  <key>
                            
                            	Index value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: buffer_len
                            
                            	Buffer Length
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: captured_pak
                            
                            	Captured Packet
                            	**type**\:  str
                            
                            	**length:** 0..1024
                            
                            .. attribute:: days
                            
                            	Days
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: day
                            
                            .. attribute:: hours
                            
                            	Hours
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: hour
                            
                            .. attribute:: ifhandle
                            
                            	If Handle
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mins
                            
                            	Minutes
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: minute
                            
                            .. attribute:: pkt_index
                            
                            	Packet Index
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: reason
                            
                            	Reason
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reason_hi
                            
                            	Reason Hi
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: secs
                            
                            	Seconds
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: total_captured
                            
                            	Total packets Captured
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: years
                            
                            	Year
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'prm-server-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                self.parent = None
                                self.index = None
                                self.buffer_len = None
                                self.captured_pak = None
                                self.days = None
                                self.hours = None
                                self.ifhandle = None
                                self.mins = None
                                self.pkt_index = None
                                self.reason = None
                                self.reason_hi = None
                                self.secs = None
                                self.total_captured = None
                                self.years = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.index is None:
                                    raise YPYModelError('Key property index is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-prm-server-oper:indx[Cisco-IOS-XR-prm-server-oper:index = ' + str(self.index) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.index is not None:
                                    return True

                                if self.buffer_len is not None:
                                    return True

                                if self.captured_pak is not None:
                                    return True

                                if self.days is not None:
                                    return True

                                if self.hours is not None:
                                    return True

                                if self.ifhandle is not None:
                                    return True

                                if self.mins is not None:
                                    return True

                                if self.pkt_index is not None:
                                    return True

                                if self.reason is not None:
                                    return True

                                if self.reason_hi is not None:
                                    return True

                                if self.secs is not None:
                                    return True

                                if self.total_captured is not None:
                                    return True

                                if self.years is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
                                return meta._meta_table['HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes.Indx']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-prm-server-oper:indxes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.indx is not None:
                                for child_ref in self.indx:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
                            return meta._meta_table['HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes']['meta_info']


                    class Idxes(object):
                        """
                        Stats for Drop packets
                        
                        .. attribute:: idx
                        
                        	Drop Stats
                        	**type**\: list of    :py:class:`Idx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes.Idx>`
                        
                        

                        """

                        _prefix = 'prm-server-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            self.parent = None
                            self.idx = YList()
                            self.idx.parent = self
                            self.idx.name = 'idx'


                        class Idx(object):
                            """
                            Drop Stats
                            
                            .. attribute:: index  <key>
                            
                            	Index value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: counters
                            
                            	Counter
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: drop_reason
                            
                            	Drop Reason
                            	**type**\:  str
                            
                            	**length:** 0..1024
                            
                            

                            """

                            _prefix = 'prm-server-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                self.parent = None
                                self.index = None
                                self.counters = None
                                self.drop_reason = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.index is None:
                                    raise YPYModelError('Key property index is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-prm-server-oper:idx[Cisco-IOS-XR-prm-server-oper:index = ' + str(self.index) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.index is not None:
                                    return True

                                if self.counters is not None:
                                    return True

                                if self.drop_reason is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
                                return meta._meta_table['HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes.Idx']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-prm-server-oper:idxes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.idx is not None:
                                for child_ref in self.idx:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
                            return meta._meta_table['HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-prm-server-oper:platform-drop'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.idxes is not None and self.idxes._has_data():
                            return True

                        if self.indxes is not None and self.indxes._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
                        return meta._meta_table['HardwareModule.Nodes.Node.Np.PlatformDrop']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-prm-server-oper:np'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.cpu is not None and self.cpu._has_data():
                        return True

                    if self.platform_drop is not None and self.platform_drop._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
                    return meta._meta_table['HardwareModule.Nodes.Node.Np']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-prm-server-oper:hardware-module/Cisco-IOS-XR-prm-server-oper:nodes/Cisco-IOS-XR-prm-server-oper:node[Cisco-IOS-XR-prm-server-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.np is not None and self.np._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
                return meta._meta_table['HardwareModule.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-prm-server-oper:hardware-module/Cisco-IOS-XR-prm-server-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
            return meta._meta_table['HardwareModule.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-prm-server-oper:hardware-module'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
        return meta._meta_table['HardwareModule']['meta_info']


class Prm(object):
    """
    prm
    
    .. attribute:: nodes
    
    	List of PRM Nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes>`
    
    

    """

    _prefix = 'prm-server-oper'
    _revision = '2016-02-22'

    def __init__(self):
        self.nodes = Prm.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        List of PRM Nodes
        
        .. attribute:: node
        
        	Node Information
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes.Node>`
        
        

        """

        _prefix = 'prm-server-oper'
        _revision = '2016-02-22'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Node Information
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: server
            
            	Server specific
            	**type**\:   :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes.Node.Server>`
            
            

            """

            _prefix = 'prm-server-oper'
            _revision = '2016-02-22'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.server = Prm.Nodes.Node.Server()
                self.server.parent = self


            class Server(object):
                """
                Server specific
                
                .. attribute:: resource
                
                	Resource specific
                	**type**\:   :py:class:`Resource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes.Node.Server.Resource>`
                
                

                """

                _prefix = 'prm-server-oper'
                _revision = '2016-02-22'

                def __init__(self):
                    self.parent = None
                    self.resource = Prm.Nodes.Node.Server.Resource()
                    self.resource.parent = self


                class Resource(object):
                    """
                    Resource specific
                    
                    .. attribute:: indexes
                    
                    	Data for software resource
                    	**type**\:   :py:class:`Indexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes.Node.Server.Resource.Indexes>`
                    
                    

                    """

                    _prefix = 'prm-server-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        self.parent = None
                        self.indexes = Prm.Nodes.Node.Server.Resource.Indexes()
                        self.indexes.parent = self


                    class Indexes(object):
                        """
                        Data for software resource
                        
                        .. attribute:: index
                        
                        	Data for software resource
                        	**type**\: list of    :py:class:`Index <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes.Node.Server.Resource.Indexes.Index>`
                        
                        

                        """

                        _prefix = 'prm-server-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            self.parent = None
                            self.index = YList()
                            self.index.parent = self
                            self.index.name = 'index'


                        class Index(object):
                            """
                            Data for software resource
                            
                            .. attribute:: index  <key>
                            
                            	Index value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: availability_status
                            
                            	Availability Status
                            	**type**\:  bool
                            
                            .. attribute:: first_available_index
                            
                            	Next Free Index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: flags
                            
                            	Resource Flags
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: free_num
                            
                            	Free Resource Count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: inconsistent
                            
                            	Inconsistice Flags
                            	**type**\:  bool
                            
                            .. attribute:: resource_name
                            
                            	Resource Name
                            	**type**\:  str
                            
                            	**length:** 0..1024
                            
                            .. attribute:: resource_type
                            
                            	Resource Type
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_index
                            
                            	Start Index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_num
                            
                            	Total Resource Count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'prm-server-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                self.parent = None
                                self.index = None
                                self.availability_status = None
                                self.first_available_index = None
                                self.flags = None
                                self.free_num = None
                                self.inconsistent = None
                                self.resource_name = None
                                self.resource_type = None
                                self.start_index = None
                                self.total_num = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.index is None:
                                    raise YPYModelError('Key property index is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-prm-server-oper:index[Cisco-IOS-XR-prm-server-oper:index = ' + str(self.index) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.index is not None:
                                    return True

                                if self.availability_status is not None:
                                    return True

                                if self.first_available_index is not None:
                                    return True

                                if self.flags is not None:
                                    return True

                                if self.free_num is not None:
                                    return True

                                if self.inconsistent is not None:
                                    return True

                                if self.resource_name is not None:
                                    return True

                                if self.resource_type is not None:
                                    return True

                                if self.start_index is not None:
                                    return True

                                if self.total_num is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
                                return meta._meta_table['Prm.Nodes.Node.Server.Resource.Indexes.Index']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-prm-server-oper:indexes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.index is not None:
                                for child_ref in self.index:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
                            return meta._meta_table['Prm.Nodes.Node.Server.Resource.Indexes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-prm-server-oper:resource'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.indexes is not None and self.indexes._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
                        return meta._meta_table['Prm.Nodes.Node.Server.Resource']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-prm-server-oper:server'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.resource is not None and self.resource._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
                    return meta._meta_table['Prm.Nodes.Node.Server']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-prm-server-oper:prm/Cisco-IOS-XR-prm-server-oper:nodes/Cisco-IOS-XR-prm-server-oper:node[Cisco-IOS-XR-prm-server-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.server is not None and self.server._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
                return meta._meta_table['Prm.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-prm-server-oper:prm/Cisco-IOS-XR-prm-server-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
            return meta._meta_table['Prm.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-prm-server-oper:prm'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_prm_server_oper as meta
        return meta._meta_table['Prm']['meta_info']



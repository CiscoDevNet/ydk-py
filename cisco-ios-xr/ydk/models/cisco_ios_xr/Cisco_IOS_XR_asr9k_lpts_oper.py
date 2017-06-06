""" Cisco_IOS_XR_asr9k_lpts_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-lpts package operational data.

This module contains definitions
for the following management objects\:
  platform\-lptsp\-ifib\: ASR9K platform ifib operational data 

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class PlatformLptspIfib(object):
    """
    ASR9K platform ifib operational data 
    
    .. attribute:: nodes
    
    	List of nodes with platform specific lpts operation data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfib.Nodes>`
    
    

    """

    _prefix = 'asr9k-lpts-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = PlatformLptspIfib.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        List of nodes with platform specific lpts
        operation data
        
        .. attribute:: node
        
        	Node with platform specific lpts data
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfib.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-lpts-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Node with platform specific lpts data
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: police
            
            	pl\_pifib police data
            	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfib.Nodes.Node.Police>`
            
            .. attribute:: stats
            
            	pl\_pifib stats
            	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfib.Nodes.Node.Stats>`
            
            

            """

            _prefix = 'asr9k-lpts-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.police = PlatformLptspIfib.Nodes.Node.Police()
                self.police.parent = self
                self.stats = PlatformLptspIfib.Nodes.Node.Stats()
                self.stats.parent = self


            class Police(object):
                """
                pl\_pifib police data
                
                .. attribute:: police_info
                
                	Per flow type police info
                	**type**\: list of    :py:class:`PoliceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfib.Nodes.Node.Police.PoliceInfo>`
                
                

                """

                _prefix = 'asr9k-lpts-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.police_info = YList()
                    self.police_info.parent = self
                    self.police_info.name = 'police_info'


                class PoliceInfo(object):
                    """
                    Per flow type police info
                    
                    .. attribute:: accepted_stats
                    
                    	accepted stats
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: acl_config
                    
                    	acl config
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: acl_str
                    
                    	acl str
                    	**type**\:  str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    .. attribute:: avgrate
                    
                    	avgrate
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: avgrate_type
                    
                    	avgrate type
                    	**type**\:  str
                    
                    	**length:** 0..50
                    
                    .. attribute:: burst
                    
                    	burst
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: change_type
                    
                    	change type
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: dropped_stats
                    
                    	dropped stats
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: flow_type
                    
                    	flow type
                    	**type**\:  str
                    
                    	**length:** 0..50
                    
                    .. attribute:: iptos_value
                    
                    	iptos value
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: np
                    
                    	np
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: policer
                    
                    	policer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: static_avgrate
                    
                    	static avgrate
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'asr9k-lpts-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.accepted_stats = None
                        self.acl_config = None
                        self.acl_str = None
                        self.avgrate = None
                        self.avgrate_type = None
                        self.burst = None
                        self.change_type = None
                        self.dropped_stats = None
                        self.flow_type = None
                        self.iptos_value = None
                        self.np = None
                        self.policer = None
                        self.static_avgrate = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lpts-oper:police-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.accepted_stats is not None:
                            return True

                        if self.acl_config is not None:
                            return True

                        if self.acl_str is not None:
                            return True

                        if self.avgrate is not None:
                            return True

                        if self.avgrate_type is not None:
                            return True

                        if self.burst is not None:
                            return True

                        if self.change_type is not None:
                            return True

                        if self.dropped_stats is not None:
                            return True

                        if self.flow_type is not None:
                            return True

                        if self.iptos_value is not None:
                            return True

                        if self.np is not None:
                            return True

                        if self.policer is not None:
                            return True

                        if self.static_avgrate is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                        return meta._meta_table['PlatformLptspIfib.Nodes.Node.Police.PoliceInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lpts-oper:police'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.police_info is not None:
                        for child_ref in self.police_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                    return meta._meta_table['PlatformLptspIfib.Nodes.Node.Police']['meta_info']


            class Stats(object):
                """
                pl\_pifib stats
                
                .. attribute:: accepted
                
                	Deleted\-entry accepted packets counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: clear_ts
                
                	Statistics clear timestamp
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: dropped
                
                	Deleted\-entry dropped packets counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: no_stats_mem_err
                
                	No statistics memory error
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'asr9k-lpts-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.accepted = None
                    self.clear_ts = None
                    self.dropped = None
                    self.no_stats_mem_err = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lpts-oper:stats'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.accepted is not None:
                        return True

                    if self.clear_ts is not None:
                        return True

                    if self.dropped is not None:
                        return True

                    if self.no_stats_mem_err is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                    return meta._meta_table['PlatformLptspIfib.Nodes.Node.Stats']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib/Cisco-IOS-XR-asr9k-lpts-oper:nodes/Cisco-IOS-XR-asr9k-lpts-oper:node[Cisco-IOS-XR-asr9k-lpts-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.police is not None and self.police._has_data():
                    return True

                if self.stats is not None and self.stats._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                return meta._meta_table['PlatformLptspIfib.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib/Cisco-IOS-XR-asr9k-lpts-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
            return meta._meta_table['PlatformLptspIfib.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
        return meta._meta_table['PlatformLptspIfib']['meta_info']



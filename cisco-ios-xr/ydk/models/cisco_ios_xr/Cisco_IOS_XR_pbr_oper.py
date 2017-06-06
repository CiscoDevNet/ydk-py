""" Cisco_IOS_XR_pbr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pbr package operational data.

This module contains definitions
for the following management objects\:
  pbr\: PBR operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class PolicyStateEnum(Enum):
    """
    PolicyStateEnum

    Different Interface states

    .. data:: active = 0

    	active

    .. data:: suspended = 1

    	suspended

    """

    active = 0

    suspended = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
        return meta._meta_table['PolicyStateEnum']



class Pbr(object):
    """
    PBR operational data
    
    .. attribute:: nodes
    
    	Node\-specific PBR operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes>`
    
    

    """

    _prefix = 'pbr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Pbr.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Node\-specific PBR operational data
        
        .. attribute:: node
        
        	PBR operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node>`
        
        

        """

        _prefix = 'pbr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            PBR operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	The node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: policy_map
            
            	Operational data for policymaps
            	**type**\:   :py:class:`PolicyMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap>`
            
            

            """

            _prefix = 'pbr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.policy_map = Pbr.Nodes.Node.PolicyMap()
                self.policy_map.parent = self


            class PolicyMap(object):
                """
                Operational data for policymaps
                
                .. attribute:: interfaces
                
                	Operational data for all interfaces
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces>`
                
                

                """

                _prefix = 'pbr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interfaces = Pbr.Nodes.Node.PolicyMap.Interfaces()
                    self.interfaces.parent = self


                class Interfaces(object):
                    """
                    Operational data for all interfaces
                    
                    .. attribute:: interface
                    
                    	PBR action data for a particular interface
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'pbr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = YList()
                        self.interface.parent = self
                        self.interface.name = 'interface'


                    class Interface(object):
                        """
                        PBR action data for a particular interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	Name of the interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: direction
                        
                        	PBR direction
                        	**type**\:   :py:class:`Direction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction>`
                        
                        

                        """

                        _prefix = 'pbr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.direction = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction()
                            self.direction.parent = self


                        class Direction(object):
                            """
                            PBR direction
                            
                            .. attribute:: input
                            
                            	PBR policy statistics
                            	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input>`
                            
                            

                            """

                            _prefix = 'pbr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.input = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input()
                                self.input.parent = self


                            class Input(object):
                                """
                                PBR policy statistics
                                
                                .. attribute:: class_stat
                                
                                	Array of classes contained in policy
                                	**type**\: list of    :py:class:`ClassStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat>`
                                
                                .. attribute:: node_name
                                
                                	NodeName
                                	**type**\:  str
                                
                                	**length:** 0..42
                                
                                .. attribute:: policy_name
                                
                                	PolicyName
                                	**type**\:  str
                                
                                	**length:** 0..65
                                
                                .. attribute:: state
                                
                                	State
                                	**type**\:   :py:class:`PolicyStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.PolicyStateEnum>`
                                
                                .. attribute:: state_description
                                
                                	StateDescription
                                	**type**\:  str
                                
                                	**length:** 0..128
                                
                                

                                """

                                _prefix = 'pbr-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.class_stat = YList()
                                    self.class_stat.parent = self
                                    self.class_stat.name = 'class_stat'
                                    self.node_name = None
                                    self.policy_name = None
                                    self.state = None
                                    self.state_description = None


                                class ClassStat(object):
                                    """
                                    Array of classes contained in policy
                                    
                                    .. attribute:: class_id
                                    
                                    	ClassId
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: class_name
                                    
                                    	ClassName
                                    	**type**\:  str
                                    
                                    	**length:** 0..65
                                    
                                    .. attribute:: counter_validity_bitmask
                                    
                                    	 Bitmask to indicate which counter or counters are undetermined. Counters will be marked undetermined when one or more classes share queues with class\-default because in such cases the value of counters for each class is invalid. Based on the flag(s) set, the following counters will be marked undetermined. For example, if value of this object returned is 0x00000101, counters TransmitPackets/TransmitBytes/TotalTransmitRate and DropPackets/DropBytes are undetermined .0x00000001 \- Transmit (TransmitPackets/TransmitBytes/TotalTransmitRate ), 0x00000002 \- Drop (TotalDropPackets/TotalDropBytes/TotalDropRate), 0x00000004 \- Httpr (HttprTransmitPackets/HttprTransmitBytes), 
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: general_stats
                                    
                                    	general stats
                                    	**type**\:   :py:class:`GeneralStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats>`
                                    
                                    .. attribute:: httpr_stats
                                    
                                    	HTTPR stats
                                    	**type**\:   :py:class:`HttprStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.class_id = None
                                        self.class_name = None
                                        self.counter_validity_bitmask = None
                                        self.general_stats = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats()
                                        self.general_stats.parent = self
                                        self.httpr_stats = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats()
                                        self.httpr_stats.parent = self


                                    class GeneralStats(object):
                                        """
                                        general stats
                                        
                                        .. attribute:: match_data_rate
                                        
                                        	Incoming matched data rate in kbps
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: kbit/s
                                        
                                        .. attribute:: pre_policy_matched_bytes
                                        
                                        	Matched bytes before applying policy
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: pre_policy_matched_packets
                                        
                                        	Matched pkts before applying policy
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: total_drop_bytes
                                        
                                        	Dropped bytes (packets/bytes)
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: total_drop_packets
                                        
                                        	Dropped packets (packets/bytes)
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: total_drop_rate
                                        
                                        	Total drop rate (packets/bytes)
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: total_transmit_rate
                                        
                                        	Total transmit rate in kbps
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: kbit/s
                                        
                                        .. attribute:: transmit_bytes
                                        
                                        	Transmitted bytes (packets/bytes)
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: transmit_packets
                                        
                                        	Transmitted packets (packets/bytes)
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.match_data_rate = None
                                            self.pre_policy_matched_bytes = None
                                            self.pre_policy_matched_packets = None
                                            self.total_drop_bytes = None
                                            self.total_drop_packets = None
                                            self.total_drop_rate = None
                                            self.total_transmit_rate = None
                                            self.transmit_bytes = None
                                            self.transmit_packets = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-oper:general-stats'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.match_data_rate is not None:
                                                return True

                                            if self.pre_policy_matched_bytes is not None:
                                                return True

                                            if self.pre_policy_matched_packets is not None:
                                                return True

                                            if self.total_drop_bytes is not None:
                                                return True

                                            if self.total_drop_packets is not None:
                                                return True

                                            if self.total_drop_rate is not None:
                                                return True

                                            if self.total_transmit_rate is not None:
                                                return True

                                            if self.transmit_bytes is not None:
                                                return True

                                            if self.transmit_packets is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                                            return meta._meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats']['meta_info']


                                    class HttprStats(object):
                                        """
                                        HTTPR stats
                                        
                                        .. attribute:: drop_bytes
                                        
                                        	Dropped bytes
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: drop_packets
                                        
                                        	Dropped  packets
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: resp_sent_bytes
                                        
                                        	TotalNum of Bytes HTTPR response sent
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: resp_sent_packets
                                        
                                        	TotalNum of pkts HTTPR response sent
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: rqst_rcvd_bytes
                                        
                                        	TotalNum of Bytes HTTP request received
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: rqst_rcvd_packets
                                        
                                        	TotalNum of pkts HTTP request received
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.drop_bytes = None
                                            self.drop_packets = None
                                            self.resp_sent_bytes = None
                                            self.resp_sent_packets = None
                                            self.rqst_rcvd_bytes = None
                                            self.rqst_rcvd_packets = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-oper:httpr-stats'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.drop_bytes is not None:
                                                return True

                                            if self.drop_packets is not None:
                                                return True

                                            if self.resp_sent_bytes is not None:
                                                return True

                                            if self.resp_sent_packets is not None:
                                                return True

                                            if self.rqst_rcvd_bytes is not None:
                                                return True

                                            if self.rqst_rcvd_packets is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                                            return meta._meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-oper:class-stat'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.class_id is not None:
                                            return True

                                        if self.class_name is not None:
                                            return True

                                        if self.counter_validity_bitmask is not None:
                                            return True

                                        if self.general_stats is not None and self.general_stats._has_data():
                                            return True

                                        if self.httpr_stats is not None and self.httpr_stats._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                                        return meta._meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-oper:input'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.class_stat is not None:
                                        for child_ref in self.class_stat:
                                            if child_ref._has_data():
                                                return True

                                    if self.node_name is not None:
                                        return True

                                    if self.policy_name is not None:
                                        return True

                                    if self.state is not None:
                                        return True

                                    if self.state_description is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                                    return meta._meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pbr-oper:direction'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.input is not None and self.input._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                                return meta._meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-pbr-oper:interface[Cisco-IOS-XR-pbr-oper:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.direction is not None and self.direction._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                            return meta._meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-oper:interfaces'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            for child_ref in self.interface:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                        return meta._meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-oper:policy-map'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interfaces is not None and self.interfaces._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                    return meta._meta_table['Pbr.Nodes.Node.PolicyMap']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-pbr-oper:pbr/Cisco-IOS-XR-pbr-oper:nodes/Cisco-IOS-XR-pbr-oper:node[Cisco-IOS-XR-pbr-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.policy_map is not None and self.policy_map._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                return meta._meta_table['Pbr.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-pbr-oper:pbr/Cisco-IOS-XR-pbr-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
            return meta._meta_table['Pbr.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-pbr-oper:pbr'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
        return meta._meta_table['Pbr']['meta_info']



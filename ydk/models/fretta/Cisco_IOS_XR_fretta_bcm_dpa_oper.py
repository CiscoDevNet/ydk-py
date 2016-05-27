""" Cisco_IOS_XR_fretta_bcm_dpa_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fretta\-bcm\-dpa package operational data.

This module contains definitions
for the following management objects\:
  dpa\: DPA operational data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class Dpa(object):
    """
    DPA operational data
    
    .. attribute:: stats
    
    	DPA voq data
    	**type**\: :py:class:`Stats <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats>`
    
    

    """

    _prefix = 'fretta-bcm-dpa-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.stats = Dpa.Stats()
        self.stats.parent = self


    class Stats(object):
        """
        DPA voq data
        
        .. attribute:: nodes
        
        	DPA data for available nodes
        	**type**\: :py:class:`Nodes <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes>`
        
        

        """

        _prefix = 'fretta-bcm-dpa-oper'
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
            	**type**\: list of :py:class:`Node <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node>`
            
            

            """

            _prefix = 'fretta-bcm-dpa-oper'
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
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: all_traps_stats_data_blocks
                
                	DPA trap stats 
                	**type**\: :py:class:`AllTrapsStatsDataBlocks <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.AllTrapsStatsDataBlocks>`
                
                .. attribute:: single_trap_stats_data_blocks
                
                	DPA stats for a single trap
                	**type**\: :py:class:`SingleTrapStatsDataBlocks <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks>`
                
                .. attribute:: all_voq_stats_data_blocks
                
                	DPA voq ingress stats 
                	**type**\: :py:class:`AllVoqStatsDataBlocks <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks>`
                
                .. attribute:: voq_base_numbers
                
                	DPA voq base stats 
                	**type**\: :py:class:`VoqBaseNumbers <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.VoqBaseNumbers>`
                
                .. attribute:: single_voq_stats_data_blocks
                
                	DPA voq ingress stats for a single interface
                	**type**\: :py:class:`SingleVoqStatsDataBlocks <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks>`
                
                

                """

                _prefix = 'fretta-bcm-dpa-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node_name = None
                    self.all_traps_stats_data_blocks = Dpa.Stats.Nodes.Node.AllTrapsStatsDataBlocks()
                    self.all_traps_stats_data_blocks.parent = self
                    self.single_trap_stats_data_blocks = Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks()
                    self.single_trap_stats_data_blocks.parent = self
                    self.all_voq_stats_data_blocks = Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks()
                    self.all_voq_stats_data_blocks.parent = self
                    self.voq_base_numbers = Dpa.Stats.Nodes.Node.VoqBaseNumbers()
                    self.voq_base_numbers.parent = self
                    self.single_voq_stats_data_blocks = Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks()
                    self.single_voq_stats_data_blocks.parent = self


                class AllTrapsStatsDataBlocks(object):
                    """
                    DPA trap stats 
                    
                    .. attribute:: all_traps_stats_data_block
                    
                    	Indicates the data block number for trap stats data block and cannot be used to extract a single data block
                    	**type**\: list of :py:class:`AllTrapsStatsDataBlock <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.AllTrapsStatsDataBlocks.AllTrapsStatsDataBlock>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.all_traps_stats_data_block = YList()
                        self.all_traps_stats_data_block.parent = self
                        self.all_traps_stats_data_block.name = 'all_traps_stats_data_block'


                    class AllTrapsStatsDataBlock(object):
                        """
                        Indicates the data block number for trap
                        stats data block and cannot be used to
                        extract a single data block
                        
                        .. attribute:: data_block_number  <key>
                        
                        	Data Block Number
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: trap_strength
                        
                        	trap strength
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: priority
                        
                        	priority
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: trap_id
                        
                        	trap id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: gport
                        
                        	gport
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fec_id
                        
                        	fec id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: policer_id
                        
                        	policer id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stats_id
                        
                        	stats id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: encap_id
                        
                        	encap id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mc_group
                        
                        	mc group
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: trap_string
                        
                        	trap string
                        	**type**\: str
                        
                        .. attribute:: id
                        
                        	id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: offset
                        
                        	offset
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: npu_id
                        
                        	npu id
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packet_dropped
                        
                        	packet dropped
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packet_accepted
                        
                        	packet accepted
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.data_block_number = None
                            self.trap_strength = None
                            self.priority = None
                            self.trap_id = None
                            self.gport = None
                            self.fec_id = None
                            self.policer_id = None
                            self.stats_id = None
                            self.encap_id = None
                            self.mc_group = None
                            self.trap_string = None
                            self.id = None
                            self.offset = None
                            self.npu_id = None
                            self.packet_dropped = None
                            self.packet_accepted = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.data_block_number is None:
                                raise YPYDataValidationError('Key property data_block_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:all-traps-stats-data-block[Cisco-IOS-XR-fretta-bcm-dpa-oper:data-block-number = ' + str(self.data_block_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.data_block_number is not None:
                                return True

                            if self.trap_strength is not None:
                                return True

                            if self.priority is not None:
                                return True

                            if self.trap_id is not None:
                                return True

                            if self.gport is not None:
                                return True

                            if self.fec_id is not None:
                                return True

                            if self.policer_id is not None:
                                return True

                            if self.stats_id is not None:
                                return True

                            if self.encap_id is not None:
                                return True

                            if self.mc_group is not None:
                                return True

                            if self.trap_string is not None:
                                return True

                            if self.id is not None:
                                return True

                            if self.offset is not None:
                                return True

                            if self.npu_id is not None:
                                return True

                            if self.packet_dropped is not None:
                                return True

                            if self.packet_accepted is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                            return meta._meta_table['Dpa.Stats.Nodes.Node.AllTrapsStatsDataBlocks.AllTrapsStatsDataBlock']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:all-traps-stats-data-blocks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.all_traps_stats_data_block is not None:
                            for child_ref in self.all_traps_stats_data_block:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                        return meta._meta_table['Dpa.Stats.Nodes.Node.AllTrapsStatsDataBlocks']['meta_info']


                class SingleTrapStatsDataBlocks(object):
                    """
                    DPA stats for a single trap
                    
                    .. attribute:: single_trap_stats_data_block
                    
                    	Trap number
                    	**type**\: list of :py:class:`SingleTrapStatsDataBlock <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks.SingleTrapStatsDataBlock>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.single_trap_stats_data_block = YList()
                        self.single_trap_stats_data_block.parent = self
                        self.single_trap_stats_data_block.name = 'single_trap_stats_data_block'


                    class SingleTrapStatsDataBlock(object):
                        """
                        Trap number
                        
                        .. attribute:: trapid  <key>
                        
                        	Trap number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: trap_data_block_number
                        
                        	Indicates the data block number for a particular trap and cannot be used to extract a particular block
                        	**type**\: list of :py:class:`TrapDataBlockNumber <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks.SingleTrapStatsDataBlock.TrapDataBlockNumber>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.trapid = None
                            self.trap_data_block_number = YList()
                            self.trap_data_block_number.parent = self
                            self.trap_data_block_number.name = 'trap_data_block_number'


                        class TrapDataBlockNumber(object):
                            """
                            Indicates the data block number for a
                            particular trap and cannot be used to
                            extract a particular block
                            
                            .. attribute:: data_block_number  <key>
                            
                            	Data Block Number
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: trap_strength
                            
                            	trap strength
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: priority
                            
                            	priority
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: trap_id
                            
                            	trap id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: gport
                            
                            	gport
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fec_id
                            
                            	fec id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: policer_id
                            
                            	policer id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stats_id
                            
                            	stats id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: encap_id
                            
                            	encap id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mc_group
                            
                            	mc group
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: trap_string
                            
                            	trap string
                            	**type**\: str
                            
                            .. attribute:: id
                            
                            	id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: offset
                            
                            	offset
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: npu_id
                            
                            	npu id
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: packet_dropped
                            
                            	packet dropped
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: packet_accepted
                            
                            	packet accepted
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.data_block_number = None
                                self.trap_strength = None
                                self.priority = None
                                self.trap_id = None
                                self.gport = None
                                self.fec_id = None
                                self.policer_id = None
                                self.stats_id = None
                                self.encap_id = None
                                self.mc_group = None
                                self.trap_string = None
                                self.id = None
                                self.offset = None
                                self.npu_id = None
                                self.packet_dropped = None
                                self.packet_accepted = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.data_block_number is None:
                                    raise YPYDataValidationError('Key property data_block_number is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:trap-data-block-number[Cisco-IOS-XR-fretta-bcm-dpa-oper:data-block-number = ' + str(self.data_block_number) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.data_block_number is not None:
                                    return True

                                if self.trap_strength is not None:
                                    return True

                                if self.priority is not None:
                                    return True

                                if self.trap_id is not None:
                                    return True

                                if self.gport is not None:
                                    return True

                                if self.fec_id is not None:
                                    return True

                                if self.policer_id is not None:
                                    return True

                                if self.stats_id is not None:
                                    return True

                                if self.encap_id is not None:
                                    return True

                                if self.mc_group is not None:
                                    return True

                                if self.trap_string is not None:
                                    return True

                                if self.id is not None:
                                    return True

                                if self.offset is not None:
                                    return True

                                if self.npu_id is not None:
                                    return True

                                if self.packet_dropped is not None:
                                    return True

                                if self.packet_accepted is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                                return meta._meta_table['Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks.SingleTrapStatsDataBlock.TrapDataBlockNumber']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.trapid is None:
                                raise YPYDataValidationError('Key property trapid is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:single-trap-stats-data-block[Cisco-IOS-XR-fretta-bcm-dpa-oper:trapid = ' + str(self.trapid) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.trapid is not None:
                                return True

                            if self.trap_data_block_number is not None:
                                for child_ref in self.trap_data_block_number:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                            return meta._meta_table['Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks.SingleTrapStatsDataBlock']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:single-trap-stats-data-blocks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.single_trap_stats_data_block is not None:
                            for child_ref in self.single_trap_stats_data_block:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                        return meta._meta_table['Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks']['meta_info']


                class AllVoqStatsDataBlocks(object):
                    """
                    DPA voq ingress stats 
                    
                    .. attribute:: all_voq_stats_data_block
                    
                    	Indicate the data block number of the voq stats data block and cannot be used to extract a single data block
                    	**type**\: list of :py:class:`AllVoqStatsDataBlock <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks.AllVoqStatsDataBlock>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.all_voq_stats_data_block = YList()
                        self.all_voq_stats_data_block.parent = self
                        self.all_voq_stats_data_block.name = 'all_voq_stats_data_block'


                    class AllVoqStatsDataBlock(object):
                        """
                        Indicate the data block number of the voq
                        stats data block and cannot be used to
                        extract a single data block
                        
                        .. attribute:: data_block_number  <key>
                        
                        	Data Block Number
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_inuse
                        
                        	is inuse
                        	**type**\: bool
                        
                        .. attribute:: rack_num
                        
                        	rack num
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: slot_num
                        
                        	slot num
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: npu_num
                        
                        	npu num
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: npu_core
                        
                        	npu core
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: port_num
                        
                        	port num
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: ifhandle
                        
                        	ifhandle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sysport
                        
                        	sysport
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pp_port
                        
                        	pp port
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: port_speed
                        
                        	port speed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: voq_base
                        
                        	voq base
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: connector_id
                        
                        	connector id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_local_port
                        
                        	is local port
                        	**type**\: bool
                        
                        .. attribute:: voq_stat
                        
                        	voq stat
                        	**type**\: list of :py:class:`VoqStat <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks.AllVoqStatsDataBlock.VoqStat>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.data_block_number = None
                            self.is_inuse = None
                            self.rack_num = None
                            self.slot_num = None
                            self.npu_num = None
                            self.npu_core = None
                            self.port_num = None
                            self.ifhandle = None
                            self.sysport = None
                            self.pp_port = None
                            self.port_speed = None
                            self.voq_base = None
                            self.connector_id = None
                            self.is_local_port = None
                            self.voq_stat = YList()
                            self.voq_stat.parent = self
                            self.voq_stat.name = 'voq_stat'


                        class VoqStat(object):
                            """
                            voq stat
                            
                            .. attribute:: gport_received_bytes
                            
                            	GportReceivedBytes
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: gport_received_pkts
                            
                            	GportReceivedPkts
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: gport_dropped_bytes
                            
                            	GportDroppedBytes
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: gport_dropped_pkts
                            
                            	GportDroppedPkts
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.gport_received_bytes = None
                                self.gport_received_pkts = None
                                self.gport_dropped_bytes = None
                                self.gport_dropped_pkts = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:voq-stat'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.gport_received_bytes is not None:
                                    return True

                                if self.gport_received_pkts is not None:
                                    return True

                                if self.gport_dropped_bytes is not None:
                                    return True

                                if self.gport_dropped_pkts is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                                return meta._meta_table['Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks.AllVoqStatsDataBlock.VoqStat']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.data_block_number is None:
                                raise YPYDataValidationError('Key property data_block_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:all-voq-stats-data-block[Cisco-IOS-XR-fretta-bcm-dpa-oper:data-block-number = ' + str(self.data_block_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.data_block_number is not None:
                                return True

                            if self.is_inuse is not None:
                                return True

                            if self.rack_num is not None:
                                return True

                            if self.slot_num is not None:
                                return True

                            if self.npu_num is not None:
                                return True

                            if self.npu_core is not None:
                                return True

                            if self.port_num is not None:
                                return True

                            if self.ifhandle is not None:
                                return True

                            if self.sysport is not None:
                                return True

                            if self.pp_port is not None:
                                return True

                            if self.port_speed is not None:
                                return True

                            if self.voq_base is not None:
                                return True

                            if self.connector_id is not None:
                                return True

                            if self.is_local_port is not None:
                                return True

                            if self.voq_stat is not None:
                                for child_ref in self.voq_stat:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                            return meta._meta_table['Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks.AllVoqStatsDataBlock']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:all-voq-stats-data-blocks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.all_voq_stats_data_block is not None:
                            for child_ref in self.all_voq_stats_data_block:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                        return meta._meta_table['Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks']['meta_info']


                class VoqBaseNumbers(object):
                    """
                    DPA voq base stats 
                    
                    .. attribute:: voq_base_number
                    
                    	Voq Base Number for a particular voq
                    	**type**\: list of :py:class:`VoqBaseNumber <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.voq_base_number = YList()
                        self.voq_base_number.parent = self
                        self.voq_base_number.name = 'voq_base_number'


                    class VoqBaseNumber(object):
                        """
                        Voq Base Number for a particular voq
                        
                        .. attribute:: base_number  <key>
                        
                        	Interface handle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: voq_base_data_block_number
                        
                        	Indicates the data block number for a particular voq base and cannot be used to extract a particular block number
                        	**type**\: list of :py:class:`VoqBaseDataBlockNumber <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseDataBlockNumber>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.base_number = None
                            self.voq_base_data_block_number = YList()
                            self.voq_base_data_block_number.parent = self
                            self.voq_base_data_block_number.name = 'voq_base_data_block_number'


                        class VoqBaseDataBlockNumber(object):
                            """
                            Indicates the data block number for a
                            particular voq base and cannot be used to
                            extract a particular block number
                            
                            .. attribute:: data_block_number  <key>
                            
                            	Data Block Number
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_inuse
                            
                            	is inuse
                            	**type**\: bool
                            
                            .. attribute:: rack_num
                            
                            	rack num
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: slot_num
                            
                            	slot num
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: npu_num
                            
                            	npu num
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: npu_core
                            
                            	npu core
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_num
                            
                            	port num
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ifhandle
                            
                            	ifhandle
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sysport
                            
                            	sysport
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pp_port
                            
                            	pp port
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: port_speed
                            
                            	port speed
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: voq_base
                            
                            	voq base
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connector_id
                            
                            	connector id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_local_port
                            
                            	is local port
                            	**type**\: bool
                            
                            .. attribute:: voq_stat
                            
                            	voq stat
                            	**type**\: list of :py:class:`VoqStat <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseDataBlockNumber.VoqStat>`
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.data_block_number = None
                                self.is_inuse = None
                                self.rack_num = None
                                self.slot_num = None
                                self.npu_num = None
                                self.npu_core = None
                                self.port_num = None
                                self.ifhandle = None
                                self.sysport = None
                                self.pp_port = None
                                self.port_speed = None
                                self.voq_base = None
                                self.connector_id = None
                                self.is_local_port = None
                                self.voq_stat = YList()
                                self.voq_stat.parent = self
                                self.voq_stat.name = 'voq_stat'


                            class VoqStat(object):
                                """
                                voq stat
                                
                                .. attribute:: gport_received_bytes
                                
                                	GportReceivedBytes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: gport_received_pkts
                                
                                	GportReceivedPkts
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: gport_dropped_bytes
                                
                                	GportDroppedBytes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: gport_dropped_pkts
                                
                                	GportDroppedPkts
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.gport_received_bytes = None
                                    self.gport_received_pkts = None
                                    self.gport_dropped_bytes = None
                                    self.gport_dropped_pkts = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:voq-stat'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.gport_received_bytes is not None:
                                        return True

                                    if self.gport_received_pkts is not None:
                                        return True

                                    if self.gport_dropped_bytes is not None:
                                        return True

                                    if self.gport_dropped_pkts is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                                    return meta._meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseDataBlockNumber.VoqStat']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.data_block_number is None:
                                    raise YPYDataValidationError('Key property data_block_number is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:voq-base-data-block-number[Cisco-IOS-XR-fretta-bcm-dpa-oper:data-block-number = ' + str(self.data_block_number) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.data_block_number is not None:
                                    return True

                                if self.is_inuse is not None:
                                    return True

                                if self.rack_num is not None:
                                    return True

                                if self.slot_num is not None:
                                    return True

                                if self.npu_num is not None:
                                    return True

                                if self.npu_core is not None:
                                    return True

                                if self.port_num is not None:
                                    return True

                                if self.ifhandle is not None:
                                    return True

                                if self.sysport is not None:
                                    return True

                                if self.pp_port is not None:
                                    return True

                                if self.port_speed is not None:
                                    return True

                                if self.voq_base is not None:
                                    return True

                                if self.connector_id is not None:
                                    return True

                                if self.is_local_port is not None:
                                    return True

                                if self.voq_stat is not None:
                                    for child_ref in self.voq_stat:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                                return meta._meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseDataBlockNumber']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.base_number is None:
                                raise YPYDataValidationError('Key property base_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:voq-base-number[Cisco-IOS-XR-fretta-bcm-dpa-oper:base-number = ' + str(self.base_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.base_number is not None:
                                return True

                            if self.voq_base_data_block_number is not None:
                                for child_ref in self.voq_base_data_block_number:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                            return meta._meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:voq-base-numbers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.voq_base_number is not None:
                            for child_ref in self.voq_base_number:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                        return meta._meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers']['meta_info']


                class SingleVoqStatsDataBlocks(object):
                    """
                    DPA voq ingress stats for a single interface
                    
                    .. attribute:: single_voq_stats_data_block
                    
                    	Interface handle for a particular voq
                    	**type**\: list of :py:class:`SingleVoqStatsDataBlock <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.single_voq_stats_data_block = YList()
                        self.single_voq_stats_data_block.parent = self
                        self.single_voq_stats_data_block.name = 'single_voq_stats_data_block'


                    class SingleVoqStatsDataBlock(object):
                        """
                        Interface handle for a particular voq
                        
                        .. attribute:: interface_handle  <key>
                        
                        	Interface handle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: voq_stats_data_block_number
                        
                        	Indicates the data block number for a particular voq and cannot be used to extract a single element
                        	**type**\: list of :py:class:`VoqStatsDataBlockNumber <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock.VoqStatsDataBlockNumber>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_handle = None
                            self.voq_stats_data_block_number = YList()
                            self.voq_stats_data_block_number.parent = self
                            self.voq_stats_data_block_number.name = 'voq_stats_data_block_number'


                        class VoqStatsDataBlockNumber(object):
                            """
                            Indicates the data block number for a
                            particular voq and cannot be used to
                            extract a single element
                            
                            .. attribute:: data_block_number  <key>
                            
                            	Data Block Number
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_inuse
                            
                            	is inuse
                            	**type**\: bool
                            
                            .. attribute:: rack_num
                            
                            	rack num
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: slot_num
                            
                            	slot num
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: npu_num
                            
                            	npu num
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: npu_core
                            
                            	npu core
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_num
                            
                            	port num
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ifhandle
                            
                            	ifhandle
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sysport
                            
                            	sysport
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pp_port
                            
                            	pp port
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: port_speed
                            
                            	port speed
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: voq_base
                            
                            	voq base
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connector_id
                            
                            	connector id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_local_port
                            
                            	is local port
                            	**type**\: bool
                            
                            .. attribute:: voq_stat
                            
                            	voq stat
                            	**type**\: list of :py:class:`VoqStat <ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper.Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock.VoqStatsDataBlockNumber.VoqStat>`
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.data_block_number = None
                                self.is_inuse = None
                                self.rack_num = None
                                self.slot_num = None
                                self.npu_num = None
                                self.npu_core = None
                                self.port_num = None
                                self.ifhandle = None
                                self.sysport = None
                                self.pp_port = None
                                self.port_speed = None
                                self.voq_base = None
                                self.connector_id = None
                                self.is_local_port = None
                                self.voq_stat = YList()
                                self.voq_stat.parent = self
                                self.voq_stat.name = 'voq_stat'


                            class VoqStat(object):
                                """
                                voq stat
                                
                                .. attribute:: gport_received_bytes
                                
                                	GportReceivedBytes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: gport_received_pkts
                                
                                	GportReceivedPkts
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: gport_dropped_bytes
                                
                                	GportDroppedBytes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: gport_dropped_pkts
                                
                                	GportDroppedPkts
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.gport_received_bytes = None
                                    self.gport_received_pkts = None
                                    self.gport_dropped_bytes = None
                                    self.gport_dropped_pkts = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:voq-stat'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.gport_received_bytes is not None:
                                        return True

                                    if self.gport_received_pkts is not None:
                                        return True

                                    if self.gport_dropped_bytes is not None:
                                        return True

                                    if self.gport_dropped_pkts is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                                    return meta._meta_table['Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock.VoqStatsDataBlockNumber.VoqStat']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.data_block_number is None:
                                    raise YPYDataValidationError('Key property data_block_number is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:voq-stats-data-block-number[Cisco-IOS-XR-fretta-bcm-dpa-oper:data-block-number = ' + str(self.data_block_number) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.data_block_number is not None:
                                    return True

                                if self.is_inuse is not None:
                                    return True

                                if self.rack_num is not None:
                                    return True

                                if self.slot_num is not None:
                                    return True

                                if self.npu_num is not None:
                                    return True

                                if self.npu_core is not None:
                                    return True

                                if self.port_num is not None:
                                    return True

                                if self.ifhandle is not None:
                                    return True

                                if self.sysport is not None:
                                    return True

                                if self.pp_port is not None:
                                    return True

                                if self.port_speed is not None:
                                    return True

                                if self.voq_base is not None:
                                    return True

                                if self.connector_id is not None:
                                    return True

                                if self.is_local_port is not None:
                                    return True

                                if self.voq_stat is not None:
                                    for child_ref in self.voq_stat:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                                return meta._meta_table['Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock.VoqStatsDataBlockNumber']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.interface_handle is None:
                                raise YPYDataValidationError('Key property interface_handle is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:single-voq-stats-data-block[Cisco-IOS-XR-fretta-bcm-dpa-oper:interface-handle = ' + str(self.interface_handle) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.interface_handle is not None:
                                return True

                            if self.voq_stats_data_block_number is not None:
                                for child_ref in self.voq_stats_data_block_number:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                            return meta._meta_table['Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-fretta-bcm-dpa-oper:single-voq-stats-data-blocks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.single_voq_stats_data_block is not None:
                            for child_ref in self.single_voq_stats_data_block:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                        return meta._meta_table['Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks']['meta_info']

                @property
                def _common_path(self):
                    if self.node_name is None:
                        raise YPYDataValidationError('Key property node_name is None')

                    return '/Cisco-IOS-XR-fretta-bcm-dpa-oper:dpa/Cisco-IOS-XR-fretta-bcm-dpa-oper:stats/Cisco-IOS-XR-fretta-bcm-dpa-oper:nodes/Cisco-IOS-XR-fretta-bcm-dpa-oper:node[Cisco-IOS-XR-fretta-bcm-dpa-oper:node-name = ' + str(self.node_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.node_name is not None:
                        return True

                    if self.all_traps_stats_data_blocks is not None and self.all_traps_stats_data_blocks._has_data():
                        return True

                    if self.single_trap_stats_data_blocks is not None and self.single_trap_stats_data_blocks._has_data():
                        return True

                    if self.all_voq_stats_data_blocks is not None and self.all_voq_stats_data_blocks._has_data():
                        return True

                    if self.voq_base_numbers is not None and self.voq_base_numbers._has_data():
                        return True

                    if self.single_voq_stats_data_blocks is not None and self.single_voq_stats_data_blocks._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                    return meta._meta_table['Dpa.Stats.Nodes.Node']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-fretta-bcm-dpa-oper:dpa/Cisco-IOS-XR-fretta-bcm-dpa-oper:stats/Cisco-IOS-XR-fretta-bcm-dpa-oper:nodes'

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
                from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
                return meta._meta_table['Dpa.Stats.Nodes']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-fretta-bcm-dpa-oper:dpa/Cisco-IOS-XR-fretta-bcm-dpa-oper:stats'

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
            from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
            return meta._meta_table['Dpa.Stats']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-fretta-bcm-dpa-oper:dpa'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.stats is not None and self.stats._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.fretta._meta import _Cisco_IOS_XR_fretta_bcm_dpa_oper as meta
        return meta._meta_table['Dpa']['meta_info']


